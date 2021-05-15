import paramiko
from django.conf import settings

def remoteActions(app):
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
    client.connect(app, username='appuser', password=psw)
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)

    for line in iter(stdout.readline, ""):
        print(line)
        out.append(line)
    client.close()
    return out 