# WARNING
This script was made with learning purposes. I'm not responsible for others' misuse.
# CUIDADO
Este script se hizo con la intención de aprender. No me hago responsable del mal uso ajeno.
# Use examples
1. Encrypt a directory or file
python enc_dec.py --encrypt <path-to-directory/file>  
 
![imagen](https://user-images.githubusercontent.com/101645735/174485387-fea85650-c228-4836-bc21-b32daf4aefba.png)  
  
2. Decrypt a directory or file
python enc_dec.py --decrypt <path-to-directory/file> --key <KeyString | path-to-key-file>  
  
![imagen](https://user-images.githubusercontent.com/101645735/174485467-44d1341c-da57-4256-a692-67a3b037ff4b.png)  

# Arguments  

-h / --help -> Displays help message  
-enc / --encrypt -> Encrypting mode, takes a path  
-dec / --decrypt -> Decrypting mode, takes a path  
-k / --key -> Key to use, takes a path or a string  
-s / --safe -> Don't delete original files  
-v / --verbose -> Display a message with the path of the encrypted/decrypted file  
-sk / --savekey -> File to save the key at, working directory by default, only meaningful when encrypting
