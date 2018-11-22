from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import  RegexpTokenizer
import re


def regex_clean_ruidos(text):
    '''
        função manual para eliminação de ruídos através de regex, descartar qualquer coisa
        que na composição possua uma 'não letra', como símbolos e números...

        Ex: ',ola' - '...'  - 'email@alguem'
    '''
    return ' '.join([
        t for t in text.strip().split() if re.match(r'[^\W\d]*$', t)
    ])


def regex_clean(text):

    '''
        função pronta da lib NLTK para limpeza de ruído
    '''
    return regex_clean_ruidos(
        ' '.join(RegexpTokenizer(r'\w+').tokenize(text)).lower()
    )


def make_tokens(text, lang):
    
    stop_words = set(stopwords.words(lang)) 
    
    word_tokens = word_tokenize(
        regex_clean(text) #Vai tirar algumas impurezas do texto, como números e alguns simbolos
    ) 
    
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    
    filtered_sentence = [] 
    
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    return ' '.join(filtered_sentence)
    
