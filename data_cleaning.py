import asyncio
from model import summarizer
from typing import List, Dict



async def process_messages(messages):
    grouped_messages = {}
    id_count = 0
    
    try:
        for message in messages:
            address = message["address"]
            body = message["body"]
            
            if address not in grouped_messages:
                grouped_messages[address] = []
            
            grouped_messages[address].append(body)

        tasks = []
        for number, msgs in grouped_messages.items():
            id_count = id_count + 1
            tasks.append(process_and_summarize_individual(id_count, number, msgs))
        result = await asyncio.gather(*tasks)
        
        return result
    except Exception as e:
        return {"error": str(e)}


async def process_and_summarize_individual(_id, number, messages):
    try:
        text = " ".join(messages)
        summary = await summarizer(text)
        return {'_id':_id, 'number':number, 'body':summary, 'error':False}
    except Exception as e:
        return {'_id':_id, 'number':number, "body": str(e), 'error':True}
