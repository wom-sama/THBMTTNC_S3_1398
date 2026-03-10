import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_of_rows = math.ceil(len(text) / key)
        num_of_full_cols = len(text) % key
        
        cols = []
        current_idx = 0
        
        for i in range(key):
            col_len = num_of_rows
            if num_of_full_cols > 0 and i >= num_of_full_cols:
                col_len = num_of_rows - 1
            
            cols.append(text[current_idx : current_idx + col_len])
            current_idx += col_len
            
        decrypted_text = ""
        for r in range(num_of_rows):
            for c in range(key):
                if r < len(cols[c]):
                    decrypted_text += cols[c][r]
                    
        return decrypted_text