import aiohttp
import os

# loading Wolfram token safely without exposing them.
app_id = os.getenv('WOLFRAM_APP_ID')

async def get_response(user_input: str) -> str:
    api_url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": user_input,
        "format": "plaintext",
        "output": "JSON",
        "appid": app_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    # extracting the "right response" for the user 
                    result = data['queryresult']['pods'][1]['subpods'][0]['plaintext']
                    return result
                except (KeyError, IndexError):
                    # if a response couldn't be found...
                    return "I couldn't find an answer to that."
            else:
                return "There was an error processing your request."
