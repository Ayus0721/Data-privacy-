
def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    
    dir_down = False
    row, col = 0, 0
    
    for ch in text:
        
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row][col] = ch
        col += 1
        
        row = row + 1 if dir_down else row - 1
    
    
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    return "".join(result)



def decrypt_rail_fence(cipher, key):
    
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    
     
    dir_down = None
    row, col = 0, 0
    
    for _ in cipher:
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        row = row + 1 if dir_down else row - 1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
      result = []
    row, col = 0, 0
    for _ in cipher:
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False
        
        result.append(rail[row][col])
        col += 1
        
        row = row + 1 if dir_down else row - 1
    
    return "".join(result)

plaintext = "HELLO WORLD"
key = 3

cipher = encrypt_rail_fence(plaintext, key)
print("Encrypted:", cipher)

decrypted = decrypt_rail_fence(cipher, key)
print("Decrypted:", decrypted)
