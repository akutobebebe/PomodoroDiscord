import disnake
from disnake.ext import commands

# --- ⚙️ SETTINGS ---
ROLES_MAP = {
    "Backend": 1453404897474248714,
    "Frontend": 1453405001153122456,
    "Python": 1453404050455531635,
    "C++": 1453404357805609052,
    "JS": 1453404523010854922,
    "Figma": 1453404711817580741,
    "Linux": 1453404769048727613
}

# English descriptions (Описи англійською)
ROLES_DESC = {
    "Backend": "Server-side logic & APIs",
    "Frontend": "UI/UX implementation",
    "Python": "Python development",
    "C++": "System programming",
    "LS": "Scripting & Code",
    "Figma": "Design & Prototyping",
    "Linux": "Open Source & SysAdmin"
}

# Emojis for each role
ROLES_EMOJI = {
    "Backend": "⚙️",
    "Frontend": "🎨",
    "Python": "🐍",
    "C++": "🔵", 
    "JS": "📜",
    "Figma": "🖌️",
    "Linux": "🐧"
}
# ---------------------------

class RoleSelect(disnake.ui.Select):
    def __init__(self):
        options = []
        for label, role_id in ROLES_MAP.items():
            options.append(
                disnake.SelectOption(
                    label=label, 
                    value=str(role_id), 
                    description=ROLES_DESC.get(label, "Role"),
                    emoji=ROLES_EMOJI.get(label, "🔹")
                )
            )

        super().__init__(
            placeholder="Select your stack...", 
            min_values=0, 
            max_values=len(options), 
            options=options,
            custom_id="role_select_menu" 
        )

    async def callback(self, inter: disnake.MessageInteraction):
        all_role_ids = list(ROLES_MAP.values())
        selected_ids = [int(val) for val in inter.values]
        
        roles_to_add = []
        roles_to_remove = []

        guild = inter.guild

        for role_id in all_role_ids:
            role = guild.get_role(role_id)
            if not role:
                continue 
            
            if role_id in selected_ids:
                roles_to_add.append(role)
            else:
                roles_to_remove.append(role)

        if roles_to_remove:
            await inter.author.remove_roles(*roles_to_remove)
        if roles_to_add:
            await inter.author.add_roles(*roles_to_add)

        await inter.response.send_message(
            f"✅ Roles updated! Added: {len(roles_to_add)}, Removed: {len(roles_to_remove)}", 
            ephemeral=True 
        )

class RoleView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None) 
        self.add_item(RoleSelect())

class SelfRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Create role selection panel")
    @commands.default_member_permissions(administrator=True) 
    async def roles_panel(self, inter):
        embed = disnake.Embed(
            title="🛠️ Choose Your Stack",
            description="Select the technologies you work with from the menu below 👇",
            color=disnake.Color.from_rgb(44, 47, 51) # Dark theme style
        )
        await inter.channel.send(embed=embed, view=RoleView())
        await inter.response.send_message("Panel created successfully!", ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RoleView())

def setup(bot):
    bot.add_cog(SelfRoles(bot))