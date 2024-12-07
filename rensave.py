import string, random, os, sys, subprocess
script = '.\\' + os.path.basename(__file__)

if os.name == 'nt':
 sl = '\\'
 os.system('cls')
else:
 sl='/'
 os.system('clear')

def token(n):
 strx = string.ascii_letters + string.digits
 token = ''.join(random.choice(strx) for _ in range(n))
 ext = '.plk'
 return token + ext

fsave = '.rootfiles'

def save(name):
 with open(fsave, 'a') as f:
  f.write(f"{name}\n")
  f.close()

nlatestx = []
ntokenx = []
if os.path.exists(fsave):
 with open(fsave, 'r') as f:
  ver = f.readlines()
  for v in ver:
   r = v.replace('\n', '')
   nlatest = r.split(f' .{sl}')[0]
   ntoken1 = r.split(f' .{sl}')[1]
   nlatestx.append(nlatest)
   ntokenx.append(ntoken1)

def proteger():
 for root, dirs, files in os.walk('.'):
  for file in files:
   rfile = os.path.join(root, file)
   findext = rfile.find('.plk')
   if rfile != script and findext == -1 and rfile != f'.{sl}.rootfiles':
    raiz = os.path.dirname(rfile) + f'{sl}'
    ntoken = raiz + token(12)
    if rfile not in nlatestx:
     name = f"{rfile} {ntoken}"
     os.rename(rfile, ntoken)
     save(name)
 if os.name == 'nt':
 	command = f'attrib +h +s {fsave}'
 	subprocess.run(command)

def desproteger():
 try:
  for a, b in zip(nlatestx, ntokenx):
   os.rename(b , a)
  os.remove(fsave)
 except:
  pass

proteger()
range=len(ntokenx)
if range != 0:
 desproteger()

