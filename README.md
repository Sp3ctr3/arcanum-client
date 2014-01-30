arcanum-client
==============

Client for arcanum server. In Arcanum, the server plays very little role. The client handles encryption as well as decryption. The server merely handles file storage and user management. This ensures that even if the server is compromised, the user data is not.

Dependencies
-----------
pyqt4
keyczar
requests
Running
------
```shell
python client.py
```
