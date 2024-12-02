def encryptRailFence(text, key):
    # cols for text and key for rails
    rail = [['\n' for i in range(len(text))] for j in range(key)]

    #dir_down var for checing the zigzak pattern maintain krna h & row col for postion 
    dir_down = False
    row, col = 0, 0
    
    # matrix banani h 
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1                               
    
    #encrypted
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    return "".join(result)

def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    # Mark the positions with *
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Replace * with cipher charac ters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    # Read the matrix in zigzag manner to get the original text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    return "".join(result)

def menu():
    while True:
        print("\nRail Fence Cipher Menu")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            text = input("Enter text to encrypt: ")
            key = int(input("Enter the length of depth: "))
            encrypted_text = encryptRailFence(text, key)
            print("Encrypted Text:", encrypted_text)
        
        elif choice == 2:
            cipher = input("Enter text to decrypt: ")
            key = int(input("Enter the length of depth: "))
            decrypted_text = decryptRailFence(cipher, key)
            print("Decrypted Text:", decrypted_text)
        
        elif choice == 3:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")


menu()
