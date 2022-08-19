
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
    body = request.values.get('Body')
    resp = MessagingResponse()
    msg = resp.message()    
    if body in ['Oi', 'oi', 'oooi', 'pastinha']:
        print('>>oi encontrado')
        msg.body("""oi ser humano\n Segue ai a lista dos comandos que eu sei !
        \nAtualmente eu sei fazer a pastinha só, mas logo logo, meu pai vai me dar novas habilidades :P.
        \n.Para requisitar a pastinha, basta digitar: pastinha "nome do setor" e eu verifico se tem crianças ! """)
    else: get_msg(body, request)
    msg.body('\nOi ser humano, em que posso ser util ?')
    
    return str(resp)

def post_it_in_db(request):
    check_in = request['check-in']
    check_out = request['check-out']
    jason_test._get_from_data(directory='kids_data_test.json')
    print('Jason pegando dos dados: ',jason_test.my_receiver.kids_sector_list)
    kid = { 'nome': request['name'],
            'idade': int(request['years']),
            'check-in':[int(check_in.split('-')[1]), int(check_in.split('-')[2])],
            'check-out':[int(check_out.split('-')[1]), int(check_out.split('-')[2])],
            'apt': request['apt'],
            'responsavel': request['parents'],
            'anot': request['anotation']}
    print(kid)
    jason_test.my_receiver.add_kid_to_sector(kid)
    jason_test._store_in_data(directory='kids_data_test.json')

@app.route('/kid_form.html', methods=['POST', 'GET'])
def add_kid():
    if request.method == 'POST':
        formu = request.form
        print(formu)
        post_it_in_db(formu)
    return render_template('kid_form.html')

@app.route('/')
def index():
    return render_template('index.html')

app.run()