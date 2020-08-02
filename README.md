# PySMS
---converting to gui tool soon---
Python SMS and email sending utility via SMTP, including phone carrier lookup if desired<br>

Usage Examples:<br>

JaneDoe = login("JaneDoe@gmail.com", "SecurePassword")<br>
Fills in login info under named variable<br>

JohnDoe = sms.getdata()  <br>
Will prompt users to fill in necessary variables, including recipient phone number, and carrier SMS string if known.<br>

JohnDoe = email.getdata()  <br>
Will prompt users to fill in recipient email.<br>

JohnDoe = sms("3334567890", "@txt.att.net")<br>
Sets up email variable with phone number and carrier SMS string.<br>

JohnDoe = email("test-email2@gmail.com")<br>
Sets up email variable with recipient email<br>

JohnDoe.send(JaneDoe)<br>
Prompts for message, sends<br>

JohnDoe.send(JaneDoe, "example")<br>
Sends with message provided in function call<br>

