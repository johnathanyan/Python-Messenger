#! /usr/bin/python
#login written by Johnathan Yan
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
e = open('registered-users.txt','a')
a = open('registered-users.txt','r')
f = {}
gg = a.read().split(',')[1:]

if len(gg) >= 1:
    for x in gg:
        f[x.split(':')[0]] = x.split(':')[1]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
page = 'Content-type: text/html\n\n'

#put red letters register thing fail

if 'register' in form.keys(): #if trying to register
    page +='''<html>

<head>
        <title>Register</title>
        <link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

        <body background="jlj.png">

        <div id="mydiv">
                <h1><center>Register</center></h1>
                <center>
                <form action="login.py" method="post">
                Username:
                <input type="text" name="registername"><br><br>
                Password:
                <input type="password" name="registerpw"><br><br>
                <input type="submit" name="registered" value="Register">
                <br>
                <br>
                If you already have registered, please <a href="login.html"> login here</a>.
                </center>
                </form>
        </div>
        
</body>'''

if 'registered' in form.keys():
    if form.getvalue('registername') in f.keys(): #username taken
        page +='''<html>

<head>
        <title>Register</title>
        <link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

        <div id="mydiv">
                <h1><center>Register</center></h1>
                <center>
		<font size='2' color='red'>Username has already been taken. Please try again.</font><br>	
                <form action="login.py" method="post">
                Username:
                <input type="text" name="registername"><br><br>
                Password:
                <input type="password" name="registerpw"><br><br>
                <input type="submit" name="registered" value="Register">
                <br>
                <br>
                If you already have registered, please <a href="login.html"> login here</a>.
                </center>
                </form>
        </div>
        
</body>'''

    elif 'registername' not in form.keys(): #username not entered
        page +='''<html>

<head>
        <title>Register</title>
        <link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

        <div id="mydiv">
                <h1><center>Register</center></h1>
                <center>
		<font size='2' color='red'>Please enter a desired username.</font><br>	
                <form action="login.py" method="post">
                Username:
                <input type="text" name="registername"><br><br>
                Password:
                <input type="password" name="registerpw"><br><br>
                <input type="submit" name="registered" value="Register">
                <br>
                <br>
                If you already have registered, please <a href="login.html"> login here</a>.
                </center>
                </form>
        </div>
        
</body>'''

    elif 'registerpw' not in form.keys(): #password not entered
        page +='''<html>

<head>
        <title>Register</title>
        <link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

        <div id="mydiv">
                <h1><center>Register</center></h1>
                <center>
		<font size='2' color='red'>Please enter a desired password.</font><br>	
                <form action="login.py" method="post">
                Username:
                <input type="text" name="registername"><br><br>
                Password:
                <input type="password" name="registerpw"><br><br>
                <input type="submit" name="registered" value="Register">
                <br>
                <br>
                If you already have registered, please <a href="login.html"> login here</a>.
                </center>
                </form>
        </div>
        
</body>'''

        
    else: #creates account
        e.write(',' + form.getvalue('registername') + ':' + form.getvalue('registerpw'))
        f[form.getvalue('registername')] = form.getvalue('registerpw')
        inbox = open('Inbox-' + form.getvalue('registername')+'.txt','w')
        outbox = open('Outbox-' + form.getvalue('registername')+'.txt','w')
        block = open('Block-' + form.getvalue('registername')+'.txt','w')
        page += '''<!DOCTYPE html PUBLIC>

<html>

<head>
	<title>Login</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<h1><center>Login</center></h1>
		<center>
		<font size='2' color='teal'>Successfully Registered.</font><br>
		<form action="login.py" method="post">
		Username:
		<input type="text" name="username"><br><br>
		Password:
		<input type="password" name="password"><br><br>
		<input type="submit" name="Login" value="Login">
		<br>
		<br>
		If you have not registered yet, please <input type="submit" name="register" value="register here."><br>
		<font size='2' color='grey'> by Johnathan Yan, Lester Lee, and Jeffrey Zheng. Period 9. <font size='3' color = 'black'><br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
        
if 'Login' in form.keys():
    if 'username' not in form.keys(): #username not entered
        page += '''<!DOCTYPE html PUBLIC>

