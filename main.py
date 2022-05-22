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

# Requerimientos Funcionales Main 
@bot.command()
async def hola( ctx ):
  await ctx.send(embed=text.hola_message )

@bot.command()
async def comandos( ctx ):
  await ctx.send(embed=text.comandos_message )
  

@bot.command()
async def tramites( ctx ):
  await ctx.send(embed=text.tramites_message )

@bot.command()
async def mapa( ctx ):
  await ctx.send(embed=text.mapa_message )

@bot.command()
async def calendario( ctx ):
  await ctx.send(embed=text.calendario_message )

# Requerimientos Tramites
@bot.command()
async def revalidacion( ctx ):
  await ctx.send(embed=text.revalidacion_message )
  await ctx.send(embed=text.revalidacion_message_2 )

@bot.command()
async def inscripcion( ctx ):
  await ctx.send(embed=text.inscripcion_message)

@bot.command()
async def reinscripcion( ctx ):
  await ctx.send(embed=text.reinscripcion_message)

@bot.command()
async def descargaMaterias( ctx ):
  await ctx.send(embed=text.descargaLibres_message )
  await ctx.send(embed=text.descargaOptativas_message )

@bot.command()
async def constancia( ctx ):
  await ctx.send(embed=text.constancia_message )

@bot.command()
async def adeudoConta( ctx ):
  await ctx.send(embed=text.adeudoconta_message )
  
@bot.command()
async def adeudoBiblio( ctx ):
  await ctx.send(embed=text.adeudobiblio_message )

@bot.command()
async def titulacionMEFI( ctx ):
  await ctx.send(embed=text.titulacionMEFI_message )

@bot.command()
async def titulacionEGEL( ctx ):
  await ctx.send(embed=text.tituEGEL_message )

@bot.command()
async def titulacionTesis( ctx ):
  await ctx.send(embed=text.tituTesis_message )

@bot.command()
async def tituDirecta( ctx ):
  await ctx.send(embed=text.tituDirecta_message )
  


# Requerimientos de informacion de importancia
  
@bot.command()
async def ciscoAcademy( ctx ):
  await ctx.send(embed=text.ciscoAcademy_message )

@bot.command()
async def bajasAcademicas( ctx ):
  await ctx.send(embed=text.bajasAcademicas_message )

@bot.command()
async def bloquesCarga( ctx ):
  await ctx.send(embed=text.bloquesCarga_message )

  
  
# Events
@bot.event
async def on_ready():
  print("FerMIT is ready")

# Bot runner
keep_alive()
bot.run(TOKEN)