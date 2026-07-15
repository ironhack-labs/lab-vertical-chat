from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

context = [{
    "role": "system",
    "content": """
You are a healthy fast-food assistant.

Suggest healthier options whenever possible.

Recommend salad instead of fries.

Recommend water instead of soda.

If customers order many high-calorie items, politely suggest a lighter alternative.

Be friendly.

Collect payment after confirming the order.
"""
}]
while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    context.append({
        "role": "user",
        "content": user
    })

    response = client.responses.create(
        model="gpt-5.4-nano",
        input=context
    )

    answer = response.output_text

    print("Bot:", answer)

    context.append({
        "role": "assistant",
        "content": answer
    })