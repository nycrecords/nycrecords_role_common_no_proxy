import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_rhsm_subscription_current(host):
    cmd = host.run("sudo subscription-manager status")

    assert "Overall Status: Current" in cmd.stdout


def test_rhscl_repos_enabled(host):
    cmd = host.run("sudo subscription-manager repos --list-enabled")

    assert "rhel-server-rhscl-7-rpms" in cmd.stdout
    assert "rhel-7-server-optional-rpms" in cmd.stdout
