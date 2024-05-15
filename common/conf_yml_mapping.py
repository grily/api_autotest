# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022/6/27 15:00
@Author: guozg
@File：conf_yml_mapping.py
"""


class ConfYmlMapping():
    """
    config.yml 的映射
    """

    def __init__(self):
        # dir_conf 模块的key
        self.__dir_conf_key = "dir_conf"
        self.__case_key = "case"
        self.__caseyml_key = "caseyml"
        self.__common_key = "common"
        self.__config_key = "config"
        self.__report_tmp_key = "report_tmp"
        self.__report_key = "report"
        self.__request_dat_key = "requestdata"
        self.__response_data_key = "responsedata"
        self.__runlog_key = "runlog"
        # 该key暂时用不到。
        self.__uploaddata_key = "uploaddata"
        # http_conf 模块的key
        self.__http_conf_key = "http_conf"
        self.__procotol_key = "procotol"
        # self.__host_key = "host"
        self.__useragent_key = "useragent"
        # 于20220824新增
        self.__v5login_moduleflag = "v5login_moduleflag"
        self.__v6console_moduleflag = "v6console_moduleflag"
        self.__v5login_testhost = "v5login_testhost"
        self.__v5login_relhost = "v5login_relhost"
        self.__v5login_prodhost = "v5login_prodhost"
        self.__v6console_testhost = "v6console_testhost"
        self.__v6console_relhost = "v6console_relhost"
        self.__v6console_prodhost = "v6console_prodhost"
        self.__cur_host_flag = "cur_host_flag"

    # ****************dir_conf模块*******************
    def get_dir_conf_key(self):
        """返回config.yml中dir_conf的key值"""
        return self.__dir_conf_key

    def get_case_key(self):
        return self.__case_key

    def get_caseyml_key(self):
        return self.__caseyml_key

    def get_common_key(self):
        return self.__common_key

    def get_config_key(self):
        return self.__config_key

    def get_report_tmp_key(self):
        return self.__report_tmp_key

    def get_report_key(self):
        return self.__report_key

    def get_requestdata_key(self):
        return self.__request_dat_key

    def get_responsedata_key(self):
        return self.__response_data_key

    def get_runlog_key(self):
        return self.__runlog_key

    def get_uploaddata_key(self):
        return self.__uploaddata_key

    # ********************* http_conf 模块 *******************
    def get_http_conf_key(self):
        return self.__http_conf_key

    def get_procotol_key(self):
        return self.__procotol_key

    # def get_host_key(self):
    #     return self.__host_key

    def get_useragent_key(self):
        return self.__useragent_key
    
    def get_v5login_moduleflag_key(self):
        return self.__v5login_moduleflag
    
    def get_v6console_moduleflag_key(self):
        return self.__v6console_moduleflag
    
    def get_v5login_testhost_key(self):
        return self.__v5login_testhost
    
    def get_v5login_relhost_key(self):
        return self.__v5login_relhost
    
    def get_v5login_prodhost_key(self):
        return self.__v5login_prodhost
    
    def get_v6console_testhost_key(self):
        return self.__v6console_testhost
    
    def get_v6console_relhost_key(self):
        return self.__v6console_relhost
    
    def get_v6console_prodhost_key(self):
        return self.__v6console_prodhost

    def get_cur_host_flag_key(self):
        return self.__cur_host_flag
    


if __name__ == '__main__':
    data = ConfYmlMapping()
    print(data.get_dir_conf_key())
    print(data.get_case_key())
    print(data.get_caseyml_key())
    print(data.get_common_key())
    print(data.get_config_key())
    print(data.get_report_tmp_key())
    print(data.get_report_key())
    print(data.get_requestdata_key())
    print(data.get_responsedata_key())
    print(data.get_runlog_key())
    print(data.get_uploaddata_key())
    print(data.get_http_conf_key())
    print(data.get_procotol_key())
    print(data.get_useragent_key())
    print(data.get_v5login_moduleflag_key())
    print(data.get_v5login_testhost_key())
    print(data.get_v5login_relhost_key())
    print(data.get_v5login_prodhost_key())
    print(data.get_v6console_moduleflag_key())
    print(data.get_v6console_testhost_key())
    print(data.get_v6console_relhost_key())
    print(data.get_v6console_prodhost_key())
    print(data.get_cur_host_flag_key())



