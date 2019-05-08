# import shutil
# from collections import namedtuple
# from ansible.parsing.dataloader import DataLoader
# from ansible.vars.manager import VariableManager
# from ansible.inventory.manager import InventoryManager
# from ansible.playbook.play import Play
# from ansible.executor.task_queue_manager import TaskQueueManager
# import ansible.constants as C
#
#
# def ansible_exec(sources, hosts, modules, cmds):
#     Options = namedtuple('Options',
#                          ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
#                           'diff'])
#     options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
#                       become_user=None, check=False, diff=False)
#
#     # initialize needed objects
#     loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
#     passwords = dict()
#
#     inventory = InventoryManager(loader=loader, sources= sources)  #主机清单所在位置
#
#     variable_manager = VariableManager(loader=loader, inventory=inventory)
#
#     play_source =  dict(
#             name = 'ansible play',
#             hosts = hosts,
#             gather_facts = 'no',
#             tasks = [
#                 dict(action=dict(module= modules, args=cmds), register='shell_out'),
#                 #dict(action=dict(module=modules, args=dict(msg='{{%s_out.stdout}}' % modules)))
#              ]
#         )
#
#     play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
#
#     tqm = None
#     try:
#         tqm = TaskQueueManager(
#                   inventory=inventory,
#                   variable_manager=variable_manager,
#                   loader=loader,
#                   options=options,
#                   passwords=passwords,
#               )
#         result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
#     finally:
#         # we always need to cleanup child procs and the structres we use to communicate with them
#         if tqm is not None:
#             tqm.cleanup()
#
#         # Remove ansible tmpdir
#         shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
#
# if __name__ == '__main__':
#     source = ['/root/PycharmProjects/day17/myansible/hosts']
#     hosts = 'webservers'
#     modules = 'shell'
#     cmds = 'mkdir /tmp/yukiko'
#     ansible_exec(source, hosts, modules, cmds)



import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C


def adhoc(sources, hsots, modules, args):
    Options = namedtuple(
        'Options',
        [
            'connection',
            'module_path',
            'forks',
            'become',
            'become_method',
            'become_user',
            'check',
            'diff'
        ]
    )
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name = 'Ansible run',
        hosts = hsots,
        ga
    )