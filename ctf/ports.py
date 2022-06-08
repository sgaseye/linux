# cat ports.py
#!/usr/bin/python3
import socket
import select
def scan(ip):
  print('\n== ' + ip)
  try:
    for port in range(1,65535):  
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(0.2)
      result = sock.connect_ex((ip, port))
      if result == 0:
        sock.setblocking(0)
        ready = select.select([sock], [], [], 0.5)
        if ready[0]:
          data = sock.recv(4096)
        print("Port {}:      Open\n  {}".format(port, data))
        sock.close()
#      else:
#        print('.', end='', flush=True)
  except KeyboardInterrupt:
    sys.exit()
  except socket.gaierror:
    print('Hostname could not be resolved.')
    return
  except socket.error:
    print("Couldn't connect to server.")
    return
scan('172.18.0.2')
# for n in range(1, 255):
#   ip = '169.254.0.{}'.format(n)
#   scan(ip)
# cat ports.py | base64 | tr -d '\n' | xclip
