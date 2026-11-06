import logging
import json
import azure.functions as func

def main(msg: func.ServiceBusMessage):
    message_body = msg.get_body().decode("utf-8")

    try:
        data = json.loads(message_body)
        logging.info("Mensagem recebida do Service Bus:")
        logging.info(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        logging.info("Mensagem recebida (texto puro):")
        logging.info(message_body)

    # Aqui você poderia:
    # - salvar em banco
    # - chamar uma API
    # - acionar uma Logic App
    # - processar dados
