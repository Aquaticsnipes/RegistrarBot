# Work with Python 3.6
import os
from os import _exit
import discord
from discord.ext import commands
import time
import datetime

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    

    author = message.author
    content = message.content
    channel = message.channel
    server = message.server
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    filename = '{}.txt'.format(server)

    f = open('{}.txt'.format(filename), 'a')
    lines_of_text = ['[{} || {}]\n'.format(channel, timestamp), '{}: {}\n'.format(author, content), '\n']
    f.writelines(lines_of_text)
    f.close()

    print('Server:{}\n'
          '[{} || {}]\n'
          '{}: {}\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(server, channel, timestamp, author, content))

    if ('flip' in message.content.lower() and 
        'table' in message.content.lower() or
        'frustrat' in message.content.lower() or
        'pisse' in message.content.lower() or
        'dammnit' in message.content.lower() or 'damn it' in message.content.lower()):
        msg = '(╯°□°）╯︵ ┻━┻'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!help'):
        msg = ('!hello - say hello to me\n'
               '!wake - bring me online\n'
               '!help - get this list\n'
               '!newroom - create a new private channel\n'
               '!enroll :class1,class2,class3,etc - will assign you access to your class channels')
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!addRole'):
        filename = '{}Roles.txt'.format(server)
        f = open('{}.txt'.format(filename), 'a')
        customRoles = message.content.split()
        for x in customRoles:
            if '!' not in x:
                f.write(x)
        f.close()
    elif message.content.startswith('!enroll') :
        try:
            seperate = message.content.split(":")
            classes = seperate[1]
            classes = classes.split(",")
            
            for x in classes:
                if 'software' in x.lower() or 'sd' in x.lower():
                    role = discord.utils.get(message.author.server.roles, name='software design')
                    await client.add_roles(message.author, role)
                elif 'os' in x.lower() or 'operating' in x.lower():
                    role = discord.utils.get(message.author.server.roles, name='os')
                    await client.add_roles(message.author, role)

                elif 'ai' in x.lower() or 'artifical' in x.lower():
                    role = discord.utils.get(message.author.server.roles, name='ai')
                    await client.add_roles(message.author, role)
                elif 'network' in x.lower():
                    role = discord.utils.get(message.author.server.roles, name='network')
                    await client.add_roles(message.author, role)
                elif 'db' in x.lower() or 'data' in x.lower():
                    role = discord.utils.get(message.author.server.roles, name='db')
                    await client.add_roles(message.author, role)
                elif 'pleb' in x.lower():
                    role = discord.utils.get(message.author.server.roles, name='Plebs')
                    await client.add_roles(message.author, role)
        except:
            msg = ('Sorry {0.author.mention}, we were unable to enroll you in the class.\n'
            'Make sure that you used the formatting as shown in the !help command.\n'
            'There should be a : after enroll and commas between the name of each class.\n'
            'Exampe command: !enroll:database,ai').format(message)
            await client.send_message(message.channel, msg)
    elif (message.content.startswith('!sleep') and
        client.user.display_name in message.content and
        (message.author.top_role.name == 'Sys_Admin' or ('bot_tester' in [role.name for role in message.author.roles]))):
        await client.change_presence(status=discord.Status.offline)
    elif (message.content.startswith('!wake') and
        client.user.display_name in message.content):
        await client.change_presence(status=discord.Status.online)
    elif (message.content.startswith('!kill') and
        client.user.display_name in message.content and
        (message.author.top_role.name == 'Sys_Admin' or ('bot_tester' in [role.name for role in message.author.roles]))):
        await client.change_presence(status=discord.Status.offline)
        print('Exit')
        client.close()
        os._exit(0)
    elif message.content.startswith('!newroom'):
        temp_ = message.content.split()
        await client.create_role(server=message.server, name=temp_[1])
        await client.create_channel(message.server, temp_[1], type=discord.ChannelType.text)
    elif message.content.startswith('!') and client.user.display_name in message.content:
        msg = '{0.author.mention} this command does not exist or requires Admin permissions. Check for possible spelling errors.'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)