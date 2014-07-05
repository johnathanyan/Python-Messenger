#!/usr/bin/python
import cgi, cgitb
import os
cgitb.enable()

form = cgi.FieldStorage()
page = 'Content-type: text/html \n\n'
h=form.getvalue('username')
x= open(str(h),'a')
x.close()

if 'inbox' in form:
    a = open('Inbox-'+form.getvalue('username')+'.txt','r').read()
    a = a.split('endmessagesplit')
    page +='''<html>
<head>
	<title>Inbox</title>
	<link href="bubble.css" rel="stylesheet" type="text/css">
</head>
<body background="jlj.png">'''
    for x in a[:-1]:
        page += '<center><p class="bubble">' + x + '<hr></p></center>'
    page +='''
<center>
<form action="login.py" method="post">
<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
<input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
<input type="hidden" name="Login" value="Login">
<input type="submit" name="submit" value="Menu">
</center>

</body></html>'''
    
elif 'outbox' in form:
    a = open('Outbox-'+form.getvalue('username')+'.txt', 'r').read()
    a = a.split('endmessagesplit' )
    page +='''<html>
<head>
	<title>Outbox</title>
	<link href="bubble.css" rel="stylesheet" type="text/css">
</head>
<body background="jlj.png">'''
    for x in a[:-1]:
        page += '<center><p class="bubble">' + x + '<hr></p></center>'
    page +='''
<center>
<form action="login.py" method="post">
<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
<input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
<input type="hidden" name="Login" value="Login">
<input type="submit" name="submit" value="Menu">
</center>
</body></html>'''

elif 'block' in form:
    page +='''
<html><head><title>Block a User</title><link href="mydiv.css" rel="stylesheet" type="text/css"></head>
<form name="input" action="blocked.py" method="post"><br>
<body background="jlj.png">
<form action="login.py" method="post">
<input type="hidden" name="username" value="'''+form.getvalue('username')+'''">
<input type="hidden" name="password" value="'''+form.getvalue('password')+'''">
<input type="hidden" name="Login" value="Login">

	<div id="mydiv">
	<center>
	<h1>Block/Unblock Page</h1><br>
Username:<font color='teal'> ''' + form.getvalue('username') + '''</font> <br><br>

Desired Blocked/Unblocked User: <input type='text' name="blockusername"><br><br>

Block : <input type='radio' name='blockorunblock' value='block' checked><br>
Unblock : <input type='radio' name='blockorunblock' value='unblock'><br><br>
<input type="submit" value="Submit">
</body>
</html>
'''
    
elif 'compose' in form:
    page += '''<html>

<head>
	<title>Compose Message</title>
	<link href="mydiv.css" rel="stylesheet" type="text/css">
</head>

<body background="jlj.png">

	<div id="mydiv">
		<form action="chat.py" method="post">
                <input type="hidden" name="username" value="''' + form.getvalue('username') + '''">
                <input type="hidden" name="password" value="''' + form.getvalue('password') + '''">
		<center><b>Compose A Message</b></center><br>
		To:<input type="text" name="receive"><br>
		Subject:<input type="text" name="subject"><br>
		<textarea rows="9" name="message" cols="57"></textarea><br><br>
		<center>
		<input type="submit" name="send" value="Send!">
		</center>
		</form>
	</div>
	
</body>

</html>'''

