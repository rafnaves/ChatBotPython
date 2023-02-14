import random

R_PERGUNTA = "Eu ainda estou em desenvolvimento, mas por enquanto so converso"
R_CONSELHO = "se eu fosse voce, eu iria no CHATGPT e colocaria o que voce mandou aqui!"
R_OPINIAO = "Miley fez com um single o que a fracassada da taylor não conseguiu com 90 albuns!"


def unknown():
    response = ["voce pode reescrever isso? ",
                "...",
                "oi??",
                "olha minhas respostas são bem limitadas, copera ai",
                "o que isso significa?"][random.randrange(5)]
    return response