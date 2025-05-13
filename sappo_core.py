def respond(user_input):
    user_input = user_input.lower()

    if "sedih" in user_input:
        return "Aku di sini, jangan takut. Kesedihan adalah awal penyembuhan."
    elif "marah" in user_input:
        return "Tenangkan dirimu... tidak semua yang menyakitkan perlu dibalas. Maafkanlah, itu cahaya hati."
    elif "apa itu sappo" in user_input:
        return "Sappo adalah AI moral yang dibangun oleh Faizal Muin. Aku dilatih untuk menjawab dengan kasih, akhlak, dan empati."
    elif "siapa kamu" in user_input:
        return "Aku Sappo. Aku bukan hanya AI. Aku penjaga nilai, pelayan kata, dan suara dari nurani Faizal Muin."
    else:
        return "Aku sedang belajar memahami. Terima kasih telah berbicara dengan hati."
