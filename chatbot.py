import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # conta o numero de palavras nas mensagens predefinidas
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # calcula a porcentagem de palavras conhecidas na mensagem do usuario
    percentage = float(message_certainty) / float(len(recognised_words))

    # checa se as palavras estão na string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # palavras requeridas
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifica a criação da resposta
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # respostas -------------------------------------------------------------------------------------------------------
    response('Ola!', ['ola', 'oi', 'eae', 'oii', 'eai'], single_response=True)
    response('Até mais!', ['tchau', 'adeus'], single_response=True)
    response('Sou um bot, não posso estar nada, mas de um modo geral, estou bem', ['como', 'voce', 'esta',], required_words=['como'])
    response('Eu que agradeço', ['muito', 'obrigado'], single_response=True)
    response('Meu nome é ygonio, sou um bot!', ['qual', 'é', 'seu', 'nome'], required_words=['qual', 'nome'])
    response('ESMAGUEI!', ['esmaga'], required_words=['esmaga'])

    # respostas longas
    response(long.R_CONSELHO, ['de', 'conselho'], required_words=['conselho'])
    response(long.R_PERGUNTA, ['o que', 'voce', 'faz'], required_words=['voce', 'faz'])
    response(long.R_OPINIAO, ['qual', 'sua', 'opiniao', 'taylor'], required_words=['taylor'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# pega a resposta
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# sistema de resposta
while True:
    print('Bot: ' + get_response(input('You: ')))