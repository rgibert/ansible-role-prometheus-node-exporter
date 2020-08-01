# Prometheus node_exporter

![Ansible Role](https://img.shields.io/ansible/role/44232?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-prometheus-node-exporter?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/44232?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/44232?label=downloads&style=flat-square)

## Description

Installs Prometheus's node_exporter

## Requirements

- ArchLinux, RHEL, or Debian

## Role Variables

| Variable | Description |
|----------|-------------|
| prometheus_node_exporter_args | Additional arguments to provide to the binary |
| prometheus_node_exporter_base_url | Base URL for other variables |
| prometheus_node_exporter_checksum | SHA256 URL for tarball |
| prometheus_node_exporter_dl_url | Tarball download URL |
| prometheus_node_exporter_group | Default group for the user to run as |
| prometheus_node_exporter_user | User to run the exporter as |
| prometheus_node_exporter_version | Version to install |

## Dependencies

- rgibert.single_binary_service

## Example Playbook

```yaml
- hosts:
    - servers
  roles:
    - role: rgibert.prometheus_node_exporter
      prometheus_node_exporter_version: 1.0.1
```

## License

GPLv3

## Author Information

Richard Gibert  
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
