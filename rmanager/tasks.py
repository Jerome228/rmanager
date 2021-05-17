# Create your tasks here
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from time import sleep
from celery import shared_task
from celery.utils.log import get_task_logger
from api.models import AppData

logger = get_task_logger(__name__)

@shared_task(bind=True, track_started=True)
def c_runCommands(self):
    cmd = """
    if [ -f ~/script.sh ]
    then
        ~/script.sh
    fi
    """
    app = AppData.objects.first()
    srv = app.hservers
    out = []
    psw = settings.USER_PSWD
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(srv, username='appuser', password=psw)
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)

    for line in iter(stdout.readline, ""):
        self.update_state(state='PROGRESS', meta={'line': line,})
        out.append(line)
    client.close()
    return "Output from Celery worker: {0}".format("".join(out))

@shared_task(bind=True)
def c_goToSleep(self, sec):
    sleep(sec)
    return 'DONE !'