##cryptographic method sha-256
def right_rotate(x,n):
    return (x>>n) | (x<<(32-n)) & 0xFFFFFFFF


def pad_message(message):
    # Step 1: Convert the message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    original_length = len(binary_message)

    # Step 2: Append '1' bit
    binary_message += '1'

    # Step 3: Pad with '0' bits until the length is congruent to 448 mod 512
    k = (448 - (original_length + 1) % 512) % 512
    binary_message += '0' * k

    # Step 4: Append the original length as a 64-bit binary
    original_length_binary = format(original_length * 8, '064b') # Length in bits
    padded_message = binary_message + original_length_binary

    return padded_message

def sha(message):
    K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,0xab1c5ed5,0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7,0xc19bf174,0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc,
    0x76f988da,0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351,0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e,0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585,0x106aa070,0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f,
    0x682e6ff3,0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,0xc67178f2
    ]

    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]
    padded_message = pad_message(message)

    for i in range(0,len(padded_message),512):
        chunks = padded_message[i:i+512]

        W=[0]*64
        for j in range(16):
            W[j] = int(chunks[j*32:(j+1)*32],2)
        for j in range(16,64):
            s0 = right_rotate(W[j-15],7) ^ right_rotate(W[j-15],18) ^ (W[j-15]>>3)
            s1= right_rotate(W[j-2],17) ^ right_rotate(W[j-2],19) ^ (W[j-2]>>10)
            W[j] = (W[j-16] + s0 + W[j-7] + s1) & 0xFFFFFFFF

        a,b,c,d,e,f,g,h=H

        for j in range(64):
            S1 = right_rotate(e,6) ^ right_rotate(e,11) ^ right_rotate(e,25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = h + S1 + ch + K[j] + W[j] & 0xFFFFFFFF
            S0 = right_rotate(a,2) ^ right_rotate(a,13) ^ right_rotate(a,22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

            H[0] = (H[0] + a) & 0xFFFFFFFF
            H[1] = (H[1] + b) & 0xFFFFFFFF
            H[2] = (H[2] + c) & 0xFFFFFFFF
            H[3] = (H[3] + d) & 0xFFFFFFFF
            H[4] = (H[4] + e) & 0xFFFFFFFF
            H[5] = (H[5] + f) & 0xFFFFFFFF
            H[6] = (H[6] + g) & 0xFFFFFFFF
            H[7] = (H[7] + h) & 0xFFFFFFFF

        hash_value="".join([format(x, '08x') for x in H])
        return hash_value

while(True):
    print("SHA-256")
    # Menu driven program
    print("1. Enter the message")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 2:
        break
    elif choice == 1:
        message = input("Enter the message: ")
        hash_value = sha(message)
        print("The hash value is: ", hash_value)
    else:
        print("Invalid choice")
