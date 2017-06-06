# PING TEST A HOST 
# TYPE1: for linux hosts, works for Windows too.
import os
host = "172.27.16.29" 
response = os.system("ping -c 3 " + host)

# response will be zero for active(up) connection
if response == 0:
  print '\nHost:',host, 'is up!'
else:
  print '\nHost:',host, 'is down!'

## TYPE2: for any hosts (linux + windows)
#def ping(host):
#    """
#    Returns True if host responds to a ping request
#    """
#    import os, platform
#
#    # Ping parameters as function of OS
#    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
#
#    # Ping
#    return os.system("ping " + ping_str + " " + host) == 0
#
#ping('172.27.16.29')

# TYPE3: You can use pyping module
