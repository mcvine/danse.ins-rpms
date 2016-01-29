#!/usr/bin/env python

import os

server = "lj7@packages.sns.gov"
# srcroot = "/var/lib/mock/epel-7-x86_64/result"
srcroot = os.path.abspath(".")
# destroot = "/var/www/html/distros/rhel/7/danse/ins"
destroot = "/var/www/html/distros/rhel/7/sns"
archs = [
    # name, source filename template, destname directory
    ('src', '%(pkg)s.src.rpm', "SRPMS"),
    ('x86_64', '%(pkg)s.x86_64.rpm', 'RPMS/x86_64'),
    # ('debuginfo', '%(name)s-debuginfo-%(version)s.x86_64.rpm', 'RPMS/debuginfo'),
]

import sys, os
name = sys.argv[1]
version = sys.argv[2]
pkg = '%s-%s' % (name, version)

for arch, src_template, dest_dir in archs:
    fn = src_template % locals()
    src = os.path.join(srcroot, fn)
    dest = os.path.join(destroot, dest_dir)
    cmd = "scp %(src)s %(server)s:%(dest)s" % locals()
    if os.system(cmd):
        print >>sys.stderr, "%s failed" % cmd
    continue
