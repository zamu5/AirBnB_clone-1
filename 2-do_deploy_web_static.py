#!/usr/bin/python3
# distributes an archive to web servers
import os
from fabric.api import *

env.hosts = ['34.73.43.83', '104.196.6.178']
env.user = "ubuntu"


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        name_c = archive_path.split('/')
        name_c = name_c[-1]
        name_file = name_c.split('.')
        name_f = "/data/web_static/releases/{}".format(name_file[0])
        run("mkdir -p {}".format(name_f))
        run("tar -xzf /tmp/{} -C {}".format(name_c, name_f))
        run("rm /tmp/{}".format(name_c))
        run("mv {}/web_static/* {}".format(name_f, name_f))
        run("rm -rf {}/web_static".format(name_file))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(name_f))
        return True
    except:
        return False
