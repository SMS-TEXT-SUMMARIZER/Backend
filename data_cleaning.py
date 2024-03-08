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
        summarized_messages = {}
        for number, msgs in grouped_messages.items():
            tasks.append(process_and_summarize_individual(number, msgs, summarized_messages))
        result = await asyncio.gather(*tasks)
        
        return result
    except Exception as e:
        return {"error": str(e)}


async def process_and_summarize_individual(number: str, messages: List[str], summarized_messages: Dict[str, str]):
    try:
        text = " ".join(messages)
        summary = await summarizer(text)
        summarized_messages[number] = summary
        return {'number':number, 'body':summary}
    except Exception as e:
        summarized_messages[number] = {"error": str(e)}
