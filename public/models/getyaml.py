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
            yamlData = yaml.load(file)
            file.close()
            return yamlData
        except Exception as ex:
            log.error('yaml文件,数据读取失败------>%s' % ex)

    # 类内部使用，获取yaml的所有数据
    def get_yaml_data(self):
        return self.get_yaml()

    # 获取elementParam项中的element_info
    def get_element_info(self,index):
        data = self.get_yaml_data()
        return data['elementParam'][index]['element_info']

    # 获取elementParam项中的find_type
    def get_find_type(self,index):
        data = self.get_yaml_data()
        return data['elementParam'][index]['find_type']

    # 获取elementParam项中的operate_type
    def get_operate_type(self,index):
        data = self.get_yaml_data()
        return data['elementParam'][index]['operate_type']

    # 获取elementParam项中的info
    def get_info(self,index):
        data = self.get_yaml_data()
        return data['elementParam'][index]['info']

    # 获取check项中的element_info
    def get_check_info(self,index):
        data = self.get_yaml_data()
        return data['check'][index]['element_info']

    # 获取check项中的find_type
    def get_check_find_type(self,index):
        data = self.get_yaml_data()
        return data['check'][index]['find_type']

    # 获取check项中的info
    def get_check_info(self,index):
        data = self.get_yaml_data()
        return data['check'][index]['info']