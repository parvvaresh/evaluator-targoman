


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


def Translate(word:str, fromLang :str, toLang:str) -> str:
    if fromLang == "fa" and toLang == "en":
        return translate(word, toLang=toLang, fromLang=fromLang)["result"]["tr"]["base"][0][1]
    if fromLang == "en" and toLang == "fa":
        return translate(word, toLang=toLang, fromLang=fromLang)["result"]["tr"]["base"][0][1]
 
 
 
