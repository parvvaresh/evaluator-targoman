import requests as req
import json

URL = "Https://targoman.ir/API"


def translate(word: str = "سلام", fromLang: str = "fa", toLang: str = "en") -> dict:
    payload = {
        "jsonrpc": "2.0",
        "method": "Targoman::translate",
        "id": 1,
        "params": [
            "sSTargomanWUI",
            word,
            "%s2%s" % (fromLang.lower().strip(), toLang.lower().strip()),
            "127.0.0.10",
            "NMT",
            True,
            True,
            True,
            None,
            "formal",
        ],
    }

    data = req.post(URL, json=payload)
    data = json.loads(data.text)
    return data

#test
print(translate("Bonjour", toLang="en", fromLang="fr")["result"]["tr"]['base'][0][1])