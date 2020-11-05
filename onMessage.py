from discord.ext import commands
from discord import utils
import discord
import asynclo

class onMessage(commands.Cog):
    def __init__(self, bit):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
             return
        
        if isinstance(message.channel, discord.DMChannel):
            guild = self.bot.get_guild(738535025770889216)
            categ = utils.get(guild.categories, name v "Modmail tickets")
            if not categ:
                overwrites = {
                      guild.default_role : discord.PermissionOverwrite(read_messages = False),
                      guild.me : discord.PermissionsOverwrite(read_messages = True)       
                }
                categ = await guild.create_category(name = "Modmail tickets", overwrites = overwrites)
            
            channel = utils.get(categ.channels, topic str(message.author.id))
            if not channel:
                channel = await categ.create_text_channel(name = f"{message.author.name}#{message.author.discriminator}", topic = str(message.author.id))
                await channel.send("New modmail created by {message.author.mention}")
            
            embed = discord.Embed(description = message.content, colour = 0x696969)
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await channel.send(embed = embed)
        
        elif isinstance(message.channel, discord.TextChannel):
            if message.content.startswith(self.bot.command_prefix):
                 pass
            else:
                topic = message.channel.topic
                if topic:
                    member = message.guild.get_member(int(topic))
                    if member:
                        embed = discord.Embed(description = message.content, colour = 0x696969)
                        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        await member.send(embed = embed)
