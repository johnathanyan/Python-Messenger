#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()

form=cgi.FieldStorage()
h=form.getvalue('username')
c=form.getvalue('blockusername')
j=form.getvalue('blockorunblock')
x= open(str(h),'a')
xx= open(str(h),'r')

page = 'Content-type: text/html\n\n'
page += '<html><head><title>Block a User</title></head>\n'
page += '<body>'
if 'blockusername' not in form:
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
		<font color='red' size='2'>You did not enter a desired user to block/unblock.</font>
		<form action="chat.py" method="post">
		<input type="submit" name="inbox" value="Inbox"><br><br>
		<input type="submit" name="outbox" value="Outbox"><br><br>
		<input type="submit" name="block" value="Block List"><br><br>
		<input type="submit" name="compose" value="Compose""><br>
		<b> <a href='login.html'>Logout</a></b>
		<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
                <input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
                <input type="hidden" name="Login" value="Login">    
		<br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
else:
    if j == 'block' and c in xx.read().split(','):
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
		<font color='red' size='2'>User already blocked</font>
		<form action="chat.py" method="post">
		<input type="submit" name="inbox" value="Inbox"><br><br>
		<input type="submit" name="outbox" value="Outbox"><br><br>
		<input type="submit" name="block" value="Block List"><br><br>
		<input type="submit" name="compose" value="Compose""><br>
		<b> <a href='login.html'>Logout</a></b>
		<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
                <input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
                <input type="hidden" name="Login" value="Login">    
		<br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
    elif j == 'block':
        x.write(',' + c)
        os.chmod(h, 0777)
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
		<font color='teal' size='2'>Successfully blocked</font>
		<form action="chat.py" method="post">
		<input type="submit" name="inbox" value="Inbox"><br><br>
		<input type="submit" name="outbox" value="Outbox"><br><br>
		<input type="submit" name="block" value="Block List"><br><br>
		<input type="submit" name="compose" value="Compose""><br>
		<b> <a href='login.html'>Logout</a></b>
		<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
                <input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
                <input type="hidden" name="Login" value="Login">
		<br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
    elif j == 'unblock' and c not in xx.read().split(','):
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
		<font color='red' size='2'>You have not blocked this user before.</font>
		<form action="chat.py" method="post">
		<input type="submit" name="inbox" value="Inbox"><br><br>
		<input type="submit" name="outbox" value="Outbox"><br><br>
		<input type="submit" name="block" value="Block List"><br><br>
		<input type="submit" name="compose" value="Compose""><br>
		<b> <a href='login.html'>Logout</a></b>
		<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
                <input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
                <input type="hidden" name="Login" value="Login">
		<br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
    elif j =='unblock':
        l = xx.read()
        l.strip(',' + str(c))
        l1 = open(str(h),'w')
        l1.write((l))
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
		<font color='teal' size='2'>Successfully unblocked</font>
		<form action="chat.py" method="post">
		<input type="submit" name="inbox" value="Inbox"><br><br>
		<input type="submit" name="outbox" value="Outbox"><br><br>
		<input type="submit" name="block" value="Block List"><br><br>
		<input type="submit" name="compose" value="Compose""><br>
		<b> <a href='login.html'>Logout</a></b>
		<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
                <input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
                <input type="hidden" name="Login" value="Login">
		<br>
		</center>
		</form>
	</div>
	
</body>

</html>'''
print page

    
