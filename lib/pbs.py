import pandas as pd
import numpy as np
import os


class PBS:
    """
    生成PBS，核心功能就是将Rule及其对应的config文件和data映射到PBS文件中，在这里只管写入line，不管具体的替换细节
    每个PBS设置为一步，生成一个独立的文件夹，其中就包含script，log，output以及workflow的step计数
    """

    def __init__(self, name, queue, work_dir, nodes, cpu_num):
        self.name = name
        self.work_dir = work_dir
        self.output_dir = os.path.join(work_dir, 'output')
        self.log_path = os.path.join(work_dir, 'log')
        if not os.path.exists(self.work_dir):
            os.mkdir(self.log_path)
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        self.command = [
            "#!/bin/bash \n",
            "",
            f"#PBS -N {name} \n",
            f"#PBS -q {queue} \n",
            f"#PBS -d {work_dir} \n",
            f'#PBS -o {os.path.join(self.log_path, name + ".out")} \n',
            f'#PBS -e {os.path.join(self.log_path, name + ".error")} \n',
            f"#PBS -l nodes={nodes}:ppn={cpu_num} \n",
            "",
        ]
        self.content = []

    def write(self):
        with open(os.path.join(self.work_dir, self.name + ".pbs"), "w") as f:
            print(f"wirte into {os.path.join(self.work_dir, self.name + '.pbs')}")
            f.writelines(self.command)
            for line in self.content:
                f.write(line + " \n")

    def submit(self):
        os.system(f'qsub {os.path.join(self.work_dir, self.name + ".pbs")}')

    def init_conda(self):
        init_info = [
            "",
            "source ~/miniconda3/etc/profile.d/conda.sh",
        ]
        self.content.extend(init_info)

    def activate_conda(self, env):
        self.content.append(f"conda activate {env}")

    def add_commands(self, command, params: pd.DataFrame, add_echo=False):
        for idx, row in params.iterrows():
            temp = command
            echo = add_echo
            for key in params.columns:
                temp = temp.replace("{" + key + "}", row[key])
            if add_echo:
                self.content.append(f'echo "{temp}"')
            self.content.append(temp)
