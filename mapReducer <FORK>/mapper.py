from preprocess import make_tokens
from txt_to_json import make as makeJson

def mapper(lang, file):

    out = []

    for line in makeJson(file):

        text = line['text']

        tweet = make_tokens(text, lang)
        tweet = tweet.strip()
        words = tweet.split()
        
        for word in words:
            out.append({"text": word, "count": 1})
    return out