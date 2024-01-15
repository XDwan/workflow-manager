import pandas as pd
import numpy as np
import os


def dir_create(path, dir_name):
    dir_path = os.path.join(path, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path


def path_join(path, dir_name):
    return os.path.join(path, dir_name)


def check_file(path):
    if os.path.exists(path):
        return True
    return False


class Workflow:
    def __init__(self, work_dir):
        """
        初始化工作流，根据工作文件夹，初始化几个默认的相关文件夹：
        1. script 工作流相关的脚本，程序
        2. input 工作流的所有输入
        3. config 工作流的所有设置
        4. workflow 工作流的所有step
        5. log 工作流的日志记录，也是重启中断的方法
        :param work_dir: 工作文件夹
        """

        self.database = None
        self.work_dir = work_dir
        self.script_dir = dir_create(self.work_dir, 'script')
        self.input_dir = dir_create(self.work_dir, 'script')
        self.config_dir = dir_create(self.work_dir, 'config')
        self.workflow_dir = dir_create(self.work_dir, 'workflow')
        self.log = dir_create(self.work_dir, 'log')

    def load_database(self):
        database_path = path_join(self.log, 'database.csv')
        if check_file(database_path):
            self.database = pd.read_csv(database_path)
        else:
            self.database = pd.DataFrame([], columns=['name', 'type', 'step', 'path'])
            self.database.to_csv(database_path)

