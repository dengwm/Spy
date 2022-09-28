import unittest

from handler_requests import send_requests
from handler_excel import HandleExcel
import os

he = HandleExcel(os.path.join(os.path.dirname(os.path.abspath(__file__)),"api_cases.xlsx"),"注册")
cases = he.read_all_datas()
he.close_file()

class TestRegister(unittest.TestCase):

    def test_register_ok(self):
        case = cases[0]
        expected = eval(case["expected"])
        # 测试数据
        response = send_requests(case["method"],case["url"],eval(case["request_data"]))
        # 断言：code==0 msg==ok
        self.assertEqual(response.json()["code"],expected["code"])
        self.assertEqual(response.json()["msg"], expected["msg"])

