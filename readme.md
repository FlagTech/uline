# LINE Push Message API for MicroPython

這是為了 MicroPython 所設計的 LINE Push Message API 套件，你可以參考〈[使用 LINE Bot 聊天機器人替代 LINE Notify 服務](https://hackmd.io/@flagmaker/SJLKW4lV1e) 〉。

如果依照上述文章使用 Google 的 Apps Script 當後端程式，可以直接傳送任何訊息給該 LINE 機器人，它會回覆給你你的 LINE user id 或是你所在群組的 LINE group id，有 id 才能傳送推播訊息。

請注意 LINE user/group id 不是你帳戶設定裡面的 LINE id，兩者不同。

這個 LINE 套件的使用方式如下：

```python
import line
...
line.line_token(Channel_access_token)
status_code = line.line_notify(
    to=LINE_user_or_group_id, # 必要引數，其他都選用
    t='要發送的推播訊息文字內容', 
    pid=Sticker_package_id, sid=Sticker_id, 
    img=Img_url)
print(type(status_code))
```
其中：

|參數|說明|必要/選用|
|---|---|---|
|`Channel_access_token`|LINE Messaging API 的 Channel access token|必要|
|`to`|LINE 訊息接收者的 user id 或是 group id|必要|
|`t`|要發送的推播訊息文字內容|選用|
|`pid`|貼圖的套件識別碼，和 `sid` 一起使用|選用|
|`sid`|貼圖的識別碼，和 `pid` 一起使用|選用|
|`img`|圖片的網址|選用|

可參考範例程式 [send_push_msg.py](send_push_msg.py)。

上文中以 Apps Script 建立的後端程式也提供有 `GET` 方法可以傳送推播訊息，除了不需要傳送 `Channel access token` 外，可接受的參數同上。

可參考範例程式 [send_push_msg_via_apps_script.py](send_push_msg_via_apps_script.py)。

