from flask import Flask, request, jsonify, redirect
import requests
import sys
import threading

print(sys.executable)

app = Flask(__name__)

# URL dell'endpoint di login dell'Authorization Server
login_url = 'http://127.0.0.1:9000/'

def auth_flow(url):
    session = requests.Session()

    response = session.get(url)
    print(response.content)
    print()

    if response.status_code == 401:
        print('Login richiesto...')

        for attempt in range(3):  # 3 tentativi
            username = input('username: ')  # admin
            password = input('password: ')  # password
            login_payload = {'username': username, 'password': password}
            login_response = session.post(login_url, json=login_payload)

            if login_response.status_code == 200:
                response = session.get(url)
                if response.status_code == 200:
                    try:
                        data = response.json()
                        location = data.get('Location')
                        if location:
                            print(f"Risposta: {location}")
                            resp=requests.get(location)
                            print(resp.status_code)
                        else:
                            print("Errore: Location non trovata nella risposta")
                    except Exception as e:
                        print(f"Errore parsing JSON: {str(e)}")
                    return
                elif response.status_code == 401:
                    continue  # Tentativo fallito, riprova
                else:
                    print(f"Errore accesso risorsa: {response.status_code}")
                    return
            else:
                print(f'Login fallito con status code: {login_response.status_code}')
        print('Credenziali errate dopo 3 tentativi')
        return

    try:
        print(response.json())
    except Exception as e:
        print(f"Errore parsing JSON: {str(e)}")


@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL'}), 400

    url = data['url']
    threading.Thread(target=auth_flow, args=(url,)).start()
    return jsonify({'status': 'OK'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=7000)
