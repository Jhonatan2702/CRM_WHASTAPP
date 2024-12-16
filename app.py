from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Token de acesso do WhatsApp
TOKEN = "SEU_TOKEN_AQUI"

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')
    
    url = f"https://graph.facebook.com/v17.0/ID_DO_SEU_NUMERO/messages"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {"body": message}
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
