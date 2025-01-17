#!/usr/bin/python3
"""Fabric script creates,distributes archive to web-servers"""
from fabric.api import env, put, run
import os.path


env.hosts = ['54.89.182.98', '52.87.20.237']
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ deploy to web server """
    if not os.path.exists(archive_path):
        return False
    try:
        f = archive_path.split("/")[-1]
        name = f.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}{}/'.format(path, name))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(f, path, name))
        run('sudo rm /tmp/{}'.format(f))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run("sudo rm -rf {}{}/web_static".format(path, name))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, name))
        return True
    except e:
        return False
