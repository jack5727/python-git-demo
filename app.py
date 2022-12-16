#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
import os
app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('nDW9QPETy7yRR0MuJL8TUIWX78Uf2Jfi5hQ3YfwJKcgmU+hrq5uwgp0NbGwTrCkZ5i/0UoqVt1PcZI0oococ+mEqMUF7mLwIg3GDD7xcjvNRZFGsWvo3nYNzDJjqdBLLupvwOdqpiYlAUMXHQCaiTQdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('36ea61dad1a2b11dd6300f42e43354c5')

	

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
  
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
 
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if re.match("你是誰",message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage("才不告訴你勒~~"))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))


#主程式

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
