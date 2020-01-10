#!/usr/bin/python3
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        tim = datetime.now()
        name_file = "versions/web_static_{}.tgz".format(tim.strftime("%Y%m%d%H%M%S"))
        local('tar -cvzf {} web_static'.format(name_file))
        return name_file
    except:
        return None
