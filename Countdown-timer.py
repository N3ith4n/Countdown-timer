from discord.ext import commands
import asyncio
import discord
import time
from datetime import date
from datetime import datetime
from pytz import timezone

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!!", intents=intents)

print("Requirments Met")

@bot.event
async def on_ready(pass_context=True):
	print ('Ready')
	
@bot.command(pass_context=True)
async def countdown(ctx):
	run = True
	while run:
		#SET AND SEND FIRST MESSAGE#
		now = datetime.now().astimezone(timezone("Asia/Manila"))
		release = datetime(year=2025, month=2, day=26, hour=11, minute=0, second=0).astimezone(timezone("Asia/Manila"))
		until_release = release - now
		
		embd = discord.Embed(title="", color=0xf0a5be)
		embd.insert_field_at(index=0, name="****", value=until_release)
		msg = await ctx.send(embed=embd)
		#########
		
		dot_count = 1
		x = 0
		#LOOP START#
		while True:
			if until_release.total_seconds() <= 0:
				embd.remove_field(index=0)
				embd = discord.Embed(title="**Welcome to Honkai: Star Rail 3.1, Trailblazers!**", description="The Astral Express wishes you good luck on your journey! ~☆", color=0xffffff)
				
				await msg.edit(content="@everyone", embed=embd)
				run = False
				break
				
			elif until_release.total_seconds() > 0:
				while until_release.total_seconds() >= 2*24*60*60:
					x += 1
					now = datetime.now().astimezone(timezone("Asia/Manila"))
					until_release = release - now
					dots = " . "*dot_count
					
					if dot_count < 3:
						dot_count += 1
						
					elif dot_count == 3:
						dot_count = 1
						
					embd.set_field_at(index=0, name=f"**Preparing for departure via Astral Express{dots}**", value=f"{until_release}")
					await msg.edit(embed=embd)
					
					if x == 30*60:
						break
						
					await asyncio.sleep(1)
					
					###
				while until_release.total_seconds() >= 1*24*60*60:
					x += 1
					now = datetime.now().astimezone(timezone("Asia/Manila"))
					until_release = release - now
					dots = " . "*dot_count
					
					if dot_count < 3:
						dot_count += 1
						
					elif dot_count == 3:
						dot_count = 1
						
					total_seconds = int(until_release.total_seconds())  # Convert to total seconds (ignoring microseconds)
					hours, remainder = divmod(total_seconds, 3600)
					minutes, seconds = divmod(remainder, 60)
					formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

					embd.set_field_at(index=0, name=f"**Preparing for arrival{dots}**", value=formatted_time)

					await msg.edit(embed=embd)
					
					if x == 30*60:
						break
						
					await asyncio.sleep(1)
					
					###
				while until_release.total_seconds() >= 30*60:
					x += 1
					now = datetime.now().astimezone(timezone("Asia/Manila"))
					until_release = release - now
					dots = " . "*dot_count
					
					if dot_count < 3:
						dot_count += 1
						
					elif dot_count == 3:
						dot_count = 1
						
					total_seconds = int(until_release.total_seconds())  # Get total seconds
					hours, remainder = divmod(total_seconds, 3600)
					minutes, seconds = divmod(remainder, 60)
					formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"  # Format as HH:MM:SS

					embd.set_field_at(index=0, name=f"**Preparing for arrival{dots}**", value=formatted_time)

					await msg.edit(embed=embd)
					
					if x == 30*60:
						break
						
					await asyncio.sleep(1)
					
				###
				while (until_release.total_seconds() < 30*60) and (until_release.total_seconds() > 0):
					x += 1
					now = datetime.now().astimezone(timezone("Asia/Manila"))
					until_release = release - now
					dots = " . "*dot_count
					
					if dot_count < 3:
						dot_count += 1
						
					elif dot_count == 3:
						dot_count = 1
						
					total_seconds = int(until_release.total_seconds())  # Get total seconds
					hours, remainder = divmod(total_seconds, 3600)
					minutes, seconds = divmod(remainder, 60)
					formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"  # Format as HH:MM:SS

					embd.set_field_at(index=0, name=f"**Arriving at your destined location{dots}**", value=formatted_time)

					await msg.edit(embed=embd)
					
					if x == 30*60:
						break
						
					await asyncio.sleep(1)
					
			await msg.delete()
			break
		
bot.run('TOKEN')
