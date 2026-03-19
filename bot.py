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
            discord.SelectOption(label="Police Roleplay Guidelines", emoji="🚓"),
            discord.SelectOption(label="Firefighter Roleplay Guidelines", emoji="🔥"),
            discord.SelectOption(label="Medic/EMS Roleplay Guidelines", emoji="🩺"),
            discord.SelectOption(label="HARS/Mechanic Roleplay Guidelines", emoji="🔧"),
            discord.SelectOption(label="Bus Driver Roleplay Guidelines", emoji="🚌"),
            discord.SelectOption(label="Truck Driver Roleplay Guidelines", emoji="🚛"),
            discord.SelectOption(label="Civilian Roleplay Guidelines", emoji="👤"),
            discord.SelectOption(label="Criminal Roleplay Guidelines", emoji="🕵️"),
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

        elif self.values[0] == "Firefighter Roleplay Guidelines":
        full_text = (
            "🔥 **Firefighter Roleplay Guidelines**\n\n"
            "- Respond promptly to fire and rescue calls, always prioritizing safety.\n"
            "- Provide detailed scene descriptions to enhance realism.\n"
            "- Follow all safety protocols during rescue operations.\n"
            "- Communicate clearly with team members and dispatch.\n"
            "- Handle fires and accidents professionally, showing respect for civilians and property.\n"
            "- Accurately document incidents for reports.\n"
            "- Perform realistic actions when extinguishing fires or rescuing victims.\n"
            "- Conduct regular equipment and vehicle checks.\n"
            "- Avoid reckless behavior during emergency responses.\n"
            "- Roleplay injuries and hazards with careful attention to detail."
        )
        await interaction.response.send_message(full_text, ephemeral=True)

    elif self.values[0] == "Medic/EMS Roleplay Guidelines":
        full_text = (
            "🩺 **Medic/EMS Roleplay Guidelines**\n\n"
            "- React promptly to medical emergencies with professionalism.\n"
            "- Assess injuries thoroughly and calmly, providing realistic first aid.\n"
            "- Communicate clearly with patients and dispatch.\n"
            "- Transport patients safely and professionally.\n"
            "- Follow medical protocols and procedures during treatment.\n"
            "- Accurately complete reports after each call.\n"
            "- Use realistic actions when treating or assisting patients.\n"
            "- Prioritize patient safety and comfort at all times.\n"
            "- Coordinate with other departments as needed.\n"
            "- Maintain equipment and vehicle readiness."
        )
        await interaction.response.send_message(full_text, ephemeral=True)

    elif self.values[0] == "HARS/Mechanic Roleplay Guidelines":
        full_text = (
            "🔧 **HARS/Mechanic Roleplay Guidelines**\n\n"
            "- Respond promptly to vehicle breakdown calls.\n"
            "- Inspect vehicles thoroughly, noting issues realistically.\n"
            "- Communicate professionally with drivers.\n"
            "- Explain repairs or towing using realistic language.\n"
            "- Follow all safety procedures near traffic.\n"
            "- Handle repairs and towing carefully and efficiently.\n"
            "- Accurately document each case.\n"
            "- Maintain equipment and vehicle readiness.\n"
            "- Avoid reckless or disruptive behavior.\n"
            "- Roleplay vehicle issues with attention to detail and realism."
        )
        await interaction.response.send_message(full_text, ephemeral=True)

    elif self.values[0] == "Bus Driver Roleplay Guidelines":
        full_text = (
            "🚌 **Bus Driver Roleplay Guidelines**\n\n"
            "- Follow designated routes and schedules accurately.\n"
            "- Greet passengers politely and create a welcoming environment.\n"
            "- Check tickets or passes when required.\n"
            "- Ensure passenger safety at all times using signals and safe driving practices.\n"
            "- Communicate delays or issues clearly to passengers and dispatch.\n"
            "- Conduct safety checks before each trip.\n"
            "- Handle passenger interactions respectfully and realistically.\n"
            "- Adhere to traffic laws and maintain realistic driving behavior.\n"
            "- Respond appropriately to traffic incidents or emergencies.\n"
            "- Regularly maintain the bus and safety equipment."
        )
        await interaction.response.send_message(full_text, ephemeral=True)

    elif self.values[0] == "Truck Driver Roleplay Guidelines":
        full_text = (
            "🚛 **Truck Driver Roleplay Guidelines**\n\n"
            "- Follow designated routes and comply with all traffic laws.\n"
            "- Perform thorough vehicle inspections before each trip.\n"
            "- Load and unload cargo carefully, describing the process realistically.\n"
            "- Communicate professionally with dispatch and clients.\n"
            "- Manage deliveries efficiently, documenting all details accurately.\n"
            "- Respond to breakdowns or delays realistically, notifying relevant parties.\n"
            "- Drive responsibly, using proper speeds, signals, and safety practices.\n"
            "- Respect weight and size restrictions on all roads.\n"
            "- Roleplay cargo security and inspection procedures faithfully.\n"
            "- Maintain the truck and equipment regularly to ensure safety and functionality."
        )
        await interaction.response.send_message(full_text, ephemeral=True)

    elif self.values[0] == "Civilian Guidelines":
        full_text = (
            "👤 **Civilian Roleplay Guidelines**\n\n"
            "- Roleplay realistically by following laws and scenario guidelines.\n"
            "- Interact respectfully with authorities and other players.\n"
            "- Respond to events naturally and report them appropriately.\n"
            "- Use detailed descriptions to make interactions immersive.\n"
            "- Avoid meta-gaming or powergaming to keep RP fair."
        )
        await interaction.response.send_message(full_text, ephemeral=True)

    elif self.values[0] == "Criminal Roleplay Guidelines":
        full_text = (
            "🕵️ **Criminal Roleplay Guidelines**\n\n"
            "- Roleplay criminal activities realistically and avoid metagaming.\n"
            "- Respond logically and appropriately to police interactions.\n"
            "- Describe actions in detail when planning or committing crimes.\n"
            "- Avoid god-moding or using unfair tactics.\n"
            "- Respect RP boundaries and follow all server rules."
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
