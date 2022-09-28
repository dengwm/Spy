from openpyxl import load_workbook
import json


class HandleExcel:

    def __init__(self,file_path,sheet_name):
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        # 遍历第1行每一列
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        all_datas = []
        titles = self.__read_titles()
        # 遍历数据行
        for item in list(self.sh.rows)[1:]:
            values = []
            for val in item:
                values.append(val.value)  # 获取每一行的值
            res = dict(zip(titles, values))  # title和每一行数据，打包成字典
            res["request_data"] = json.loads(res["request_data"])  # 将请求数据从json字符串转换成字典对象
            all_datas.append(res)
        return all_datas

    def close_file(self):
        self.wb.close()



if __name__ == '__main__':
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
    exc = HandleExcel(file_path,"login")
    cases = exc.read_all_datas()
    exc.close_file()
    for case in cases:
        print(case)