#!/usr/bin/python3
""" Deploymwnt Module """
import os.path
from fabric.api import run, env, put


env.hosts = ['54.152.30.192', '54.144.155.174']


def do_deploy(archive_path):
    '''Upload achive to web servers'''
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        path_no_ext = '/data/web_static/releases/{}/'.format(no_ext)
        symlink = '/data/web_static/current'
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path_no_ext))
        run('tar -xzf /tmp/{} -C {}'.format(filename, path_no_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(path_no_ext, path_no_ext))
        run('rm -rf {}web_static'.format(path_no_ext))
        run('rm -rf {}'.format(symlink))
        run('ln -s {} {}'.format(path_no_ext, symlink))
        return True
    except Exception:
        return False
