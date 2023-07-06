#!/usr/bin/python3
"""Fabric script creates,distributes archive to web-servers"""

from fabric.api import local
from datetime import datetime

env.hosts = ['54.82.173.73', '54.237.69.144']

def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir versions")
        f = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(f))
        return f
    except:
        return None