elif 'send' in form:
    blocked = open(form.getvalue('username'),'r').read().split(',')
    if form.getvalue('receive') in blocked:
        page += '''
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
		<font color='red' size='2'>User is blocked</font>
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
    elif 'receive' not in form:
        page += '''<html>

    <head>
            <title>Menu</title>
            <link href="mydiv.css" rel="stylesheet" type="text/css">
    </head>

    <body background="jlj.png">

            <div id="mydiv">
                    <h1><center>JLJ Messenger</center></h1>
                    <center>
                    <font color='red' size='2'>Recipient not specified.</font><br>
                    <form action="chat.py" method="post">
                    <input type="hidden" name="username" value="''' + form.getvalue('username') + '''">
                    <input type="hidden" name="password" value="''' + form.getvalue('password') + '''">
                    <input type="submit" name="inbox" value="Inbox"><br><br>
                    <input type="submit" name="outbox" value="Outbox"><br><br>
                    <input type="submit" name="block" value="Ignore List"><br><br>
                    <input type="submit" name="compose" value="Compose"><br>
                    <b> <a href='login.html'>Logout</a></b>
                    <br>
                    </center>
                    </form>
            </div>
            
    </body>

    </html>'''
    elif 'subject' not in form:
        page += '''<html>

    <head>
            <title>Menu</title>
            <link href="mydiv.css" rel="stylesheet" type="text/css">
    </head>

    <body background="jlj.png">

            <div id="mydiv">
                    <h1><center>JLJ Messenger</center></h1>
                    <center>
                    <font color='red' size='2'>Subject not specified.</font><br>
                    <form action="chat.py" method="post">
                    <input type="hidden" name="username" value="''' + form.getvalue('username') + '''">
                    <input type="hidden" name="password" value="''' + form.getvalue('password') + '''">
                    <input type="submit" name="inbox" value="Inbox"><br><br>
                    <input type="submit" name="outbox" value="Outbox"><br><br>
                    <input type="submit" name="block" value="Ignore List"><br><br>
                    <input type="submit" name="compose" value="Compose"><br>
                    <b> <a href='login.html'>Logout</a></b>
                    <br>
                    </center>
                    </form>
            </div>
            
    </body>

    </html>'''
    elif 'message' not in form:
        page += '''<html>

    <head>
            <title>Menu</title>
            <link href="mydiv.css" rel="stylesheet" type="text/css">
    </head>

    <body background="jlj.png">

            <div id="mydiv">
                    <h1><center>JLJ Messenger</center></h1>
                    <center>
                    <font color='red' size='2'>You did not enter a message.</font><br>
                    <form action="chat.py" method="post">
                    <input type="hidden" name="username" value="''' + form.getvalue('username') + '''">
                    <input type="hidden" name="password" value="''' + form.getvalue('password') + '''">
                    <input type="submit" name="inbox" value="Inbox"><br><br>
                    <input type="submit" name="outbox" value="Outbox"><br><br>
                    <input type="submit" name="block" value="Ignore List"><br><br>
                    <input type="submit" name="compose" value="Compose"><br>
                    <b> <a href='login.html'>Logout</a></b>
                    <br>
                    </center>
                    </form>
            </div>
            
    </body>

    </html>'''
        
    else: #written by Lester
        a = open('Outbox-'+form.getvalue('username')+'.txt', 'a')#sender's outbox
        a.write(form.getvalue('username') + ' to ' + form.getvalue('receive') + '<br><br> \n')
        a.write('Subject: ' + form.getvalue('subject') + '<br><br> \n')
        a.write(form.getvalue('message') + '<br><br> endmessagesplit \n')
        b = open('Inbox-' + form.getvalue('receive')+'.txt','a')#receiver's inbox
        b.write(form.getvalue('username') + ' to ' + form.getvalue('receive') + '<br><br> \n')
        b.write('Subject: ' + form.getvalue('subject') + '<br><br> \n')
        b.write(form.getvalue('message') + '<br><br> endmessagesplit \n')

        page += '''<html>

    <head>
            <title>Menu</title>
            <link href="mydiv.css" rel="stylesheet" type="text/css">
    </head>

    <body background="jlj.png">

            <div id="mydiv">
                    <h1><center>JLJ Messenger</center></h1>
                    <center>
                    <font color='green' size='2'>Message sent.</font><br>
                    <form action="chat.py" method="post">
                    <input type="hidden" name="username" value="''' + form.getvalue('username') + '''">
                    <input type="hidden" name="password" value="''' + form.getvalue('password') + '''">
                    <input type="submit" name="inbox" value="Inbox"><br><br>
                    <input type="submit" name="outbox" value="Outbox"><br><br>
                    <input type="submit" name="block" value="Ignore List"><br><br>
                    <input type="submit" name="compose" value="Compose"><br>
                    <b> <a href='login.html'>Logout</a></b>
                    <br>
                    </center>
                    </form>
            </div>
            
    </body>

    </html>'''

print page


    
