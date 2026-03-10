from flask import Flask, request, jsonify
from caesar import CaesarCipher
from vigenere import VigenereCipher
from railfence import RailFenceCipher
from playfair import PlayFairCipher
from Transpostsition import TranspositionCipher
app = Flask(__name__) 
#Caesar
caesar_cipher = CaesarCipher()
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "plain_text" hoặc "key"'}), 400
    text = data.get('plain_text')
    try:
        key = int(data.get('key'))
        encrypted_text = caesar_cipher.encrypt_text(text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': '"key" phải là một số nguyên'}), 400

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "cipher_text" hoặc "key"'}), 400
    text = data.get('cipher_text')
    try:
        key = int(data.get('key'))
        decrypted_text = caesar_cipher.decrypt_text(text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': '"key" phải là một số nguyên'}), 400



#Vigenere
vigenere_cipher = VigenereCipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "plain_text" hoặc "key"'}), 400
    text = data.get('plain_text')
    key = data.get('key')
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(text, key)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "cipher_text" hoặc "key"'}), 400
    text = data.get('cipher_text')
    key = data.get('key')
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(text, key)})



#Railfence
railfence_cipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "plain_text" hoặc "key"'}), 400
    text = data.get('plain_text')
    try:
        key = int(data.get('key'))
        encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': '"key" phải là một số nguyên'}), 400

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "cipher_text" hoặc "key"'}), 400
    text = data.get('cipher_text')
    try:
        key = int(data.get('key'))
        decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': '"key" phải là một số nguyên'}), 400



#Playfair
playfair_cipher = PlayFairCipher()
@app.route('/api/playfair/creatematrix',methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    if not data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "key"'}), 400
    key = data.get('key')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix":playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "plain_text" hoặc "key"'}), 400
    text = data.get('plain_text')
    key = data.get('key')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(text, playfair_matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "cipher_text" hoặc "key"'}), 400
    text = data.get('cipher_text')
    key = data.get('key')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(text, playfair_matrix)})


#Transposition
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "plain_text" hoặc "key"'}), 400
    plain_text = data.get('plain_text')
    try:
        key = int(data.get('key'))
        encrypted_text = transposition_cipher.encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': '"key" phải là một số nguyên'}), 400

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu thiếu "cipher_text" hoặc "key"'}), 400
    cipher_text = data.get('cipher_text')
    try:
        key = int(data.get('key'))
        decrypted_text = transposition_cipher.decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': '"key" phải là một số nguyên'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)