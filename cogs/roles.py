import disnake

from disnake.ext import commands

class Roles(commands.Cog):
    def __init__ (self, bot):
         self.bot = bot


    @commands.Cog.listener()
    async def on_member_join (self,member):
        role = member.guild.get_role(1422267233874481323)

        if role:
            await member.add_roles(role)





def setup(bot):
    bot.add_cog(Roles(bot))