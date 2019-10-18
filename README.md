# Prometheus node_exporter

Installs Prometheus's node_exporter

## Requirements

- none

## Role Variables

| Variable | Description |
|----------|-------------|
| prometheus_node_exporter_version | Version to install |
| prometheus_node_exporter_base_url | Base URL for other variables |
| prometheus_node_exporter_dl_url | Tarball download URL |
| prometheus_node_exporter_sha256_url | SHA256 URL for tarball |

## Dependencies

- none

## Example Playbook

```yaml
- hosts:
    - servers
  roles:
    - role: rgibert.prometheus_node_exporter
      prometheus_node_exporter_version: 0.18.1
```

## License

GPLv3

## Author Information

Richard Gibert
[richard@gibert.ca](mailto:richard@gibert.ca)
[https://richard.gibert.ca/](https://richard.gibert.ca/)
