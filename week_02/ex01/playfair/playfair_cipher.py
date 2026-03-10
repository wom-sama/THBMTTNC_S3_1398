class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = "".join(filter(str.isalpha, key.upper().replace("J", "I")))
        
        matrix_chars = []
        seen = set()
        for char in key:
            if char not in seen:
                matrix_chars.append(char)
                seen.add(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in seen:
                matrix_chars.append(letter)

        playfair_matrix = [matrix_chars[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = "".join(c for c in plain_text.upper().replace("J", "I") if c.isalpha())

        modified_text = ""
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            if i + 1 == len(plain_text):
                modified_text += a + 'X'
                break
            b = plain_text[i+1]
            if a == b:
                modified_text += a + 'X'
                i += 1
            else:
                modified_text += a + b
                i += 2

        encrypted_text = ""
        for i in range(0, len(modified_text), 2):
            pair = modified_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = "".join(c for c in cipher_text.upper().replace("J", "I") if c.isalpha())
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return decrypted_text