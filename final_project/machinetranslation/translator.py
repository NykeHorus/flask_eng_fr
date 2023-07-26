"""Code for Translation of Text"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):

    '''Function to trasnslate English to French'''
    french_text= MyMemoryTranslator(source='en-GB',target='french').translate(english_text)
    return french_text


def french_to_english(french_text):

    '''Function to translate French to English'''
    english_text=MyMemoryTranslator(source='fr-FR',target='english').translate(french_text)
    return english_text
