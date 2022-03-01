import smtplib


def send(user):
    print("to:")
    rec = input()

    print("write message:")
    info = input()
    server.sendmail(user, rec, info)


def log():
    print("username:")
    username = input()

    print("password:")
    password = input()

    try:
        server.login(username, password)  # user logging in
        send(username)

    except:
        print("Username or password incorrect, try again")
        log()


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # email address and port num.

log()
