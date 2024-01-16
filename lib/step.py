import pandas as pd

from lib.utils import *


class Step:
    def __init__(self, step_name, workdir):
        self.name = step_name
        self.script_dir = dir_create(workdir, 'script')
        self.input_dir = dir_create(workdir, 'input')
        self.output_dir = dir_create(workdir, 'output')
        self.log_dir = dir_create(workdir, 'log')
        self.input_dict = None
        self.output_dict = None
        self.config = None
        self.command = None

    def parse_config(self, step_config, config_name):
        """
        通过config_name寻找config中的对应的config 减少文件数量
        :param config_name:
        :param step_config:
        :return:
        """
        self.command = ''
        input_list = []
        output_list = []
        self.config = load_yaml(step_config)[config_name]
        self.input_dict = self.config['path']['input']
        self.output_dict = self.config['path']['output']
        self.command += self.config['command'] + " "
        for setting in self.config['config']:
            if type(setting) is dict:
                for key in setting.keys():
                    value = setting[key]
                    self.command += add_config(key, value)
            else:
                self.command += setting + " "
        return self.command

    def parse_database(self, database):
        input_data_path_list = []
        input_data_name_list = []
        for key in self.input_dict.keys():
            data_type = self.input_dict[key]['type']
            data_step = self.input_dict[key]['step']
            input_data_path_list.append(
                database.loc[(database['type'] == data_type) & (database['step'] == data_step)]['path'])
            input_data_name_list.append(
                database.loc[(database['type'] == data_type) & (database['step'] == data_step)]['name'])
        input_path = merge_list(input_data_path_list)
        input_name = merge_list(input_data_name_list)
        path_frame = pd.DataFrame(input_path, columns=self.input_dict.keys())
        input_name_frame = pd.DataFrame(input_name, columns=self.input_dict.keys())
        new_name_list = []
        for idx, row in input_name_frame.iterrows():
            new_name_list.append('.'.join(row))
        output_frame = pd.DataFrame([], columns=['name', 'type', 'step', 'path'])
        for output in self.config['path']['output'].keys():
            ext = output
            content = self.config['path']['output'][output]
            temp
        path_frame['output_name'] = new_name_list
        return path_frame


if __name__ == '__main__':
    minimap2 = Step('minimap2-asm20', 'E://test-workflow')
    config = load_yaml('D:\\tools\work-manager\config\\temple.yaml')
    print(config)
    command = minimap2.parse_config('D:\\tools\work-manager\config\\temple.yaml', 'minimap2-asm20')
    print(minimap2.input_dict)
    print(minimap2.output_dict)
    print(command)
