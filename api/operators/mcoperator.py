"""
"""
import os
from pathlib import Path

class Operator(object):
    """
    """
    def __init__(self, name, install_commands, operatorhub_link, uninstall_commands=None):
        """
        """
        self.name = name
        self.install_commands = install_commands
        self.link_to_operatorhub = operatorhub_link
        self.kinds = None
        self.uninstall_commands = uninstall_commands
        # place holder for more parameters to come

    def install(self):
        """
        """
        pass

    def uninstall(self, uninstall_commands):
        """
        """
        pass

    def register(self):
        """
        """
        playbooks_path = os.path.join(Path(os.path.dirname(__file__)).parent.parent, "playbooks")
        file_name = self.name + "_install.sh"
        

    def unregister(self):
        """
        """
        pass
