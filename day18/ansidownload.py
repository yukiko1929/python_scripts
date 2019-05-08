from ansible.module_utils.basic import AnsibleModule
import wget

def download():
    module = AnsibleModule(
        argument_spec=dict(
            sour=dict(required=True,type='str'),
            desti=dict(required=True,type='str')
        )
    )
    wget.download(module.params['url'], module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    download()