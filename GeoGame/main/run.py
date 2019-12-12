import random

uf_estados = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiania',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracajú',
    'Tocantins': 'Palmas'
}

estados = list(uf_estados.keys())
chances = 3
pontos = 0

while chances > 0:
    if pontos == 26:
        chances = 0
        print(f'Você acertou todas as capitais, parabéns! Jogo finalizado com {pontos} pontos.')
    else:
        rand_uf = random.choice(estados)
        quest = input(f'Qual é a capital do seguinte estado? {rand_uf}: ')
        resp = uf_estados.get(rand_uf)
        if quest == resp:
            estados.remove(rand_uf)
            pontos += 1
            print(f'Você acertou e ganhou 1 ponto! Pontuação: {pontos}')
        else:
            chances -= 1
            if chances == 0:
                print(f'Acabaram suas chances, sua pontuação final foi de {pontos} pontos!')
            elif chances == 1:
                print(f'Resposta incorreta! Você agora só tem mais {chances} chance.')
            else:
                print(f'Resposta incorreta! Você tem mais {chances} chances.')

