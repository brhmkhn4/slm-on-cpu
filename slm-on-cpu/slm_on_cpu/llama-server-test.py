import requests
import json
from typing import List, Dict

# headers = {"Content-Type": "application/json"}

prompt = {"prompt":"Building a website can be done in 10 simple steps"}

# # Function to send a request to the server and get a response
# def get_response(
#     server_url: str,
#     messages: List[Dict[str, str]],
#     temperature: float = 0.7,
#     top_p: float = 0.9,
#     max_tokens: int = 2000,
#     stream: bool = True,
# ) -> str:
#     headers = {"Content-Type": "application/json"}
#     data = {
#         "messages": messages,
#         "temperature": temperature,
#         "top_p": top_p,
#         "max_tokens": max_tokens,
#         "stream": stream,
#     }



async def test():
    response = requests.post(
        "http://127.0.0.1:8080/completion",                     
         data=prompt
         headers = "Content-Type": "application/json"
        )
response = test()
print(response)