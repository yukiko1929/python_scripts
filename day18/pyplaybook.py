import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C
from ansible.executor import playbook_executor   # a class to execute


Options = namedtuple(
    'Options',
    [
        'remote_user',
        'ack_pass',
        'sudo_user',
        'forks',
        'sudo_pass',
        'ask_sudo_pass',
        'verbosity',
        'module_path',
        'become',
        'become_method',
        'become_user',
        'check',
        'diff',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax'
    ]
)

options = Options()

loader = DataLoader()   #用于分析文件格式
passwords = dict()   #免密无需密码
inventory = InventoryManager(loader=loader, sources='myansible/hosts')
variable_mamager=VariableManager(loader=loader,)

def runpb(pb_path):
    playbook = playbook_executor(
        playbooks=pb_path,
        inventory=inventory,
        loader=loader,
        options=options,
        passwords=passwords
    )
    result = playbook.run()



