from django.core.mail import send_mail


def enviar_email_confirmacao(adocao):
    assunto = "Adoção realizada com sucesso!"
    conteudo = f"Parabéns por realizar a adoção do pet {adocao.pet.nome} com o valor mensal de {adocao.valor}"
    remetente = "adote.pets2022@gmail.com"
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)