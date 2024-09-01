import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

my_role_id = 1276864217869193307 #OWNER ROLLEN ID

@bot.event
async def on_ready():
    print(f'{bot.user} ist bereit und online!')

    regel_id = 1276607334071931072  # REGEL CHANNEL ID
    regel = bot.get_channel(regel_id)

    rollen_id = 1276607893273055304  # ROLLEN CHANNEL ID
    rollen = bot.get_channel(rollen_id)

    info_id = 1276607690465874022 #INFORMATIONS CHANNEL
    info = bot.get_channel(info_id)

    sprache_id = 1276630353460596950 #programmiersprache channel id
    sprache = bot.get_channel(sprache_id)

    support_id = 1276608425685418035 #ID VOM SUPPORT CHANNEL
    support = bot.get_channel(support_id)
    # EMBED ROLLEN
    embed_rollen = discord.Embed(
        title="🔹 Server Rollen",
        description="Hier ist eine Übersicht der verfügbaren Rollen auf unserem Server:",
        color=discord.Color.from_str("#008080")  # Petrol-blau
    )

    embed_rollen.add_field(
        name="👑 **Owner**",
        value="• Die höchste Rolle auf dem Server.\n• **Verantwortlich** für die Verwaltung und das Wohl des Servers.\n• Hat **volle Kontrolle** über alle Einstellungen und Mitglieder.",
        inline=False
    )

    embed_rollen.add_field(
        name="🔧 **Helfer**",
        value="• Unterstützt die Owner bei der **Moderation**.\n• Kann Nachrichten **löschen** und Benutzer **stumm schalten**.\n• **Ansprechpartner** bei Problemen und Fragen.",
        inline=False
    )

    embed_rollen.add_field(
        name="👥 **Member**",
        value="• Die Standardrolle für alle **Mitglieder**.\n• Kann an **Diskussionen** teilnehmen und **Inhalte** teilen.\n• Sollte die **Server-Regeln** beachten und eine freundliche Atmosphäre fördern.",
        inline=False
    )

    embed_rollen.set_footer(text="Danke, dass du Teil unserer Community bist! 😊")

    # EMBED REGEL
    embed = discord.Embed( 
        title="📜 Server Regeln",
        description="Bitte halte dich an die folgenden Regeln, um eine freundliche und sichere Umgebung zu gewährleisten:",
        color=discord.Color.from_str("#008080")  # Petrol-blau
    )

    embed.add_field(
        name="1️⃣ **Respekt**",
        value="• **Respektiere** jeden im Server.\n• Keine **beleidigenden** oder **diskriminierenden** Kommentare.",
        inline=False
    )

    embed.add_field(
        name="2️⃣ **Keine Werbung**",
        value="• Werbung ist nur in den dafür vorgesehenen Kanälen erlaubt.\n• Kein **Spam** von Links oder Nachrichten.",
        inline=False
    )

    embed.add_field(
        name="3️⃣ **Kein Spam**",
        value="• Vermeide das wiederholte Senden von Nachrichten oder Emojis.\n• **Flooding** und **Trolling** sind verboten.",
        inline=False
    )

    embed.add_field(
        name="4️⃣ **Kanalthemen beachten**",
        value="• Poste nur Inhalte, die zum jeweiligen Kanal passen.\n• **Off-Topic**-Diskussionen bitte in den entsprechenden Kanälen führen.",
        inline=False
    )

    embed.add_field(
        name="5️⃣ **Moderatoren Anweisungen**",
        value="• Folge den Anweisungen der Moderatoren.\n• **Missachtung** kann zu einem **Ban** führen.",
        inline=False
    )

    embed.set_footer(text="Danke, dass du Teil unserer Community bist! 😊")

    await regel.purge()  # ALLES AUS REGEL CHANNEL LÖSCHEN
    await regel.send(embed=embed)  # EMBED SENDEN IN REGEL

    await rollen.purge()
    await rollen.send(embed=embed_rollen)

    embed_info = discord.Embed(
        title="🚫 Wichtige Mitteilung 🚫",
        description="Dieser Server wird **nie online gehen**. Er dient nur als **Übungsprojekt**, um meine Fähigkeiten zu verbessern.",
        color=discord.Color.red()
    )
    
    embed_info.add_field(
        name="📜 Zweck des Projekts",
        value="Dieser Server wurde erstellt, um verschiedene Aspekte der Bot-Entwicklung zu üben, einschließlich:\n"
              "- **Befehlsverarbeitung**\n"
              "- **Nachrichtenmanagement**\n"
              "- **Benutzerinteraktionen**",
        inline=False
    )
    
    embed_info.add_field(
        name="🛠️ Technologien",
        value="Dieser Bot nutzt die `discord.py` Bibliothek und ist auf den folgenden Technologien aufgebaut:\n"
              "- **Python**\n"
              "- **Discord API**",
        inline=False
    )
    
    embed_info.add_field(
        name="📅 Zeitplan",
        value="Da es sich um ein Übungsprojekt handelt, gibt es keinen **Fertigstellungstermin** oder **geplante Funktionen**.",
        inline=False
    )
    
    embed_info.add_field(
        name="💬 Kontakt",
        value="Wenn du Fragen oder Feedback hast, zögere nicht, mich zu kontaktieren.",
        inline=False
    )
    
    embed_info.set_footer(text="Danke für dein Verständnis! 😊")

    await info.purge()
    await info.send(embed=embed_info)

    # ROLEBUTTONS EMBED UND VIEW
    class RoleButtonView(discord.ui.View):
        def __init__(self, html_role_id, js_role_id, python_role_id):
            super().__init__(timeout=None)
            self.html_role_id = html_role_id
            self.js_role_id = js_role_id
            self.python_role_id = python_role_id

        @discord.ui.button(label="HTML/CSS", style=discord.ButtonStyle.secondary)  # Grau
        async def html_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            role = interaction.guild.get_role(self.html_role_id)
            
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"Die Rolle {role.name} wurde entfernt.", ephemeral=True)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"Du hast die Rolle {role.name} erhalten!", ephemeral=True)

        @discord.ui.button(label="JavaScript", style=discord.ButtonStyle.secondary)  # Grau
        async def js_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            role = interaction.guild.get_role(self.js_role_id)
            
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"Die Rolle {role.name} wurde entfernt.", ephemeral=True)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"Du hast die Rolle {role.name} erhalten!", ephemeral=True)

        @discord.ui.button(label="Python", style=discord.ButtonStyle.secondary)  # Grau
        async def python_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            role = interaction.guild.get_role(self.python_role_id)
            
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"Die Rolle {role.name} wurde entfernt.", ephemeral=True)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"Du hast die Rolle {role.name} erhalten!", ephemeral=True)

    view = RoleButtonView(HTML_ROLE_ID, JS_ROLE_ID, PYTHON_ROLE_ID)
    embed_role_buttons = discord.Embed(
        title="`Wähle deine Programmiersprache aus, die du lernen möchtest:`",
        color=discord.Color.from_str('#008080')
    )
    embed_role_buttons.add_field(
        name="**Sprache entfernen**",
        value="Um eine Programmiersprache wieder zu entfernen, klicke erneut auf den Button.",
        inline=False
    )
    
    await sprache.purge()
    await sprache.send(embed=embed_role_buttons, view=view)

    embed_dm_instruction = discord.Embed( #SUPPORT INSTRUCTION
    title="📩 Schick dem Bot eine Nachricht!",
    description=(
        "Falls du Hilfe benötigst oder eine Frage hast, "
        "sende bitte **dem Bot** eine Direktnachricht (DM) und nicht mir persönlich. "
        "Auf diese Weise kann das Team oder ich deine Nachricht schneller sehen und darauf reagieren."
    ),
    color=discord.Color.green()
    )

    embed_dm_instruction.add_field(
        name="🔹 Wie funktioniert das?",
        value=(
        "Klicke einfach auf den Bot-Namen und wähle **Nachricht** aus, um eine DM zu senden. "
        "Der Bot wird deine Nachricht dann automatisch an uns weiterleiten, sodass wir dir helfen können."
        ),
        inline=False
    )

    embed_dm_instruction.set_footer(text="Vielen Dank! 😊")

    await support.purge()
    await support.send(embed=embed_dm_instruction)


