import pytest
 # 前置条件：登录

# 用例1：头部传用户登陆token，可以查询个人信息
#  用例2：头部传错误的token，不能获取到个人信息

@pytest.fixture(scope="function")
def login():
    """自定义一个前置的操作"""
    print("先登录")

# def setup_module():
#     print("整个模块只调用一次")
#
# def setup_function():
#     """函数级别的前置"""
#     print("函数级别的前置：每个用例都会调用一次")

def test_01(login):
    print("用例1：头部传用户登陆token，可以查询个人信息")

def test_02():
    print("用例:2：头部传错误的token，不能获取到个人信")
