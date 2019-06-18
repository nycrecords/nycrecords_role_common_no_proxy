import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_proxy_profile_script_exists(host):
    f = host.file("/etc/profile.d/proxy.sh")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_http_proxy_set(host):
    cmd = host.run("env | grep http_proxy")

    assert cmd.stdout.strip() == "http_proxy=http://bcpxy.nycnet:8080"


def test_https_proxy_set(host):
    cmd = host.run("env | grep https_proxy")

    assert cmd.stdout.strip() == "https_proxy=http://bcpxy.nycnet:8080"


def test_no_proxy_set(host):
    cmd = host.run("env | grep no_proxy")

    assert cmd.stdout.strip() == "no_proxy=localhost,127.0.0.1,::1"

