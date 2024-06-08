def encrypt_message(message, key):

    message = message.replace(" ", "")
    
    num_columns = len(key)
    
    num_rows = -(-len(message) // num_columns)  
    
    padding_length = num_columns * num_rows - len(message)
    message += ' ' * padding_length
    
    matrix = [message[i:i + num_columns] for i in range(0, len(message), num_columns)]

    ordered_key = sorted(range(len(key)), key=lambda k: key[k])
    
    cipher_text = ''.join(''.join(row[column] for row in matrix) for column in ordered_key)
    
    return cipher_text

def decrypt_message(cipher_text, key):

    num_columns = len(key)
    
    num_rows = -(-len(cipher_text) // num_columns) 
    
    ordered_key = sorted(range(len(key)), key=lambda k: key[k])

    cipher_matrix = [''] * num_columns
    start = 0
    for column in ordered_key:
        cipher_matrix[column] = cipher_text[start:start + num_rows]
        start += num_rows
    
    original_message = ''.join(''.join(cipher_matrix[column][row] for column in range(num_columns)) for row in range(num_rows))
    
    return original_message.strip()

# Ejemplo de uso
message = "Este codigo es secreto"
key = "clave"

# Cifrar el mensaje
cipher_text = encrypt_message(message, key)
print(f"Texto cifrado: {cipher_text}")

# Descifrar el mensaje
decrypted_message = decrypt_message(cipher_text, key)
print(f"Mensaje descifrado: {decrypted_message}")
