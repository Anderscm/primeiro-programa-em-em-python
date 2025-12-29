nome = (input("digite seu nome \n"))
ano_nasc = int (input("digite a seu ano de nascimento \n"))
ano_atual = int(input("digite o ano atual \n"))
idade = ano_atual - ano_nasc
idade_especial = 17
print(nome, "voce tem", idade, "anos de idade")

# exemplo com estrutura de condição

if idade >= 18:
    print("vc é maior de idade, pode tirar a CNH")
elif idade == 17:
    print("pode fazer as aulas teoricas, mas não pode fazer aulas práticas ainda")
else:
    print("menor de idade, ainda não pode tirar a CNH")

print("segue abaixo as informações inseridas")

#criando discionarios
informações = {
    "nome": nome,
    "sua idade é": idade,
    "seu ano de nascimento": ano_nasc,
    "o ano atual é": ano_atual,
}
print(informações)

