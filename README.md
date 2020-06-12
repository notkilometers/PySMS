# PySMS

Python SMS sending utility via SMTP, including carrier lookup if desired

Usage Examples:

JohnDoe = SMS.getdata()  
Will prompt users to fill in necessary variables, including recipient phone number, sender's email & password.

JohnDoe = SMS("test-email@gmail.com", "TestPassword123", "3334567890")<br>
Prompts if user wishes to use carrier lookup to find carrier extension to send message, if not known

JohnDoe = SMS("test-email@gmail.com", "TestPassword123", "3334567890", "No")<br>
Same usage, opts out of carrier lookup

JohnDoe = SMS("test-email@gmail.com", "TestPassword123", "3334567890", "No", "@txt.att.net")<br>
Pre-fills with string for SMS with carrier 

