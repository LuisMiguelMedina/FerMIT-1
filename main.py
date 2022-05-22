 # Description: Make the functionalities of the actual FerMIT bot
# Developers: Angel Magaña, Luis Inzunza, David Perez, Luis Medina
# Bugs: 1
# State: In progress

import os
import discord
from discord.ext import commands
import Fermit.src.Info.info
from Fermit.BotRunner.webserver import keep_alive

text = Fermit.src.Info.info.Texts()

# Secret Token
TOKEN = os.environ.get("FerMIT_Secret")

# Bot commands
bot = commands.Bot( command_prefix = '!', 
description = "Hola, soy FerMIT, ¿En que puedo ayudarte?" )

bot.remove_command( 'help' )

@bot.command()
async def ayuda( ctx ):
  await ctx.send(embed=text.help_message )

@bot.command()
async def comandos( ctx ):
  await ctx.send(embed=text.comandos_message )

@bot.command()
async def constancia( ctx ):
  await ctx.send(embed=text.constancia_message )

@bot.command()
async def inscripcion( ctx ):
  await ctx.send(embed=text.inscripcion_message)

@bot.command()
async def reinscripcion( ctx ):
  await ctx.send(embed=text.reinscripcion_message)

@bot.command()
async def revalidacion( ctx ):
  await ctx.send(embed=text.revalidacion_message )
  await ctx.send(embed=text.revalidacion_message_2 )

@bot.command()
async def adeudoconta( ctx ):
  await ctx.send(embed=text.adeudoconta_message )

@bot.command()
async def adeudobiblio( ctx ):
  await ctx.send(embed=text.adeudobiblio_message )
  
# Events
@bot.event
async def on_ready():
  print("My bot is ready")

# Bot runner
keep_alive()
bot.run(TOKEN)