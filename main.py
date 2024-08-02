import discord
from discord.ext import commands
import socket
import random
import string
from dotenv import load_dotenv
import os



# Load environment variables from .env file
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('TOKEN')

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True

# Set up the bot with the specified prefix
bot = commands.Bot(command_prefix='sudo ', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} has connected to Discord!')

# Command to perform basic network mapping using the 'socket' library
@bot.command()
async def netmap(ctx, ip_or_url: str):
    try:
        # Basic host availability check
        ip_address = socket.gethostbyname(ip_or_url)
        await ctx.send(f'<:hatsune_miku_leek:1268782401266516009> IP address of {ip_or_url} is {ip_address}')

        # Basic port scanning
        ports = [21, 22, 23, 80, 443]  # Common ports
        result = ''
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result_code = sock.connect_ex((ip_address, port))
            if result_code == 0:
                result += f'Port {port}: Open\n'
            else:
                result += f'Port {port}: Closed\n'
            sock.close()

        await ctx.send(f'```\n{result}\n```')
    except Exception as e:
        await ctx.send(f'<:MikuExclamation:1268783070933417995> An error occurred: {str(e)}')
        
# Command to generate a random password
@bot.command()
async def genpass(ctx, length: int = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    await ctx.send(f'<:miku_surprised:1267143844890411202> Generated Password: `{password}`')

# Command to find the IP address of a website
@bot.command()
async def findip(ctx, website: str):
    try:
        ip_address = socket.gethostbyname(website)
        await ctx.send(f'<:miku_cry:1267143453045686397> The IP address of {website} is `{ip_address}`')
    except socket.gaierror:
        await ctx.send(f'<:MikuExclamation:1268783070933417995> Could not resolve the IP address for {website}')
    except Exception as e:
        await ctx.send(f'<:MikuExclamation:1268783070933417995> An error occurred: {str(e)}')

# Command to create a password list
@bot.command()
async def passlist(ctx, count: int = 10, length: int = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [''.join(random.choice(characters) for i in range(length)) for _ in range(count)]
    await ctx.send(f'<:miku_hearts:1268784520056934431> Generated Password List:\n```\n' + '\n'.join(password_list) + '\n```')

# Command to display help information
@bot.command(name='-h')
async def help_command(ctx):
    embed = discord.Embed(title="HELP MENU", description="<:MikuDab:1267151238622089251> List of available commands:", color=0x0000ff)
    embed.add_field(name="sudo netmap <ip_or_url>", value="Perform basic network mapping", inline=False)
    embed.add_field(name="sudo genpass [length]", value="Generate a random password", inline=False)
    embed.add_field(name="sudo findip <website>", value="Find the IP address of a website", inline=False)
    embed.add_field(name="sudo passlist [count] [length]", value="Create a password list", inline=False)
    embed.add_field(name="sudo -h", value="Display this help message", inline=False)
    embed.add_field(name="sudo neofetch", value="Display information about Miku", inline=False)
    embed.add_field(name="sudo ping", value="Display WebSocket latency", inline=False)
    embed.add_field(name="sudo youtube", value="Send a special YouTube video link", inline=False)
    await ctx.send(embed=embed)

# Command to display ASCII art of Miku and version information
@bot.command(name='neofetch')
async def neofetch_command(ctx):
    ascii_art = r"""
         __     
       <(o )___
        (  ._> /
         `---' 
    """
    version_info = "Miku Bot\nVersion: 1.0\nMade by: Shadow University"
    await ctx.send(f'```\n{ascii_art}\n{version_info}\n```')

# Command to display WebSocket latency
@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f'<:kali:1268771406460747868> **Websocket Latency** : {latency * 1000:.2f} ms')

# Command to send a special YouTube video link
@bot.command()
async def youtube(ctx):
    special_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    await ctx.send(f'<:MikuHeart:1268780241380446229> See This Oni San!!!...: {special_link}')

# Respond to bot mention with its information
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.author.bot:
        embed = discord.Embed(
            title="About Miku",
            description=f"<:miku_thanks:1267146633766895656> Hello! I'm {bot.user.name}. I use the prefix `sudo `.",
            color=0x0000ff
        )
        embed.add_field(name="Commands", value="Use `sudo -h` to see the list of available commands.", inline=False)
        await message.channel.send(embed=embed)

    # Ensure other commands work
    await bot.process_commands(message)

bot.run(TOKEN)
