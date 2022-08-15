
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from jason_pastoleiro import Jason
from jason_actions import do_list_for_whats

jason_test = Jason('Jason whats')

app = Flask(__name__)

def get_msg(msg:str, request):
    msg = msg.lower()
    if 'pastinha clubinho' in msg:
        print('Clubinho encontrado na msg')
        return do_list_for_whats('clubinho', request)
    elif 'pastinha clube' in msg:
        print('Clube encontrado na msg')
        return do_list_for_whats('clube', request)
    elif 'pastinha kids club' in msg:
        print('kids club encontrado na msg')
        return do_list_for_whats('kids club', request)
    return request.values.get('ProfileName')


@app.route('/bot', methods=['POST', 'GET'])
def send_msg():
    print(request.values.get)
    body = request.values.get('Body')
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("""oi ser humano\n Segue ai a lista dos comandos que eu sei !
    \nAtualmente eu sei fazer a pastinha só, mas logo logo, meu pai vai me dar novas habilidades :P.
    \n.Para requisitar a pastinha, basta digitar: pastinha "nome do setor" e eu verifico se tem crianças ! """)
    resposta = get_msg(body, request)
    msg.body(resposta)
    # msg.body(concat_kids_list(resposta))
    print(msg.body)
    
    return str(resp)

@app.route('/', methods=['POST', 'GET'])
def index():
    formu = request.form
    print(formu)
    return render_template('index.html')

app.run(debug= True)