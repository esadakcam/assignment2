from hashlib import sha256
comments=[]

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

while True:
    cmmnt=input("Any comments?")
    pw=input("Password?:")
    if pw == 'q':
        break
    else:
        password_hsh=create_hash(pw)
        if password_hsh == 'df8b30e1d76295a2210d5e6caf75d73150baaa3e3da2d8f9cd2462a58ba4e853':
          comments.append(cmmnt)  
          break
        else:
            print("Wrong Passowrd")
            break
print("""Preivous Comments:
 """)
print(comments)           
          
       

        