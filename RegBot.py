# Compatible with python up to v3.6
import os
from os import _exit
import discord
import time
import datetime

TOKEN = ''

regBot = discord.Client()

# responds with polite greeting
# @parameter message object
async def hello(message):
    msg = 'Hi {0.author.mention}, hope you are having a wonderful day!'.format(message)
    await regBot.send_message(message.channel, msg)
    
# prints list of bot commands
# @parameter message object
async def help(message):
    msg = ('!hello - say hello to me\n'
        '!wake - bring me online\n'
        '!help - get this list\n'
        '!newroom - create a new private channel\n'
        '!enroll :class1,class2,class3,etc - will assign you access to your class channels')
    await regBot.send_message(message.channel, msg)

# reads in roles from {servername}Roles.txt file
# checks to see if selected courses are in the list.
# gives assigns roles that match.
# @parameter message object
async def enroll(message):
    filename = '{}Roles.txt'.format(message.server)
    f = open('{}'.format(filename), 'r')

    try:
        roles = message.content.split(" ",1)
        roles = roles[1]
        roles = roles.split(",")

        validateRoles = f.readline()
        validateRoles = validateRoles.split(',')
        print(validateRoles)
        for x in roles:
            for i in validateRoles:
                print(x)
                print(i)
                if x == i:
                    role = discord.utils.get(message.server.roles, name=i)
                    await regBot.add_roles(message.author, role)
                    msg = '{0.author.mention}, you have been enrolled succesfully.'.format(message)
                    await regBot.send_message(message.channel, msg)
    except:
        msg = 'Sorry {0.author.mention}, I am having difficulties processing your requrest.'.format(message)
        await regBot.send_message(message.channel, msg)


# reads role name and writes it to a file.
# file is saves as {servername}Roles.txt
# @parameter message object
async def addRole(message):
    try:
        filename = '{}Roles.txt'.format(message.server)
        f = open('{}'.format(filename), 'a')
        roleString = message.content.split(" ",1)
        f.write('{},'.format(roleString[1]))
        f.close()
        msg = '{0.author.mention}, the role has been added succesfully.'.format(message)
        await regBot.send_message(message.channel, msg)  
        

    except:
        msg = 'Sorry {0.author.mention}, I am having difficulties processing your requrest.'.format(message)
        await regBot.send_message(message.channel, msg)        

# overwrites previous roles file for the server.
# removes all roles from bots access.
async def clearRoles(message):
        filename = '{}Roles.txt'.format(message.server)
        f = open('{}'.format(filename), 'w')
        f.close()
        msg = '{0.author.mention}, I now have no roles to grant people.'.format(message)
        await regBot.send_message(message.channel, msg)  
# this function is called when a message is sent in any server
# this bot is present on
# temporarily a driver for testing.  Dictionary needs added to do quicker command calls
@regBot.event
async def on_message(message):
    if message.content.startswith('!addRole'):
        await addRole(message)
    elif message.content.startswith('!enroll'):
        await enroll(message)
    elif message.content.startswith('!hello'):
        await hello(message)
    elif message.content.startswith('!clearRoles'):
        await clearRoles(message)

@regBot.event
async def on_ready():
    print('Logged in as')
    print(regBot.user.name)
    print(regBot.user.id)
    print('------')

regBot.run(TOKEN)

    

    