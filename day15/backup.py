#to backup all txt files

import os
import hashlib
import re

def backup(srcdir, destdir, recordfile):



    patt = '.*\.txt'
    cpa = re.compile(patt)
    for path, dirs, files in os.walk(srcdir):
        for file in files:im

