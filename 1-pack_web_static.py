#!/usr/bin/python3
"""
this  Fabric script shld  generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    archive created must be:
    web_static_<year><month><day><hour><minute><second>.tgz
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file_name = "web_static_" + date + ".tgz"
    local("tar -cvzf versions/ webstatic" + file_name)

    if local("ls versions/" + file_name, capture=True).succeeded:
        return "versions/" + file_name
    else:
        return None
