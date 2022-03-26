# -*- coding: utf-8 -*-
import os
import asyncio
import discord
from discord.ext import commands
import tools.codm_parsers

LANG = 'en' #ru - for russian, en - for english, use that for global language settings
lang_list = ['ru', 'ру', 'en', 'eng', 'fr', 'fren'] #список для проверки языка / list for language checks
PREFIX = '*' # задаем префикс / set prefix

TOKEN = os.getenv("DISCORD_TOKEN") #строка для запуска на Heroku / string for Heroku launch
#TOKEN = "OTU2NTcyODM3OTQwOTgxNzkw.YjyL4A.nxiySd-Vg4spSB7thz1fF2hq-Jw" #строка для запуска где-то, кроме Heroku / string for launch not on the Heroku

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents) #задаем префикс бота и разрешения для работы / setting PREFIX and intents
version = 'v0.1'
bot.remove_command("help") #удаляем дефолтный help от библиотеки discord.py / remove default help from discord.py

@bot.event #запуск бота / bot launching
async def on_ready():
    if LANG == 'ru':
        print('Вошёл как')
    elif LANG == 'en':
        print('Login as')
    elif LANG == 'fr':
        print('Se connecter en tant que')
    print(bot.user.name)
    print(bot.user.id)
    print(version)
    print('------')
    await bot.change_presence(activity=discord.Game(name=PREFIX + "help"))

