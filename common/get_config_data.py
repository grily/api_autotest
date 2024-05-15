# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022/6/27 15:38
@Author: guozg
@File：get_config_data.py
"""
import os,yaml
from threading import Lock,RLock
cur_path = os.path.dirname(os.path.realpath(__file__))
proj_path = os.path.dirname(cur_path)

from common.conf_yml_mapping import ConfYmlMapping

class GetConfData():
    '''
    获取配置文件数据，对各自的路径进行拼接。调用方式如下: \n
    confdata = GetConfData.get_instance()  \n
    confdata.get_case_dir_path()
    '''

    # __instance_lock = Lock()
    __instance_lock = RLock()
    __instance = None

    def __new__(cls, *args, **kwargs):
        raise ImportError("不允许实例化")

    # 注意原来为__init__()，此时就不能进行初始化了。要变更为普通的函数。
    def __init(self):
        self.__mapping = ConfYmlMapping()
        self.__yml = "config/config.yml"
        self.__conf_yml_fp = os.path.join(proj_path,self.__yml)
        # 获取config.yml文件的中内容
        self.__conf_yml_data = self.get_conf_yml_data()
        # 获取dir_conf key对应的数据
        self.__dirconf_dict = self.get_dirconf_data()
        # 获取http_conf key 对应的数据
        self.__httpconf_dict = self.get_httpconf_data()

    @classmethod
    def get_instance(cls):
        # 使用with 可以自动进行加锁和释放锁。因为有可能会出现多线程同时实例化操作。
        with cls.__instance_lock:
            if cls.__instance == None:
                cls.__instance = super().__new__(cls)
        # 进行“初始化”
        cls.__instance.__init()
        return cls.__instance

    def get_conf_yml_data(self) -> dict:
        '''获取config.yml文件的内容'''
        return yaml.safe_load(open(self.__conf_yml_fp,'r',encoding='utf-8'))

    # ****************** dir_conf 模块的数据 **************************
    def get_dirconf_data(self)->dict:
        '''获取dir_conf 相关的数据'''
        data = self.__conf_yml_data
        key = self.__mapping.get_dir_conf_key()
        return data.get(key)

    def get_case_dir_path(self):
        '''获取case目录路径'''
        key = self.__mapping.get_case_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_caseyml_dir_path(self):
        '''获取caseyml目录路径'''
        key = self.__mapping.get_caseyml_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_common_dir_path(self):
        '''获取common目录路径'''
        key = self.__mapping.get_common_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_config_dir_path(self):
        '''获取config目录路径'''
        key = self.__mapping.get_config_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_reporttmp_dir_path(self):
        '''获取临时report目录路径'''
        key = self.__mapping.get_report_tmp_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_report_dir_path(self):
        '''获取report目录路径'''
        key = self.__mapping.get_report_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_requestdata_dir_path(self):
        '''获取requestdata目录路径'''
        key = self.__mapping.get_requestdata_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_responsedata_dir_path(self):
        '''获取responsedata目录路径'''
        key = self.__mapping.get_responsedata_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_runlog_dir_path(self):
        '''获取runlog目录路径'''
        key = self.__mapping.get_runlog_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    def get_upload_data_dir_path(self):
        key = self.__mapping.get_uploaddata_key()
        data = self.__dirconf_dict
        return os.path.join(proj_path,data.get(key))

    # ****************** http_conf 模块的数据 **************************
    def get_httpconf_data(self)->dict:
        key = self.__mapping.get_http_conf_key()
        data = self.__conf_yml_data
        return data.get(key)

    def get_procotol(self):
        key = self.__mapping.get_procotol_key()
        data = self.__httpconf_dict
        return data.get(key)

    # def get_host(self):
    #     key = self.__mapping.get_host_key()
    #     data = self.__httpconf_dict
    #     return data.get(key)

    def get_useragent(self):
        key = self.__mapping.get_useragent_key()
        data = self.__httpconf_dict
        return data.get(key)

    def get_v5login_moduleflag(self):
        key = self.__mapping.get_v5login_moduleflag_key()
        data = self.__httpconf_dict
        return data.get(key)
    
    def get_v6console_moduleflag(self):
        key = self.__mapping.get_v6console_moduleflag_key()
        data = self.__httpconf_dict
        return data.get(key)
    
    def get_v5login_testhost(self):
        key = self.__mapping.get_v5login_testhost_key()
        data = self.__httpconf_dict
        return data.get(key)
    
    def get_v5login_relhost(self):
        key = self.__mapping.get_v5login_relhost_key()
        data = self.__httpconf_dict
        return data.get(key)
    
    def get_v5login_prodhost(self):
        key = self.__mapping.get_v5login_prodhost_key()
        data = self.__httpconf_dict
        return data.get(key)

    def get_v6console_testhost(self):
        key = self.__mapping.get_v6console_testhost_key()
        data = self.__httpconf_dict
        return data.get(key)

    def get_v6console_relhost(self):
        key = self.__mapping.get_v6console_relhost_key()
        data = self.__httpconf_dict
        return data.get(key)

    def get_v6console_prodhost(self):
        key = self.__mapping.get_v6console_prodhost_key()
        data = self.__httpconf_dict
        return data.get(key)

    def get_cur_host_flag(self):
        key = self.__mapping.get_cur_host_flag_key()
        data = self.__httpconf_dict
        '''
        要支持从jenkins传过来的参数
        '''
        jenkins_data = os.getenv(key)
        data_tmp = data.get(key)
        if jenkins_data != None and jenkins_data.replace(" ","") !="":
            jenkins_data = jenkins_data.lower()
            if "test" in jenkins_data or "测试"  in jenkins_data:
                data_tmp = "test"
            elif "rel" in jenkins_data or "灰度" in jenkins_data or "预生产" in jenkins_data:
                data_tmp = "rel"
            elif "prod" in jenkins_data or "生产" in jenkins_data or "正式" in jenkins_data:
                data_tmp ="prod"
        return data_tmp



if __name__ == "__main__":
    data = GetConfData.get_instance()
    print(f"\n{'*' * 16} dir_conf 模块 {'*' * 16}")
    print(data.get_conf_yml_data())
    print(data.get_dirconf_data())
    print(data.get_case_dir_path())
    print(data.get_caseyml_dir_path())
    print(data.get_common_dir_path())
    print(data.get_config_dir_path())
    print(data.get_reporttmp_dir_path(),os.path.exists(data.get_reporttmp_dir_path()))
    print(data.get_report_dir_path())
    print(data.get_requestdata_dir_path())
    print(data.get_responsedata_dir_path())
    print(data.get_runlog_dir_path())
    print(data.get_upload_data_dir_path())
    print(f"\n{'*'*16} http_conf 模块 {'*'*16}")
    print(data.get_httpconf_data())
    print(data.get_procotol())
    # print(data.get_host())
    print(data.get_useragent())
    
    print(data.get_v5login_moduleflag())
    print(data.get_v5login_testhost())
    print(data.get_v5login_relhost())
    print(data.get_v5login_prodhost())


    print(data.get_v6console_moduleflag())
    print(data.get_v6console_testhost())
    print(data.get_v6console_relhost())
    print(data.get_v6console_prodhost())

    print(data.get_cur_host_flag())



