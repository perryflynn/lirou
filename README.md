# linux-router

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

### ath10k does not change country code

The country of the wireless card cannot be changed. It's always US or UNSET.

The wireless-regdb is signed and the default debian kernel only accept untouched
and signed regdbs. 

Options:

- Rebuild whole kernel without regdb crypto
- Patch `ath` kernel module [like so](https://github.com/twisteroidambassador/arch-linux-ath-user-regd/issues/1)

```
ii  wireless-regdb                   2022.06.06-1                   all          wireless regulatory database for Linux
ii  firmware-atheros                 20230210-5                     all          Binary firmware for Qualcomm Atheros wireless cards
```

```
~# cat /boot/config-6.4.0-3-amd64 | grep 'CFG80211' | grep -v '#'
CONFIG_CFG80211=m
CONFIG_CFG80211_REQUIRE_SIGNED_REGDB=y
CONFIG_CFG80211_USE_KERNEL_REGDB_KEYS=y
CONFIG_CFG80211_DEFAULT_PS=y
CONFIG_CFG80211_CRDA_SUPPORT=y
CONFIG_CFG80211_WEXT=y
CONFIG_CFG80211_WEXT_EXPORT=y
```

```
~# cat /etc/modprobe.d/cfg80211.conf
options cfg80211 internal_regdb=y
options cfg80211 crda_support=y
options cfg80211 ieee80211_regdom=DE
```

```
05:00.0 Network controller: Qualcomm Atheros QCA986x/988x 802.11ac Wireless Network Adapter
```

```
ath: EEPROM regdomain: 0x0
ath: EEPROM indicates default country code should be used
ath: doing EEPROM country->regdmn map search
ath: country maps to regdmn code: 0x3a
ath: Country alpha2 being used: US
ath: Regpair used: 0x3a
ath10k_pci 0000:05:00.0 wlp5s0: renamed from wlan0
ath10k_pci 0000:05:00.0: pdev param 0 not supported by firmware
```

```
~# iw reg get
global
country 98: DFS-UNSET
        (2400 - 2472 @ 40), (N/A, 20), (N/A)
        (5150 - 5250 @ 100), (N/A, 23), (N/A), NO-OUTDOOR, AUTO-BW
        (5250 - 5350 @ 100), (N/A, 20), (0 ms), NO-OUTDOOR, DFS, AUTO-BW
        (5470 - 5725 @ 160), (N/A, 24), (0 ms), DFS
        (5725 - 5730 @ 5), (N/A, 13), (0 ms), DFS
        (5730 - 5850 @ 80), (N/A, 13), (N/A)
        (5850 - 5875 @ 25), (N/A, 13), (N/A), NO-OUTDOOR, PASSIVE-SCAN
        (5945 - 6425 @ 160), (N/A, 12), (N/A), NO-OUTDOOR, PASSIVE-SCAN
        (57240 - 66000 @ 2160), (N/A, 40), (N/A)

phy#0
country US: DFS-FCC
        (902 - 904 @ 2), (N/A, 30), (N/A)
        (904 - 920 @ 16), (N/A, 30), (N/A)
        (920 - 928 @ 8), (N/A, 30), (N/A)
        (2400 - 2472 @ 40), (N/A, 30), (N/A)
        (5150 - 5250 @ 80), (N/A, 23), (N/A), AUTO-BW
        (5250 - 5350 @ 80), (N/A, 24), (0 ms), DFS, AUTO-BW
        (5470 - 5730 @ 160), (N/A, 24), (0 ms), DFS
        (5730 - 5850 @ 80), (N/A, 30), (N/A), AUTO-BW
        (5850 - 5895 @ 40), (N/A, 27), (N/A), NO-OUTDOOR, AUTO-BW, PASSIVE-SCAN
        (5925 - 7125 @ 320), (N/A, 12), (N/A), NO-OUTDOOR, PASSIVE-SCAN
        (57240 - 71000 @ 2160), (N/A, 40), (N/A)
```

## Resources

Wifi, hostapd etc:

- https://medium.com/@renaudcerrato/how-to-setup-a-virtual-ssid-with-hostapd-804c13c9a3c2
- https://linuxiswonderful.wordpress.com/2016/06/20/wifi-access-point-and-station-on-same-chip/
