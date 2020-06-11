import smtplib, ssl, json, requests
# doesnt sanatize input but thats not my problem
# only supports ATT due to not having enough numbers to compare to API output
# adding carrier lookup with numverify api

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
        print("Number type not supported (landline)")
    else:
        print("not landline, continuing")
    carrier = resp.split("carrier': '")[1]
    carrier = carrier.split("'")[0]
    print(carrier)
    return carrier

class SMS:
    def __init__(self, selfUser, selfPass , targetN, carrier="", targetNF="", lookupYN=""):
        targetN = str(targetN)
        self.selfUser = selfUser
        self.selfPass = selfPass
        self.targetN = targetN
        self.context =  ssl.create_default_context()
        if (lookupYN == "true" or lookupYN == "True" or lookupYN == "yes" or lookupYN == "Yes"):
            cLookup(self.targetN)
        else:
            cAdd = input("Enter SMS string for carrier including @ : ")
        if (carrier == "AT&T Mobility LLC"):
            cAdd = "@txt.att.net"
        elif (carrier == ""):
            pass
        else:
            cAdd = "@txt.att.net" # default to using most common carrier
        smtpString = self.selfUser.split("@")[1]
        if (smtpString == "gmail.com"):
            self.smtp = "smtp.gmail.com"
            self.port = 465 # ssl
        elif(smtpString == "outlook.com"):
            self.smtp = "smtp-mail.outlook.com"
            self.port = 587 # tls
        elif (smtpString == "yahoo.com"):
            self.smtp = "smtp.mail.yahoo.com"
            self.port = 465 # ssl
        elif (smtpString == "icloud.com"):
            self.smtp = "smtp.mail.me.com"
            self.port = 587 # tls
        elif (smtpString == "aol.com"):
            self.smtp = "smtp.aol.com"
            self.port = 465 # ssl
        elif (smtpString == "mail.com"):
            self.smtp = "smtp.mail.com"
            self.port = 587 #tls
        else:
            print("Email host not supported yet, existing.")
            exit()
        targetNF = targetN + cAdd
        self.targetNF = targetNF
    @classmethod
    def getdata(cls):
        return cls(
            lookupYN = input("Look Up Carrier for Phone Number? "),
            selfUser = input("Enter Your Email Including @ : "),
            selfPass = input("Enter Your Password : "),
            targetN = input("Enter Target Phone Number : "),
            targetNF = ""
        ) 
    def send(self):
        with smtplib.SMTP_SSL(self.smtp, self.port, context=self.context) as server:
            targetM = input("Enter Desired Message : ")
            server.login(self.selfUser, self.selfPass)
            server.sendmail(self.selfUser, self.targetNF, targetM)
