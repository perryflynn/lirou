# Copyright (c) 2024, Christian Blechert <christian@serverless.industries>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError

DOCUMENTATION = '''
  name: isinterfacebridge
  short_description: Checks if a bridge uses a given interface as member
  version_added: 0.1.0
  author: Christian Blechert (@perryflynn)
  description:
    - Checks if a bridge uses a given interface as member
  options:
    _input:
      description: Bridge interface definition
      type: dict
      required: true
    lan:
      description: LAN interface to find the Bridge for
      type: dict
      required: true
'''

EXAMPLES = '''
- name: Make sure that bridge uses given interface as member
  ansible.builtin.assert:
    that: bridge is brickburg.linuxrouter.isinterfacebridge(phy_lan)
'''

RETURN = '''
  _value:
    description: Whether the bridge has the interface as member
    type: bool
'''

def isinterfacebridge(bridge, lan):
    """
    Example:
      - bridge is brickburg.linuxrouter.isinterfacebridge(phy_lan)
    """

    if not isinstance(bridge, dict):
        raise AnsibleError(f'bridge requires a dict')

    if not isinstance(lan, dict):
        raise AnsibleError(f'lan requires a dict')

    if bridge['state'] != 'present':
        return False

    if bridge['kind'] != 'bridge' or lan['kind'] == 'bridge':
        return False

    if 'interfaces' not in bridge['bridge']:
        return False

    return lan['name'] in bridge['vlan']['interfaces'] or ('aliases' in lan and len(list(set(lan['aliases']) & set(bridge['vlan']['interfaces']))) > 0)


class TestModule(object):
    ''' Ansible test wether VLAN belongs to LAN '''

    def tests(self):
        return {
            'isinterfacebridge': isinterfacebridge,
        }
