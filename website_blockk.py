import time
from datetime import datetime as dt
hosts_path="C:/Windows/System32/drivers/etc/HOSTS"
redirect=["127.0.0.1","127.0.0.2","127.0.0.3","127.0.0.4","127.0.0.5"]
website_list=["www.youtube.com"] #here you can add random websites which you want to block.
i=0
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,1) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.seek(0)
                    file.write(redirect[i]+"       "+ website+"\n")
                    i=i+1
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
