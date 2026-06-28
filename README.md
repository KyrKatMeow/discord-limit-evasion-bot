# A bot to "evade" Discord account limitations

> [!NOTE]
> I know the code is propaply garbage, i am pretty new to Python :/

## "Evade" Discord Warning System Limits
![Violation exmaple][https://support.discord.com/hc/article_attachments/38516009773847]

### How to use?
Go to the Discord Developer Portal[https://discord.com/developers/home]
Create a bot
Go to "Bot" tab and enable the Server Members Intent
Copy it's Token
> [!WARNING]
> DONT SHARE THE TOKEN, if someone has it, they can control your bot!
Then go to OAuth2, and generate a install URL, Scopes: bot Permissions: Administrator
Make a new server, if the violation dosen't say "You have limited access to servers until xx/xx/xx"
Download Python: https://www.python.org
Run the following commands in Terminal:
> [!NOTE]
> If you're on Windows, use WSL, CMD won't work
> ```bash
> pip3 install discord
> git clone https://github.com/KyrKatMeow/discord-limit-evasion-bot/
> cd discord-limit-evasion-bot
> ```
Then edit the main.py file, go to the bottom, and find the line:
> ```python
> bot.run("Your Token :3)
> ```
Replace "Your Token :3" with your token

Then run:
> ```bash
> python3 main.py
> ```
The bot should now start
Add the bot using the URL from earlier
A info channel will be created, read it
> [!TIP]
> If there are alredy members that you want to sync, run /sync-members
> To send messages, use /send

