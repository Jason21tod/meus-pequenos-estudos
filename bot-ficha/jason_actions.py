from unittest import TestCase, main
from writers import text_assests
from twilio.rest import Client
from time import sleep
import pyautogui
import os

import jason_pastoleiro

jason = jason_pastoleiro.Jason('Actions jason')

def find_whats(group_name:str):
    sleep(1)
    pyautogui.press('win')
    pyautogui.write('Whatsapp', interval=0.05)
    pyautogui.press('enter')
    sleep(17)
    pyautogui.click(x=99, y=116)
    sleep(2)
    pyautogui.write(group_name)
    sleep(0.5)
    pyautogui.click(x=133, y=268)

def do_list_of_kids(sector, group_name='Audios'):
    find_whats(group_name)
    sleep(5)
    pyautogui.click(x=608, y=688)
    pyautogui.write(f'Olha só a pastinha do {sector}')
    pyautogui.hotkey('ctrl', 'enter')
    jason.make_list_kids(sector)
    text_assests.close_archives()
    return f'A pastinha do {sector} esta saindo !'

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def concat_kids_list(kids_list: list):
    kid_string = '\n'
    for kid in kids_list:
        kid_string = '\n'+kid_string+kid
    return kid_string

def do_list_for_whats(sector, request):
    jason._get_from_data()
    # kid = jason.my_receiver.kids_sector_list[sector][0]
    kids_list = []
    message = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body=f'Segue ai a pastinha do {sector}',
                        to=request.values.get('From')
                    )
    if len(jason.my_receiver.kids_sector_list[sector]) > 0:
        for kid in jason.my_receiver.kids_sector_list[sector]:
            kids_list.append(f"{kid['nome']} {kid['apt']} {kid['responsavel']} {kid['anot']}\n")
        kids_list = concat_kids_list(kids_list)
        message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=str(kids_list),
                              to=request.values.get('From')
                          )
    else:
        print(jason.my_receiver.kids_sector_list[sector])
        message = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body='n tem crianças nesses setor',
                        to=request.values.get('From')
                    )



if __name__ == '__main__':
    class TestFuctions(TestCase):
        def test_list_of_kids(self):
            list_of_kids = do_list_of_kids('clube')

    main()
