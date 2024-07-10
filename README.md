# linux-router

> *SaaR - systemd as a Router*

Router based on good ol' classic Debian Stable, but with systemd as network- and service management.

## Current State

Interfaces, WAN Interface / SNAT / Masquerade, DHCP/DNS, Wifi and Routing works, 
Firewall just one static ruleset. Basic support for DNAT.

The project in general, is a work-in-progress.

## Features

⬜ = open; 🟨 = wip; ✅ = done

Architecture:

- ✅ Copy + Execute Ansible on the router (it's getting stuck on IP changes right now)

OS:

- ✅ Install packages
- ✅ Set hostname
- ✅ Root password + SSH keys
- ✅ vimrc
- ✅ htoprc
- ✅ lm-sensors
- ✅ SMART
- ✅ Kernel Flags

Interfaces:

- ✅ LAN Interfaces (systemd-networkd)
- ✅ Bridges (systemd-networkd)
- ✅ Wifi Interfaces (systemd-networkd)
- ✅ Software Wifi Interfaces (systemd-networkd)
- ✅ WPA_Supplicant (systemd-networkd)
- ✅ hostapd Wifi APs including 5GHz 802.11ac
- ✅ LAN as WAN/Upstream interface (systemd-networkd)
- ✅ Wifi Client as WAN/Upstream interface (systemd-networkd)
- ✅ Additional interface IPs (systemd-networkd)
- ✅ networkd-dispatcher for interface event scripts

DHCP:

- ✅ DHCP Client (systemd-networkd)
- ✅ DHCP Server (dnsmasq)
- ✅ DNS Server (dnsmasq)

Firewall:

- ✅ Very basic nftables setup with one WAN and multiple LAN interfaces
- ✅ SNAT / Masquerade
- ✅ DNAT

Services:

- ✅ DynDNS via nsupdate

Hardware:

- ✅ PCEngines: Serial Console + `flashrom`

TODO:

- ⬜ https://wiki.ubuntuusers.de/overlayroot/
- ⬜ NTP
- ⬜ DHCP -> nsupdate for leases
- ⬜ VDSL
- ⬜ OpenVPN Server
- ⬜ OpenVPN Client
- ⬜ Fancy config for Firewall rules
- ⬜ Fancy configs for Port forwarding
- ⬜ Check_MK Monitoring
- ⬜ IPv6

## Open Issues

- [ath10k does not change country code](./README-wifi.md)
- No support for static default gateways
- nftables sets always masquerade on default gateway

## Install

- Get a router board
- Install Debian stable or testing on it
- Download this collection into your Ansible environment 
  (something like `collections/ansible_collections/brickburg/linuxrouter`)
- Ensure the `collections_paths` config parameter in your `ansible.cfg`
- Create a [config file](./config-example.yml)
- Add the router board to your Ansible inventory:

```yml
linuxrouter:
  ansible_host: '192.168.42.177'
  ansible_become: no
  ansible_ssh_user: root
  lirou_configfile: "{{(inventory_dir + '/../linux-router/config-myrouter.yml') | realpath}}"
```

- Deploy ansible, code and config to the router: `ansible-playbook -i your/inventory brickburg.linuxrouter.deploy --limit linuxrouter`
- Login to the router as root
- Execute `lirou-apply.sh`

## Config Schema

- Install the VSCode extension `redhat.vscode-yaml`
- Configure schema:

```json
{
    "yaml.schemas": {
        "collections/ansible_collections/brickburg/linuxrouter/lirou-config-schema.json": "lirou-config-*.yml"
    }
}
```

## Credits

This code was created by Christian Blechert <[christian@serverless.industries](mailto:christian@serverless.industries)>.

## License

This code is published under [GPL v3](./LICENSE.txt).
