# lirou Architecture

Architecture principles for lirou.

## No custom configuration services

The idea behind lirou is to avoid custom configuration scripts and anything which cannot be archieved with
a classic Debian Stable and systemd as far as possible. No dark magic, any configuration should be understandable
for a Network Admin / Debian User.

At any point it must be possible to stop using the lirou Ansible code and make manual changes to the system.

## Use systemd if possible

The event driven design and dependency management of systemd solves alot problems older router systemd had.
It is possible to start services / trigger scripts if an interface was created, also literally any type of
interface can be create and managed with systemd-networkd. networkd-dispatcher can be used to trigger scripts
when the state of an interface changes (a new IP was assigned for example).

## Do not rename interfaces

Renaming a interface is only possible once. So if a router is configured once, renaming a interface is only possible
with a reboot. But keeping the original interface name and add altnames, is always possible. So use a systemd unit
or script to add aliases as altnames to an interface right after the interface was created.