# BEGRÜßUNG
@bot.event
async def on_member_join(member):
    wilkommen_id = 1276605608820346900  # ID VON WILKOMMEN CHANNEL
    wilkommen = bot.get_channel(wilkommen_id)

    # EMBED FÜR BEGRÜßUNG
    embed = discord.Embed(
        title="👋 Willkommen auf CODING HILFEN!",
        description=f"Hallo {member.mention}, willkommen auf unserem Server! 🎉\n\n",
        color=discord.Color.from_str("#008080") 
    )
    embed.add_field(
        name="🔹 **Server Regeln**",
        value="Bitte lies dir zuerst die **Regeln** durch, um Missverständnisse zu vermeiden.",
        inline=False
    )
    embed.set_footer(text="Viel Spaß beim Programmieren Lernen! 😊")

    # AUTOMATISCH MEMBER ROLLE HINZUFÜGEN
    member_role = member.guild.get_role(1276862374850203680)
    await member.add_roles(member_role)

    await wilkommen.send(embed=embed)  # EMBED IN CHANNEL SENDEN

# PROGRAMMIERSPRACHE AUSWÄHLEN
HTML_ROLE_ID = 1276627495176900658  # HTML ROLLEN ID
JS_ROLE_ID = 1276627619885879438   # JavaScript ROLLEN ID
PYTHON_ROLE_ID = 1276627700429361254  # Python ROLLEN ID

