import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), help_command=None)
TOKEN = "MTI1OTg2OTI1MDY1OTU0OTI5Nw.GP6Y7y.YL_8PWLeQQVSM8MZ9zae0SeFyfK_m9m6uiu7mY"

@bot.event
async def on_ready():
    print(f"{bot.user.name} 로그인 성공!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))

@bot.command(name="도움말", help="Show all commands", aliases=["Help"])
async def help(ctx):
    await ctx.channel.send("<명령어 목록>")
    await ctx.channel.send("모든 명령어는 앞에 $를 붙입니다!")
    await ctx.channel.send("Help, 도움말 : 도움말을 출력해줍니다.")

bot.run(TOKEN)