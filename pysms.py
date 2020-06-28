import smtplib, ssl, json, requests

# doesnt sanatize input but thats not my problem
# only supports ATT due to not having enough numbers to compare to API output

api = "" # put api key here, get from numverify.com for 250 free lookups

def cLookup(targetN, carrier=""):
    targetN = str(targetN)
    url = "http://apilayer.net/api/validate?access_key=" + api +"&number=" + "1" + targetN
    req = requests.get(url)
    resp = repr(req.json())
    print(resp)
    linetype = resp.split("line_type': '")[1]
    print(linetype)
    linetype = linetype.split("'")[0]
    if (linetype == "landline"):
        print("Number type not supported for lookup(reported as landline)")
    else:
        print("not landline, continuing")
    carrier = resp.split("carrier': '")[1]
    carrier = carrier.split("'")[0]
    print(carrier)
    return carrier

def setupcarrier(self):
        if (self.carrier == "AT&T Mobility LLC"):
            self.cAdd = "@txt.att.net"
        elif (self.carrier == ""):
            pass
        else:
            cAdd = "@txt.att.net" # default to using most common carrier
        targetNF = self.targetN + self.cAdd
        self.targetNF = targetNF
        
def sendSetup(self, login):
    login.context =  ssl.create_default_context()
    smtpString = login.email.split("@")[1]
    if (smtpString == "gmail.com"):
        login.smtp = "smtp.gmail.com"
        login.port = 465 # ssl
    elif(smtpString == "outlook.com"):
        login.smtp = "smtp-mail.outlook.com"
        login.port = 587 # tls
    elif (smtpString == "yahoo.com"):
        login.smtp = "smtp.mail.yahoo.com"
        login.port = 465 # ssl
    elif (smtpString == "icloud.com"):
        login.smtp = "smtp.mail.me.com"
        login.port = 587 # tls
    elif (smtpString == "aol.com"):
        login.smtp = "smtp.aol.com"
        login.port = 465 # ssl
    elif (smtpString == "mail.com"):
        login.smtp = "smtp.mail.com"
        login.port = 587 #tls
    else:
        print("Email host not supported yet, existing.")
        exit()

class login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class email:
    def __init__(self, targetEmail):
        self.targetEmail = targetEmail
        
    def send(self, login, targetM):
        sendSetup(self, login)
        with smtplib.SMTP_SSL(login.smtp, login.port, context=login.context) as server:
            if(targetM == ""):
                targetM = input("Enter Desired Message : ")
            server.login(login.email, login.password)
            server.sendmail(login.email, self.targetEmail, targetM)
            
    @classmethod
    def getdata(cls):
        return cls(
            selfUser = input("Enter Your Email Including @ : "),
            selfPass = input("Enter Your Password : "),
            targetEmail = input("Enter Target Email : ")
        )

class sms:
    def __init__(self, targetN, cAdd=""):
        self.carrier = ""
        targetN = str(targetN)
        self.targetN = targetN
        self.cAdd = cAdd

    @classmethod
    def getdata(cls):
        return cls(
            targetN = input("Enter Target Phone Number : "),
            cAdd = input("(leave blank if unknown)\nEnter SMS string for carrier including @ : ")
        ) 
    def send(self, login, targetM):
        if (self.cAdd == "" ):
            self.carrier = cLookup(self.targetN)
        setupcarrier(self)
        sendSetup(self, login)
        with smtplib.SMTP_SSL(login.smtp, login.port, context=login.context) as server:
            if(targetM == ""):
                targetM = input("Enter Desired Message : ")
            server.login(login.email, login.password)
            server.sendmail(login.email, self.targetNF, targetM)
