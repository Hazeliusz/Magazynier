import discord
import json
import os
from discord.ext import commands
from dotenv import load_dotenv
import officer
# global
prefix = "$"
client = commands.Bot(command_prefix=prefix)
json_file = "founds.json"

load_dotenv()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# region Officer

@client.command()
async def o(ctx, arg1, arg2):
    role = discord.utils.get(ctx.guild.roles, name="Oficer")
    if role not in ctx.author.roles:
        await ctx.send(f"Tylko oficerowie mogą używać tych komend.")
        return
    if arg1 == "withdraw":
        await officer.withdraw(ctx, arg2)
    elif arg1 == "deposit":
        await officer.deposit(ctx, arg2)


# endregion

# region Personal
@client.command()
async def founds(ctx, arg1):
    if arg1 == "check":
        with open(json_file) as foundsJson:
            data = json.load(foundsJson)
            await ctx.send("W kasie kompanii znajduje się " + str(data["founds"]) + " golda.")


# endregion
@client.event
async def on_command_error(ctx, error):
    await ctx.send("Nie czaję o co chodzi.")

client.run(os.getenv("TOKEN"))
client.add_command(o)
