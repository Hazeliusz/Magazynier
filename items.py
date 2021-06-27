import json
from random import randint


async def random_magic_item(ctx, rarity, desc):
    if rarity == "common":
        f = open("meta/items/common.json", 'r')
        items = json.load(f)
        number = randint(0, len(items) - 1)
        await ctx.send("Wylosowałeś " + items[number]["name"] + "!\n" + "Powszechny przedmiot typu " + items[number]["type"] +"\n" + ("Wymaga zestrojenia." if items[number]["attuned"] else "Nie wymaga zestrojenia"))
        if desc:
            f = open("meta/items/common_desc.json", 'r')
            descs = json.load(f)
            await ctx.send(descs[number])
    elif rarity == "uncommon":    
        f = open("meta/items/uncommon.json", 'r')
        items = json.load(f)
        number = randint(0, len(items) - 1)
        await ctx.send("Wylosowałeś " + items[number]["name"] + "!\n" + "Niespotykany przedmiot typu " + items[number]["type"] +"\n" + ("Wymaga zestrojenia." if items[number]["attuned"] else "Nie wymaga zestrojenia"))
        if desc:
            f = open("meta/items/uncommon_desc.json", 'r')
            descs = json.load(f)
            await ctx.send(descs[number])
    elif rarity == "rare":    
        f = open("meta/items/rare.json", 'r')
        items = json.load(f)
        number = randint(0, len(items) - 1)
        await ctx.send("Wylosowałeś " + items[number]["name"] + "!\n" + "Rzadki przedmiot typu " + items[number]["type"] +"\n" + ("Wymaga zestrojenia." if items[number]["attuned"] else "Nie wymaga zestrojenia"))
        if desc:
            f = open("meta/items/rare_desc.json", 'r')
            descs = json.load(f)
            await ctx.send(descs[number])
    elif rarity == "vrare":    
        f = open("meta/items/vrare.json", 'r')
        items = json.load(f)
        number = randint(0, len(items) - 1)
        await ctx.send("Wylosowałeś " + items[number]["name"] + "!\n" + "Bardzo rzadki przedmiot typu " + items[number]["type"] +"\n" + ("Wymaga zestrojenia." if items[number]["attuned"] else "Nie wymaga zestrojenia"))
        if desc:
            f = open("meta/items/vrare_desc.json", 'r')
            descs = json.load(f)
            await ctx.send(descs[number])
    elif rarity == "legendary":    
        f = open("meta/items/legendary.json", 'r')
        items = json.load(f)
        number = randint(0, len(items) - 1)
        await ctx.send("Wylosowałeś " + items[number]["name"] + "!\n" + "Legendarny przedmiot typu " + items[number]["type"] +"\n" + ("Wymaga zestrojenia." if items[number]["attuned"] else "Nie wymaga zestrojenia"))
        if desc:
            f = open("meta/items/legendary_desc.json", 'r')
            descs = json.load(f)
            await ctx.send(descs[number])
    elif rarity == "artifact":    
        f = open("meta/items/artifacts.json", 'r')
        items = json.load(f)
        number = randint(0, len(items) - 1)
        await ctx.send("Wylosowałeś " + items[number]["name"] + "!\n" + "Artefakt typu " + items[number]["type"] +"\n" + ("Wymaga zestrojenia." if items[number]["attuned"] else "Nie wymaga zestrojenia"))
        if desc:
            f = open("meta/items/legendary_desc.json", 'r')
            descs = json.load(f)
            await ctx.send(descs[number])
    else:
        await ctx.send("Nieprawdiłowy typ przedmiotu.")