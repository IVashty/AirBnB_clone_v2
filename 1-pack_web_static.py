#!/usr/bin/python3
"""
this  Fabric script shld  generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """
    archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkdir -p versions")
        filename = "web_static_" + date + ".tgz"
        local("tar -cvzf versions/" + filename + " web_static")
        return "versions/" + filename
    else:
        return None
