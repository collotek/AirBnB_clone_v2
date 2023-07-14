#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime


def do_pack():
    """Local execute command to generate a .tgz archive"""
    try:
        local("mkdir -p versions")
        current_day = datetime.now()
        current_time = current_day.strftime("%Y%m%d%H%M%S")
        location = "versions/web_static_{}.tgz".format(current_time)
        local_name = local("tar -cvzf {} web_static".format(location))
        return local_name
    except Exception:
        return None
