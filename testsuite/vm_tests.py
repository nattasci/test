#!/usr/bin/env python3

from cibase import CIBaseTest

class VmTestsRemoteRepo(CIBaseTest):

    """
    Test commands in VM over SSH

    :avocado: tags=vmtests-remote-repo
    """
    # Test login prompt
    def test_getty(self):
        self.init("/build")
        self.vm_start('arm64','bullseye', image='keb-debug-image', \
                       cmd='sleep 10 && systemctl is-active getty.target')
    
    # Test watchdog service
    def test_watchdog_service(self):
        self.init("/build")
        self.vm_start('arm64','bullseye', image='keb-debug-image', \
                      cmd='sleep 10 && systemctl is-active watchdog.service')
