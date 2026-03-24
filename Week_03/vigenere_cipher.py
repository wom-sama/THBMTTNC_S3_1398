import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        
        try:
            key_value = self.ui.txt_key.toPlainText().strip()
        except ValueError:
            QMessageBox.critical(self, "Error", "Key is required!")
            return

        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText().strip(),
            "key": key_value
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                try:
                    data = response.json()
                    self.ui.txt_cipher_text.setPlainText(data.get("encrypted_text", ""))
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Encrypted Successfully")
                    msg.exec_()
                except requests.exceptions.JSONDecodeError as e:
                    QMessageBox.critical(self, "Error", f"JSON Decode Error: {e}")
            else:
                QMessageBox.warning(self, "API Error", f"Error: {response.text}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", f"Cannot connect to API:\n{e}")


    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        
        try:
            key_value = self.ui.txt_key.toPlainText().strip()
        except ValueError:
            QMessageBox.critical(self, "Error", "Key is required!")
            return

        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText().strip(),
            "key": key_value
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                try:
                    data = response.json()
                    self.ui.txt_plain_text.setPlainText(data.get("decrypted_text", ""))
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decrypted Successfully")
                    msg.exec_()
                except requests.exceptions.JSONDecodeError as e:
                    QMessageBox.critical(self, "Error", f"JSON Decode Error: {e}")
            else:
                QMessageBox.warning(self, "API Error", f"Error: {response.text}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", f"Cannot connect to API:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())