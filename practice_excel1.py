from xlrd import open_workbook

def read_locators(pagename):
    wb = open_workbook(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\objects.xls")
    ws = wb.sheet_by_name(pagename)
    used_rows = ws.nrows
    locators = {}
    for i in range(1,used_rows):
        data = ws.row_values(i)
        locators[data[0]] = (data[1],data[2])
    return locators

print(read_locators("loginpage"))