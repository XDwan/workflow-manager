import yaml


def load_yaml(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def add_config(key, value):
    return key + " " + str(value) + " "


class Step:
    def __init__(self, step_name, step_dir):
        self.name = step_name
        self.config = None
        self.input = None
        self.output = None
        self.command = None

    def parse_config(self, step_config):
        command = ''
        input_list = []
        output_list = []
        config = load_yaml(step_config)[self.name]
        command += config['command'] + " "
        for setting in config['config']:
            print(type(setting))
            if type(setting) is dict:
                for key in setting.keys():
                    print(key)
                    value = setting[key]
                    command += add_config(key, value)
            else:
                command += setting + " "
        self.command = command
        return command


if __name__ == '__main__':
    minimap2 = Step('minimap2-asm20', 'D:\\tools\work-manager\config\\temple.yaml')
    config = load_yaml('D:\\tools\work-manager\config\\temple.yaml')
    print(config)
    command = minimap2.parse_config('D:\\tools\work-manager\config\\temple.yaml')
    print(command)
