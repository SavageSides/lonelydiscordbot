import discord
from discord.ext import commands
import random
import time


TOKEN = 'NDc5MDM4NjAwODgxNjM1MzU0.DlTbGA.GGTVwCRVT2LDrsA8PxbQM7spmf8'


client = commands.Bot(command_prefix='?')
newUserMessage = """
**Welcome to Lonely! We all hope you have a good time here at Lonely :smile:**
```If you would like to invite your friends we would appreicate it!
Have a good time```https://giphy.com/gifs/pitchperfect-movie-pitch-perfect-pitchperfect2-MVDPX3gaKFPuo
"""

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Prefix | "?"'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot is ready to preform master')

@client.event
async def on_member_join(member):
    print("Recognized that a member called " + member.name + " jonied")
    await client.send_message(member, newUserMessage)
    print("Sent message to " +member.name)



@client.command(pass_context=True)
@commands.has_role("Mod")
async def kick(ctx, user: discord.Member):
    await client.say("User has been kicked :thumbsup:")
    await client.kick(user)

@client.command(pass_context=True)
@commands.has_role("Dev")
async def ban(ctx, user: discord.Member):
    await client.say("The user has been Banned :thumbsup:")
    await client.ban(user)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def mute(ctx, user: discord.Member):
    MutedRole = discord.utils.get(ctx.message.server.roles,name='Muted')
    await client.say("User Muted :white_check_mark: ")
    await client.add_roles(user, MutedRole)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def unmute(ctx, user: discord.Member):
    MutedRole = discord.utils.get(ctx.message.server.roles,name='Muted')
    await client.say("User Unmuted :white_check_mark:")
    await client.remove_roles(user, MutedRole)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def purge(ctx, amount=500):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted :white_check_mark:')

@client.command(pass_context=True)
@commands.has_role("Mod")
async def verifie(ctx, user: discord.Member):
    NotLonely = discord.utils.get(ctx.message.server.roles,name='Not Lonely')
    LonelyMembers = discord.utils.get(ctx.message.server.roles,name='Lonely Members')
    await client.say("User Verified :white_check_mark: ")
    await client.add_roles(user, LonelyMembers)
    await client.remove_roles(user, NotLonely)
    await client.add_roles(user, LonelyMembers)
    await client.remove_roles(user, NotLonely)
    await client.remove_roles(user, NotLonely)


@client.command(pass_context=True)
@commands.has_role("Mod")
async def verifacation(ctx, user: discord.Member):
    NotLonely = discord.utils.get(ctx.message.server.roles,name='Not Lonely')
    LonelyMembers = discord.utils.get(ctx.message.server.roles,name='Lonely Members')
    await client.say("User Put back in verifacation :white_check_mark: ")
    await client.remove_roles(user, LonelyMembers)
    await client.add_roles(user, NotLonely)
    await client.remove_roles(user, LonelyMembers)
    await client.add_roles(user, NotLonely)
    await client.remove_roles(user, LonelyMembers)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Not Lonely')
    await client.add_roles(member, role)
                                                            


@client.command(pass_context=True)
async def modrules(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.teal()
    )

    embed.set_author(name='Mod Rules')
    embed.add_field(name='Rule #1', value='Abusing your perms and making jokes of the whole clan will cause a demotion!', inline=False)
    embed.add_field(name='Rule #2', value='Banning and kicking a member that did nothing is abusing so you will get demotion', inline=True)
    embed.add_field(name='Rule #3', value='Before you put someone back in verifacation you will go to #verifacation-logging and you will type who you put back to verifacation and why you did it!', inline=True)

    


    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def serverhelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.teal()
    )

    embed.set_author(name='Lonely clan Help center')
    embed.add_field(name='Display', value='?display, Showing you what the bot is and why it was coded', inline=False)
    embed.add_field(name='Devs Need some help?', value='?mod, Devs you can do this command to see the commands so you can use them', inline=True)
    embed.add_field(name='Wanna know the invite link?', value='?link, This command will send you the invite', inline=True)

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def mod(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.teal()
    )

    embed.set_author(name='Lonely clan Moderator help center')
    embed.add_field(name='Kicking', value='?kick, This command is for Moderators and Admins only!', inline=False)
    embed.add_field(name='Banning', value='?ban, This command is for Moderators and Admin only!', inline=True)
    embed.add_field(name='Muting', value='?mute, This command is for muting people when they are not minding well!', inline=True)
    embed.add_field(name='Unmuting', value='?unmute, This command is for unmuting the user/member!', inline=True)
    embed.add_field(name='Purging', value='?purge, When you purge it deletes the message. Devs you will only delete the messages needed to be deleted!', inline=True)
    embed.add_field(name='Verifie', value='?verifie, is when you verifie a user so they can get into the clan!', inline=True)
    embed.add_field(name='Verifacation', value='?verifacation, If you thought that someone will betray us you will type that!', inline=True)
                    

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def rules(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.teal()
    )

    embed.set_author(name='The rules')
    embed.add_field(name='Rule #1', value='You will never spam!', inline=False)
    embed.add_field(name='Rule #2', value='Keep the profanity down.', inline=True)
    embed.add_field(name='Rule #3', value='Your other discord users will apreciate if you didnt bully or harass them! So, no harrasinh for Bullying', inline=True)
    embed.add_field(name='Rule #4', value='Last and final rule! Always have fun here at lonely', inline=True)

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(
    title = "Users Info",
    description = "Here's what I could find",
    colour = discord.Colour.teal()
    )

    embed.add_field(name='Name', value=user.name, inline=True)
    embed.add_field(name='Status', value=user.status, inline=True)
    embed.add_field(name='Highest Role', value=user.top_role, inline=True)
    embed.add_field(name='Joined', value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)

    await client.say(embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.teal()
    )

    embed.set_author(name='Lonely Clan Invite')
    embed.add_field(name='Invite Link', value='https://discord.gg/fHsshw', inline=False)
    embed.add_field(name='Purpose', value='Make sure to stick with Lonely for more cool Stuff!', inline=True)

    await client.send_message(author, embed=embed)
                    

client.run(TOKEN)
