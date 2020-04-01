from bottle import Bottle, route, run, template, static_file, request, get, post
import os
import sys
from hashlib import sha256
page_template = """
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Projects</title>
		<style>
			html {	  
	
				background-color:#DEE7EC;
 
			}
			.content{
				font-family:Verdana;
	
	
			}
			body {
				text-align:center;
	
			}
			.menu a:hover{
				background-color:white;
			}


			
				
			
			.buton {
				color:#89928A;
				
			}
			.link {
				text-decoration:none;
				text-align:center;
				padding-left:15px;
				padding-right:15px;
				padding-top:5px;
				padding-bottom:5px;
				
				
				
			}
			.imag{
				padding:25px;
			
			}
			h2 {
				font-family:verdana;
			
			}
		
				
			
			
		
	
	
			</style>
	</head>
	<body>
		<div class="content">
			<div class="menu">
				<img src="/static/logo.png" alt="logo" width="40" style="float:left;" >
				<a href="/index" class="link"><span class="buton"> Home</span></a> 
				<a href="/biography" class="link"> <span class="buton">Biography</span></a> 
				<a href="/" class="link"><span class="buton"> Projects</span></a>  				 
				<a href="/contact" class="link"><span class="buton"> Contact Me</span></a> 
			</div>
			<hr>


         	
         
          <h3>Ip Adresses</h3> %(clientip)s
	   <br>
        
            <h3>Counts</h3>%(number)s
	<h4>This webpage is:</h4>

<form >
  <input type="radio" name="s" value="great" checked >Great<br>
  <input type="radio" name="s" value="soso"> Not bad<br>
  <input type="radio" name="s" value="improvable" >Improvable<br>
  
</form>

	
			
			
			
			
				
				
	
				
				
		
	</div>	
	</body>
</html>
"""  
liste=[]



@route ('/index')
def index():

        
    
    return template ('index')  
@route ('/login', method='POST')
def index_login():
    global liste
    def create_hash(password):
        pw_bytestring = password.encode()
        return sha256(pw_bytestring).hexdigest()
   

    
    password = request.forms.get ( 'password' )   
    pw = create_hash(password)
    if pw == 'df8b30e1d76295a2210d5e6caf75d73150baaa3e3da2d8f9cd2462a58ba4e853':
        for i in range(len(liste)): 
            liste.clear()
        return template ('index')
    else:
        return "<p> failed</p>"
@route ('/biography')
def biography():
    
   
    return template ('biography')
    	

@route ('/contact')
def contact():
	return template ('contact')	

@route ('/')

def projects():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')   
    
    global liste

    liste=liste + [client_ip]

        
    
    q=0
    y = []
    while q < len(liste):
        if liste[q] not in y:
            y.append(liste[q])
        q += 1 
    k=[]
    for i in y:
        k =k+[liste.count(i)] 
        


    return page_template % {"clientip": y, "number": k}




	
@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./staticfiles')

	

	
run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug ='True', reloader='True')



