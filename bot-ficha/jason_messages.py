
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from jason_pastoleiro import Jason

jason_test = Jason('Jason whats')

app = Flask(__name__)

def get_msg(msg):
    if 'clubinho' in msg:
        print('Clubinho encontrado na msg')
        return 'A pastinha do clubinho está saindo !'
    else:
        print('Clubinho n encontrado na msg')
        return 'Não entendi :/'

@app.route('/bot', methods=['POST', 'GET'])
def send_msg():
    print(request.values.get('Body'))
    body = request.values.get('Body')
    resp = MessagingResponse()
    resposta = get_msg(body)
    msg = resp.message()
    msg.body(resposta)

    return str(resp)

@app.route('/')
def index():
    return 'Funciona'

app.run(debug= True)