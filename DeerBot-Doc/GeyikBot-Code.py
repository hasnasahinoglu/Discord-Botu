import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import os
import time
import random 
import asyncio


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.command()
async def geyikbot(ctx):
  await ctx.send("Selam geyik!")


@client.event
async def on_ready():
  prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
  print(Fore.CYAN + "Canı sıkılan biri var...")
  print(prfx + "  Kullanıcı: " + Fore.YELLOW + str(client.user.name))


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="karşılama-ve-kurallar")
    await channel.send(f"{member.mention} canı sıkılanlar sohbetine hoş gelmiş!..")
    print(f"{member} canı sıkılanlar sohbetine hoş gelmiş!..")


@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="karşılama-ve-kurallar")
    await channel.send(f"{member.mention} gruptan ayrıldı.")
    print(f"{member} gruptan ayrıldı.")  


@client.command(aliases=['durdur', 'kes'])
async def sus(ctx):
  await ctx.send("Tamam, sustum.")
  await client.close()


@client.command(aliases=['minfo', 'sordur'])
async def bilgi(ctx, member:discord.Member=None):
  if member == None:
    member = ctx.message.author
  roles = [role for role in member.roles]
  embed = discord.Embed(title="Üye bilgileri", description=f"Üye {member.mention}", color=discord.Color.green(), timestamp = ctx.message.created_at)
  embed.set_thumbnail(url=member.avatar)
  embed.add_field(name="ID", value = member.id)
  embed.add_field(name="Ad", value = f"{member.name}#{member.discriminator}")
  embed.add_field(name="Nick", value = member.display_name)
  embed.add_field(name="Durum", value = member.status)
  embed.add_field(name="Şu tarihte oluşturuldu", value = member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
  embed.add_field(name="Şu tarihte katıldı", value = member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
  embed.add_field(name=f"Roller ({len(roles)})", value = " ".join([role.mention for role in roles]))
  embed.add_field(name="Etkin Rol", value = member.top_role.mention)
  embed.add_field(name="Bot?", value = member.bot)
  await ctx.send(embed=embed)


@client.command(aliases=['sinfo', 'serverinfo'])  
async def sunucubilgi(ctx):
  embed = discord.Embed(title="Sunucu Bilgileri", description=f"Bot geliştirmek için kurulmuştur {ctx.guild.name}", color=discord.Color.green(), timestamp=ctx.message.created_at)
  embed.set_thumbnail(url=ctx.guild.icon)
  embed.add_field(name="Üyeler", value = ctx.guild.member_count)
  embed.add_field(name="Kanallar", value = f"{len(ctx.guild.text_channels)} metin / {len(ctx.guild.voice_channels)} ses")
  embed.add_field(name="Kurucu", value = ctx.guild.owner.mention)
  embed.add_field(name="Açıklama", value = ctx.guild.description)
  embed.add_field(name="Şu tarihte oluşturuldu", value = ctx.guild.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
  await ctx.send(embed=embed)


@client.command(aliases=['hesap', 'işlem'])
async def mat(ctx, expression):
  symbols = ['+', '-', '*', '/', '%']
  if any(s in expression for s in symbols):
    calculated=eval(expression)
    embed = discord.Embed(title="Mat İşlemi", description=f"Hesapla {expression} \n Sonuç {calculated}", color=discord.Color.orange(), timestamp=ctx.message.created_at)
  else:
    await ctx.send("Sadece 4 işlem kabul edilir.")
  await ctx.send(embed=embed)  


@client.command(aliases=['topaç'])
async def zar(ctx, yuz:int=6):
  number=random.randint(1,yuz)
  await ctx.send(number)


@client.command(aliases=['sayıver'])
async def sayıseç(ctx, alt:int=1,ust:int=10):
  sayı=random.randrange(alt,ust)
  await ctx.send(sayı)


@ client.command(aliases=['para']) 
async def yazıtura(ctx, secim): 
  values = ['yazı', 'tura'] 
  computerChoice = random.choice(values) 
  if secim not in values: 
    await ctx.send("Önce tahminini de alayım:") 
  else : 
    if computerChoice == secim: 
      await ctx.send(f" Doğru tahmin, {secim}") 
    elif computerChoice != secim: 
      await ctx.send(f"Şansına küs, {computerChoice}")


@client.command(aliases=['karar'])
async def seç(ctx, *, args):
  arguments = args.split(" ")
  choice = random.choice(arguments)
  thinking = await ctx.send(":clock12: Bi Düşüneyim...")
  await asyncio.sleep(0.2)
  for i in range(4):
    await thinking.edit(content=f":clock{i+1}: Düşüneyim...")
    await asyncio.sleep(0.2)
  await ctx.send(choice)
  

client.run(os.getenv("TOKEN"))
