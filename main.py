import disnake 
from disnake.ext import commands
import os
from dotenv import load_dotenv
import asyncio

is_running = False

load_dotenv()


intents = disnake.Intents.default()
intents.message_content = True  


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("Work!")


@bot.command()
async def work(ctx, work_time: int = 25, break_time: int = 5):
    global is_running  
    
    if ctx.author.voice is None:
        await ctx.send("❌ Зайди в канал!")
        return

    
    is_running = True
    
    await ctx.send(f"🍅 Помодоро запущено на {work_time} хв! (Напиши !stop для зупинки)")

    
    for i in range(work_time * 60): 
        if not is_running: 
            return          
        await asyncio.sleep(1)

   
    if not is_running: return 

    channel = ctx.author.voice.channel
    voice = await channel.connect()
    voice.play(disnake.FFmpegPCMAudio("alarm.mp3"))
    await ctx.send(f"☕ Час відпочивати! Перерва {break_time} хв.")

    while voice.is_playing():
        await asyncio.sleep(1)

   
    for i in range(break_time * 60):
        if not is_running: 
            await voice.disconnect() 
            return
        await asyncio.sleep(1)
        
    
    voice.play(disnake.FFmpegPCMAudio("alarm.mp3"))
    await ctx.send("🚀 Пора за роботу!")

    while voice.is_playing():
        await asyncio.sleep(1)
        
    await voice.disconnect()
    is_running = False 


@bot.command()
async def stop(ctx):
    global is_running
    
    if not is_running:
        await ctx.send("🤔 Та я і так нічого не роблю.")
        return

    
    is_running = False
    await ctx.send("🛑 **Стоп машина!** Зупиняю таймер...")
    
    
    if ctx.guild.voice_client:
        await ctx.guild.voice_client.disconnect()






    






bot.run(os.getenv("DISCORD_TOKEN"))
