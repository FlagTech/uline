import network
import line

line_access_token = '+3IbMT1lkYhiHzOh2BlM4ztYGViVKEnvrd1VfQqoiWm5kGzXRyvsLWd58onLsaN4qqtHj89y+Nx3ovBtIJKrITnEQxTpFSU14MW8r+ThLitqlX0NK8TKsvF9gZYnSKBYJQF88ZbdHGVrgn4W9zw8jwdB04t89/1O/w1cDnyilFU='
lineUserID = 'U3d2299e075241e1705d3e41fdd93f67f'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('FLAG-SCHOOL', '12345678')
while not sta_if.isconnected():
    pass
print('已連上 Wi-Fi')


line.line_token(line_access_token)
status_code = line.line_notify(
    lineUserID,        # 必要引數，其他都選用
    '從模組來的通知', 
    pid=446, sid=1988,
    img='https://www.flag.com.tw/assets/img/bookpic/F4328.jpg')
print(status_code)
