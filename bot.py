import discord
from discord.ext import commands
from discord.ui import Select, View
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Dropdown Class
class RulesDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Police Roleplay Guidelines",
                description="Rules for Police Roleplay"
            ),
            discord.SelectOption(label="Option 2", description="Description 2"),
            discord.SelectOption(label="Option 3", description="Description 3"),
            discord.SelectOption(label="Option 4", description="Description 4"),
            discord.SelectOption(label="Option 5", description="Description 5"),
            discord.SelectOption(label="Option 6", description="Description 6"),
            discord.SelectOption(label="Option 7", description="Description 7"),
            discord.SelectOption(label="Option 8", description="Description 8"),
        ]
        super().__init__(
            placeholder="Press Here For In-Game Guidelines",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Police Roleplay Guidelines":
            full_text = (
                "**Police Roleplay Guidelines**\n\n"
                "1. Greeting Civilians\n"
                '   Begin interactions politely: "Good day, sir/ma\'am. May I see your license and registration?"\n\n'
                "2. Roleplay Interaction Protocol\n"
                "   -takes- → taking documents/items\n"
                "   -checking- → inspecting documents/vehicle\n"
                "   -gives back- → returning documents/items\n"
                "   -questions- → questioning civilians\n"
                "   -searching- → searching vehicle/person, if needed\n\n"
                "3. Document Checks\n"
                '   "Please hand over your license and registration."\n'
                "   -takes- the documents\n"
                "   -checking- their validity\n"
                "   -gives back- after inspection\n\n"
                "4. Response & Feedback\n"
                '   Clear: "You\'re all set, sir/ma\'am. You may proceed."\n'
                '   Issues: "There are some problems with your documents. Please wait while I verify further."\n\n'
                "5. Handling Suspicious Behavior\n"
                '   "Where are you headed?"\n'
                "   -questions- the civilian as needed\n\n"
                "6. Efficiency & Realism\n"
                "   Keep checks brief, ideally 1–2 exchanges per interaction\n"
                "   Follow realistic procedures with detailed descriptions\n\n"
                "7. Respect & Professionalism\n"
                "   Treat all civilians respectfully, regardless of behavior\n\n"
                "8. Time Management\n"
                "   Complete each check within a few minutes to prevent delays\n\n"
                "9. Reporting & Conduct\n"
                "   Report any misconduct and follow all protocols to maintain high standards"
            )
            await interaction.response.send_message(full_text, ephemeral=True)
        else:
            await interaction.response.send_message(f"You selected: {self.values[0]}", ephemeral=True)

# View Class
class RulesView(View):
    def __init__(self):
        super().__init__()
        self.add_item(RulesDropdown())

# Command
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
    await ctx.send(embed=embed, view=RulesView())

# Run Bot
bot.run(TOKEN)
