import pandas as pd
import numpy as np

from lib.database import Database
from lib.step import Step
from lib.utils import *


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

        self.step_list = []
        self.database = None
        self.work_dir = work_dir
        self.script_dir = dir_create(self.work_dir, 'script')
        self.input_dir = dir_create(self.work_dir, 'input')
        self.config_dir = dir_create(self.work_dir, 'config')
        self.workflow_dir = dir_create(self.work_dir, 'workflow')
        self.log = dir_create(self.work_dir, 'log')

    def load_database(self):
        database_path = path_join(self.log, 'database.csv')
        self.database = Database(database_path)

    def create_step(self, step_name, config_file, config_name):
        step = Step(step_name)
        self.step_list.append(step)
        dir_create(self.workflow_dir, step_name)
        step.parse_config(path_join(self.config_dir, config_file), config_name)  # 在config文件夹中寻找config file
        return step

    def creat_pbs(self):
        pass
