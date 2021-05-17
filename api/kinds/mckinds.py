"""
"""
import yaml
import os
import subprocess
from pathlib import Path
from ..dbconnect import connection as conn

class CustomResource(object):
    """
    """
    def __init__(self, name, operator=None, definition=None):
        """
        """
        self.name = name
        self.operatorname = operator
        self.definition = definition
 
    def create(self, yaml_definition):
        """
        """
        try:
            resources_path = os.path.join(Path(os.path.dirname(__file__)).parent.parent, "resources")
            full_path = os.path.join(resources_path, self.name+".yaml")
            with open(full_path, 'w') as file:
                yaml.dump(yaml_definition, file)
            cursr = conn.cursor()
            query = f'INSERT INTO resources VALUES ("{self.name[0:7]}", "{self.name}", \
                        "{self.operatorname}", "{full_path}")'
            cursr.execute(query)
            conn.commit()
        except Exception as ex:
            print(ex)
            raise ex

    def update(self, yaml_definition):
        """
        """
        try:
            resources_path = os.path.join(Path(os.path.dirname(__file__)).parent.parent, "resources")
            full_path = os.path.join(resources_path, self.name+".yaml")
            with open(full_path, 'w') as file:
                yaml.dump(yaml_definition, file)
        except Exception as ex:
            print(ex)
            raise ex
    

    def deploy(self):
        """
        """
        try:
            query = f"select path from resources where name='{self.name}'"
            cursr = conn.cursor()
            cursr.execute(query)
            path = cursr.fetchone()['path']
            output = subprocess.run(["kubectl", "apply", "-f", path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            return output.stdout or output.stderr
        except Exception as ex:
            print(ex)
            raise ex

    def get(self):
        """
        """
        try:
            query = f"select path from resources where name='{self.name}'"
            cursr = conn.cursor()
            cursr.execute(query)
            path = cursr.fetchone()['path']
            with open(path, 'r') as file:
                yaml_defintion = yaml.load(file)
            return yaml_defintion
        except Exception as ex:
            print(ex)
            raise ex

    def delete(self):
        """
        """
        try:
            query = f"select path from resources where name='{self.name}'"
            cursr = conn.cursor()
            cursr.execute(query)
            path = cursr.fetchone()['path']
            output = subprocess.run(["kubectl", "delete", "-f", path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            return output.stdout or output.stderr
        except Exception as ex:
            print(ex)
            raise ex
