# Compatible with python up to v3.6
import os
from os import _exit
import discord
import time
import datetime

TOKEN = 'NDk3MTkwODI2NTI3NTU1NTg2.DphPJw.zR5V3MXlHKKujwY2U7uYT2b7-Aw'

regBot = discord.Client()

#responds with polite greeting
# @parameter message object
def hello(message):
    msg = 'Hi {0.author.mention}, hope you are having a wonderful day!'.format(message)
    regBot.send_message(message.channel, msg)
    
#prints list of bot commands
# @parameter message object
def help(message):
    msg = ('!hello - say hello to me\n'
        '!wake - bring me online\n'
        '!help - get this list\n'
        '!newroom - create a new private channel\n'
        '!enroll :class1,class2,class3,etc - will assign you access to your class channels')
    regBot.send_message(message.channel, msg)

#reads in roles from {servername}Roles.txt file
#checks to see if selected courses are in the list.
#gives assigns roles that match.
# @parameter message object
def enroll(message):
    filename = '{}Roles.txt'.format(message.server)


#reads role name and writes it to a file.
#file is saves as {servername}Roles.txt
# @parameter message object
def addRole(message):
    filename = '{}Roles.txt'.format(message.server)
    f = open('{}'.format(filename), 'a')
    roleString = message.content.split(" ",1)
    f.write(roleString[1])




@regBot.event
async def on_message(message):
    addRole(message)

@regBot.event
async def on_ready():
    print('Logged in as')
    print(regBot.user.name)
    print(regBot.user.id)
    print('------')

regBot.run(TOKEN)

    

    