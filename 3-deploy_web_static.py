#!/usr/bin/python3
"""
now deploy the archive
"""
from fabric.api import *
import os
from fabric.operations import run, put, env


env.hosts = ["52.55.249.213", "54.157.32.137"]


def deploy():
    """
    deploys the archive to the web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
