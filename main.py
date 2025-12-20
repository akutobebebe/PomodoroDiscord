import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()


intents = disnake.Intents.default()
intents.message_content = True
intents.members = True 


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} успішно зайшов у мережу!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        
        extension_name = f"cogs.{filename[:-3]}"
        try:
            bot.load_extension(extension_name)
            print(f"📂 Завантажено модуль: {filename}")
        except Exception as e:
            print(f"❌ Не вдалося завантажити {filename}: {e}")


bot.run(os.getenv("DISCORD_TOKEN"))