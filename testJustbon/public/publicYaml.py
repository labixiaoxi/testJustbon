# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/8 10:46
import os,yaml
class PublicGetYaml:

    def __init__(self,path):
        self.path=path

    def get_Yaml(self):
        try:
            with open(self.path,'rb') as f:
                data=f.read()
                result=yaml.load(data,Loader=yaml.FullLoader)
                f.close()
                return result
        except Exception:
            return "未找到yaml文件"


if __name__ == '__main__':
    yaml_path = '../config/login.yaml'
    getYaml = PublicGetYaml(yaml_path)
    print (getYaml.get_Yaml()['loginCase'])
