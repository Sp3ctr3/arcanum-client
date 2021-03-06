arcanum-client
==============
>Arcanum is a file sharing and storage service that utilizes client side encryption to assure that no body other than the intended recipient can open the files.

Client for arcanum server. In Arcanum, the server plays very little role. The client handles encryption as well as decryption. The server merely handles file storage and user management. This ensures that even if the server is compromised, the user data is not.

During registration, the client generates a public,private key pair (RSA 2048). The private key is stored locally (encrypted with AES 256 in CBC mode) while the public key is sent to the server. The server stores the public key and a generated uuid to store files. When the client wants to send a file to another client, it fetches the other client's public key from the server. It generates a 256 bit AES key and encrypts the file with it. The AES key is then encrypted with the obtained public key and prepended to the symmetrically encrypted data. The file is sent to the server via a POST request. The other client fetches the file, decrypts the header using it's private key and then decrypts the rest of the message using the prepended AES key.

Dependencies
-----------
pyqt4
keyczar
requests

Running
------
First time
```shell
pip install -r requirements.txt
sudo apt-get install python-qt4

```
```shell
python client.py
```
