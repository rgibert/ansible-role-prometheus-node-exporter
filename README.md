# Ansible Role - Prometheus blackbox_exporter

![Ansible Role](https://img.shields.io/ansible/role/44232?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-prometheus-node-exporter?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/44232?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/44232?label=downloads&style=flat-square)

## Description

Installs Prometheus's blackbox_exporter

## Requirements

- RHEL or Debian-based OSes

## Role Variables

| Variable | Description |
|----------|-------------|
| prometheus_blackbox_exporter_base_url | Base URL for other variables |
| prometheus_blackbox_exporter_checksum | SHA256 URL for tarball |
| prometheus_blackbox_exporter_dl_url | Tarball download URL |
| prometheus_blackbox_exporter_version | Version to install |
| prometheus_blackbox_exporter_user | User to run the exporter as |
| prometheus_blackbox_exporter_group | Default group for the user to run as |
| prometheus_blackbox_exporter_conf_path | Path to the config file |
| prometheus_blackbox_exporter_port | Port to listen on |
| prometheus_blackbox_exporter_conf_file | Config file |
| prometheus_blackbox_exporter_config | Contents for the configuration file |

## Dependencies

- Ansible Roles:
  - rgibert.user_setup
  - rgibert.single_binary_setup

## Example Playbook

```yaml
- hosts:
    - servers
  roles:
    - role: rgibert.prometheus_blackbox_exporter
      prometheus_blackbox_exporter_version: 0.16.0
```

## License

GPLv3

## Author Information

Richard Gibert  
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
