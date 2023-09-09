#!/usr/bin/python3
""" Deploymwnt Module """
import os
from fabric.api import run, env, put

env.hosts = ['54.152.30.192', '54.144.155.174']


def do_deploy(archive_path):
    """Deploys the static files to the host servers."""

    if not os.path.exists(archive_path):
        return False
    filename = archive_path.split('/')[1]
    filepath = f"/data/web_static/releases/{filename.replace('.tgz', '')}/"
    try:
        put(archive_path, "/tmp/")
        run(f"mkdir -p {filepath}")
        run(f"tar -xzf /tmp/{filename} -C {filepath}")
        run(f"rm /tmp/{filename}")
        run(f"mv {filepath}web_static/* {filepath}")
        run(f"rm -rf {filepath}web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {filepath} /data/web_static/current")
        return True
    except Exception:
        return False
