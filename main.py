import coffee
import dados

escolha = input("O que você vai querer? (espreso/latte/cappuccino): ")
if escolha == "relatorio":
    print(coffee.mostrar_relatorio(dados.resources))

