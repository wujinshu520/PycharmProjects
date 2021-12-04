import os
import time

from selenium import webdriver

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(10)
driver.get("https://www.cnblogs.com/")

#time.sleep(60)
'''  获取cookie '''
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)


driver.add_cookie({'domain': '.cnblogs.com', 'expiry': 1664371784, 'httpOnly': False, 'name': '__gads', 'path': '/', 'secure': False, 'value': 'ID=6e19ae6f34df626f:T=1630675784:S=ALNI_MYIxZbDZOIh-VquWrshFzM2pY5Mew'})
driver.add_cookie({'domain': 'www.cnblogs.com', 'httpOnly': True, 'name': '.AspNetCore.Antiforgery.b8-pDmTq1XM', 'path': '/', 'secure': False, 'value': 'CfDJ8NACB8VE9qlHm6Ujjqxvg5BBLySP-ktz_PigM_Wk7QdxODMPuy2oNFyOVA1MK8XVWJxk2o8EfrYCVDgJ2Sj61pWHy8O3_fRw547NDYpgWlOk8Z_P0zR3mpej4ZzmivDVpQGIF3u7Hgi56Yy_N3H9lVE'})
driver.add_cookie({'domain': '.cnblogs.com', 'expiry': 1693747799, 'httpOnly': False, 'name': '_ga_3Q0DVSGN10', 'path': '/', 'secure': False, 'value': 'GS1.1.1630675786.1.1.1630675799.0'})
driver.add_cookie({'domain': '.cnblogs.com', 'expiry': 1631971799, 'httpOnly': True, 'name': '.CNBlogsCookie', 'path': '/', 'secure': False, 'value': '2ACCAD1DDEEA5FD49F5CAE56D8C48AAA1387F526536F5A1DA48A3314F883C92DD8F4A8169520248EB3038492A5A9933BD670E20050009BA1E2445A07DD5DD3DB2E4884CAA47564ACA2189E013E0C1F8DD934C449'})
driver.add_cookie({'domain': '.cnblogs.com', 'expiry': 1631971799, 'httpOnly': True, 'name': '.Cnblogs.AspNetCore.Cookies', 'path': '/', 'secure': False, 'value': 'CfDJ8NACB8VE9qlHm6Ujjqxvg5BsgteBzeV1RWQbtlA1YBYahN2jxmhXobrNtkBlYMraZbgAjsbBo1kZzYkz2hAb-EeVf-3O1ZmauanQTDyc8XEVQ9VXhZFGVRlh2BOhs4owy6w1YN3NoJE4QStxD0ZD7j1n2Vu9blKBDtJlxQzbwbPdipfh0jP82ginxeUrJzNbrPjIyXCeAqmdtbLA0tvOvbQrOsq7qhMAmMkOp84r6fBAWXTQYOwSxj636Feerqj41uE2SfYfm4eVkZOY2vDg0sgroCWOqaTIXKIvhAbPkRuXdst-4WcNL2ljHyjkQa27iJdKSgm-JwRdJl0Z9yiefsozNxIfQhWWS2hQCNDpOL3rp0yAcncDZJ_qivTzwEaaf8vCDJosMFb0fz1aPWA215EDzhDLZKumKtgS0VdiItAgA2UkoiKH1LAFfN_6FuBa3l1bxJLShkzdAocuxWFrUL3SRrBYgiJcNW0_iU1YCR8R51dXvl40TsvQpCLSmNGPN92q2kPI9qYA3Lev6Tq35mNvHIv76kT8rFVGlgVzXzfuDGiWkYRkvyen7P3JV6ryyQ'})
driver.add_cookie({'domain': '.cnblogs.com', 'expiry': 1693747799, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1473937500.1630675784'})
driver.add_cookie({'domain': '.cnblogs.com', 'expiry': 1630762199, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1567810746.1630675784'})

time.sleep(3)
driver.refresh()