@bot.command()
async def test(ctx):
    await ctx.send('Der Test hat funktioniert!')

#SUPPORT SYSTEM
class SupportActionsView(discord.ui.View): #LÖSCHEN BUTON
    def __init__(self, timeout=60):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="Alle Nachrichten löschen", style=discord.ButtonStyle.danger)
    async def delete_all_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.manage_messages:
            channel = interaction.channel
            await channel.purge()
            await interaction.response.send_message("Alle Nachrichten wurden gelöscht.", ephemeral=True)
        else:
            await interaction.response.send_message("Du hast nicht die Berechtigung, Nachrichten zu löschen.", ephemeral=True)

@bot.event
async def on_message(message):
    # Überprüfe, ob die Nachricht eine DM ist und nicht vom Bot stammt
    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        # Channel-ID, in den die DMs weitergeleitet werden sollen
        dm_forward_channel = bot.get_channel(1276932768990756864)

        if dm_forward_channel:
            # Erstelle ein Embed für die Weiterleitung
            embed_forward = discord.Embed(
                title="📩 Neue Direktnachricht",
                description=message.content,
                color=discord.Color.blue()
            )
            embed_forward.set_author(name=f"{message.author} ({message.author.id})", icon_url=message.author.avatar.url)

            # Sende das Embed an den gewünschten Channel
            forwarded_message = await dm_forward_channel.send(embed=embed_forward)

            # Füge eine Erwähnung deiner Rolle hinzu
            guild = bot.get_guild(1276604005287723070)  # Ersetze dies mit deiner Server-ID
            role = guild.get_role(my_role_id)

            # Füge den Button zum Löschen aller Nachrichten hinzu
            view = SupportActionsView()
            await dm_forward_channel.send(f"Bitte schaut euch diese Nachricht an, {role.mention}.")
            await dm_forward_channel.send(view=view)

        # Erstelle ein Bestätigungs-Embed, das an den Benutzer zurückgeschickt wird
        embed_response = discord.Embed(
            title="✅ Nachricht erhalten!",
            description=(
                "Deine Nachricht wurde erfolgreich an unser Team weitergeleitet. "
                "Wir werden uns so schnell wie möglich bei dir melden."
            ),
            color=discord.Color.green()
        )
        embed_response.set_footer(text="Danke, dass du uns kontaktiert hast!")

        # Antwort an den Benutzer mit dem Embed
        await message.author.send(embed=embed_response)

    # Stelle sicher, dass andere Befehle und Nachrichten weiterhin funktionieren
    await bot.process_commands(message)

bot.run('TOKEN')
