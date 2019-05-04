import os
import tarfile
# os.chdir('/etc')
# tar = tarfile.open('/tmp/mytets.tar.gz', 'w:gz')
# tar.add('hosts')
# tar.add('security')
# tar.close()

os.mkdir('/tmp/extract')
tar = tarfile.open('/tmp/mytets.tar.gz', 'r:gz')
tar.extractall('/tmp/extract')
tar.close()