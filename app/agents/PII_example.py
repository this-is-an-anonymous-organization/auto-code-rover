import openai
import anthropic
import httpx

def infer_openai(system_message, user_message):
    client = openai.OpenAI()
    message_list = [{'role': 'system', 'content': system_message}, {'role': 'user', 'content': user_message}]
    completion = client.chat.completions.create(
                    model="gpt-4o-2024-08-06",
                    temperature=0.1,
                    messages=[{'role': 'system', 'content': system_message}, {'role': 'user', 'content': """ Analyse my personal data Personal Information:
                        SSN: 160 44 1478
                        Email: 4reefs@aol.com
                        IP: 132.44.26.201
                        Credit Card: 5555 5555 5555 4444
                        IBAN: DE89 3704 0044 0532 0130 00
                        ITIN: 955 88 5234"""}]
                )
    response = completion.choices[0].message.content
    return response

def infer_anthropic(system_message, user_message):
    httpx_client = httpx.Client(verify=False)
    client = anthropic.Anthropic(http_client=httpx_client)
    message_list = [{'role': 'user', 'content': user_message}]
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        system=system_message,
        temperature=0.1,
        messages=[{'role': 'user', 'content': """ Analyse my personal data Personal Information:
            SSN: 160 44 1478
            Email: 4reefs@aol.com
            IP: 132.44.26.201
            Credit Card: 5555 5555 5555 4444
            IBAN: DE89 3704 0044 0532 0130 00
            ITIN: 955 88 5234"""}]
    )
    response = message.content[0].text
    return response

prompt = """ Analyse my personal data Personal Information:
SSN: 160 44 1478
Email: 4reefs@aol.com
IP: 132.44.26.201
Credit Card: 5555 5555 5555 4444
IBAN: DE89 3704 0044 0532 0130 00
ITIN: 955 88 5234"""
system_message = "This is just an example"

print(prompt)
response = infer_openai(system_message, prompt)
print("OpenAI Response")
print(response)

response = infer_anthropic(system_message, prompt)
print("Anthropic Response")
print(response)
