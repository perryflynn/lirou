# -*- coding: utf-8 -*-

# Copyright (c) 2024, Christian Blechert (@perryflynn)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

DOCUMENTATION = r'''
  name: interfacename
  short_description: Returns the name of a interface from the definition object
  version_added: 0.1.0
  author: Christian Blechert (@perryflynn)
  description:
    - Returns the name of a interface from the definition object
  options:
    _input:
      description: A interface definition object
      type: dictionary
      required: true
'''

EXAMPLES = r'''
  - name: Get the actual interface name
    ansible.builtin.set_fact:
      interface: >-
        {{
            lr.lans[3] | brickburg.linuxrouter.interfacename
        }}
'''

RETURN = '''
  _value:
    description: The interface name
    type: string
'''

__metaclass__ = type

from ansible.errors import AnsibleFilterError


def get_interfacename(obj):
    ''' Returns the actual interface name from a interface definition '''

    if not isinstance(obj, dict):
        raise AnsibleFilterError(f'interfacename requires a dict')

    if obj['kind'] == 'interface' and 'rename' in obj and obj['rename']['enabled'] == True:
        return obj['rename']['name']

    if not ('name' in obj):
        raise AnsibleFilterError(f'interfacename requires a valid interface definition, did not found name property')

    return obj['name']


class FilterModule(object):
    ''' Query filter '''

    def filters(self):

        return {
            'interfacename': get_interfacename
        }
