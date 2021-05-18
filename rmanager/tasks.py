# Create your tasks here
from django.conf import settings
from django.utils.html import escape
import paramiko
import ansiconv
from time import sleep
from celery import shared_task
from celery_progress.backend import ProgressRecorder
from celery.utils.log import get_task_logger
from api.models import AppData

logger = get_task_logger(__name__)

@shared_task(bind=True)
def c_runCommands(self):
    progress_recorder = ProgressRecorder(self)
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
    i = 0
    for line in iter(stdout.readline, ""):
        i += 1
        out.append(line.replace('\r', ''))
        txt2html = convert2html(out)
        self.update_state(state='PROGRESS', meta={'line': txt2html, 'iter': i})
    client.close()
    return convert2html(out)

@shared_task(bind=True)
def c_goToSleep(self, sec):
    sleep(sec)
    return 'DONE !'


def convert2html(output):
    txt = ansiconv.to_plain('\n'.join(output))
    html = ansiconv.to_html(txt)
    css = ansiconv.base_css()
    return """
            <html>
            <head><style>{0}</style></head>
            <body>
            <pre class="ansi_fore ansi_back">{1}</pre>
            </body>
            </html>
            """.format(css, escape(html))
