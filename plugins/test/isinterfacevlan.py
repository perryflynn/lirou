# Copyright (c) 2024, Christian Blechert <christian@serverless.industries>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError

DOCUMENTATION = '''
  name: isinterfacevlan
  short_description: Checks if a vlan belongs to a specific interface name
  version_added: 0.1.0
  author: Christian Blechert (@perryflynn)
  description:
    - Checks if a vlan belongs to a specific interface name
  options:
    _input:
      description: VLAN interface definition
      type: dict
      required: true
    lan:
      description: LAN interface to find the VLANs for
      type: dict
      required: true
'''

EXAMPLES = '''
- name: Make sure that vlan belongs to physical interface
  ansible.builtin.assert:
    that: vlan is brickburg.linuxrouter.isinterfacevlan(phy_lan)
'''

RETURN = '''
  _value:
    description: Whether the vlan belongs to the lan.
    type: bool
'''

def isinterfacevlan(vlan, lan):
    """
    Example:
      - vlan is brickburg.linuxrouter.isinterfacevlan(phy_lan)
    """

    if not isinstance(vlan, dict):
        raise AnsibleError(f'vlan requires a dict')

    if not isinstance(lan, dict):
        raise AnsibleError(f'lan requires a dict')

    if vlan['state'] != 'present':
        return False

    if vlan['kind'] != 'vlan' or lan['kind'] != 'interface':
        return False

    if not vlan['vlan']['interface']:
        return False

    return vlan['vlan']['interface'] == lan['name'] or ('aliases' in lan and vlan['vlan']['interface'] in lan['aliases'])


class TestModule(object):
    ''' Ansible test wether VLAN belongs to LAN '''

    def tests(self):
        return {
            'isinterfacevlan': isinterfacevlan,
        }
