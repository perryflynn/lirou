# linux-router

> *SaaR - systemd as a Router*

Router based on good ol' classic Debian Stable.

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

## Install

- Get a router board
- Install Debian stable or testing on it
- Download this collection
- Create a [config file](./config-example.yml)
- Add the router board to your inventory:

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
