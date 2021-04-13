import requests



session = requests.session()
session.post(url='http://localhost:8080/sisqp-web/j_spring_security_check',data={'j_username':'admin_1_12','userName':'admin','j_password':'f','companyId':'1','departmentId':'12'})

cookiejar = session.cookies
print(cookiejar.get_dict())
index_req = requests.post(url='http://localhost:8080/sisqp-web/dms-fd/fd-ajax.action?method=checkSrcFileCode',data={'srcFileCode':'srcFileCode'},headers=session.headers,cookies=cookiejar.get_dict())
print(index_req.text)

