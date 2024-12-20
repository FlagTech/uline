import network
import socket
import urequests

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('無線網路名稱', '無線網路密碼')
while not sta_if.isconnected():
    pass
print('已連上 Wi-Fi')
appsScriptURL = 'Apps Script 後端程式部署後的網址'
lineUserID = '傳送對象'

# 傳送訊息給指定的使用者
# 查詢字串參數：
# id: LINE 使用者的識別碼（不是 LINE ID 喔）
# t: 文字訊息
# pid: 貼圖的套件識別碼
# sid: 貼圖的識別碼
# img: 圖片的網址

txt = "你好啊！"
pid = 446
sid = 1990
img = 'https://www.flag.com.tw/assets/img/bookpic/F4328.jpg'
res = urequests.get(
    f'{appsScriptURL}'
    f'?to={lineUserID}'
    f'&t={txt}'
    f'&pid={pid}&sid={sid}'
    f'&img={img}')
print(res.status_code)
res.close()


