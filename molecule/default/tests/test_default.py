import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bin_file(host):
    assert host.file(
        "/usr/local/share/prometheus_blackbox_exporter-0.16.0"
        "/blackbox_exporter-0.16.0.linux-amd64/blackbox_exporter"
    ).exists


def test_service_file(host):
    assert host.file(
        "/etc/systemd/system/prometheus_blackbox_exporter.service"
    ).exists


def test_service_enabled(host):
    assert host.service('prometheus_blackbox_exporter').is_enabled


def test_service_running(host):
    assert host.service('prometheus_blackbox_exporter').is_running
