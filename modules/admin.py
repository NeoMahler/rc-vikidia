#!/usr/bin/env python
# -*- coding: cp1252 -*-

def join(phenny, input): 
   u"""Join the specified channel."""
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin: 
      channel, key = input.group(1), input.group(2)
      if not key: 
         phenny.write(['JOIN'], channel)
      else: phenny.write(['JOIN', channel, key])
join.commands = ['join']
join.priority = 'low'
join.example = '.join #example or .join #example key'

def part(phenny, input): 
   u"""Part the specified channel."""
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin: 
      phenny.write(['PART'], input.group(2))
part.commands = ['part']
part.priority = 'low'
part.example = '.part #example'

def quit(phenny, input): 
   """Quit from the server."""
   # Can only be done in privmsg by the owner
   if input.sender.startswith('#'): return
   if input.owner: 
      phenny.write(['QUIT'])
      __import__('os')._exit(0)
quit.commands = ['quit']
quit.priority = 'low'

def msg(phenny, input): 
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   a, b = input.group(2), input.group(3)
   if (not a) or (not b): return
   if input.admin: 
      phenny.msg(a, b)
msg.rule = (['msg'], r'(#?\S+) (.+)')
msg.priority = 'low'

def me(phenny, input): 
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin: 
      msg = '\x01ACTION %s\x01' % input.group(3)
      phenny.msg(input.group(2) or input.sender, msg)
me.rule = (['me'], r'(#?\S+) (.+)')
me.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
