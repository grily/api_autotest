# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2023-3-13 14:50
@Author: test
@File：jsonschema_validate.py
"""
import json
import traceback

from jsonschema import validate
from genson import SchemaBuilder
import os
from common.get_json_filepath import get_json_filepath
DEFAULT_URI = 'http://json-schema.org/draft-07/schema#'

def jschema_validate(validate_data:dict or None,req_json:dict)->str or None or bool:
    '''
    对响应结果数据时等jsonschema 验证
    :param validate_data: yaml文件中 jschema_validate 数据
    :param req_json: 接口的响应结果
    :return: 验证后的结果: None(表示验证通过或首次存jsonschema文件) 或者 出错的信息(表示验证未通过) 或 json文件找不着的error信息
     或 bool(当传入的值为None或validate的值为false时,表示不需要进行验证,则返回false 或location的值为mysql或redis时，也会返回false)。
    '''
    '''
    逻辑处理如下：
    # jsonschema 校验，校验的整体规则如下(一期,针对将jsonschema存放在本地的json文件中)：
    # 1：当jschema_validate的值为None 或 validate的值为False时，表示不需要进行校验，返回 False
    # 2：当需要校验时，会优先检测filepath的值是否有录入，若没有录入时，会返回 file_error
    # 3：当filepath有录入值时：
    #   3.1：会优先判断filelocation的值是mysql、redis 还是local（非mysql、redis，其他的值均被认为为local).当为mysql 或 redis时，会返回False
    #   3.2：当值为local时，会进入如下的判断：
    #      3.2.1：first的值是否为true，当为true时，表示是第一次运行该接口，要将返回的json数据进行转换为jsonschema并存入到json文件中。具体逻辑如下：
    #           3.2.1.1:当filepath里指定的json文件不存在时，则会将返回的json数据进行转换为jsonschema，并存入到filepath里指定的json文件中，并返回None
    #           3.2.1.2:当filepath里指定的json文件存在时，则会读取json文件的内容，进行如下的判断：
    #               3.2.1.2.1：当内容为空时，逻辑同2.1.1，即会将response的json文件进行转换为jsonschema，并存入到filepath里指定的json文件，并返回None
    #               3.2.1.2.2：当内容不为空时，会直接进行jsonschema的校验。校验通过，则返回None；校验不通过时，则会返回匹配失败的具体信息 
    #       3.2.2：当first的值为false时：
    #           3.2.2.1：当filepath 指定的json文件不存在时，则返回 file_error
    #           3.2.2.2：当filepath 指定的json文件存在时：
    #               3.2.2.2.1：当内容为空时，会返回 file_null
    #               3.2.2.2.2：当内容不为空时，会进行jsonschema 校验。当校验通过时，返回None；当校验未通过时，则返回具体的匹配失败的信息。                
    '''
    vdata = validate_data
    # 表示不需要进行jsonschema校验。
    # 实际上应该不存在 vdata 为""的情况
    if vdata == None or vdata['validate'] == False or vdata == "":
        return False
    # 表示需要进行jsonschema校验
    else:
        # json文件名称(在response_data目录下的名称，注意不要跟其他的json文件重名)
        filepath = vdata['filepath']
        # 必须先判断filepath的值是否为None或为""
        if filepath == None or filepath == "":
            return "file_error"

        # jsonschema 数据所在的位置,默认值为local(含loc、空及其他输错的值),当值为mysql 或 redis时(二期或有诉求时再实现),则直接不进行任何的校验,返回False
        location_flag = vdata['filelocation']
        # 判断是本地还是mysql或redis
        if location_flag !=None and (location_flag.lower()=="mysql" or location_flag.lower()=="redis"):
            # 是否更新数据库中存入的jsonshema内容的标识，默认值为false(含空),该字段为拓展字段，在二期或诉求时再实现。即当location的值为 mysql 或 redis时 才会用到该字段。
            update_flag = vdata['update']
            if update_flag == False:
                pass
            else:
                pass
            return False
        # 当location的值 为非mysql和非redis时,表示要读取本地的json文件
        else:
            # 是否为第一次进行jsonschema的校验,默认值为false(含空)
            first_flag = vdata['first']
            # 当first_flag 的值为False 或 不来True时，均被当为False对待。
            if first_flag != True:
                # 判断filepath里指定的json文件不存在时，则返回error
                # 获取json文件的路径
                filepath = get_json_filepath(filepath)
                # 当文件存在时
                if os.path.exists(filepath):
                    # 进行内容读取
                    with open(filepath, 'r', encoding='utf-8') as fp:
                        filedata = fp.read()

                    # 判断内容是否为空，为空时返回 file_null
                    if filedata == "":
                        return "file_null"

                    # 表示内容不为空，则进行jsonschema校验
                    else:
                        # 此时应该进行将内容转化为dict后，验证type是否为dict,若是不为dict，则应该报错。说明jsonschema有问题。
                        # 先不进行jsonschema校验
                        schema = json.loads(filedata)

                        try:
                            # 进行jsonschema校验
                            validate(req_json, schema)
                            return None
                        except Exception as e:
                            print(f"jsonschema 校验失败，如下如下：\n{e}")
                            # 不能直接返回e,因为的type为<class 'jsonschema.exceptions.ValidationError'>
                            return traceback.format_exc()

                # 表示文件不存在
                else:
                    return "file_error"

            # 不为False时，其他的任何值均为True
            else:
                filepath = get_json_filepath(filepath)
                # 当文件不存在时,则表示首次进行jsonschema的文件转存,并返回None
                if os.path.exists(filepath) == False:
                    builder = SchemaBuilder()
                    # 为解决console里的警告，特意给$schema 加上版本号
                    builder.DEFAULT_URI = DEFAULT_URI
                    # 此时逻辑若进行更加严谨的处理，还应该校验statuscode 是否为200 及 req_json是否为dict,两者需要同时满足。
                    # 本次不进行此逻辑判断
                    builder.add_object(req_json)
                    with open(filepath, "w", encoding="utf-8") as fp:
                        fp.write(builder.to_json(indent=2))

                    return None

                # 当文件存在时,只在当内容为空时，才会更新jsonschema内容,否则会直接进行jsonschema校验。
                else:
                    with open(filepath, 'r', encoding='utf-8') as fp:
                        filedata = fp.read()

                    # 判断内容是否为空,此时要将返回的数据进行转换为jsonschema，并存入到文件中。并返回None
                    if filedata == "":
                        # 若进行严格处理,此时还应该判断状态是否为200 及 数据是否是否为dict,且这两项必须同时满足。
                        # 本次不进行逻辑判断
                        builder = SchemaBuilder()
                        # 为解决console里的警告，特意给$schema 加上版本号
                        builder.DEFAULT_URI = DEFAULT_URI
                        builder.add_object(req_json)
                        with open(filepath, 'w', encoding='utf-8') as fp:
                            fp.write(builder.to_json(indent=2))

                        return None

                    # 表示有内容不为空。此时不在进行jsonschema的内容变更，而是直接进行jsonschema validate
                    else:
                        schema = json.loads(filedata)
                        try:
                            validate(req_json, schema)
                            return None
                        except Exception as e:
                            print(f"jsonschema 校验失败，如下如下：\n{e}")
                            # 不能直接返回e,因为的type为<class 'jsonschema.exceptions.ValidationError'>
                            return traceback.format_exc()

