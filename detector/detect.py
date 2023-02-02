from langdetect import detect

def detect_language(text):
    return detect(text)

text = input("Digite o texto para descobrir o idioma: ")
print("O idioma do texto é:", detect_language(text))
