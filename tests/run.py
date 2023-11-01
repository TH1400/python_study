import unittest

# 一、创建一个测试套件
suite = unittest.TestSuite()
# 二、创建一个用例加载器
loader = unittest.TestLoader()
# 三、将用例加载到测试套件
# 方法一 通过类名加载测试用例
# from test_01demo import Test1
# from test_02demo import Test1
# suite.addTest(loader.loadTestsFromTestCase(Test1))
# suite.addTest(loader.loadTestsFromTestCase(Test1))
# 方法二 通过用例模块加载
# import test_01demo
# import test_02demo
# suite.addTest(loader.loadTestsFromModule(test_02demo))
# suite.addTest(loader.loadTestsFromModule(test_01demo))
# 方法三 通过用例文件所在路径加载
suite.addTest(loader.discover(r'D:\CodeFile\python_study\tests'))
# 四、获取套件中的用例数量
print(suite.countTestCases())