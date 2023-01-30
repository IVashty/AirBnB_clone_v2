#!/usr/bin/python3
"""
this  Fabric script shld  generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(date)
    file_path = "version/{}".format(file_name)

    local("mkdir -p versions")
    local("tar -cvzf versions/".format(file_path))
    if local("test -f {}".format(file_path), capture=True).succeeded:
        return file_path
    else:
        return None
