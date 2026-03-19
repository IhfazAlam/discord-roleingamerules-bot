import discord
from discord.ext import commands
from discord.ui import Select, View
import os

# --- Token from Environment Variables ---
TOKEN = os.environ["DISCORD_TOKEN"]

# --- DEFINE INTENTS BEFORE CREATING BOT ---
intents = discord.Intents.default()
intents.message_content = True  # needed for message commands

# --- CREATE BOT ---
bot = commands.Bot(command_prefix="!", intents=intents)

# -------------------------
# Dropdown Class
# -------------------------
class RulesDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="🚓 Police Roleplay Guidelines"),
            discord.SelectOption(label="Option 2"),
            discord.SelectOption(label="Option 3"),
            discord.SelectOption(label="Option 4"),
            discord.SelectOption(label="Option 5"),
            discord.SelectOption(label="Option 6"),
            discord.SelectOption(label="Option 7"),
            discord.SelectOption(label="Option 8"),
        ]
        super().__init__(
            placeholder="Press Here For In-Game Guidelines",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "🚓 Police Roleplay Guidelines":
            full_text = (
                "🚓 **Police Roleplay Guidelines**\n\n"
                "1️⃣ Greeting Civilians\n\n"
                '- Start politely: "Good day, sir/ma\'am. May I see your license and registration?"\n\n'
                "2️⃣ Roleplay Actions\n\n"
                "Use descriptive actions for immersion:\n\n"
                "- -takes- = taking documents/items\n"
                "- -checking- = inspecting documents/vehicle\n"
                "- -gives back- = returning documents/items\n"
                "- -questions- = questioning civilians\n"
                "- -searching- = searching vehicle/person if needed\n\n"
                "3️⃣ Document Checks\n\n"
                '- "Please hand over your license and registration."\n'
                "- -takes- the documents\n"
                "- -checking- validity\n"
                "- -gives back- once done\n\n"
                "4️⃣ Response & Feedback\n\n"
                "- ✅ Clear: \"You're all set, sir/ma'am. You may proceed.\"\n"
                "- ⚠️ Issues: \"There are some problems with your documents. Please wait while I verify further.\"\n\n"
                "5️⃣ Handling Suspicious Behavior\n\n"
                '- "Where are you headed?"\n'
                "- -questions- the civilian as needed\n\n"
                "6️⃣ Efficiency & Realism\n\n"
                "- Keep checks short (1–2 exchanges ideally)\n"
                "- Use realistic procedures & detailed RP\n\n"
                "7️⃣ Respect & Professionalism\n\n"
                "- Always treat civilians respectfully, no exceptions\n\n"
                "8️⃣ Time Management\n\n"
                "- Complete checks in a few minutes to avoid delays\n\n"
                "9️⃣ Reporting & Conduct\n\n"
                "- Report misconduct and follow all protocols to maintain high standards"
            )
            await interaction.response.send_message(full_text, ephemeral=True)
        else:
            await interaction.response.send_message(f"You selected: {self.values[0]}", ephemeral=True)

# -------------------------
# View Class
# -------------------------
class RulesView(View):
    def __init__(self):
        super().__init__()
        self.add_item(RulesDropdown())

# -------------------------
# Command
# -------------------------
@bot.command()
async def ehroleingames(ctx):
    embed = discord.Embed(
        title="📖 Departments, Civilians & Criminals – In-Game Rules",
        description=(
            "Welcome to SRP | SERIOUS RP! Below you will find role-specific rules for all Departments, Civilians, and Criminals. "
            "These rules are essential to make roleplay smooth and fair alongside the general #[Discord Channel]. "
            "Reading and understanding them is required to fully participate in RP scenes.\n\n"
            "⚠️ Important Notice\n"
            "By playing on SRP | SERIOUS RP, you automatically agree to follow all server rules.\n\n"
            "Failure to comply may result in:\n"
            "- Warnings\n"
            "- Kicks\n"
            "- Temporary or permanent bans\n"
            "- Restrictions on roles or departments"
        ),
        color=discord.Color.blue()
    )
    embed.set_image(url="https://i.postimg.cc/3NQ5LBVL/Roleplay-guideline.png")  # <-- your image URL

    await ctx.send(embed=embed, view=RulesView())

# -------------------------
# RUN BOT
# -------------------------
bot.run(TOKEN)
