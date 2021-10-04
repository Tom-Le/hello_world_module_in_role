#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: say_hello_world

short_description: Say 'Hello world!'

version_added: "1.0.0"

description: Say 'Hello world!' or a message of your choice.

author:
    - Son Le (@Tom-Le)
'''

EXAMPLES = r'''
- name: Test with a message
  leson_dev.ansible_module_in_role_test.say_hello_world:
    message: Hello friends!
'''

RETURN = r'''
message: I said "Hello world!"
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        message=dict(type='str', required=False),
    )

    result = dict(
        changed=False,
        message='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result['message'] = "I said \"" + module.params['message'] + "\""
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
