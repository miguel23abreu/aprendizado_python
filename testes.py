import  socket as s
host = 'www.cursoemvideo.com'
ip = s.gethostbyname(host)
print(f'O ip do host {host} é {ip}')