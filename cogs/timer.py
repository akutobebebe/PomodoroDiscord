import disnake
from disnake.ext import commands
import asyncio

sessions = {}

class PomoControl(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Stop", style=disnake.ButtonStyle.danger)
    async def stop_callback(self, button, interaction):
        user_id = interaction.user.id
        if sessions.get(user_id):
            sessions[user_id] = False
            await interaction.response.send_message("🛑 Таймер зупинено кнопкою!", ephemeral=True)
        else:
            await interaction.response.send_message("🤔 У тебе немає активного таймера.", ephemeral=True)

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Запустити таймер")
    async def work(self, inter, work_time: int, break_time: int):
        user_id = inter.author.id
        
        if inter.author.voice is None:
            await inter.response.send_message("❌ Зайди в канал!", ephemeral=True)
            return

        sessions[user_id] = True
        view = PomoControl()
        
        await inter.response.send_message(f"🍅 Помодоро запущено на {work_time} хв!", view=view)
        
        for i in range(work_time * 60): 
            if not sessions.get(user_id, False): 
                return          
            await asyncio.sleep(1)

        if not sessions.get(user_id, False): return 

        channel = inter.author.voice.channel
        try:
            voice = await channel.connect()
        except:
            voice = inter.guild.voice_client

        if voice and not voice.is_playing():
            voice.play(disnake.FFmpegPCMAudio("alarm.mp3"))
        
        await inter.channel.send(f"☕ {inter.author.mention}, час відпочивати! Перерва {break_time} хв.")

        while voice.is_playing():
            await asyncio.sleep(1)

        for i in range(break_time * 60):
            if not sessions.get(user_id, False): 
                return
            await asyncio.sleep(1)
            
        if voice and not voice.is_playing():
            voice.play(disnake.FFmpegPCMAudio("alarm.mp3"))
            
        await inter.channel.send(f"🚀 {inter.author.mention}, пора за роботу!")

        while voice.is_playing():
            await asyncio.sleep(1)
            
        if user_id in sessions:
            del sessions[user_id]
            
        if voice:
            await voice.disconnect()

    @commands.slash_command(description="Зупинити роботу")
    async def stop(self, inter):
        user_id = inter.author.id
        
        if sessions.get(user_id):
            sessions[user_id] = False
            await inter.response.send_message("🛑 Таймер зупинено.", ephemeral=True)
        else:
            await inter.response.send_message("🤔 У тебе нічого не запущено.", ephemeral=True)

def setup(bot):
    bot.add_cog(Timer(bot))