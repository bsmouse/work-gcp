import os
import openai

# openai.organization = "org-kKd2RYxKu2zAcqTGE1to8zxP"
openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant",
#             "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="What's new in Korea?",
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

# print(response)
print(response.choices[0].text)
