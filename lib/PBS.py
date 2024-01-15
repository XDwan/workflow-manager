class PBS:
    """
    生成PBS，核心功能就是将Rule及其对应的config文件和data映射到PBS文件中，在这里只管写入line，不管具体的替换细节
    每个PBS设置为一步，生成一个独立的文件夹，其中就包含script，log，output以及workflow的step计数
    """
