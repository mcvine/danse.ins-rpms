#!/usr/bin/env python

import os
from pkgs import pkgs

# $ ./upload-to-package.sns.gov.py danse.ins 0.1-0

for pkg in pkgs:
    name, version = pkg.split('-')
    cmd = "./upload-to-package.sns.gov.py %(name)s %(version)s-0" % locals()
    if os.system(cmd):
        print "* Failed: %s" % cmd
    continue
