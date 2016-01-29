#!/usr/bin/env python

"""
download rpms from package cloud.
those rpms were built from each package using cmake, make test-rpm
after downloading them, run upload.py to upload them to packages.sns.gov
"""

# distribution = "fedora"
distribution = "el" # centos
version = 7

# rpm type
# type = "src"
type = "x86_64"

from pkgs import pkgs

import os, sys

for pkg in pkgs:
    rpm = "%(pkg)s-0.%(type)s.rpm" % locals()
    cmd = "wget https://packagecloud.io/danse/ins/packages/%(distribution)s/%(version)s/%(rpm)s/download  -O %(rpm)s" % locals()
    if os.system(cmd):
        print >> sys.stderr, "%s failed" % cmd
