# -*- coding: utf-8 -*-

def info(phenny, input):
    phenny.msg(input.nick, "Hi! I'm a bot, and my work is feed all recent changes on vikidia wikis (except ru.vikidia and de.vikidia). More information at http://tools.wmflabs.org/rc-vikidia/ or contact NeoMahler.")

info.commands = ['help', 'info', 'doc', 'commands']
