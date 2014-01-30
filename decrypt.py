def decrypt(data,name):
	from keyczar.keys import RsaPrivateKey,AesKey
	key=RsaPrivateKey.Read(open(name).read())
	aes=key.Decrypt(data[:261])
	aeskey=AesKey.Read(aes)
	return aeskey.Decrypt(data[261:])
