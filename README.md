
# Encrypt - Decrypt with Fernet method

[Linux/Windows] - Allows encrypting and decrypting files/directories.






## Run locally

Clone the project

```bash
  sudo git clone https://github.com/Gurguii/Encrypt-decrypt-Fernet
```
Go to the project directory
```bash
    cd Encrypt-decrypt-Fernet
```
Execute the script
```bash
    python3 enc_dec.py
```
# Options
- -enc / --encrypt <file> or <path-to-file> - File or directory to encrypt 
- -dec / --decrypt <file> or <path-to-file> - File or directory to decrypt 
- -k / --key <Keystring> or <Path-to-key-file> - Must give when decrypting
- -s / --safe - When used original files won't be deleted
- -v / --verbose - Display info about which files get encrypted/decrypted
- -sk / --savekey <path> - Saves key in given path(when encrypting), default ./encryption_key
# Usage examples:
Encrypting a directory:
```bash
    python3 enc_dec.py --encrypt directory
```
Decrypting that same directory:
```bash
    python3 enc_dec.py --decrypt directory --key ./encryption_key
```
# Testing it
## Initial situation
```bash
    tree directory
```
![imagen](https://user-images.githubusercontent.com/101645735/175177942-2afd9191-f90b-46b5-9ebc-08d978b6aa09.png)

## Encrypting
```bash
    sudo python enc_dec.py --encrypt directory
```
 ![imagen](https://user-images.githubusercontent.com/101645735/175178180-9069ca72-ec4e-44a8-b400-61c402b1b72b.png)

## Checking encryption
```bash
    cat directory/file?; cat directory/anotherDir/file?
```
![imagen](https://user-images.githubusercontent.com/101645735/175178309-5044c063-8a47-4b0f-8dcf-8a1a8ffdd00b.png)

## Decrypting
```bash
    sudo python enc_dec.py --decrypt directory --key ./encryption_key
```
![imagen](https://user-images.githubusercontent.com/101645735/175178469-374c8aba-b62f-4fe7-92dd-065c730c6320.png)

## Checking decryption
```bash
    cat directory/file?; cat directory/anotherDir/file?
```
![imagen](https://user-images.githubusercontent.com/101645735/175178553-685c9960-095a-400f-be9e-c22025452786.png)
