#!/usr/bin/python3
""" Module to pack files into .tgz """
import os
from datetime import datetime
from fabric.api import runs_once, local


@runs_once
def do_pack():
    """ Archives web_static """
    if os.path.exists('versions') or os.mkdir('versions'):
        timestamp = datetime.now()
        out_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                timestamp.year,
                timestamp.month,
                timestamp.day,
                timestamp.hour,
                timestamp.minute,
                timestamp.second
                )

        try:
            print("Packing web_static to {}".format(out_path))
            local("tar -cvzf {} web_static".format(out_path))
            size = os.stat(output).st_size
            print("web_static packed: {} -> {} Bytes".format(out_path, size))
        except Exception:
            out_path = None

        return out_path
