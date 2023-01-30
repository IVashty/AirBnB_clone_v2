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
    try:
        if isdir("versions") is False:
            local("mkdir -p versions")
        file_name = "web_static_" + date + ".tgz"
        local("tar -cvzf versions/" + file_name + " web_static")
        return "versions/" + file_name
    except Exception:
        return None
