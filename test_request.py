#导入pytest
import pytest
import requests

def test_01_login():
    assert 2>1
    print('第一个pytest代码')

def test_02_login():
    assert 3<2

#执行所有用例; pytest ./ --alluredir=result
#将用例执行结果保存到报告文件中； allure generate result -o report --clean
#每次保存一次运行结果就清空之气的数据
#打开allure报告；allure open report