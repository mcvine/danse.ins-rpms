# danse.ins-rpms
scripts for creating and uploading rpms to repositories

Steps:
* For each package, clone from github, build it with
  - $ mkdir build && cd build 
  - $ cmake -D DOCKER_PKGING_RPM_DIST_NAME=centos -D DOCKER_PKGING_RPM_DIST_VERSION=7 ..
  - $ make test-rpm
  These commands will build srpm, upload to pkgcloud, download to test; then build rpm,
  upload to pkgcloud, and download to test.
* Run download.py: this will download all rpms listed in pkgs.py to local disk
* Run upload.py: this will upload all rpms listed in pkgs.py to package.sns.gov
