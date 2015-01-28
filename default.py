nick = 'rc-vikidia'
host = 'irc.freenode.net'
channels = ['#example', '#test'] #Channels to connect here
owner = '' #Owner nick here

# password is the NickServ password, serverpass is the server password
password = '' #Your nickerv password here
# serverpass = 'serverpass'

# These are people who will be able to use admin.py's functions...
admins = [owner, '']
# But admin.py is disabled by default, as follows:
exclude = []

# If you want to enumerate a list of modules rather than disabling
# some, use "enable = ['example']", which takes precedent over exclude
# 
# enable = []

# Directories to load user modules from
# e.g. /path/to/my/modules
extra = []

# Services to load: maps channel names to white or black lists
external = { 
   '#liberal': ['!'], # allow all
   '#conservative': [], # allow none
   '*': ['!'] # default whitelist, allow all
}

# EOF

