"""
"""
import os
import subprocess
import pymysql.cursors
from pathlib import Path
from ..dbconnect import connection as conn
import shutil


def get_all_operators():
    """
    """
    try:
        cursr = conn.cursor()
        query = f'select * from operators'
        cursr.execute(query)
        full_data = cursr.fetchone()
        return full_data
    except Exception as ex:
        print(ex)


class Operator(object):
    """
    """
    def __init__(self, name, install_commands=None, operatorhub_link=None, uninstall_commands=None):
        """
        """
        self.name = name
        self.install_commands = install_commands
        self.link_to_operatorhub = operatorhub_link
        self.kinds = None
        self.uninstall_commands = uninstall_commands
        self.full_path = None
        # place holder for more parameters to come

    def register(self):
        """
        """
        try:
            playbooks_path = os.path.join(Path(os.path.dirname(__file__)).parent.parent, "playbooks")

            install_file_name = self.name + "_install.sh"
            
            full_path = os.path.join(playbooks_path, self.name)

            if not os.path.exists(full_path):
                try:
                    os.makedirs(full_path)
                    os.chmod(full_path, 0o777)
                except Exception as ex:
                    raise ex

            install_file = os.path.join(full_path, install_file_name)
            
            with open(install_file, "w+") as installfile:
                for command in self.install_commands:
                    installfile.write(command + '\n')
            
            os.chmod(install_file, 0o777)

            uninstall_file_name = self.name + "_uninstall.sh"
            uninstall_file = os.path.join(full_path, uninstall_file_name)

            with open(uninstall_file, "w+") as installfile:
                for command in self.uninstall_commands:
                    installfile.write(command + '\n')
            
            os.chmod(uninstall_file, 0o777)

            self.full_path = full_path

            cursr = conn.cursor()
            query = f'INSERT INTO operators VALUES ("{self.name}", "{full_path}")'
            cursr.execute(query)
            conn.commit()
        except Exception as ex:
            print(ex)
            raise ex

    def install(self):
        """
        """
        try:
            cursr = conn.cursor()
            query = f'select path from operators where name="{self.name}"'
            cursr.execute(query)
            full_path = cursr.fetchone()['path']
            install_path = os.path.join(full_path, self.name+"_install.sh")
            subprocess.call(install_path, shell=True)
        except Exception as ex:
            print(ex)
            raise ex

    def uninstall(self):
        """
        """
        try:
            cursr = conn.cursor()
            query = f'select path from operators where name="{self.name}"'
            cursr.execute(query)
            full_path = cursr.fetchone()['path']
            uninstall_path = os.path.join(full_path, self.name+"_uninstall.sh")
            subprocess.call(uninstall_path, shell=True)
        except Exception as ex:
            print(ex)
            raise ex

    def delete(self):
        """
        """
        try:
            # Make sure it is uninstalled
            cursr = conn.cursor()
            query = f'select path from operators where name="{self.name}"'
            cursr.execute(query)
            full_path = cursr.fetchone()['path']
            shutil.rmtree(full_path)
            cursr = conn.cursor()
            query = f'delete from operators where name="{self.name}"'
            cursr.execute(query)
            conn.commit()
        except Exception as ex:
            print(ex)
            raise ex

    def get(self):
        """
        """
        try:
            cursr = conn.cursor()
            query = f'select * from operators where name="{self.name}"'
            cursr.execute(query)
            full_data = cursr.fetchone()
            return full_data
        except Exception as ex:
            print(ex)
            raise ex
