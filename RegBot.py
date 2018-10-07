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
async def assistance(message):
    msg = ('!hello - say hello to me\n'
        '!addRole roleName - gives bot permission to assign role\n'
        '!clearRoles - removes all assigning permisions from bot\n'
        '!wake - bring me online\n'
        '!help - get this list\n'
        '!newroom - create a new private channel\n'
        '!enroll roleName, roleNamem, etc - will assign you access to your class channels')
    await regBot.send_message(message.channel, msg)

# reads in roles from {servername}Roles.txt file
# checks to see if selected courses are in the list.
# gives assigns roles that match.
# @parameter message object
async def enroll(message):
    filename = '{}Roles.txt'.format(message.server)
    f = open('{}'.format(filename), 'r')
    complete = False

    try:
        roles = message.content.split(" ",1)
        roles = roles[1]
        roles = roles.split(",")

        validateRoles = f.readline()
        validateRoles = validateRoles.split(',')
        print(validateRoles)
        for x in roles:
            for i in validateRoles:
                if i.startswith(' '):
                    i = i.split(" ", 1)[1]
                x = x.replace(" ", "")
                temp = i
                temp = temp.replace(" ", "")
                print(x)
                print(temp)
                if x == temp:
                    role = discord.utils.get(message.server.roles, name=i)
                    await regBot.add_roles(message.author, role)
                    msg = '{0.author.mention}, you have been enrolled succesfully.'.format(message)
                    await regBot.send_message(message.channel, msg)
                    complete = True
        if complete == False:
            msg = 'Sorry {0.author.mention}, I am having difficulties processing your requrest.'.format(message)
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
# @parameter message object (passed in from discord)
@regBot.event
async def on_message(message):

    bot_commands = {
        "!hello": hello,
        "!help": assistance,
        "!enroll": enroll,
        "!addRole": addRole,
        "!clearRoles": clearRoles
    }

    command = message.content.split()

    if command[0] in bot_commands and message.author != regBot.user:
        await bot_commands[command[0]](message)

@regBot.event
async def on_ready():
    print('Logged in as')
    print(regBot.user.name)
    print(regBot.user.id)
    print('------')

regBot.run(TOKEN)

    

    