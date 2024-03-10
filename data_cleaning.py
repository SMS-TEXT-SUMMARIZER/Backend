import asyncio
from model import summarizer
from typing import List, Dict

async def process_messages(messages):
    grouped_messages = {}
    
    try:
        for message in messages:
            address = message["address"]
            body = message["body"]
            
            if address not in grouped_messages:
                grouped_messages[address] = []
            
            grouped_messages[address].append(body)

        tasks = []
        for number, msgs in grouped_messages.items():
            tasks.append(process_and_summarize_individual(number, msgs))
        result = await asyncio.gather(*tasks)
        
        return result
    except Exception as e:
        return {"error": str(e)}


async def process_and_summarize_individual(number: str, messages: List[str]):
    try:
        text = " ".join(messages)
        summary = await summarizer(text)
        return {'number':number, 'body':summary, 'error':False}
    except Exception as e:
        return {'number':number, "body": str(e), 'error':True}