<html>

<head>
	<title>Login</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<h1><center>Login</center></h1>
		<center>
		<font size='2' color='red'>Invalid Username/Password Combination. Please try again.</font><br>
		<form action="login.py" method="post">
		Username:
		<input type="text" name="username"><br><br>
		Password:
		<input type="password" name="password"><br><br>
		<input type="submit" name="Login" value="Login">
		<br>
		<br>
		If you have not registered yet, please <input type="submit" name="register" value="register here."><br>
		<font size='2' color='grey'> by Johnathan Yan. Period 9. <font size='3' color = 'black'><br>
		</center>
		</form>
	</div>
	
</body>

</html>'''


    elif 'password' not in form.keys(): #password not entered
        page += '''<!DOCTYPE html PUBLIC>

<html>

<head>
	<title>Login</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<h1><center>Login</center></h1>
		<center>
		<font size='2' color='red'>Invalid Username/Password Combination. Please try again.</font><br>
		<form action="login.py" method="post">
		Username:
		<input type="text" name="username"><br><br>
		Password:
		<input type="password" name="password"><br><br>
		<input type="submit" name="Login" value="Login">
		<br>
		<br>
		If you have not registered yet, please <input type="submit" name="register" value="register here."><br>
		<font size='2' color='grey'> by Johnathan Yan. Period 9. <font size='3' color = 'black'><br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
    elif form.getvalue('username') not in f.keys(): #username not registered
        page += '''<!DOCTYPE html PUBLIC>

<html>

<head>
	<title>Login</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<h1><center>Login</center></h1>
		<center>
		<font size='2' color='red'>Invalid Username/Password Combination. Please try again.</font><br>
		<form action="login.py" method="post">
		Username:
		<input type="text" name="username"><br><br>
		Password:
		<input type="password" name="password"><br><br>
		<input type="submit" name="Login" value="Login">
		<br>
		<br>
		If you have not registered yet, please <input type="submit" name="register" value="register here."><br>
		<font size='2' color='grey'> by Johnathan Yan. Period 9. <font size='3' color = 'black'><br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
    elif f[form.getvalue('username')] != form.getvalue('password'): #username/password combo invalid
        page += '''<!DOCTYPE html PUBLIC>

<html>

<head>
	<title>Login</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<h1><center>Login</center></h1>
		<center>
		<font size='2' color='red'>Invalid Username/Password Combination. Please try again.</font><br>
		<form action="login.py" method="post">
		Username:
		<input type="text" name="username"><br><br>
		Password:
		<input type="password" name="password"><br><br>
		<input type="submit" name="Login" value="Login">
		<br>
		<br>
		If you have not registered yet, please <input type="submit" name="register" value="register here."><br>
		<font size='2' color='grey'> by Johnathan Yan. Period 9. <font size='3' color = 'black'><br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
        
    elif f[form.getvalue('username')] == form.getvalue('password'):
        page +='''
<!DOCTYPE html PUBLIC>

<html>

<head>
	<title>Menu</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<h1><center>JLJ Messenger</center></h1>
		<center>
		<form action="chat.py" method="post">
		<input type="submit" name="inbox" value="Inbox"><br><br>
		<input type="submit" name="outbox" value="Outbox"><br><br>
		<input type="submit" name="block" value="Block List"><br><br>
		<input type="submit" name="compose" value="Compose""><br><br>
		<b> <a href='login.html'>Logout</a></b>
		<input type="hidden" name="username" value="''' + form.getvalue('username') + '''">
                <input type="hidden" name="password" value="''' + form.getvalue('password') + '''">
		<br>
		</center>
		</form>
	</div>
	
</body>

</html>'''

e.close()
a.close()


print page
