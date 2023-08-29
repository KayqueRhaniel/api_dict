import requests


url = "http://dict-np-h.pi.rsfn.net.br:16532/api-np/v1/keys/check"

payload = """<?xml version="1.0" encoding="UTF-8" ?>
<CheckKeysRequest>
    <Keys>
        <Key>mail@mail.com</Key>
        <Key>mail2@mail.com</Key>
        <Key>+5561999999999</Key>
        <Key>+5561888888888</Key>
        <Key>99999999999</Key>
        <Key>99999999999999</Key>
    </Keys>
</CheckKeysRequest>
"""


headers = {
    'Content-Type': 'application/xml'
}


response = requests.post(url, headers=headers, data=payload)


if response.status_code == 200:
    print("Solicitação bem-sucedida!")
    print(response)
else:
    print(f"A solicitação falhou com o código de status: {response.status_code}")
    print(response)
