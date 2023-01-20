import ftplib

ftp = ftplib.FTP("ftp.example.com")
ftp.login("username", "password")

with open("log.txt", "wb") as f:
    ftp.retrbinary("RETR log.txt", f.write)

ftp.quit()
