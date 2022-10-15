nome = "a"
while nome.count(" ") == 0:
    nome = input("escreva o seu nome completo:")
    if nome.count(" ") == 0:
        print("(lembre-se é o seu nome completo)")
nomemi = nome.lower()
con = nomemi.count("a") +nomemi.count("e")+nomemi.count("i")+nomemi.count("o")+nomemi.count("u")
pnome = nomemi.split()
print("é um prazer sr(a).",pnome[nomemi.count(" ")],"!!!")
print("o seu nome tem no total ",len(nomemi) - nomemi.count(" ")," lestras, sendo elas: ", con, "vogais e ",(len(nome) - con - nome.count(" "))," consoantes" )
