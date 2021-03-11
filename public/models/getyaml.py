import yaml
from public.models import log

log = log.Log()


# 获取yaml数据
class getYaml():

    # 初始化，获取yaml文件路径
    def __init__(self, filePath):
        self.filePath = filePath

    # 获取yaml数据对象
    def get_yaml(self):
        try:
            file = open(self.filePath, encoding='UTF-8')
            yamlDate = yaml.load(file)
            file.close()
            return yamlDate
        except Exception as ex:
            log.error('yaml文件,数据读取失败------>%s' % ex)