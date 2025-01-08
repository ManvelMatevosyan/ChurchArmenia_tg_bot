import telebot
from telebot import types

def english (bot,message):
    if message.message:
        if message.data == 'english':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=4)

            Button1 = types.InlineKeyboardButton(
                "Aragacotn", callback_data='ansver_button1')
            Button2 = types.InlineKeyboardButton(
                "Ararat", callback_data='ansver_button2')
            Button3 = types.InlineKeyboardButton(
                "Armavir", callback_data='ansver_button3')
            Button4 = types.InlineKeyboardButton(
                "Gexarqunik", callback_data='ansver_button4')
            Button5 = types.InlineKeyboardButton(
                "Kotayq", callback_data='ansver_button5')
            Button6 = types.InlineKeyboardButton(
                "Lori", callback_data='ansver_button6')
            Button7 = types.InlineKeyboardButton(
                "Shirak", callback_data='ansver_button7')
            Button8 = types.InlineKeyboardButton(
                "Syuniq", callback_data='ansver_button8')
            Button9 = types.InlineKeyboardButton(
                "Tavush", callback_data='ansver_button9')
            Button10 = types.InlineKeyboardButton(
                "Vayoc cor", callback_data='ansver_button10')
            Button11 = types.InlineKeyboardButton(
                "Erevan", callback_data='ansver_button11')

            keyboard.add(Button1, Button2, Button3, Button4, Button5, Button6,
                       Button7, Button8, Button9, Button10, Button11)

            bot.send_message(
                message.message.chat.id, "Mark the region where you want to visit📍", reply_markup=keyboard)

        elif message.data == "ansver_button1":
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            saxmosavank = types.InlineKeyboardButton(
                "Saxmosavank", url="https://maps.app.goo.gl/Z91XELPvmNPHnpLp9")
            hovhanavank = types.InlineKeyboardButton(
                "Hovhannavank", url="https://maps.app.goo.gl/5q8WLQaetGbQzqAU9")
            talin = types.InlineKeyboardButton(
                "Talin Tachar", url="https://maps.app.goo.gl/QPjGbKDn7cP2M7fw5")
            AstvacacinAragacotn = types.InlineKeyboardButton(
                "St.Astvacacin", url="https://maps.app.goo.gl/iTTm4Ri2x1T4nL5AA")
            hakob = types.InlineKeyboardButton(
                "St.Hakob", url="https://maps.app.goo.gl/dF8ZjSydtPwxZgwq5")
            gevorg = types.InlineKeyboardButton(
                "St.Gevorg", url="https://maps.app.goo.gl/Sz7uLvFR5Y7R6mPz6")
            muxni = types.InlineKeyboardButton("Muxni",url="https://maps.app.goo.gl/ZnEFVKVcTVeznkeYA")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(saxmosavank, hovhanavank, talin,
                         AstvacacinAragacotn, hakob, gevorg,muxni,back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 7 most famous churches and monastic complexes of Aragatsotn region.📍", reply_markup=keyboard)
        elif message.data == 'ansver_button2':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            xorvirap = types.InlineKeyboardButton(
                "Xor Virap", url="https://maps.app.goo.gl/k9w7VoSkG34s62pe7")
            HovhannesArarat = types.InlineKeyboardButton(
                "St.Hovhannes", url="https://maps.app.goo.gl/iQ6LdLwKfnJRge1g9")
            nshan = types.InlineKeyboardButton(
                "St.Nshan", url="https://maps.app.goo.gl/gWsuAvHo2orZNU5t9")
            AstvacacinArarat = types.InlineKeyboardButton(
                "St.Astvacacin", url="https://maps.app.goo.gl/YWAySdHMd3F1Q1qg8")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(HovhannesArarat, xorvirap,
                         nshan, AstvacacinArarat, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 4 most famous churches and monastic complexes of Ararat region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button3':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            AstvacacinArmavir = types.InlineKeyboardButton(
                "St.Aastvacacin", url="https://maps.app.goo.gl/Qb4T89H8BR12Sbrn7")
            HovhannesArmavir = types.InlineKeyboardButton(
                "St.Hovhannes", url="https://maps.app.goo.gl/ycgqJ7kSG3NYJD1t9")
            GevorgArmavir = types.InlineKeyboardButton(
                "St.Gevorg", url="https://maps.app.goo.gl/coWSG3vXKdiBCCLV9")
            MayrtacharArmavir = types.InlineKeyboardButton(
                "Mayr Tachar", url="https://maps.app.goo.gl/skfJziZjyq6yYQe38")
            MariamArmavir = types.InlineKeyboardButton(
                "St.Mariam", url="https://maps.app.goo.gl/qE7TgbsywQ99WgfN8")
            shoxakat = types.InlineKeyboardButton("St.Shoxakat",url="https://maps.app.goo.gl/KAi2GnHwW24R6AH8A")
            gayane = types.InlineKeyboardButton("St.Gayane",url="https://maps.app.goo.gl/aC7j7Cr35xLGqW8U7")
            hripsime = types.InlineKeyboardButton("St.Hripsime",url="https://maps.app.goo.gl/R4tBeMCPqUcfBCjt7")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(AstvacacinArmavir, HovhannesArmavir,
                         GevorgArmavir, MayrtacharArmavir, MariamArmavir,shoxakat,gayane,hripsime,back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 8 most famous churches and monastic complexes of Armavir region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button4':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            HakobGexarqunik = types.InlineKeyboardButton(
                "St.Hakob", url="https://maps.app.goo.gl/nSpGDqLk97t2CDNe8")
            sevanavank = types.InlineKeyboardButton(
                "Sevanavank", url="https://maps.app.goo.gl/vm4owci4TNByce6XA")
            AstvacacinGexarqunik = types.InlineKeyboardButton(
                "Astvacaciin", url="https://maps.app.goo.gl/ZF5PdZiCUDse4eNG6")
            AstvacacinGexarqunik2 = types.InlineKeyboardButton(
                "St.Astvacacin", url="https://maps.app.goo.gl/bmMGgrQiaksH4SrNA")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(HakobGexarqunik, sevanavank,
                         AstvacacinGexarqunik, AstvacacinGexarqunik2, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 4 most famous churches and monastic complexes of Gexarqunik region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button5':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            kecharis = types.InlineKeyboardButton(
                "Kecharis", url="https://maps.app.goo.gl/eJB8kEapnwztnrZBA")
            kaptavanq = types.InlineKeyboardButton(
                "Kaptavanq", url="https://maps.app.goo.gl/UTR5HdUHATESctjz6")
            ghuk = types.InlineKeyboardButton(
                "Ghuk", url="https://maps.app.goo.gl/nCTHUXCL7qV27UCD9")
            tezharuyk = types.InlineKeyboardButton(
                "Tezharuyk", url="https://maps.app.goo.gl/LaE6SaTKyripuNm18")
            dzakavanq = types.InlineKeyboardButton(
                "Dzakavanq", url="https://maps.app.goo.gl/xa2WpuGwcGhXsFB89")
            ptxnavanq = types.InlineKeyboardButton(
                "Ptxavanq", url="https://maps.app.goo.gl/eeWpX4BTqGLLbiLb9")
            kiraki = types.InlineKeyboardButton(
                "St.Kiraki", url="https://maps.app.goo.gl/Rr96NZ1MCQBU7FjN6")
            mayravanq = types.InlineKeyboardButton(
                "Mayravanq", url="https://maps.app.goo.gl/t6Q6Qf3qzhTCpxdk8")
            garni = types.InlineKeyboardButton(
                "Garni", url="https://maps.app.goo.gl/rqVthcnZHX1WZnb78")
            gexadri = types.InlineKeyboardButton("Gexadri",url="https://maps.app.goo.gl/78nMrBJeKngA9ivH7")
            juxtak = types.InlineKeyboardButton("Juxtak",url="https://maps.app.goo.gl/R1YtjcTCAj3DE1o1A")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(kecharis, kaptavanq, ghuk, tezharuyk,
                         dzakavanq, ptxnavanq, kiraki, mayravanq, garni,gexadri,juxtak,back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 11 most famous churches and monastic complexes of Kotayq region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button6':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            sanahin = types.InlineKeyboardButton(
                "Sanahin", url="https://maps.app.goo.gl/62sukQHRo8v4GD4z7")
            Haghpat = types.InlineKeyboardButton(
                "Haghpat", url="https://maps.app.goo.gl/7n78pafw79hp63QB9")
            odzun = types.InlineKeyboardButton(
                "Odzun", url="https://maps.app.goo.gl/Mni3niCqtHZ4eVuC7")
            horomayr = types.InlineKeyboardButton(
                "Horomayr", url="https://maps.app.goo.gl/axQHrAeQuG1eFBqH9")
            Ardvi = types.InlineKeyboardButton(
                "Ardvi", url="https://maps.app.goo.gl/L41tYvtNXd1RCqrk6")
            kobair = types.InlineKeyboardButton(
                "Kobair", url="https://maps.app.goo.gl/3Zm3xBJaAP1UiVJN7")
            alxata = types.InlineKeyboardButton(
                "Alxata", url="https://maps.app.goo.gl/Ez9ecs9bkyF8As1P7")
            hnevank = types.InlineKeyboardButton(
                "hnevank", url="https://maps.app.goo.gl/TNvby46pzQgoCpoF6")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(sanahin, Haghpat, odzun, horomayr,
                         Ardvi, kobair, alxata, hnevank, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 9 most famous churches and monastic complexes of Lori region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button7':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            GrigorLusavorich = types.InlineKeyboardButton(
                "St.Grigor Lusavorich", url="https://maps.app.goo.gl/jKpH3CFmiFUF4CBH9")
            StAmenaprkich = types.InlineKeyboardButton(
                "St,Amenaprkich", url="https://maps.app.goo.gl/eLavRpAH82JVF8cb8")
            yotverq = types.InlineKeyboardButton(
                "St.Astvacacin", url="https://maps.app.goo.gl/21n2Re1EMQ9ymNvR8")
            hakobShirak = types.InlineKeyboardButton(
                "St.Hakob", url="https://maps.app.goo.gl/rjLAVNMwsNEAGLWy5")
            sargisShirak = types.InlineKeyboardButton(
                "St.sargis", url="https://maps.app.goo.gl/c44AFm4jvFpf8Vxy9")
            marmarashen = types.InlineKeyboardButton(
                "Marmarashen", url="https://maps.app.goo.gl/ksVwQntMKcVjSwaC9")
            StAstvacacin = types.InlineKeyboardButton(
                "St.Astvacacin", url="https://maps.app.goo.gl/EU5TKLTxC9gaVd8d9")
            harichavanq = types.InlineKeyboardButton(
                "Harichavanq", url="https://maps.app.goo.gl/D4BufMeYB2MCpQsD6")
            lmbatavanq = types.InlineKeyboardButton(
                "Lmbatavanq", url="https://maps.app.goo.gl/shhi7ZKjFG9uRN3x8")
            GevorgShirak = types.InlineKeyboardButton(
                "St.gevorg", url="https://maps.app.goo.gl/JgLGwrBgLHR4BdrU7")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(GrigorLusavorich, StAmenaprkich, yotverq, hakobShirak, sargisShirak,
                         marmarashen, StAstvacacin, harichavanq, lmbatavanq, GevorgShirak, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 10 most famous churches and monastic complexes of Shirak region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button8':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            bex = types.InlineKeyboardButton(
                "Bekh desert", url="https://maps.app.goo.gl/gaXysH4wEpghsjox8")
            zvaravank = types.InlineKeyboardButton(
                "Zvaravank", url="https://maps.app.goo.gl/6STrsPfZgX6z8CeD7")
            ripsime = types.InlineKeyboardButton(
                "St.Ripsime", url="https://maps.app.goo.gl/uohPRdfzPZRAX6G38")
            vorotnavanq = types.InlineKeyboardButton(
                "Vorotnavanq", url="https://maps.app.goo.gl/gZBSFdf6RBrP44fV8")
            alan = types.InlineKeyboardButton(
                "King Alan's", url="https://maps.app.goo.gl/hUXWYgun2vPLdL8g7")
            noravanq = types.InlineKeyboardButton(
                "Bxeno-Noravanq", url="https://maps.app.goo.gl/hbnoSWB8WEZacs5S9")
            GrigorLusavorichSyuniq = types.InlineKeyboardButton(
                "St.Grigor Lusavorich", url="https://maps.app.goo.gl/3YH9zJwgRC2wqu2T9")
            tatev = types.InlineKeyboardButton("Tatev monastery",url="https://maps.app.goo.gl/Y6Pwtiw39udy2sJ46")
            
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(bex, zvaravank, ripsime,
                         vorotnavanq, alan, noravanq, GrigorLusavorichSyuniq,tatev, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 8 most famous churches and monastic complexes of Syuniq region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button9':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            haxarcin = types.InlineKeyboardButton(
                "Haxarcin", url="https://maps.app.goo.gl/aEWCoQaRPrMBnG4t6")
            goshavanq = types.InlineKeyboardButton(
                "Goshavanq", url="https://maps.app.goo.gl/tmKByea91UaSPLHKA")
            mroDzor = types.InlineKeyboardButton(
                "MroDzor", url="https://maps.app.goo.gl/HygyvNe97kLQWDm97")
            xoranashat = types.InlineKeyboardButton(
                "Xoranashat", url="https://maps.app.goo.gl/e7bq8ZRvnUf8P44L6")
            makaravanq = types.InlineKeyboardButton(
                "Makaravanq", url="https://maps.app.goo.gl/sKCMWkvWxQYQxvD76")
            varagavanq = types.InlineKeyboardButton(
                "Nor Varagavanq", url="https://maps.app.goo.gl/w5BxApweNvP6Zhdb8")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(haxarcin, goshavanq,
                         mroDzor, xoranashat, makaravanq, varagavanq, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 6 most famous churches and monastic complexes of Tavush region.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button10':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            noravanqVayocCor = types.InlineKeyboardButton(
                "Noravanq", url="https://maps.app.goo.gl/u2gXHwo25Bx6SKDC9")
            gndevanq = types.InlineKeyboardButton(
                "Gndevanq", url="https://maps.app.goo.gl/auT4W2RdofKmYDJ57")
            zorac = types.InlineKeyboardButton(
                "Zorac", url="https://maps.app.goo.gl/TC4AffgERWEyd5YH8")
            mamas = types.InlineKeyboardButton(
                "St.Mamas", url="https://maps.app.goo.gl/UpzpggW9tP7KvRTg6")
            shativanq = types.InlineKeyboardButton(
                "Shativanq", url="https://maps.app.goo.gl/rrJajvYhQyCHT9hn8")
            caxacQar = types.InlineKeyboardButton(
                "Caxac Qar", url="https://maps.app.goo.gl/4AohsLPQc2miSVucA")
            AstvacacinVayocCor = types.InlineKeyboardButton(
                "St.astvacacin", url="https://maps.app.goo.gl/nRPoZ3bm3Vgkd7Mv9")
            arates = types.InlineKeyboardButton(
                "Arates", url="https://maps.app.goo.gl/vYYKDQ1g8sVRM3rD8")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(noravanqVayocCor, gndevanq, zorac, mamas,
                         shativanq, caxacQar, AstvacacinVayocCor, arates, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 9 most famous churches and monastic complexes of Vayoc Cor region📍", reply_markup=keyboard)

        elif message.data == 'ansver_button11':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            sargis = types.InlineKeyboardButton(
                "St.Sargis", url="https://maps.app.goo.gl/Ho2g48ySi9Kqf1F89")
            grigor = types.InlineKeyboardButton(
                "St.Grigor Lusavorich", url="https://maps.app.goo.gl/coayno5VodpweJk39")
            mkrtich = types.InlineKeyboardButton(
                "St.Hovhannes Mkrtich", url="https://maps.app.goo.gl/G1XboAfRL7u9jXE56")
            anna = types.InlineKeyboardButton(
                "St.Katoxike & St.Anna", url="https://maps.app.goo.gl/6i3TxjKCv9n6Tp5D6")
            zoravar = types.InlineKeyboardButton(
                "St.Zoravar Astvacacin", url="https://maps.app.goo.gl/158woVuYMGZvmwvE9")
            mariam2 = types.InlineKeyboardButton(
                "St.Mariam Astvacacin", url="https://maps.app.goo.gl/QrKqDrQ5rFWse8EA6")
            sargis1 = types.InlineKeyboardButton(
                "St.sargis", url="https://maps.app.goo.gl/LXvEbw6U7hw6pBqw8")

            gevorg2 = types.InlineKeyboardButton(
                "St.Gevorg", url="https://maps.app.goo.gl/AquD5uqjgSfEi8CQ8")
            hakob2 = types.InlineKeyboardButton(
                "St.Hakob", url="https://maps.app.goo.gl/fa98pKFDvZ3pzTb87")
            xach2 = types.InlineKeyboardButton(
                "St.xach", url="https://maps.app.goo.gl/trgHTj2eDtyJPimx5")
            nahatakac = types.InlineKeyboardButton(
                "St.Nahatakac", url="https://maps.app.goo.gl/tirwzoDr5EG5Y86q7")
            astvacacin2 = types.InlineKeyboardButton(
                "St.Astvacacin", url="https://maps.app.goo.gl/aTYteohSRDjT4FYDA")
            errord = types.InlineKeyboardButton(
                "St.Errordutyun", url="https://maps.app.goo.gl/ctYV1xujUQT5C63r6")
            xach3 = types.InlineKeyboardButton(
                "St.Xach", url="https://maps.app.goo.gl/VbMifw6BuDKhvRcG7")
            back = types.InlineKeyboardButton("⬅️Back", callback_data='back')

            keyboard.add(sargis, grigor, mkrtich, anna, zoravar, mariam2, sargis1,
                         gevorg2, hakob2, xach2, nahatakac, astvacacin2, errord, xach3, back)

            bot.send_message(
                message.message.chat.id, "We suggest visiting the 15 most famous churches and monastic complexes of Erevan.📍", reply_markup=keyboard)

        elif message.data == 'back':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            Button1 = types.InlineKeyboardButton(
                "Aragacotn", callback_data='ansver_button1')
            Button2 = types.InlineKeyboardButton(
                "Ararat", callback_data='ansver_button2')
            Button3 = types.InlineKeyboardButton(
                "Armavir", callback_data='ansver_button3')
            Button4 = types.InlineKeyboardButton(
                "Gexarqunik", callback_data='ansver_button4')
            Button5 = types.InlineKeyboardButton(
                "Kotayq", callback_data='ansver_button5')
            Button6 = types.InlineKeyboardButton(
                "Lori", callback_data='ansver_button6')
            Button7 = types.InlineKeyboardButton(
                "Shirak", callback_data='ansver_button7')
            Button8 = types.InlineKeyboardButton(
                "Syuniq", callback_data='ansver_button8')
            Button9 = types.InlineKeyboardButton(
                "Tavush", callback_data='ansver_button9')
            Button10 = types.InlineKeyboardButton(
                "Vayoc cor", callback_data='ansver_button10')
            Button11 = types.InlineKeyboardButton(
                "Erevan", callback_data='ansver_button11')

            keyboard.add(Button1, Button2, Button3, Button4, Button5,
                         Button6, Button7, Button8, Button9, Button10, Button11)

            bot.send_message(
                message.message.chat.id, "Mark the region where you want to visit📍", reply_markup=keyboard)
