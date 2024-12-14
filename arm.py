import telebot
from telebot import types


def armenia(bot, message):
    if message.message:
        if message.data == 'armenia':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            Button1 = types.InlineKeyboardButton( "Արագածոտն", callback_data='ansver_button1')
            Button2 = types.InlineKeyboardButton("Արարատ", callback_data='ansver_button2')
            Button3 = types.InlineKeyboardButton("Արմավիր", callback_data='ansver_button3')
            Button4 = types.InlineKeyboardButton("Գեղարքունիք", callback_data='ansver_button4')
            Button5 = types.InlineKeyboardButton("Կոտայք", callback_data='ansver_button5')
            Button6 = types.InlineKeyboardButton("Լոռի", callback_data='ansver_button6')
            Button7 = types.InlineKeyboardButton("Շիրակ", callback_data='ansver_button7')
            Button8 = types.InlineKeyboardButton("Սյունիք", callback_data='ansver_button8')
            Button9 = types.InlineKeyboardButton("Տավուշ", callback_data='ansver_button9')
            Button10 = types.InlineKeyboardButton("Վայոց ձոր", callback_data='ansver_button10')
            Button11 = types.InlineKeyboardButton("Երևան", callback_data='ansver_button11')

            keyboard.add(Button1, Button2, Button3, Button4, Button5, Button6,Button7, Button8, Button9, Button10, Button11)

            bot.send_message(message.message.chat.id, "Նշեք այն մարզը որտեղ ցանկանում եք այցելել📍", reply_markup=keyboard)

        elif message.data == "ansver_button1":
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            saxmosavank = types.InlineKeyboardButton(
                "Սաղմոսավանք", url="https://maps.app.goo.gl/Z91XELPvmNPHnpLp9")
            hovhanavank = types.InlineKeyboardButton(
                "Հովհաննավանք", url="https://maps.app.goo.gl/5q8WLQaetGbQzqAU9")
            talin = types.InlineKeyboardButton(
                "Թալինի տաճար", url="https://maps.app.goo.gl/QPjGbKDn7cP2M7fw5")
            AstvacacinAragacotn = types.InlineKeyboardButton(
                "Սբ․Աստվածածին", url="https://maps.app.goo.gl/iTTm4Ri2x1T4nL5AA")
            hakob = types.InlineKeyboardButton(
                "Սբ․Հակոբ", url="https://maps.app.goo.gl/dF8ZjSydtPwxZgwq5")
            gevorg = types.InlineKeyboardButton(
                "Սբ․Գևորգ", url="https://maps.app.goo.gl/Sz7uLvFR5Y7R6mPz6")
            muxni = types.InlineKeyboardButton("Մուղնի",url="https://maps.app.goo.gl/ZnEFVKVcTVeznkeYA")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(saxmosavank, hovhanavank, talin,
                         AstvacacinAragacotn, hakob, gevorg,muxni,back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Արագածոտնի մարզի 7 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button2':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            xorvirap = types.InlineKeyboardButton(
                "Խոր Վիրապ", url="https://maps.app.goo.gl/k9w7VoSkG34s62pe7")
            HovhannesArarat = types.InlineKeyboardButton(
                "Սբ․Հովհաննես", url="https://maps.app.goo.gl/iQ6LdLwKfnJRge1g9")
            nshan = types.InlineKeyboardButton(
                "Սբ․Նշան", url="https://maps.app.goo.gl/gWsuAvHo2orZNU5t9")
            AstvacacinArarat = types.InlineKeyboardButton(
                "Սբ․Աստվածածին", url="https://maps.app.goo.gl/YWAySdHMd3F1Q1qg8")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(HovhannesArarat, xorvirap,
                         nshan, AstvacacinArarat, back)
            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Արարատի մարզի 4 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button3':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            AstvacacinArmavir = types.InlineKeyboardButton(
                "Սբ․Աստվածածին", url="https://maps.app.goo.gl/Qb4T89H8BR12Sbrn7")
            HovhannesArmavir = types.InlineKeyboardButton(
                "Սբ․Հովհաննես", url="https://maps.app.goo.gl/ycgqJ7kSG3NYJD1t9")
            GevorgArmavir = types.InlineKeyboardButton(
                "Սբ․Գևորգ", url="https://maps.app.goo.gl/coWSG3vXKdiBCCLV9")
            MayrtacharArmavir = types.InlineKeyboardButton(
                "Մայր տաճար", url="https://maps.app.goo.gl/skfJziZjyq6yYQe38")
            MariamArmavir = types.InlineKeyboardButton(
                "Սբ․Մարիամ", url="https://maps.app.goo.gl/qE7TgbsywQ99WgfN8")
            shoxakat = types.InlineKeyboardButton("Սբ․Շողակաթ",url="https://maps.app.goo.gl/KAi2GnHwW24R6AH8A")
            gayane = types.InlineKeyboardButton("Սբ․Գայանե",url="https://maps.app.goo.gl/aC7j7Cr35xLGqW8U7")
            hripsime = types.InlineKeyboardButton("Սբ․Հռիփսիմե",url="https://maps.app.goo.gl/R4tBeMCPqUcfBCjt7")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(AstvacacinArmavir, HovhannesArmavir,
                         GevorgArmavir, MayrtacharArmavir, MariamArmavir,shoxakat,gayane,hripsime,back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Արմավիրի մարզի 8 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button4':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            HakobGexarqunik = types.InlineKeyboardButton(
                "Սբ․Հակոբ", url="https://maps.app.goo.gl/nSpGDqLk97t2CDNe8")
            sevanavank = types.InlineKeyboardButton(
                "Սևանավանք", url="https://maps.app.goo.gl/vm4owci4TNByce6XA")
            AstvacacinGexarqunik = types.InlineKeyboardButton(
                "Աստվածածին", url="https://maps.app.goo.gl/ZF5PdZiCUDse4eNG6")
            AstvacacinGexarqunik2 = types.InlineKeyboardButton(
                "Սբ.Աստվածածին", url="https://maps.app.goo.gl/bmMGgrQiaksH4SrNA")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(HakobGexarqunik, sevanavank,
                         AstvacacinGexarqunik, AstvacacinGexarqunik2, back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Գեղարքունիքի մարզի 4 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)
            
        elif message.data == 'ansver_button5':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            kecharis = types.InlineKeyboardButton(
                "Կեչարիս", url="https://maps.app.goo.gl/eJB8kEapnwztnrZBA")
            kaptavanq = types.InlineKeyboardButton(
                "Կապտվանք", url="https://maps.app.goo.gl/UTR5HdUHATESctjz6")
            ghuk = types.InlineKeyboardButton(
                "Գհուկ", url="https://maps.app.goo.gl/nCTHUXCL7qV27UCD9")
            tezharuyk = types.InlineKeyboardButton(
                "Թեզհարույք", url="https://maps.app.goo.gl/LaE6SaTKyripuNm18")
            dzakavanq = types.InlineKeyboardButton(
                "Ձականավանք", url="https://maps.app.goo.gl/xa2WpuGwcGhXsFB89")
            ptxnavanq = types.InlineKeyboardButton(
                "Պտղավանք", url="https://maps.app.goo.gl/eeWpX4BTqGLLbiLb9")
            kiraki = types.InlineKeyboardButton(
                "Սբ․Կիրակի", url="https://maps.app.goo.gl/Rr96NZ1MCQBU7FjN6")
            mayravanq = types.InlineKeyboardButton(
                "Մայրավանք", url="https://maps.app.goo.gl/t6Q6Qf3qzhTCpxdk8")
            garni = types.InlineKeyboardButton(
                "Գառնի", url="https://maps.app.goo.gl/rqVthcnZHX1WZnb78")
            gexadri = types.InlineKeyboardButton("Գեղարդի վանք",url="https://maps.app.goo.gl/78nMrBJeKngA9ivH7")
            juxtak = types.InlineKeyboardButton("Ջուխտակ",url="https://maps.app.goo.gl/R1YtjcTCAj3DE1o1A")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(kecharis, kaptavanq, ghuk, tezharuyk,
                         dzakavanq, ptxnavanq, kiraki, mayravanq, garni,gexadri,juxtak,back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Կոտայքի մարզի 11 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button6':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            sanahin = types.InlineKeyboardButton(
                "Շանահին", url="https://maps.app.goo.gl/62sukQHRo8v4GD4z7")
            Haghpat = types.InlineKeyboardButton(
                "Հաղպատ", url="https://maps.app.goo.gl/7n78pafw79hp63QB9")
            odzun = types.InlineKeyboardButton(
                "Օձուն", url="https://maps.app.goo.gl/Mni3niCqtHZ4eVuC7")
            horomayr = types.InlineKeyboardButton(
                "Հորամայր", url="https://maps.app.goo.gl/axQHrAeQuG1eFBqH9")
            Ardvi = types.InlineKeyboardButton(
                "Արդվի", url="https://maps.app.goo.gl/L41tYvtNXd1RCqrk6")
            kobair = types.InlineKeyboardButton(
                "Քոբայր", url="https://maps.app.goo.gl/3Zm3xBJaAP1UiVJN7")
            alxata = types.InlineKeyboardButton(
                "Ալխաթա", url="https://maps.app.goo.gl/Ez9ecs9bkyF8As1P7")
            hnevank = types.InlineKeyboardButton(
                "Հնեվանք", url="https://maps.app.goo.gl/TNvby46pzQgoCpoF6")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(sanahin, Haghpat, odzun, horomayr,
                         Ardvi, kobair, alxata, hnevank, back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Լոռու մարզի 9 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button7':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            GrigorLusavorich = types.InlineKeyboardButton(
                "ՍԲ․Գրիգոր Լուսավորիչ", url="https://maps.app.goo.gl/jKpH3CFmiFUF4CBH9")
            StAmenaprkich = types.InlineKeyboardButton(
                "Սբ․Ամենափրկիչ", url="https://maps.app.goo.gl/eLavRpAH82JVF8cb8")
            yotverq = types.InlineKeyboardButton(
                "Սբ.Աստվածածին", url="https://maps.app.goo.gl/21n2Re1EMQ9ymNvR8")
            hakobShirak = types.InlineKeyboardButton(
                "Սբ․Հակոբ", url="https://maps.app.goo.gl/rjLAVNMwsNEAGLWy5")
            sargisShirak = types.InlineKeyboardButton(
                "Սբ․Սարգիս", url="https://maps.app.goo.gl/c44AFm4jvFpf8Vxy9")
            marmarashen = types.InlineKeyboardButton(
                "Մարմարաշեն", url="https://maps.app.goo.gl/ksVwQntMKcVjSwaC9")
            StAstvacacin = types.InlineKeyboardButton(
                "Սբ․Աստվածածին", url="https://maps.app.goo.gl/EU5TKLTxC9gaVd8d9")
            harichavanq = types.InlineKeyboardButton(
                "Հառիճավանք", url="https://maps.app.goo.gl/D4BufMeYB2MCpQsD6")
            lmbatavanq = types.InlineKeyboardButton(
                "Լմբատավանք", url="https://maps.app.goo.gl/shhi7ZKjFG9uRN3x8")
            GevorgShirak = types.InlineKeyboardButton(
                "Սբ.Գևորգ", url="https://maps.app.goo.gl/JgLGwrBgLHR4BdrU7")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(GrigorLusavorich, StAmenaprkich, yotverq, hakobShirak, sargisShirak,
                         marmarashen, StAstvacacin, harichavanq, lmbatavanq, GevorgShirak, back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Շիրակի մարզի 10 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button8':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            bex = types.InlineKeyboardButton(
                "Բեխ", url="https://maps.app.goo.gl/gaXysH4wEpghsjox8")
            zvaravank = types.InlineKeyboardButton(
                "Զվարավանք", url="https://maps.app.goo.gl/6STrsPfZgX6z8CeD7")
            ripsime = types.InlineKeyboardButton(
                "Սբ․Հռիփսիմե", url="https://maps.app.goo.gl/uohPRdfzPZRAX6G38")
            vorotnavanq = types.InlineKeyboardButton(
                "Վորթանավանք", url="https://maps.app.goo.gl/gZBSFdf6RBrP44fV8")
            alan = types.InlineKeyboardButton(
                "Ալան արքա", url="https://maps.app.goo.gl/hUXWYgun2vPLdL8g7")
            noravanq = types.InlineKeyboardButton(
                "Նորավանք", url="https://maps.app.goo.gl/hbnoSWB8WEZacs5S9")
            GrigorLusavorichSyuniq = types.InlineKeyboardButton(
                "Սբ․Գրիգոր Լուսավորիչ", url="https://maps.app.goo.gl/3YH9zJwgRC2wqu2T9")
            tatev = types.InlineKeyboardButton("Տաթևի վանք",url="https://maps.app.goo.gl/Y6Pwtiw39udy2sJ46")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(bex, zvaravank, ripsime,
                         vorotnavanq, alan, noravanq, GrigorLusavorichSyuniq,tatev,back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Սյունիքի մարզի 8 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button9':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            haxarcin = types.InlineKeyboardButton(
                "Հաղարձին", url="https://maps.app.goo.gl/aEWCoQaRPrMBnG4t6")
            goshavanq = types.InlineKeyboardButton(
                "Գոշավանք", url="https://maps.app.goo.gl/tmKByea91UaSPLHKA")
            mroDzor = types.InlineKeyboardButton(
                "Մրո Ձորո", url="https://maps.app.goo.gl/HygyvNe97kLQWDm97")
            xoranashat = types.InlineKeyboardButton(
                "Խորհանաշատ", url="https://maps.app.goo.gl/e7bq8ZRvnUf8P44L6")
            makaravanq = types.InlineKeyboardButton(
                "Մակարավանք", url="https://maps.app.goo.gl/sKCMWkvWxQYQxvD76")
            varagavanq = types.InlineKeyboardButton(
                "Նոր Վարագավանք", url="https://maps.app.goo.gl/w5BxApweNvP6Zhdb8")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(haxarcin, goshavanq,
                         mroDzor, xoranashat, makaravanq, varagavanq, back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Տավուշի մարզի 6 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button10':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            noravanqVayocCor = types.InlineKeyboardButton(
                "Նորավանք", url="https://maps.app.goo.gl/u2gXHwo25Bx6SKDC9")
            gndevanq = types.InlineKeyboardButton(
                "Գնդեվանք", url="https://maps.app.goo.gl/auT4W2RdofKmYDJ57")
            zorac = types.InlineKeyboardButton(
                "Զորաց", url="https://maps.app.goo.gl/TC4AffgERWEyd5YH8")
            mamas = types.InlineKeyboardButton(
                "Սբ․Մամաս", url="https://maps.app.goo.gl/UpzpggW9tP7KvRTg6")
            shativanq = types.InlineKeyboardButton(
                "Շատիվանք", url="https://maps.app.goo.gl/rrJajvYhQyCHT9hn8")
            caxacQar = types.InlineKeyboardButton(
                "Ծախած քար", url="https://maps.app.goo.gl/4AohsLPQc2miSVucA")
            AstvacacinVayocCor = types.InlineKeyboardButton(
                "Սբ․Աստվածածին", url="https://maps.app.goo.gl/nRPoZ3bm3Vgkd7Mv9")
            arates = types.InlineKeyboardButton(
                "Արատես", url="https://maps.app.goo.gl/vYYKDQ1g8sVRM3rD8")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(noravanqVayocCor, gndevanq, zorac, mamas,
                         shativanq, caxacQar, AstvacacinVayocCor, arates, back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Վայոց ձոր Մարզի 9 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'ansver_button11':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

            sargis = types.InlineKeyboardButton(
                "Սբ․Սարգիս", url="https://maps.app.goo.gl/Ho2g48ySi9Kqf1F89")
            grigor = types.InlineKeyboardButton(
                "Սբ․Գրիգոր Լուսավորիչ", url="https://maps.app.goo.gl/coayno5VodpweJk39")
            mkrtich = types.InlineKeyboardButton(
                "Սբ․Հովհաննես Մկրտիչ", url="https://maps.app.goo.gl/G1XboAfRL7u9jXE56")
            anna = types.InlineKeyboardButton(
                "Սբ․Կաթողիկե և Սբ․Աննա", url="https://maps.app.goo.gl/6i3TxjKCv9n6Tp5D6")
            zoravar = types.InlineKeyboardButton(
                "Սբ․Զորավար Աստվածածին", url="https://maps.app.goo.gl/158woVuYMGZvmwvE9")
            mariam2 = types.InlineKeyboardButton(
                "Սբ․Մարիամ Աստվածածին", url="https://maps.app.goo.gl/QrKqDrQ5rFWse8EA6")
            sargis1 = types.InlineKeyboardButton(
                "Սբ․Սարգիս", url="https://maps.app.goo.gl/LXvEbw6U7hw6pBqw8")
            gevorg2 = types.InlineKeyboardButton(
                "Սբ․Գևորգ", url="https://maps.app.goo.gl/AquD5uqjgSfEi8CQ8")
            hakob2 = types.InlineKeyboardButton(
                "Սբ․Հակոբ", url="https://maps.app.goo.gl/fa98pKFDvZ3pzTb87")
            xach2 = types.InlineKeyboardButton(
                "Սբ․Խաչ", url="https://maps.app.goo.gl/trgHTj2eDtyJPimx5")
            nahatakac = types.InlineKeyboardButton(
                "Սբ․Նահատանած", url="https://maps.app.goo.gl/tirwzoDr5EG5Y86q7")
            astvacacin2 = types.InlineKeyboardButton(
                "Սբ․Աստվածածին", url="https://maps.app.goo.gl/aTYteohSRDjT4FYDA")
            errord = types.InlineKeyboardButton(
                "Սբ․Երրորդություն", url="https://maps.app.goo.gl/ctYV1xujUQT5C63r6")
            xach3 = types.InlineKeyboardButton(
                "Սբ․Խաչ", url="https://maps.app.goo.gl/VbMifw6BuDKhvRcG7")
            back = types.InlineKeyboardButton("⬅️Հետ", callback_data='back')

            keyboard.add(sargis, grigor, mkrtich, anna, zoravar, mariam2, sargis1,
                         gevorg2, hakob2, xach2, nahatakac, astvacacin2, errord, xach3, back)

            bot.send_message(
                message.message.chat.id, "Առաջարկում ենք այցելել Երևանի 15 ամենահայտնի եկեղեցիներն ու վանական համալիրները։📍", reply_markup=keyboard)

        elif message.data == 'back':
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)

            Button1 = types.InlineKeyboardButton( "Արագածոտն", callback_data='ansver_button1')
            Button2 = types.InlineKeyboardButton("Արարատ", callback_data='ansver_button2')
            Button3 = types.InlineKeyboardButton("Արմավիր", callback_data='ansver_button3')
            Button4 = types.InlineKeyboardButton("Գեղարքունիք", callback_data='ansver_button4')
            Button5 = types.InlineKeyboardButton("Կոտայք", callback_data='ansver_button5')
            Button6 = types.InlineKeyboardButton("Լոռի", callback_data='ansver_button6')
            Button7 = types.InlineKeyboardButton("Շիրակ", callback_data='ansver_button7')
            Button8 = types.InlineKeyboardButton("Սյունիք", callback_data='ansver_button8')
            Button9 = types.InlineKeyboardButton("Տավուշ", callback_data='ansver_button9')
            Button10 = types.InlineKeyboardButton("Վայոց ձոր", callback_data='ansver_button10')
            Button11 = types.InlineKeyboardButton("Երևան", callback_data='ansver_button11')

            keyboard.add(Button1, Button2, Button3, Button4, Button5, Button6,Button7, Button8, Button9, Button10, Button11)

            bot.send_message(message.message.chat.id, "Նշեք այն մարզը որտեղ ցանկանում եք այցելել📍", reply_markup=keyboard)
