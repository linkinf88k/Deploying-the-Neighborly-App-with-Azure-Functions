import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):

	logging.info('Function triggered to process a message: ', event.get_body())

    result = json.dumps({
        'id': event.id,
        'data': event.data,
        'subject': event.subject,
        'event_type': event.event_type,
    })


    logging.info('Python EventGrid trigger processed an event: %s', result)



