import os
import argparse
from cryptography.fernet import Fernet
import sys
key = "" # Holds the key used to encrypt-decrypt (symmetric key)
savekeypath = os.path.join(os.getcwd(),"encryption_key") # Holds the key file path, encryption_key in current working directory by default
def Encrypt_File(path):
    file_to_encrypt = path
    encrypted_file = path+"_encrypted"
    with open(file_to_encrypt,'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(encrypted_file,'wb') as file:
        file.write(encrypted_data)
    if not args.safe:
        os.remove(file_to_encrypt)
        os.rename(encrypted_file,file_to_encrypt)
        args.verbose and print("File {} - ENCRYPTED".format(file_to_encrypt))
        return
    args.verbose and print("File {} - ENCRYPTED".format(encrypted_file))

def Decrypt_File(path):
    file_to_decrypt = path
    decrypted_file = path+"_decrypted"
    with open(file_to_decrypt,'rb') as file:
        data = file.read()  
    try:
        decrypted_data = fernet.decrypt(data)
    except:
        return
    with open(decrypted_file,'wb') as file:
        file.write(decrypted_data)
    if not args.safe:
        os.remove(file_to_decrypt)
        os.rename(decrypted_file,file_to_decrypt)
        args.verbose and print("File {} - DECRYPTED".format(file_to_decrypt))
        return
    args.verbose and print("File {} - DECRYPTED".format(decrypted_file))

def iterateDirectory(path):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path,file)):
            # Code to execute when path points to a directory
            iterateDirectory(os.path.join(path,file))
            continue
        # Code to execute when path points to a file
        if file == "enc_dec.py" or file == "encryption_key" or file == "cosa.py": # Avoid deleting the key file or the script itself
            continue
        if args.encrypt: # If user wants to encrypt we call Encrypt_File() function, else we call Decrypt_File() function.
            Encrypt_File(os.path.join(path,file))
        else:
            Decrypt_File(os.path.join(path,file))

# Create argument parser
parser = argparse.ArgumentParser(description="Encrypt/Decrypt files using Fernet symmetric encryption method\nCreator: Gurgui",usage=f"\n<ENCRYPTING> python3 {sys.argv[0]} --encrypt <path>\n<DECRYPTING> python3 {sys.argv[0]} --decrypt <path> --key <path>")

# Add arguments
enc_dec = parser.add_mutually_exclusive_group(required=True)                                # These 3 lines allow me to force
enc_dec.add_argument("-enc","--encrypt", help="Encryption mode - takes a path", metavar="") # the user to use rather -enc or -dec 
enc_dec.add_argument("-dec","--decrypt", help="Decryption mode - takes a path", metavar="") # option but not both at the same time.
parser.add_argument("-k","--key", help="Key to use - must use when decrypting", metavar="")
parser.add_argument("-s","--safe", action='store_true', help="Don't delete original files")
parser.add_argument("-v","--verbose", action='store_true', help="Display extra info")
parser.add_argument("-sk","--savekey", help="File to save the key at. Current working directory by default", metavar="")

# Parse arguments
args = parser.parse_args()
# Make sure user has given a key when if decrypting
if args.decrypt and not args.key:
    print("\n[!] Key must be included when decrypting, <KeyString> or <PathToKeyFile>\n[!] Exiting")
    exit(0)

# Make sure the user wants remove source files
if not args.safe:
    rsp = input("\n[!] Save mode disabled [!] original file/s will be deleted - continue? y/n: ").lower()
    if rsp != "y" and rsp != "yes" and rsp != "ye":
        print("[!] Exiting")
        exit(0)

# Set keypath value if user used -kp/--keypath argument
if args.savekey:
    savekeypath=args.savekey

# If encrypt mode is chosen:
if args.encrypt:
    if args.encrypt == '.':
       enc_path = os.getcwd()
    else:
        enc_path = args.encrypt
    key = Fernet.generate_key()
    fernet = Fernet(key)
    if not os.path.exists(enc_path):
        print("[!] Path {} does not exist\n[!] Exiting".format(enc_path))
        exit(0)
    with open(savekeypath,'wb') as file:
        file.write(key)
    if os.path.isdir(enc_path):
        iterateDirectory(enc_path)
        print("\n[!] Directory {} recursevely encrypted".format(enc_path))
        print("[!] Encryption key saved at {}".format(savekeypath))
        exit(0)
    else:
        Encrypt_File(enc_path)
        print("[!] File {} succesfully encrypted".format(enc_path))
        print("[!] Encryption key saved at {}".format(savekeypath))
        exit(0)

# At this point decrypt mode is the choice, since you can't do --encrypt --decrypt && above if condition didn't happen (not encrypting)
# other way it would have ended in an exit(0) function and this code wouldn't have been executed.

if os.path.exists(args.key) and os.path.isfile(args.key):
    with open(args.key,'rb') as file:
        key = file.read()
else:
    key = args.key
if args.decrypt == '.':
    dec_path = os.getcwd()
else:
    dec_path = args.decrypt
fernet = Fernet(key)
if not os.path.exists(dec_path):
    print("[!] Path {} does not exist\n[!] Exiting".format(dec_path))
    exit(0)
if os.path.isdir(dec_path):
    iterateDirectory(dec_path)
    print("\n[!] Directory {} recursevely decrypted".format(dec_path))
    exit(0)
else:
    Decrypt_File(dec_path)
    print("[!] File {} succesfully decrypted".format(dec_path))
    exit(0)
