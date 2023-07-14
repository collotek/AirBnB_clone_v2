#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime


def do_pack():
    """Local execute command to generate a .tgz archive"""
    local("mkdir -p versions")
    current_day = datetime.now()
    current_time = current_day.strftime("%Y%m%d%H%M%S")
    location = "versions/web_static_{}.tgz".format(current_time)
    local_name = ("tar -czvf web_static {} web_static".format(location))
    if local_name.succeeded is False:
        return None
    return local_name
