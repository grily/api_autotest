"# api_autotest"

使用pytest  yaml allure 搭建的接口自动化
--断言  
pytest-assume  在yaml文件中直接写断言语句
      - pytest.assume(200 == response.status_code)
      - pytest.assume("OK" in jsonpath(resp_json, "$.message"))
      - pytest.assume(1 <= len(jsonpath(resp_json, "$.data['*']")))
eval(asert_exp) 直接执行python语句

--接口响应数据的提取 用于后面接口的断言
  设置存储的文件路径 设置存储的数据 文件中的key值
    - filepath: user_exam_id_wl.json
      resp_keys:
        - $.data[0].latest_score.latest_exam_id
        - $.data[0].id
      keys: [ latest_exam_id, id ]

--数据依赖处理 
  depends_on:
    #    依赖login登录的token 和 userExamList我的测评实验列表的 id
    - - <<: *userlogin
      - <<: *exam_id
在接口的请求参数中 使用$ 到时可以用模板替换掉的方式 替换变量
  request_param: &comprehensive_req_param
    url: $url
    method: get
    headers:
      Content-Type: application/x-www-form-urlencoded
      User-Agent: *agent
      Authorization: Bearer $token
    params: &comprehensive_req_params
      subject_id: 1
      id: $id

casedata_tmp = Template(casedata_str).safe_substitute(**depend_data_tmp)

--全局环境变量
--数据驱动
@pytest.mark.parametrize
--如何并发
  接口间存在并发 不能使用pytest-xdist==3.5.0 同一个用例间有互相依赖 并发时不能保证执行的顺序 
  暂时用单进程方式
768个用例  用时1分半==90秒  