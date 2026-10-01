import discord
from discord.ext import commands
import os
from datetime import timedelta

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)
TOKEN=os.getenv("DISCORD_TOKEN")
GUILD_ID=1542563753315409970
GUILD=discord.Object(id=GUILD_ID)
@bot.event
async def on_ready():
    commands=await bot.tree.sync(guild=GUILD)
    print("ядерная ракета запущена")
    print("зарегистририваны команды:")
    for command in commands:
        print(command.name)


@bot.command()
async def привет(ctx):
    await ctx.send("пока")

@bot.command()
async def как_дела(ctx):
    await ctx.send("все харафо")


@bot.command()
async def ты_плохой_бот(ctx):
    await ctx.send("сам плохой")

@bot.tree.command(name = "help",description="показать помощь",guild=GUILD)
async def help(interaction:discord.Interaction):
    await interaction.response.send_message("пока обойдёшся")

@bot.tree.command(name = "delite",description="показать уууууууудолить",guild=GUILD)
@commands.has_permissions(manage_messages=True)
async def delite(interaction:discord.Interaction,amount:int):
    channel = interaction.channel
    await interaction.response.send_message(f"удоляю {amount} сообщений ПОНЯТНО??",ephemeral=True)
    await channel.purge(limit=amount)

@bot.tree.command(name = "bad",description="показать оскорбление(ТЫ ПЛОХОЙ)",guild=GUILD)
async def bad(interaction:discord.Interaction):
    await interaction.response.send_message("ТЫ САМ НАПРОСИЛСЯ (включается эпичная музыка из андертейла и жосткий файт с сансом вы побиждаете)")

@bot.tree.command(name = "say",description="повторить текст",guild=GUILD)
async def say(interaction:discord.Interaction,text:str):
    await interaction.response.send_message(text)

@bot.tree.command(name="mute", description="выдать мут", guild=GUILD)
async def mute(
        interaction: discord.Interaction,member: discord.Member,minutes:int):
    try:
    await member.timeout(timedelta(minutes=minutes),reason="админ")
    await interaction.response.send_message( f"{member.mention}получил тайм-аут на {minutes} минута.")
    except discord.errors.Forbidden:
    await interaction.response.send_message(f"Недостаточно прав{member.mention}")


bot.run(TOKEN)



