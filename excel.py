from xlrd import open_workbook

wb = open_workbook(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\objects.xls")
# ws = wb.sheet_by_name("loginpage")

# used_login_rows = ws.nrows
# print(used_login_rows)

# ws = wb.sheet_by_name("registrationpage")
# used_registration_rows = ws.nrows
# print(used_registration_rows)


# d={'field_name':('locator_type','locator_value')}

# d = {}
# for i in range(1, used_registration_rows):
#     data = ws.row_values(i)
#     d[data[0]] = (data[1],data[2])
# print(d)

def read_locators(pagename):
    ws = wb.sheet_by_name(pagename)
    used_rows = ws.nrows
    d = {}
    for i in range(1,used_rows):
        data = ws.row_values(i)
        d[data[0]] = (data[1],data[2])
    return d
    
print(read_locators("registrationpage"))

