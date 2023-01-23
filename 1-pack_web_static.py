#!/usr/bin/python3
"""
this  Fabric script shld  generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "web_static_" + date + ".tgz"
        local("tar -cvzf versions/" + filename + " web_static")
        return "versions/" + filename
    except:
        return None
