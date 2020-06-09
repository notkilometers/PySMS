import smtplib, ssl
# doesnt sanatize input but thats not my problem
#only uses gmail and at&t for the first iteration, will add other options later
#adding carrier lookup with numverify api 
class Number:
    def __init__(self, selfUser, selfPass , targetN, targetM, targetC):
        self.selfUser = selfUser 
        self.selfPass = selfPass
        self.targetN = targetN + "@txt.att.net"
        self.targetM = targetM
        self.targetC = targetC
        self.port = 465 # for ssl
        self.smtp = "smtp.gmail.com"
        self.context =  ssl.create_default_context()    
    @classmethod
    def getdata(cls):
        return cls(
            selfUser = input("Enter Your Email Including @ : "),
            selfPass = input("Enter Your Password : "),
            targetN = input("Enter Target Phone Number : "),
            targetC = input("Enter Target Phone Carrier : "),
            targetM = input("Enter Desired Message : ")
        ) 
    def send(self):
        with smtplib.SMTP_SSL(self.smtp, self.port, context=self.context) as server:
            server.login(self.selfUser, self.selfPass)
            server.sendmail(self.selfUser, self.targetN, self.targetM)
