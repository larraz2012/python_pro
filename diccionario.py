dicionario={"mongolo" : "persona tonta",
            "palomitas":"tambien conocidas como rosas"
}

word = input("escribe la palabra que no sepas")

if word in dicionario.keys():
    print(dicionario[word])

else:
    print("esa palabra no esta en este diccionario")
