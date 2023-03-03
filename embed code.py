@bot.slash_command(name= "(command name here)", description= "(command description here)")
async def command_name(ctx):
    embed = discord.Embed(title= "hello world!!", description= "hiii!!")
    await ctx.respond(embed=embed)