@bot.command(pass_context=True, aliases=["Info", "инфо", "Инфо"])
async def info(ctx, weapon: str = None):

    if weapon is None:
        if LANG == 'ru':
            await ctx.send(embed = discord.Embed(description = "Введите название оружия!", color = 0x00ff00))
            return
        elif LANG == 'en':
            await ctx.send(embed = discord.Embed(description = "Enter the weapon name!", color = 0x00ff00))
            return
            elif LANG == 'fr':
            await ctx.send(embed = discord.Embed(description = "Entrez le nom de l'arme !", color = 0x00ff00))
            return
  
    result = await tools.codm_parsers.weapon_parser(weapon.lower(), LANG)

    if result is None:
        if LANG == 'ru':
            await ctx.send(embed = discord.Embed(description = "Не получилось найти оружие! Попробуйте убрать пробел или кавычки в названии оружия.", color = 0x00ff00))
            return
        elif LANG == 'en':
            await ctx.send(embed = discord.Embed(description = "I can't found weapon! Remove spaces and quotes in weapon name.", color = 0x00ff00))
            return
        elif LANG == 'fr':
            await ctx.send(embed = discord.Embed(description = "je ne trouve pas d'arme ! Supprimez les espaces et les guillemets dans le nom de l'arme.", color = 0x00ff00))
            return

    if LANG == 'ru':
        embed = discord.Embed(title = "Информация о " + result[0], color = 0x00ff00)
        embed.set_image(url=result[10])
        embed.add_field(name="Тип:", value=result[1], inline=False)
        embed.add_field(name="Описание:", value=result[2], inline=False)
        embed.add_field(name="Характеристики:", value=f'Урон: {str(result[4])}\nТочность: {str(result[5])}\nДистанция: {str(result[6])}\nТемп стрельбы: {str(result[7])}\nПодвижность: {str(result[8])}\nКонтроль: {str(result[9])}', inline=False)
        embed.set_footer(text=f'Изменения: {result[3]}')
        await ctx.send(embed=embed)
        print('Обработал info о', weapon, 'для пользователя', ctx.author.name)
    elif LANG == 'en':
        embed = discord.Embed(title = "Information about " + result[0], color = 0x00ff00)
        embed.set_image(url=result[10])
        embed.add_field(name="Type:", value=result[1], inline=False)
        embed.add_field(name="Description:", value=result[2], inline=False)
        embed.add_field(name="Stats:", value=f'Damage: {str(result[4])}\nAccuracy: {str(result[5])}\nRange: {str(result[6])}\nFire Rate: {str(result[7])}\nMobility: {str(result[8])}\nControl: {str(result[9])}', inline=False)
        embed.set_footer(text=f'Changes: {result[3]}')
        await ctx.send(embed=embed)
        print('Give info for', weapon, 'for user', ctx.author.name)
    elif LANG == 'fr':
        embed = discord.Embed(title = "Des informations sur " + result[0], color = 0x00ff00)
        embed.set_image(url=result[10])
        embed.add_field(name="Type:", value=result[1], inline=False)
        embed.add_field(name="Description:", value=result[2], inline=False)
        embed.add_field(name="Stats:", value=f'Dégats: {str(result[4])}\nPrécision: {str(result[5])}\nPortée: {str(result[6])}\nCadence de tir: {str(result[7])}\nMobilité: {str(result[8])}\nContrôle: {str(result[9])}', inline=False)
        embed.set_footer(text=f'Changements: {result[3]}')
        await ctx.send(embed=embed)
        print('Donner des infos pour', weapon, 'pour l'utilisateur', ctx.author.name)

@bot.command(pass_context=True, aliases=["Compare", "сравни", "Сравни"])
async def compare(ctx, weapon1: str = None, weapon2: str = None):

    if weapon1 is None or weapon2 is None:
        if LANG == 'ru':
            await ctx.send(embed = discord.Embed(description = "Введите название оружия!", color = 0x00ff00))
            return
        elif LANG == 'en':
            await ctx.send(embed = discord.Embed(description = "Enter the weapon name!", color = 0x00ff00))
            return
            
         elif LANG == 'fr':
            await ctx.send(embed = discord.Embed(description = "Entrez le nom de l'arme !", color = 0x00ff00))
            return
  
    result1 = await tools.codm_parsers.weapon_parser(weapon1.lower(), LANG)
    result2 = await tools.codm_parsers.weapon_parser(weapon2.lower(), LANG)

    if result1 is None or result2 is None:
        if LANG == 'ru':
            await ctx.send(embed = discord.Embed(description = "Не получилось найти оружие! Попробуйте убрать пробел или кавычки в названии оружия.", color = 0x00ff00))
            return
        elif LANG == 'en':
            await ctx.send(embed = discord.Embed(description = "I can't found weapon! Remove spaces and quotes in weapon name.", color = 0x00ff00))
            return
        elif LANG == 'fr:
            await ctx.send(embed = discord.Embed(description = "Je ne trouve pas d'arme ! Supprimez les espaces et les guillemets dans le nom de l'arme.", color = 0x00ff00))
            return

    if LANG == 'ru':
        embed = discord.Embed(title = f"Сравнение {result1[0]} и {result2[0]}", color = 0x00ff00)
        embed.set_image(url=result1[10])
        embed.set_thumbnail(url=result2[10])
        embed.add_field(name="Тип:", value=f"{result1[1]} / {result2[1]}", inline=False)
        embed.add_field(name="Описание:", value=f"{result1[2]} / {result2[2]}", inline=False)
        embed.add_field(name="Характеристики:", value=f'Урон: {str(result1[4])} / {str(result2[4])}\nТочность: {str(result1[5])} / {str(result2[5])}\nДистанция: {str(result1[6])} / {str(result2[6])}\nТемп стрельбы: {str(result1[7])} / {str(result2[7])}\nПодвижность: {str(result1[8])} / {str(result2[8])}\nКонтроль: {str(result1[9])} / {str(result2[9])}', inline=False)
        embed.set_footer(text=f'Изменения: {result1[3]} / {result2[3]}')
        await ctx.send(embed=embed)
        print('Обработал сравнение о', weapon1, 'и', weapon2, 'для пользователя', ctx.author.name)
    elif LANG == 'en':
        embed = discord.Embed(title = f"Compare {result1[0]} and {result2[0]}", color = 0x00ff00)
        embed.set_image(url=result1[10])
        embed.set_thumbnail(url=result2[10])
        embed.add_field(name="Type:", value=f"{result1[1]} / {result2[1]}", inline=False)
        embed.add_field(name="Description:", value=f"{result1[2]} / {result2[2]}", inline=False)
        embed.add_field(name="Stats:", value=f'Damage: {str(result1[4])} / {str(result2[4])}\nAccuracy: {str(result1[5])} / {str(result2[5])}\nRange: {str(result1[6])} / {str(result2[6])}\nFire Rate: {str(result1[7])} / {str(result2[7])}\nMobility: {str(result1[8])} / {str(result2[8])}\nControl: {str(result1[9])} / {str(result2[9])}', inline=False)
        embed.set_footer(text=f'Changes: {result1[3]} / {result2[3]}')
        await ctx.send(embed=embed)
        print('Give compare for', weapon1, 'and', weapon2, 'for user', ctx.author.name)

@bot.command(aliases=["мета", "Meta", "Мета"])
async def meta(ctx):
  
    result = await tools.codm_parsers.meta_parser()

    if LANG == 'ru':
        embed = discord.Embed(title = 'Мета-отчёт', color = 0x00ff00)
        embed.add_field(name=f"Тир {result[2]}:", value=result[3], inline=False)
        embed.add_field(name=f"Тир {result[4]}:", value=result[5], inline=False)
        embed.add_field(name=f"Тир {result[6]}:", value=result[7], inline=False)
        embed.add_field(name=f"Тир {result[8]}:", value=result[9], inline=False)
        await ctx.send(embed=embed)
        print('Обработал meta для пользователя', ctx.author.name)
    elif LANG == 'en':
        embed = discord.Embed(title = 'Meta-report:', color = 0x00ff00)
        embed.add_field(name=f"Tier {result[2]}:", value=result[3], inline=False)
        embed.add_field(name=f"Tier {result[4]}:", value=result[5], inline=False)
        embed.add_field(name=f"Tier {result[6]}:", value=result[7], inline=False)
        embed.add_field(name=f"Tier {result[8]}:", value=result[9], inline=False)
        await ctx.send(embed=embed)
        print('Give meta for user', ctx.author.name)

@bot.command(aliases=["Help", "помощь", "Помощь"])
async def help(ctx):
    if LANG == 'ru':
        embed = discord.Embed(title = 'Помощь', color = 0x00ff00)
        embed.add_field(name=f"{PREFIX}инфо", value=f'Алиасы:\n{PREFIX}инфо название-оружия, {PREFIX}Info название-оружия, {PREFIX}Инфо название-оружия\nПолучить информацию о оружии.\nНазвание оружия нужно вводить без пробелов (с тире можно) и без кавычек.\nПример: {PREFIX}инфо асвал', inline=False)
        embed.add_field(name=f"{PREFIX}сравни", value=f'Алиасы:\n{PREFIX}Compare название-первого-оружия название-второго-оружия, {PREFIX}Сравни название-первого-оружия название-второго-оружия\nПолучить информацию о двух оружиях.\nНазвание оружия нужно вводить без пробелов (с тире можно) и без кавычек.\nПример: {PREFIX}сравни асвал топор', inline=False)
        embed.add_field(name=f"{PREFIX}мета", value=f'Алиасы:\n{PREFIX}Meta, {PREFIX}Мета, {PREFIX}meta\nПолучить мета-отчет.', inline=False)
        embed.add_field(name='Исходный код:', value='https://github.com/Sux0Phone/Kravchenko', inline=False)
        embed.set_footer(text=f"Автор бота SuxOPhone\nВерсия бота: {version}")
        await ctx.send(embed=embed)
        print('Обработал help для пользователя', ctx.author.name)
    elif LANG == 'en':
        embed = discord.Embed(title = 'Help:', color = 0x00ff00)
        embed.add_field(name=f"{PREFIX}info", value=f'Aliases:\n{PREFIX}инфо weapon-name, {PREFIX}Info weapon-name, {PREFIX}Инфо weapon-name\nGet information about weapon.\nPlease, input weapon name without spaces (you can use dashes) and without quotes.\nExample: {PREFIX}info asval', inline=False)
        embed.add_field(name=f"{PREFIX}compare", value=f'Aliases:\n{PREFIX}Compare first-weapon-name second-weapon-name, {PREFIX}сравни first-weapon-name second-weapon-name, {PREFIX}Сравни first-weapon-name second-weapon-name\nGet information about weapons.\nPlease, input weapon name without spaces (you can use dashes) and without quotes.\nExample: {PREFIX}compare asval axe', inline=False)
        embed.add_field(name=f"{PREFIX}meta", value=f'Aliases:\n{PREFIX}Meta, {PREFIX}мета, {PREFIX}Мета\nGet meta-report.', inline=False)
        embed.add_field(name='Source code:', value='https://github.com/Sux0Phone/Kravchenko', inline=False)
        embed.set_footer(text=f"Bot author: SuxOPhone\nBot version:{version}")
        await ctx.send(embed=embed)
        print('Give help for user', ctx.author.name)

bot.run(TOKEN)
