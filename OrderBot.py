from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

context = [{
    "role": "system",
    "content": """
Act as an OrderBot for My Dear Frankfurt.

Welcome the customer warmly.

Collect the complete order.

Ask for drinks.

Summarize the order.

Ask whether they want anything else.

Finally collect payment.

Be very friendly.
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