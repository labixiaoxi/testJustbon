#-*-coding:utf-8 -*-
#__author__ = 'xiaoxi'
#@time:2019/1/22 15:33
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
from public import publicEamil
import unittest,os,time,HTMLTestRunner
from public.publicLocust import PublicLocust
from multiprocessing import Process
# def run():
#
#     case_path = os.path.join(os.getcwd(), "..\\testCase")
#     discover = unittest.defaultTestLoader.discover(case_path,
#                                                         pattern="test_a_login_page.py",
#                                                         top_level_dir=None)
#     report_path = os.path.join(os.getcwd(), "..\\report\\report_justbon.html")
#     fp=open(report_path,'wb')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
#                         title=u'用例执行情况',
#                         description=u'嘉宝生活家UI自动化:')
#     runner.run(discover)
#     fp.close()
#
# run()
# def run_locust():
#     PublicLocust().run()


# if __name__ == "__main__":
#     run()
    # p2 = Process(target=run_locust)
    # p1.start()
    # p2.start()
    # p1 = Process(target=run)
    # p2.join()

# import unittest
# from BeautifulReport import BeautifulReport
#
# if __name__ == '__main__':
#     test_suite = unittest.defaultTestLoader.discover('../testCase', pattern='test*.py')
#     result = BeautifulReport(test_suite)
#     result.report(filename='测试报告', description='测试报告', log_path='report')
import unittest
from BeautifulReport import BeautifulReport
from public.publicExcel import PublicExcel
def case():
    test_suite = unittest.defaultTestLoader.discover('..\\testCase', pattern='formalJustbonCase.py')
    result = BeautifulReport(test_suite)
    result.report(filename='justbon_test', description='正式环境嘉宝生活家', log_path='..\\report')
if __name__ == '__main__':
    case()










