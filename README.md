# PySMS

Python SMS and Email sending utility via SMTP, including phone carrier lookup if desired

Usage Examples:

JohnDoe = SMS.getdata()  
Will prompt users to fill in necessary variables, including recipient phone number, sender's email & password.

JohnDoe = Email.getdata()  
Will prompt users to fill in necessary variables, including recipient email, sender's email & password.

JohnDoe = SMS("test-email@gmail.com", "TestPassword123", "3334567890", "@txt.att.net")<br>
Pre-fills with string for SMS with carrier

JohnDoe = Email("test-email@gmail.com", "TestPassword123", "test-email2@gmail.com")<br>
Sets up email variable with login information @ recipient email

JohnDoe.send()<br>
Prompts for message, sends

JohnDoe.send("example")<br>
Sends with message provided in function call

