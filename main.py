import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("I mean we logged in")
  print("Trying to sync commands...")
  try:
    await bot.tree.sync()
    print("Commands synced successfully!")
  except:
      print("Failed to sync commands.")
  
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Grand Theft Auto VII"))

  @bot.event
  async def on_guild_join(guild):
     if guild.me.guild_permissions.administrator:
        info_channel = await guild.create_text_channel("info")
        embed = discord.Embed(title="What is this for?",description=f"{bot.user.name} is a bot to help people bypass false Discord account limitations!\n How to use it?\nAdda friend to the server (eg. using another platform), when they join a text channel will be created for you and them that only you and the member can access, then in that channel use the /send command to send a message with a webhook matching your profile!\n Why does it work?\nThe reason is pretty simple, Discord forgot/didn't prevent limited accounts from using / commands in servers!")
        await info_channel.send(embed=embed)
        await info_channel.set_permissions(guild.default_role,send_messages=False,view_channel=True)

@bot.event
async def on_member_join(member):
   try:
      channel = await member.guild.create_text_channel(member.name)
   except Exception as e:
      await member.guild.owner.send(content=f"There is an error: {e}")
      return
   await channel.set_permissions(member.guild.default_role,view_channel=False)
   await channel.set_permissions(member,view_channel=True)
   
@bot.tree.command(name="send",description="Break the TOS but like anyone cares!")
async def send(interaction: discord.Interaction,message: str):
   avatar_bytes = await interaction.user.display_avatar.read()
   webhook = await interaction.channel.create_webhook(name=interaction.user.display_name,avatar=avatar_bytes)
   await webhook.send(content=message)
   await webhook.delete()
   await interaction.response.send_message("@silent Message Sent!")
   await interaction.delete_original_response()

@bot.tree.command(name="sync-members",description="Create a private channel for every member!")
async def sync(interaction: discord.Interaction):
   if interaction.user.guild_permissions.manage_channels:
      for member in interaction.guild.members:
         if not member.bot and not member == interaction.guild.owner:
            try:
               channel = await interaction.guild.create_text_channel(member.name)
               await channel.set_permissions(interaction.guild.default_role,view_channel=False)
               await channel.set_permissions(member,view_channel=True)
            except:
               pass
      await interaction.response.send_message("Syncing complete!")

bot.run("Your Token :3")
