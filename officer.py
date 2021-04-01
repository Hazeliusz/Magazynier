import json

json_file = "founds.json"


async def withdraw(ctx, amount):
    if not amount.isnumeric():
        await ctx.send("Ilość pieniążków musi być liczbą.")
        return
    with open(json_file) as foundsJson:
        data = json.load(foundsJson)
        if data["founds"] < int(amount):
            await ctx.send("Zasoby kompanii są niewystarczające.")
            return
        data["founds"] -= int(amount)
        with open(json_file, "w") as output:
            json.dump(data, output)
        await ctx.send('Wypłacono ' + amount + " golda.")


async def deposit(ctx, amount):
    if not amount.isnumeric():
        await ctx.send("Ilość pieniążków musi być liczbą.")
        return
    with open(json_file) as foundsJson:
        data = json.load(foundsJson)
        data["founds"] += int(amount)
        with open(json_file, "w") as output:
            json.dump(data, output)
        await ctx.send('Wpłacono ' + amount + " golda.")
