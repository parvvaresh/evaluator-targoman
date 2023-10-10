from get_data import translate

def Translate() -> str:
    word = input("please enter word who wants  to be translated : ")
    fromLang = input("from lan  : ")
    toLang = input("to lan : ")
    if fromLang == "fa" and toLang == "en":
        return translate("Bonjour", toLang="en", fromLang="fr")["result"]["tr"]['base'][0][1]
