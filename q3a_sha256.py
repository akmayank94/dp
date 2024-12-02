##using rsa library
import rsa

def gen_hash(pswd):
    pswd = pswd.encode('utf-8')
    hash = rsa.compute_hash(pswd, 'SHA-256')
    hex = hash.hex()
    return hex

def choice():
    print("\n\nEnter 0 to exit")
    print("Enter 1 to generate another hash: ")
    ch = int(input("Your choice: "))
    if(ch not in (0,1)):
        print("\nInvalid choice")
        ch = choice()
    return ch

def main():
    ch = 1
    while(ch):
        pswd = input("Enter a password: ")
        hash = gen_hash(pswd)
        print(hash)
        print("Length of hash digest : ",len(hash))
        ch = choice()

main()
