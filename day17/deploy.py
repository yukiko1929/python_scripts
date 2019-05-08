import requests
import wget
import os
import hashlib
import tarfile


def new_ver(ver_fname, ver_url):
    if not os.path.isfile(ver_fname):
        return True

    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    r = requests.get(ver_url)
    remote_ver = r.text

    if local_ver != remote_ver:
        return True
    return False


def has_error(fname, md5_url):
    checked = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            checked.update(data)

    r = requests.get(md5_url)
    if checked.hexdigest() == r.text.strip():
        return False    # intact file, return False
    # os.remove(fname)    #delete broken file
    return True     # means the file is broken


def deploy(app_fname):
    # app_fname = /var/www/download/myweb-1.0.tar.gz
    deploy_dir = '/var/www/deploy'
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall(path=deploy_dir)
    tar.close()
    base = os.path.basename(app_fname)
    base = base.replace('.tar.gz','')
    # fin-name = deploy_dir + base


if __name__ == '__main__':
    app_dir = '/var/www/download'
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.20/deploy/live_ver'
    if not new_ver():
        print('no new version')
        exit(1)

    #otherwise download
    r = requests.get(ver_url)
    ver = r.text.strip()   # get server's file version
    app_url = 'http://192.168.4.20/deploy/download/project1905-%s.tar.gz' % ver
    wget.download(app_url)
    # download latest version
    # next to step ----> to check whether the package is intact
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(app_dir, app_fname)
    md5_file = app_fname + ',md5'
    if has_error(app_fname, md5_file):
        print('broken package')
        os.remove(app_fname)
        exit(2)
    # deploy if no problem'
    # release tar package to deploy directory
