from email import header
from xlrd import open_workbook

wb = open_workbook(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\testdata.xls")

ws =wb.sheet_by_name("smoke")
used_rows = ws.nrows



# for i in range(0, used_rows):
#     rows = ws.row_values(i)
#     if rows[0] == "test_login_negative":
#         rowser = ws.row_values(i)
#         rowser = [rows for rows in rowser if rows]
#         print(rowser)

# def read_data(sheetname, test_case_name):
#     wb = open_workbook(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\testdata.xls")
#     ws =wb.sheet_by_name(sheetname)
#     used_rows = ws.nrows
#     for i in range(0,used_rows):
#         rows = ws.row_values(i)
#         if rows[0] == test_case_name:
#             rowser = ws.row_values(i)
#             rowser = [rows for rows in rowser if rows]
#     return rowser

# print(read_data("smoke","test_payment"))

  