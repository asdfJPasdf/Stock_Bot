import discord 
import yfinance as yf
import datetime
from datetime import datetime
from discord.ext import commands
from dateutil import tz
from keep_alive import keep_alive
import os
    
client = commands.Bot(command_prefix= "$")# was man vor einen command schreiben muss
client.remove_command("help")
@client.event
async def on_ready():
  print('Money is raining!')


@client.group(invoke_without_command=True)
async def help(message): 
  embed = discord.Embed(title="Information", colour=discord.Colour(0x441c20), description="Für weitere Informationen über ein Command '$help <command>'\nVor jeden Command ein: '$' Bei allen(ausser top) Commands sollte nach dem Command noche das Symbol(z.B. TSLA für Tesla eingegeben werden.)", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
  embed.add_field(name=":information_source: info", value="infos über das Unternehmen")
  embed.add_field(name=":mountain_snow:  all", value="Alles")
  embed.add_field(name=":game_die:  summary", value="Eine Zusammenfassung der Tätigkeiten des Unternehmens")
  embed.add_field(name=":chart_with_upwards_trend: price", value="Der Aktuelle Aktienprice")
  embed.add_field(name=":8ball:  icon", value="Ein Bild des Firmenlogo")
  embed.add_field(name=':top: top',value='Einer Liste der Aktienpreise von Topaktien')
  embed.add_field(name=':symbols: symbol',value='Link mit einer Liste von Symbols')
  await message.send(embed=embed)

@help.command()
async def info(message):
    embed = discord.Embed(title="info", colour=discord.Colour(0xffec00), description="Gibt auskunft zu folgenden Themen eines Unternehmens:", timestamp=datetime.now(tz=tz.gettz("Europe/Berlin")))
    embed.add_field(name="Informationen:", value="Branche, Anzahl Vollzeitmitarbeiter, Webseite, Land")
    embed.add_field(name="**Syntax**", value="$info <Symbol>",inline=False)
    await message.send(embed=embed)
@help.command()
async def all(message):
    embed = discord.Embed(title="all", colour=discord.Colour(0xffec00), description="Alle Informationen", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name="**Syntax**", value="$all <Symbol>")
    await message.send(embed=embed)
@help.command()
async def summary(message):
    embed = discord.Embed(title="summary", colour=discord.Colour(0xffec00), description="Eine Beschreibung der Tätikeiten des Unternehmens", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name="**Syntax**", value="$summary <Symbol>")
    await message.send(embed=embed)
@help.command()
async def symbol(message):
    embed = discord.Embed(title="symbol", colour=discord.Colour(0xffec00), description="Liste mit Symbols von Firmen", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name="**Syntax**", value="$symbol <Symbol>")
    await message.send(embed=embed)
@help.command()
async def price(message):
    embed = discord.Embed(title="price", colour=discord.Colour(0xffec00), description="Der Aktuelle Aktienkurs", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name="**Syntax**", value="$price <Symbol>")
    await message.send(embed=embed)
@help.command()
async def icon(message):
    embed = discord.Embed(title="icon", colour=discord.Colour(0xffec00), description="Das Logo der Firma", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name="**Syntax**", value="$icon <Symbol>")
    await message.send(embed=embed)
@help.command()
async def top(message):
    embed = discord.Embed(title="top", colour=discord.Colour(0xffec00), description="Eine Auflistung einpaar Topaktien", timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name="**Topaktien**:", value="Apple, Tesla, Microsoft, Amazon, Netflix, Alphabet")
    embed.add_field(name="**Syntax**", value="$top",inline=False)
    await message.send(embed=embed)


@client.command(aliases=['top'])
async def _top(message):
    tickerdata=yf.Ticker('AAPL')
    tickerinfo=tickerdata.info
    apple=tickerinfo['regularMarketPrice']
    tickerdata=yf.Ticker('TSLA')
    tickerinfo=tickerdata.info
    tesla=tickerinfo['regularMarketPrice']
    tickerdata=yf.Ticker('MSFT')
    tickerinfo=tickerdata.info
    microsoft=tickerinfo['regularMarketPrice']
    tickerdata=yf.Ticker('AMZN')
    tickerinfo=tickerdata.info
    amazon=tickerinfo['regularMarketPrice']
    tickerdata=yf.Ticker('NFLX')
    tickerinfo=tickerdata.info
    netflix=tickerinfo['regularMarketPrice']
    tickerdata=yf.Ticker('GOOGL')
    tickerinfo=tickerdata.info
    google=tickerinfo['regularMarketPrice']
    embed = discord.Embed(title='Price Topaktien', colour=discord.Colour(0x3e9c35), timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name= 'Apple:',value='%s $'%apple)
    embed.add_field(name= 'Tesla:',value='%s $'%tesla)
    embed.add_field(name= 'Microsoft:',value='%s $'%microsoft)
    embed.add_field(name= 'Amazon:',value='%s $'%amazon)
    embed.add_field(name= 'Netflix:',value='%s $'%netflix)
    embed.add_field(name= 'Alphabet:',value='%s $'%google)
    await message.send(embed=embed)

@client.command(aliases=["symbol"])
async def _symbol(message):
    embed = discord.Embed(title='Symbols', colour=discord.Colour(0x3e9c35), timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name= 'Branche des Unternehmens:',value="Eine Liste von Firmen Symbols finden Sie [hier](https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed-symbols_csv/data/595a1f263719c09a8a0b4a64f17112c6/nasdaq-listed-symbols_csv.csv)")
    await message.send(embed=embed)

@client.command(aliases=["info"])
async def _info(message,*,tickersymbol):
    tickerdata=yf.Ticker(tickersymbol)
    tickerinfo=tickerdata.infos
    embed = discord.Embed(title=tickerinfo['shortName'], colour=discord.Colour(0x3e9c35), timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name= 'Branche des unternehmens:',value=tickerinfo['sector'])
    embed.add_field(name= 'Anzahl Vollzeit Mitarbeiter:',value=tickerinfo['fullTimeEmployees'])
    embed.add_field(name= 'Webseite:',value=tickerinfo['website'])
    embed.add_field(name= 'Land:',value=tickerinfo['country'])
    embed.set_thumbnail(url=tickerinfo['logo_url'])
    await message.send(embed=embed)

@client.command(aliases=["all"])
async def _all(message,*,tickersymbol):
    tickerdata=yf.Ticker(tickersymbol)
    tickerinfo=tickerdata.info
    embed = discord.Embed(title=tickerinfo['shortName'], colour=discord.Colour(0x3e9c35), timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name= 'Preis der Aktie:',value="%s$"%tickerinfo['regularMarketPrice'])
    embed.add_field(name= 'Branche des Unternehmens:',value=tickerinfo['sector'])
    embed.add_field(name= 'Anzahl Vollzeit Mitarbeiter:',value=tickerinfo['fullTimeEmployees'])
    embed.add_field(name= 'Land:',value=tickerinfo['country'])
    embed.add_field(name= 'Webseite:',value=tickerinfo['website'])
    embed.set_thumbnail(url=tickerinfo['logo_url'])
    await message.send(embed=embed)

@client.command(aliases=["price"])
async def _price(message,*,tickersymbol):
    tickerdata=yf.Ticker(tickersymbol)
    tickerinfo=tickerdata.info
    embed = discord.Embed(title=tickerinfo['shortName'], colour=discord.Colour(0x3e9c35), timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name= 'Aktienpreis:',value="%s$"%tickerinfo['regularMarketPrice'])
    embed.set_thumbnail(url=tickerinfo['logo_url'])
    await message.send(embed=embed)

@client.command(aliases=["icon"])
async def _icon(message,*,tickersymbol):
    tickerdata=yf.Ticker(tickersymbol)
    tickerinfo=tickerdata.info
    embed = discord.Embed(title=tickerinfo['shortName'], colour=discord.Colour(0x3e9c35),  timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.set_image(url=tickerinfo['logo_url'])
    await message.send(embed=embed)

@client.command(aliases=["summary"])
async def _summary(message,*,tickersymbol):
    tickerdata=yf.Ticker(tickersymbol)
    tickerinfo=tickerdata.info
    embed = discord.Embed(title=tickerinfo['shortName'], colour=discord.Colour(0x3e9c35), timestamp=datetime.now(tz=tz.gettz("europe/berlin")))
    embed.add_field(name= 'Firmentätigkeiten:',value=tickerinfo['longBusinessSummary'])
    embed.set_thumbnail(url=tickerinfo['logo_url'])
    await message.send(embed=embed)

client.run(os.getenv('TOKEN'))
