# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022-8-25 10:31
@Author: test
@File：get_host.py
"""
from common.get_config_data import GetConfData


def get_host(ymldata:dict,casedata:dict)->str or None:
    '''
    获取host域名。
    :param ymldata:  当前case所在的yaml文件的yml文件数据
    :param casedata:  当前case对应的yml 数据
    :return:  经过处理后的host值
    '''

    '''
    于20220825定下最终的逻辑规则：
    一: case 自己的module_flag 有值时，则 根据 当前的 环境标记(cur_host_flag)进行如下的逻辑判断：
        1: 优先通过 从config.yml中获取对应的域名
            A: 当config.yml中不存在时，则再case所在的yml文件中获取
                a: 若case 所在的yml文件中 仍然不存在，则使用case自己的host值(后续有可能将逻辑变更为:若是case所在的yaml文件中仍然不存在
                则直接将当前的case置为fail,不在运行该case)
    二: case自己的module_flag 无值时,
        1: 使用case自己的host(后续有可能将逻辑变更为:直接将case置为fail,不在运行)
    
    module_flag 的值 与 host 环境 key的对应关系如下：
    module_flag: xxxx  对应的host 环境的key 则为：
    xxxx_testhost,xxxx_devhost,xxxx_prodhost
    如：
    module_flag: v5login
    则对应的 host 各个环境的key如下：
    v5login_testhost: xxxxx
    v5login_relhost: xxxx
    v5login_prodhost: xxxxx
    
    各个host环境的值 优先级：
    jenkins > config.yml > case 所在的yaml文件中的 域名环境  >  case 自己的 host值
    '''
    conf_data = GetConfData.get_instance()
    # 将可能有的大写统一转为小写
    cur_host_flag = str.lower(conf_data.get_cur_host_flag())
    # 测试环境域名 对应的 key 的名称的 后缀 list, 默认情况下只支持 _testhost 这种方式，但是为了防止他人写错了,所以进行了兼容
    testhost_suffix = ["_testhost" , "_test_host","testhost","test_host"]
    # 测试环境域名 对应的 key 的名称的 后缀 list, 默认情况下只支持 _relthost 这种方式，但是为了防止他人写错了,所以进行了兼容
    relhost_suffix = ["_relhost", "_rel_host","relhost","rel_host","_releasehost","_release_host","releasehost","release_host"]
    # 测试环境域名 对应的 key 的名称的 后缀 list, 默认情况下只支持 _prodhost 这种方式，但是为了防止他人写错了,所以进行了兼容
    prodhost_suffix = ["_prodhost","_prod_host","prodhost","prod_host","_producthost","_product_host","producthost","product_host"]
    host = "$host"
    host_suffix_list = []
    if "test" in cur_host_flag:
        host_suffix_list = testhost_suffix
    elif "rel" in cur_host_flag:
        host_suffix_list = relhost_suffix
    elif "prod" in cur_host_flag:
        host_suffix_list = prodhost_suffix

    # 获取module_flag的值
    module_flag_str = "module_flag"
    module_name = casedata.get(module_flag_str)

    # 进行拼接 host_key
    host_key = ""
    if module_name:
        # 拼接key
        ''''''
        flag = 0
        # 先从config.yml 中获取
        http_conf = conf_data.get_httpconf_data()
        for item in host_suffix_list:
            host_key = f"{module_name}{item}"

            host_tmp = http_conf.get(host_key)
            if host_tmp and host_tmp != "":
                host = host_tmp
                flag = 1
                break
        # 当config.yml 中未获取到对应的 module_flag 所对应的host时，要从case所在的yml文件中获取。
        if flag == 0:
            for item in host_suffix_list:
                host_key = f"{module_name}{item}"
                host_tmp = ymldata.get(host_key)
                if host_tmp and host_tmp !="":
                    host = host_tmp
                    flag = 1
                    break
        # 当case 所对应的yml数据中也没有 对应的module_flag 所对应的host时，此时取case自己的host
        if flag == 0:
            host = casedata.get('host')
            if host == "":
                host = "$host"

        return host

    else:
        host = casedata.get('host')
        if host == "" :
            host = "$host"

        return host


