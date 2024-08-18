from openai import OpenAI
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful virtual assistant named Jarvis skilled in general tasks like Alex, Siri and Google assistant."},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message)