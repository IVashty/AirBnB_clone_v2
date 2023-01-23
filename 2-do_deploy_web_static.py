#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:

    Prototype: def do_deploy(archive_path):
    Returns False if the file at the path archive_path doesn’t exist
"""
from fabric.api import *
import os.path
from fabric.operations import run, put, env


env.hosts = ["52.55.249.213", "54.157.32.137"]


def do_deploy(archive_path):
    """
    distribute an archive to the web server
    """
    if exists(archive_path) is False:
        return False

    try:
        file_name = archive_path.split("/")[-1]
        dir_name = file_name.split(".")[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(dir_name))
        run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                file_name, dir_name
            )
        )
        run("rm /tmp/{}".format(file_name))
        run(
            "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
                dir_name, dir_name
            )
        )
        run("rm -rf /data/web_static/releases/{}/web_static".format(dir_name))
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
                dir_name
            )
        )
        return True
    except:
        return False
