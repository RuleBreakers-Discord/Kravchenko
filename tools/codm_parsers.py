# -*- coding: utf-8 -*-
import asyncio

async def weapon_parser(weapon, lang):
    import requests
    from bs4 import BeautifulSoup

    weapons_dict = {
        #primary weapons
        '157': ['agr556'], #SMG
        '9': ['ak-47', 'ак-47', 'ak47', 'ак47'], #Assault
        '11': ['ak117', 'ак117'], #Assault
        '174': ['asval', 'val', 'асвал', 'вал'], #Assault
        '14': ['asm10'], #Assault
        '20': ['арктика', 'арктика.50', 'арктика50', 'arctic.50', 'arctic', 'arctic50'], #Sniper
        '13': ['вк57', 'bk57'], # Assault
        '30': ['by15'], #Shotgun
        '4': ['chicom'], #SMG
        '130': ['chopper', 'колун'], #LMG
        '73': ['cordite', 'кордит'], #SMG
        '21': ['dlq33'], #Sniper
        '135': ['dr-h'], #Assault
        '148': ['echo', 'эхо'], #Shotgun
        '168': ['fr.556', 'fr556'], #Assault
        '151': ['fennec', 'фенек'], #SMG
        '7': ['gks'], #SMG
        '103': ['hbra3'], #Assault
        '3': ['hg40'], #SMG
        '28': ['hs0405'], #Shotgun
        '31': ['hs2126'], #Shotgun
        '16': ['hvk30'], #Assault
        '191': ['holger-26', 'holger26', 'холгер-26', 'холгер26'], #LMG
        '46': ['icr1', 'icr-1'], #Assault
        '17': ['kn44', 'kn-44'], #Assault
        '47': ['krm262'], #Shotgun
        '139': ['kilo', 'кило'], #Marksman
        '8': ['lk24'], #Assault
        '18': ['locus', 'локус'], #Sniper
        '15': ['m16'], #Assault
        '22': ['m21ebr', 'm21'], #Sniper
        '10': ['m4'], #Assault
        '27': ['m4lmg'], #LMG
        '190': ['mk2', 'мк2'], #Marksman
        '2': ['msmc'], #SMG
        '96': ['man-o-war', 'manowar', 'агрессор'], #Assault
        '152': ['na-45', 'na45'], #Sniper
        '19': ['outlaw', 'бандит'], #Sniper
        '5': ['pdw-57', 'pdw57'], #SMG
        '180': ['пп-19бизон', 'пп-19', 'бизон', 'pp-19bizon', 'pp-19', 'bizon'], #SMG
        '164': ['peacekeepermk2', 'mk2', 'peacekeeper', 'мк2миротворец', 'мк2', 'миротворец'], #Assault
        '6': ['pharo', 'фараон'], #SMG
        '126': ['qq9'], #SMG
        '163': ['qxr'], #SMG
        '24': ['rpd', 'рпд'], #LMG
        '1': ['рус-79у', 'rus-79u'], #SMG
        '123': ['razorback', 'секач'], #SMG
        '26': ['s36'], #LMG
        '171': ['sks'], #Marksman
        '175': ['sp-r208', 'spr208'], #Marksman
        '29': ['striker', 'страйкер'], #Shotgun
        '12': ['type25', 'тип25', 'тип-25'], #Assault
        '25': ['ul736'], #LMG
        '23': ['xpr-50', 'xpr50'], #Sniper
        #secondary weapons
        '156': ['.50gs', '50gs'], #Pistol
        '45': ['axe', 'топор'], #Axe - Melee
        '162': ['basemelee', 'базовоехолодноеоружие'], #Base Melee - Melee
        '100': ['baseballbat', 'bat', 'бейбольнаябита', 'бита'], #Baseball Bat - Melee
        '36': ['fhj-18', 'fhj18', 'fhj'], #Launcher
        '105': ['foldingknife'], #Base Melee - Melee / не знаю официальный перевод на русский
        '161': ['glowstick'], #Base Melee - Melee / не знаю официальный перевод на русский
        '97': ['hachi'], #Base Melee - Melee / не знаю официальный перевод на русский
        '99': ['iceaxe', 'ледоруб'], #Base Melee - Melee
        '33': ['j358'], #Pistol
        '98': ['kerambit', 'керамбит'], #Base Melee - Melee
        '155': ['katana', 'катана'], #Base Melee - Melee
        '34': ['knife', 'нож'], #Knife - Melee
        '32': ['mw11'], #Pistol
        '181': ['renetti', 'ренетти'], #Pistol
        '35': ['smrs'], #Launcher
        '179': ['shovel', 'лопата'], # Shovel - Melee
        '192': ['sickle', 'серп'] #Sickle - Melee
    }

    codm_gg_id = ''

    for weapon_id in weapons_dict:
        if weapon in weapons_dict[weapon_id]:
            codm_gg_id = weapon_id

    if codm_gg_id == '':
        return None

    page = requests.get('https://codm.gg/base-item/id=' + codm_gg_id + '/')
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'lxml')
    
    weapon_name = soup.find("p", "title is-3").contents[0]
    weapon_type = soup.find("p", "subtitle is-5").contents[0]
    weapon_desc = soup.find("p", "mb-5").contents[0]
    try:
        weapon_changes = soup.find("p", "content").contents[2]
    except AttributeError:
        weapon_changes = 'No'
    weapon_stats = soup.find_all("p", "progress-value has-text-black")
    weapon_damage = weapon_stats[0].get_text().replace('Damage: ', '')
    weapon_accuracy = weapon_stats[1].get_text().replace('Accuracy: ', '')
    weapon_range = weapon_stats[2].get_text().replace('Range: ', '')
    weapon_firerate = weapon_stats[3].get_text().replace('Fire Rate: ', '')
    weapon_mobility = weapon_stats[4].get_text().replace('Mobility: ', '')
    if weapon_type not in ['Base Melee', 'Baseball Bat', 'Axe']:
        weapon_control = weapon_stats[5].get_text().replace('Control: ', '')
    else:
        weapon_control = '70'
    weapon_icon = 'https://cdn.codm.gg/assets/weapons/base/weapon_' + str(codm_gg_id) +'.jpg'
    if weapon_changes != 'No':
        weapon_changes = weapon_changes[1:]
    if lang == 'ru':
        if weapon_type == 'Assault':
            weapon_type = 'Штурмовая винтовка'
        elif weapon_type == 'Sniper':
            weapon_type = 'Снайперская винтовка'
        elif weapon_type == 'LMG':
            weapon_type = 'Ручной пулемет'
        elif weapon_type == 'SMG':
            weapon_type = 'Пистолет-пулемет'
        elif weapon_type == 'Shotgun':
            weapon_type = 'Дробовик'
        elif weapon_type == 'Marksman':
            weapon_type = 'Винтовка'
        elif weapon_type == 'Pistol':
            weapon_type = 'Пистолет'
        elif weapon_type == 'Launcher':
            weapon_type = 'Гранатомет'
        elif weapon_type == 'Axe':
            weapon_type = 'Рукопашное: топор'
        elif weapon_type == 'Base Melee':
            weapon_type = 'Рукопашное: базовое холодное оружие'
        elif weapon_type == 'Baseball Bat':
            weapon_type = 'Рукопашное: бейсбольная бита'
        elif weapon_type == 'Knife':
            weapon_type = 'Нож'
        elif weapon_type == 'Shovel':
            weapon_type = 'Рукопашное: лопата'
        elif weapon_type == 'Sickle':
            weapon_type = 'Рукопашное: серп'

        if weapon_changes == 'No':
            weapon_changes = 'Нет'
        else: 
            weapon_changes = weapon_changes.replace('Weapon stats have changed in version', 
            'Характеристики оружия были изменены в версии')

    return (weapon_name, weapon_type, weapon_desc, weapon_changes.lower().strip(), weapon_damage, weapon_accuracy, 
    weapon_range, weapon_firerate, weapon_mobility, weapon_control, weapon_icon)

async def meta_parser():
    import requests
    from bs4 import BeautifulSoup

    page = requests.get('https://zilliongamer.com/call-of-duty-mobile/c/weapon-guide/call-of-duty-mobile-weapon-tier-list')
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'lxml')
    
    meta_table = soup.find('table').get_text('|')
    meta_table = meta_table.split('|')

    return meta_table
