from xnatum import Xnat

username = 'your_username';
password = 'your_password';
xnat_instance_url = 'http://your-xnat-instace.com'
x = Xnat(xnat_instance_url, username, password)
print(x.list_projects())