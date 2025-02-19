# -*- coding: UTF-8 -*-
# 设置utf-8  显示中文
"""
@Create Time: 2024-1-30 15:45
@Author: test
@File：run.py.py
"""
import subprocess

import pytest


if __name__ == "__main__":
    print(f"\n********************* 开始执行任务 *********************")

    # file = "test_app_exam_list.py"
    # file = "test_app_shiyan.py"
    file = "test_comments.py"
    pytest.main([f"case/{file}", "--alluredir","report/tmp"])
    # pytest.main([f"case", "--alluredir","report/tmp"])

    # 使用subprocess.run生成Allure报告
    report_generate_command = "allure generate report/tmp -o report/report -c"
    result = subprocess.run(report_generate_command, shell=True, capture_output=True, text=True)
    #
    # 检查命令是否成功执行
    if result.returncode == 0:
        print("\n********************** 报告生成完毕 *********************\n")
    else:
        print("\n********************** 报告生成失败 *********************\n")
