# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022-8-15 15:40
@Author: test
@File：upload_files.py
"""


def convert_files_to_stream(files_data):
    """
    处理上传文件，包括批量上传操作
    :param files_data: files的内容
    :return: 将要上传的文件转化为字节流后的内容
    """
    data = files_data
    # 进行类型判断
    
    if isinstance(data,dict):
        data_tmp = {}
        for key ,item in data.items():
            data_tmp[key] = convert_files_to_stream(item)
        return data_tmp
    elif isinstance(data,list):
        data_tmp = []
        for item in data:
            data_tmp.append(convert_files_to_stream(item))
        return data_tmp

    elif isinstance(data,tuple):
        data_tmp = []
        for item in data:
            data_tmp.append(convert_files_to_stream(item))
        return tuple(data_tmp)

    elif isinstance(data,str):
        data_tmp = data
        if "open(" in data:
            data_tmp = eval(data)
        return data_tmp

if __name__ == "__main__":
    """
    请在项目的根目录下运行，即在nb_api_autotest 目录下运行
     python common/upload_files.py
    """
    data =  {
    "field1": ["filename1", 'open("upload_data/1.log", "rb")'],
    "field4": ['open("upload_data/2.log", "rb")'],
    "field5": 'open("upload_data/2.log", "rb")',
    "field2": ["filename2", 'open("upload_data/1.jpg", "rb")', "image/jpeg"],
    "field3": ("filename3", 'open("upload_data/2.png", "rb")', "image/png", {"refer": "localhost"}),
    "field6": ['open1("upload_data/2.log", "rb")'],
    "field7": [("filename1", 'open("upload_data/1.log", "rb")'),
               ("filename2", 'open("upload_data/2.png", "rb")', "image/png"),
               'open("upload_data/1.log", "rb")',
               'open("upload_data/2.log", "rb").read()'],
    "files8":[
                ["files[]",'open("upload_data/2.log", "rb")'],
                ["files[]",'open("upload_data/1.log", "rb")']
            ]
    }
    data1 = [
                ["files[]",'open("upload_data/2.log", "rb")'],
                ["files[]",'open("upload_data/1.log", "rb")']
            ]
    value = convert_files_to_stream(data)
    print(value)
    print("*"*20)
    value1 = convert_files_to_stream(data1)
    print(value1)