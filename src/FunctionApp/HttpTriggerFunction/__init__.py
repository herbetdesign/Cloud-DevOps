import logging
import json
import os
import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP Trigger acionado.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Corpo da requisição inválido. Envie um JSON.",
            status_code=400
        )

    message_content = json.dumps(req_body)

    servicebus_connection_str = os.environ.get("SERVICE_BUS_CONNECTION")
    queue_name = os.environ.get("SERVICE_BUS_QUEUE")

    try:
        with ServiceBusClient.from_connection_string(
            conn_str=servicebus_connection_str
        ) as client:
            sender = client.get_queue_sender(queue_name=queue_name)
            with sender:
                message = ServiceBusMessage(message_content)
                sender.send_messages(message)

        return func.HttpResponse(
            "Mensagem enviada com sucesso para o Service Bus.",
            status_code=200
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            "Erro ao enviar mensagem para o Service Bus.",
            status_code=500
        )
