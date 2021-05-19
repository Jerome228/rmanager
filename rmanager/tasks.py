# Create your tasks here
from django.conf import settings
from django.utils.html import escape
import paramiko
from ansi2html import Ansi2HTMLConverter
from time import sleep
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True)
def c_runCommands(self, srv):
    cmd = """
    if [ -f ~/script.sh ]
    then
        ~/script.sh
    fi
    """
    out = []
    psw = settings.USER_PSWD
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(srv, username='appuser', password=psw)
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)
    i = 0
    for line in iter(stdout.readline, ""):
        i += 1
        out.append(line)
        txt2html = convert2html(out)
        self.update_state(state='PROGRESS', meta={'line': txt2html, 'iter': i})
    client.close()
    return convert2html(out)

@shared_task(bind=True)
def c_goToSleep(self, sec):
    sleep(sec)
    return 'DONE !'


def convert2html(output):
    conv = Ansi2HTMLConverter()
    ansi = ''.join(output)
    return conv.convert(ansi)
