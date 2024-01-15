import pandas as pd
import numpy as np
import os

from lib.utils import check_file


class Database:
    """
    管理数据库，每一条数据包含如下信息：
    name：该数据的名称-不唯一标识
    type：该数据的类型 如log paf fa
    step: 该数据输出的step 如 input minimap
    path: 该数据对应的绝对路径
    """

    def __init__(self, database_path):
        if not check_file(database_path):
            self.database = pd.DataFrame([], columns=['name', 'type', 'step', 'path'])
            self.database.to_csv(database_path)
        self.database = pd.read_csv(database_path)

    def database_append(self, new_name, new_type, new_step, new_path):
        record = [new_name, new_type, new_step, new_path]
        self.database.loc[len(self.database)] = record

    def database_expand(self, other):
        self.database = pd.concat([self.database, other], ignore_index=True)


