import smtplib
fromaddr='sanjaykumarnayak400@gmail.com'
toaddrs='sanjaykunayk2014@gmail.com'
msg='pir motion sensor'
username='sanjaykumarnayak400@gmail.com'
password='bholi123@N'
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddrs,msg)
print("success")
server.quit()
