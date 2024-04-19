import os
import openai

openai.api_key = YourAPIKey

prompt = input("Enter your prompt: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or another chat model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message['content'])
print("\nComplete response message:\n")
print(response)

prompt = input("\nEnter a string for sentiment analysis: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or another chat model
    messages=[
        {"role": "system", "content": "Classify user messages as positive or negative sentiment."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message['content'])
print("\nComplete response message:\n")
print(response)