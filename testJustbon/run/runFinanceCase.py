import unittest
from BeautifulReport import BeautifulReport
from public.publicExcel import PublicExcel
def case():
    test_suite = unittest.defaultTestLoader.discover('..\\testCase', pattern='testFinanceCase.py')
    result = BeautifulReport(test_suite)
    result.report(filename='report_finance', description='收费系统测试报告', log_path='..\\report')
if __name__ == '__main__':
    case()