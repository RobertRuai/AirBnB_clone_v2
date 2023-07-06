#!/usr/bin/python3
"""Fabric script creates,distributes archive to web-servers"""
from fabric.api import local
from datetime import datetime
import os.path


env.hosts = ['54.82.173.73', '54.237.69.144']
env.user = "ubuntu"

def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        f = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(f))
        return f
    except e:
        return None

def do_deploy(archive_path):
    """ deploy to web server """
    if not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        path = "/data/web_static/releases/".format(name)
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}{}/'.format(path, name))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file, path, name))
        run('sudo rm /tmp/{}'.format(file))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run("sudo rm -rf {}{}/web_static".format(path, name))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, name))
        run('echo "New version deployed!"')
        return True
    except e:
        return False
