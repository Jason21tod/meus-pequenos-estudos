
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from jason_pastoleiro import Jason
from jason_actions import do_list_of_kids
from time import sleep

jason_test = Jason('Jason whats')

app = Flask(__name__)

def get_msg(msg:str, request):
    msg = msg.lower()
    ATUAL_GROUP = 'Audios'
    if 'clubinho' in msg:
        print('Clubinho encontrado na msg')
        return do_list_of_kids('clubinho', ATUAL_GROUP)
    elif 'clube' in msg:
        print('Clube encontrado na msg')
        return do_list_of_kids('clube', ATUAL_GROUP)
    elif 'kids club' in msg:
        print('kids club encontrado na msg')
        return do_list_of_kids('kids club', ATUAL_GROUP)
    else:
        return request.values.get('ProfileName')

@app.route('/bot', methods=['POST', 'GET'])
def send_msg():
    print(request.values)
    body = request.values.get('Body')
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Oieeee')
    resposta = get_msg(body, request)
    msg.body(resposta)

    return str(resp)

@app.route('/')
def index():
    return 'Funciona'

app.run(debug= True)