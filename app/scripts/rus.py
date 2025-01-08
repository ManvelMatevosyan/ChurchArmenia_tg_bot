import telebot
from telebot import types

def russian(bot,message):
    if message.message:
        if message.data =='russian':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=4)

            Button1 = types.InlineKeyboardButton(
                "Арагацотн", callback_data='ansver_button1')
            Button2 = types.InlineKeyboardButton(
                "Арарат", callback_data='ansver_button2')
            Button3 = types.InlineKeyboardButton(
                "Армавир", callback_data='ansver_button3')
            Button4 = types.InlineKeyboardButton(
                "Гехаркуник", callback_data='ansver_button4')
            Button5 = types.InlineKeyboardButton(
                "Котайк", callback_data='ansver_button5')
            Button6 = types.InlineKeyboardButton(
                "Лори", callback_data='ansver_button6')
            Button7 = types.InlineKeyboardButton(
                "Ширак", callback_data='ansver_button7')
            Button8 = types.InlineKeyboardButton(
                "Сюник", callback_data='ansver_button8')
            Button9 = types.InlineKeyboardButton(
                "Тавуш", callback_data='ansver_button9')
            Button10 = types.InlineKeyboardButton(
                "Вайоц Дзор", callback_data='ansver_button10')
            Button11 = types.InlineKeyboardButton(
                "Ереван", callback_data='ansver_button11')
        
            keyboard.add(Button1, Button2, Button3, Button4, Button5, Button6,
               Button7, Button8, Button9, Button10, Button11)
            
            bot.send_message(
                message.message.chat.id, "Отметьте регион, который вы хотите посетить📍", reply_markup=keyboard)
            
        elif message.data == "ansver_button1":
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            saxmosavank = types.InlineKeyboardButton(
                "Сахмосаванк", url="https://maps.app.goo.gl/Z91XELPvmNPHnpLp9")
            hovhanavank = types.InlineKeyboardButton(
                "Ованнаванк", url="https://maps.app.goo.gl/5q8WLQaetGbQzqAU9")
            talin = types.InlineKeyboardButton(
                "Таллиннский собор", url="https://maps.app.goo.gl/QPjGbKDn7cP2M7fw5")
            AstvacacinAragacotn = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/iTTm4Ri2x1T4nL5AA")
            hakob = types.InlineKeyboardButton(
                "Св.Акоб", url="https://maps.app.goo.gl/dF8ZjSydtPwxZgwq5")
            gevorg = types.InlineKeyboardButton(
                "Св.Геворг", url="https://maps.app.goo.gl/Sz7uLvFR5Y7R6mPz6")
            muxni = types.InlineKeyboardButton("Мугни",url="https://maps.app.goo.gl/ZnEFVKVcTVeznkeYA")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(saxmosavank, hovhanavank, talin,
                         AstvacacinAragacotn, hakob, gevorg,muxni,back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 7 самых известных церквей и монастырских комплексов Арагацотнского региона.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button2':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            xorvirap = types.InlineKeyboardButton(
                "Хор Вирап", url="https://maps.app.goo.gl/k9w7VoSkG34s62pe7")
            HovhannesArarat = types.InlineKeyboardButton(
                "Св.Оганнес", url="https://maps.app.goo.gl/iQ6LdLwKfnJRge1g9")
            nshan = types.InlineKeyboardButton(
                "Св.Знак", url="https://maps.app.goo.gl/gWsuAvHo2orZNU5t9")
            AstvacacinArarat = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/YWAySdHMd3F1Q1qg8")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(HovhannesArarat, xorvirap,
                         nshan, AstvacacinArarat, back)
            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 4 самых известных церкви и монастырских комплекса Араратского региона.📍", reply_markup=keyboard)

        elif message.data == 'ansver_button3':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            AstvacacinArmavir = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/Qb4T89H8BR12Sbrn7")
            HovhannesArmavir = types.InlineKeyboardButton(
                "Св.Оганнес", url="https://maps.app.goo.gl/ycgqJ7kSG3NYJD1t9")
            GevorgArmavir = types.InlineKeyboardButton(
                "Св.Геворг", url="https://maps.app.goo.gl/coWSG3vXKdiBCCLV9")
            MayrtacharArmavir = types.InlineKeyboardButton(
                "Мать-Церковь", url="https://maps.app.goo.gl/skfJziZjyq6yYQe38")
            MariamArmavir = types.InlineKeyboardButton(
                "Св.Мариям", url="https://maps.app.goo.gl/qE7TgbsywQ99WgfN8")
            shoxakat = types.InlineKeyboardButton("Св.Шохакат",url="https://maps.app.goo.gl/KAi2GnHwW24R6AH8A")
            gayane = types.InlineKeyboardButton("Св.Гаяане",url="https://maps.app.goo.gl/aC7j7Cr35xLGqW8U7")
            hripsime = types.InlineKeyboardButton("Св.Рипсиме",url="https://maps.app.goo.gl/R4tBeMCPqUcfBCjt7")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(AstvacacinArmavir, HovhannesArmavir,
                         GevorgArmavir, MayrtacharArmavir, MariamArmavir,shoxakat,gayane,hripsime,back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 8 самых известных церквей и монастырских комплексов Армавирской области.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button4':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            HakobGexarqunik = types.InlineKeyboardButton(
                "Св,Акоб", url="https://maps.app.goo.gl/nSpGDqLk97t2CDNe8")
            sevanavank = types.InlineKeyboardButton(
                "Севанаванк", url="https://maps.app.goo.gl/vm4owci4TNByce6XA")
            AstvacacinGexarqunik = types.InlineKeyboardButton(
                "Богородица", url="https://maps.app.goo.gl/ZF5PdZiCUDse4eNG6")
            AstvacacinGexarqunik2 = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/bmMGgrQiaksH4SrNA")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(HakobGexarqunik, sevanavank,
                         AstvacacinGexarqunik, AstvacacinGexarqunik2, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 4 самых известных церкви и монастырские комплексы региона Гехаркуник.📍", reply_markup=keyboard)
        elif message.data == 'ansver_button5':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            kecharis = types.InlineKeyboardButton(
                "Кечарис", url="https://maps.app.goo.gl/eJB8kEapnwztnrZBA")
            kaptavanq = types.InlineKeyboardButton(
                "Каптаванк", url="https://maps.app.goo.gl/UTR5HdUHATESctjz6")
            ghuk = types.InlineKeyboardButton(
                "Гхук", url="https://maps.app.goo.gl/nCTHUXCL7qV27UCD9")
            tezharuyk = types.InlineKeyboardButton(
                "Тезхаруйк", url="https://maps.app.goo.gl/LaE6SaTKyripuNm18")
            dzakavanq = types.InlineKeyboardButton(
                "Дзакаванк", url="https://maps.app.goo.gl/xa2WpuGwcGhXsFB89")
            ptxnavanq = types.InlineKeyboardButton(
                "Птхаванк", url="https://maps.app.goo.gl/eeWpX4BTqGLLbiLb9")
            kiraki = types.InlineKeyboardButton(
                "Св.Воскресенье", url="https://maps.app.goo.gl/Rr96NZ1MCQBU7FjN6")
            mayravanq = types.InlineKeyboardButton(
                "Майраванк", url="https://maps.app.goo.gl/t6Q6Qf3qzhTCpxdk8")
            garni = types.InlineKeyboardButton(
                "Гарни", url="https://maps.app.goo.gl/rqVthcnZHX1WZnb78")
            gexadri = types.InlineKeyboardButton("Гехадри",url="https://maps.app.goo.gl/78nMrBJeKngA9ivH7")
            juxtak = types.InlineKeyboardButton("Джухтак",url="https://maps.app.goo.gl/R1YtjcTCAj3DE1o1A")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(kecharis, kaptavanq, ghuk, tezharuyk,
                         dzakavanq, ptxnavanq, kiraki, mayravanq, garni,gexadri,juxtak,back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 11 самых известных церквей и монастырских комплексов Котайкского региона.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button6':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            sanahin = types.InlineKeyboardButton(
                "Шанаин", url="https://maps.app.goo.gl/62sukQHRo8v4GD4z7")
            Haghpat = types.InlineKeyboardButton(
                "Ахпат", url="https://maps.app.goo.gl/7n78pafw79hp63QB9")
            odzun = types.InlineKeyboardButton(
                "Одзун", url="https://maps.app.goo.gl/Mni3niCqtHZ4eVuC7")
            horomayr = types.InlineKeyboardButton(
                "Хорамайр", url="https://maps.app.goo.gl/axQHrAeQuG1eFBqH9")
            Ardvi = types.InlineKeyboardButton(
                "Арвди", url="https://maps.app.goo.gl/L41tYvtNXd1RCqrk6")
            kobair = types.InlineKeyboardButton(
                "Кобаир", url="https://maps.app.goo.gl/3Zm3xBJaAP1UiVJN7")
            alxata = types.InlineKeyboardButton(
                "Алхата", url="https://maps.app.goo.gl/Ez9ecs9bkyF8As1P7")
            hnevank = types.InlineKeyboardButton(
                "Хневанк", url="https://maps.app.goo.gl/TNvby46pzQgoCpoF6")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(sanahin, Haghpat, odzun, horomayr,
                         Ardvi, kobair, alxata, hnevank, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 9 самых известных церквей и монастырских комплексов Лорийского региона.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button7':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            GrigorLusavorich = types.InlineKeyboardButton(
                "Св.Григор Лусаворич", url="https://maps.app.goo.gl/jKpH3CFmiFUF4CBH9")
            StAmenaprkich = types.InlineKeyboardButton(
                "Св.Спаситель", url="https://maps.app.goo.gl/eLavRpAH82JVF8cb8")
            yotverq = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/21n2Re1EMQ9ymNvR8")
            hakobShirak = types.InlineKeyboardButton(
                "Св.Акоб", url="https://maps.app.goo.gl/rjLAVNMwsNEAGLWy5")
            sargisShirak = types.InlineKeyboardButton(
                "Св.Сарги", url="https://maps.app.goo.gl/c44AFm4jvFpf8Vxy9")
            marmarashen = types.InlineKeyboardButton(
                "Мармарашен", url="https://maps.app.goo.gl/ksVwQntMKcVjSwaC9")
            StAstvacacin = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/EU5TKLTxC9gaVd8d9")
            harichavanq = types.InlineKeyboardButton(
                "Аричаванк", url="https://maps.app.goo.gl/D4BufMeYB2MCpQsD6")
            lmbatavanq = types.InlineKeyboardButton(
                "Лмбатаванк", url="https://maps.app.goo.gl/shhi7ZKjFG9uRN3x8")
            GevorgShirak = types.InlineKeyboardButton(
                "Св.Геворг", url="https://maps.app.goo.gl/JgLGwrBgLHR4BdrU7")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(GrigorLusavorich, StAmenaprkich, yotverq, hakobShirak, sargisShirak,
                         marmarashen, StAstvacacin, harichavanq, lmbatavanq, GevorgShirak, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 10 самых известных церквей и монастырских комплексов Ширакской области.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button8':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            bex = types.InlineKeyboardButton(
                "Бак Десерт", url="https://maps.app.goo.gl/gaXysH4wEpghsjox8")
            zvaravank = types.InlineKeyboardButton(
                "Звараванк", url="https://maps.app.goo.gl/6STrsPfZgX6z8CeD7")
            ripsime = types.InlineKeyboardButton(
                "Св.Рипсиме", url="https://maps.app.goo.gl/uohPRdfzPZRAX6G38")
            vorotnavanq = types.InlineKeyboardButton(
                "Вортанаванк", url="https://maps.app.goo.gl/gZBSFdf6RBrP44fV8")
            alan = types.InlineKeyboardButton(
                "Алан король", url="https://maps.app.goo.gl/hUXWYgun2vPLdL8g7")
            noravanq = types.InlineKeyboardButton(
                "Нораванк", url="https://maps.app.goo.gl/hbnoSWB8WEZacs5S9")
            GrigorLusavorichSyuniq = types.InlineKeyboardButton(
                "Св.Григор Лусаворич", url="https://maps.app.goo.gl/3YH9zJwgRC2wqu2T9")
            tatev = types.InlineKeyboardButton("Татевский монастырь",url="https://maps.app.goo.gl/Y6Pwtiw39udy2sJ46")
            
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(bex, zvaravank, ripsime,
                         vorotnavanq, alan, noravanq, GrigorLusavorichSyuniq,tatev, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 8 самых известных церквей и монастырских комплексов Сюникского региона.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button9':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            haxarcin = types.InlineKeyboardButton(
                "Ахарцин", url="https://maps.app.goo.gl/aEWCoQaRPrMBnG4t6")
            goshavanq = types.InlineKeyboardButton(
                "Гошаванк", url="https://maps.app.goo.gl/tmKByea91UaSPLHKA")
            mroDzor = types.InlineKeyboardButton(
                "МроДзор", url="https://maps.app.goo.gl/HygyvNe97kLQWDm97")
            xoranashat = types.InlineKeyboardButton(
                "Жоранашат", url="https://maps.app.goo.gl/e7bq8ZRvnUf8P44L6")
            makaravanq = types.InlineKeyboardButton(
                "Макараванк", url="https://maps.app.goo.gl/sKCMWkvWxQYQxvD76")
            varagavanq = types.InlineKeyboardButton(
                "Нор Варагаванк", url="https://maps.app.goo.gl/w5BxApweNvP6Zhdb8")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(haxarcin, goshavanq,
                         mroDzor, xoranashat, makaravanq, varagavanq, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 6 самых известных церквей и монастырских комплексов Тавушского региона.📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button10':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            noravanqVayocCor = types.InlineKeyboardButton(
                "Нораванк", url="https://maps.app.goo.gl/u2gXHwo25Bx6SKDC9")
            gndevanq = types.InlineKeyboardButton(
                "Гндеванк", url="https://maps.app.goo.gl/auT4W2RdofKmYDJ57")
            zorac = types.InlineKeyboardButton(
                "Зора", url="https://maps.app.goo.gl/TC4AffgERWEyd5YH8")
            mamas = types.InlineKeyboardButton(
                "Св.Мамас", url="https://maps.app.goo.gl/UpzpggW9tP7KvRTg6")
            shativanq = types.InlineKeyboardButton(
                "Шативанк", url="https://maps.app.goo.gl/rrJajvYhQyCHT9hn8")
            caxacQar = types.InlineKeyboardButton(
                "Цахац Кар", url="https://maps.app.goo.gl/4AohsLPQc2miSVucA")
            AstvacacinVayocCor = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/nRPoZ3bm3Vgkd7Mv9")
            arates = types.InlineKeyboardButton(
                "Аратес", url="https://maps.app.goo.gl/vYYKDQ1g8sVRM3rD8")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(noravanqVayocCor, gndevanq, zorac, mamas,
                         shativanq, caxacQar, AstvacacinVayocCor, arates, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 9 самых известных церквей и монастырских комплексов региона ВайоЦ Цор📍", reply_markup=keyboard)

        elif message.data == 'ansver_button11':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            sargis = types.InlineKeyboardButton(
                "Св.Саргис", url="https://maps.app.goo.gl/Ho2g48ySi9Kqf1F89")
            grigor = types.InlineKeyboardButton(
                "Св.Григор Лусаворич", url="https://maps.app.goo.gl/coayno5VodpweJk39")
            mkrtich = types.InlineKeyboardButton(
                "Св.ОГаннес Мкртич", url="https://maps.app.goo.gl/G1XboAfRL7u9jXE56")
            anna = types.InlineKeyboardButton(
                "Св.Катохике и Св.Анна", url="https://maps.app.goo.gl/6i3TxjKCv9n6Tp5D6")
            zoravar = types.InlineKeyboardButton(
                "Св.Зоравар Богородица", url="https://maps.app.goo.gl/158woVuYMGZvmwvE9")
            mariam2 = types.InlineKeyboardButton(
                "Св.Мариам Богородица", url="https://maps.app.goo.gl/QrKqDrQ5rFWse8EA6")
            sargis1 = types.InlineKeyboardButton(
                "Св.Саргис", url="https://maps.app.goo.gl/LXvEbw6U7hw6pBqw8")
            gevorg2 = types.InlineKeyboardButton(
                "Св.Геворг", url="https://maps.app.goo.gl/AquD5uqjgSfEi8CQ8")
            hakob2 = types.InlineKeyboardButton(
                "Св.Акоб", url="https://maps.app.goo.gl/fa98pKFDvZ3pzTb87")
            xach2 = types.InlineKeyboardButton(
                "Св.Крест", url="https://maps.app.goo.gl/trgHTj2eDtyJPimx5")
            nahatakac = types.InlineKeyboardButton(
                "St.Наатакац", url="https://maps.app.goo.gl/tirwzoDr5EG5Y86q7")
            astvacacin2 = types.InlineKeyboardButton(
                "Св.Богородица", url="https://maps.app.goo.gl/aTYteohSRDjT4FYDA")
            errord = types.InlineKeyboardButton(
                "Св.Ерордутюн", url="https://maps.app.goo.gl/ctYV1xujUQT5C63r6")
            xach3 = types.InlineKeyboardButton(
                "Св.Крест", url="https://maps.app.goo.gl/VbMifw6BuDKhvRcG7")
            back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')

            keyboard.add(sargis, grigor, mkrtich, anna, zoravar, mariam2, sargis1,
                         gevorg2, hakob2, xach2, nahatakac, astvacacin2, errord, xach3, back)

            bot.send_message(
                message.message.chat.id, "Предлагаем посетить 15 самых известных церквей и монастырских комплексов Еревана.📍", reply_markup=keyboard)
            
        elif message.data == 'back':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            Button1 = types.InlineKeyboardButton(
                "Арагацотн", callback_data='ansver_button1')
            Button2 = types.InlineKeyboardButton(
                "Арарат", callback_data='ansver_button2')
            Button3 = types.InlineKeyboardButton(
                "Армавир", callback_data='ansver_button3')
            Button4 = types.InlineKeyboardButton(
                "Гехаркуник", callback_data='ansver_button4')
            Button5 = types.InlineKeyboardButton(
                "Котайк", callback_data='ansver_button5')
            Button6 = types.InlineKeyboardButton(
                "Лори", callback_data='ansver_button6')
            Button7 = types.InlineKeyboardButton(
                "Ширак", callback_data='ansver_button7')
            Button8 = types.InlineKeyboardButton(
                "Сюник", callback_data='ansver_button8')
            Button9 = types.InlineKeyboardButton(
                "Тавуш", callback_data='ansver_button9')
            Button10 = types.InlineKeyboardButton(
                "Вайоц Дзор", callback_data='ansver_button10')
            Button11 = types.InlineKeyboardButton(
                "Ереван", callback_data='ansver_button11')

            keyboard.add(Button1, Button2, Button3, Button4, Button5,
                         Button6, Button7, Button8, Button9, Button10, Button11)

            bot.send_message(
                message.message.chat.id, "Отметьте регион, который вы хотите посетить📍", reply_markup=keyboard)
        