#username = ['yuki','mika','sayuri','kiko','shizuka']
#password = ['Zyk198199.','123456']
#import getpass
pair = {'name':'yuki', 'password':'yuki123'}
counter = 0

while counter < 3:
     counter += 1
     user = input('user:')
     se_pass = input('password:')
     if user == pair['name'] and se_pass == pair['password']:
         print('login in management system')
         break
     else:
         print('login failed, please try again')
else:
    print('please contact the administartor')
