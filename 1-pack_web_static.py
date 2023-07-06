#!/usr/bin/python3
"""Fabric script creates,distributes archive to web-servers"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    f = "versions/web_static_{}.tgz".format(date)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(f))
        return f
    except e:
        return None
