from openai import AsyncOpenAI
from dotenv import load_dotenv
import panel as pn
import os
import asyncio

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)

pn.extension()

# Define the initial context with the system prompt for the OrderBot role
context = [{'role':'system', 'content':"""
Act as an OrderBot, you work collecting orders in a delivery-only fast food restaurant called
My Dear Frankfurt. First welcome the customer, in a very friendly way, then collect the order. 
You wait to collect the entire order, beverages included, then summarize it and check for a final 
time if everything is ok or the customer wants to add anything else. Finally, you collect the payment.
Make sure to clarify all options, extras, and sizes to uniquely identify the item from the menu.
You respond in a short, very friendly style. The menu includes:

burger  12.95, 10.00, 7.00
frankfurt   10.95, 9.25, 6.50
sandwich   11.95, 9.75, 6.75
fries 4.50, 3.50
salad 7.25
Toppings:
extra cheese 2.00
mushrooms 1.50
martra sausage 3.00
canadian bacon 3.50
romesco sauce 1.50
peppers 1.00
Drinks:
coke 3.00, 2.00, 1.00
sprite 3.00, 2.00, 1.00
vichy catalan 5.00
"""}]

async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    # Add the user's message to the context
    context.append({'role': 'user', 'content': contents})
    
    # Generate a response using the existing context
    response = await aclient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=context,
        stream=True,
    )

    message = ""
    async for chunk in response:
        part = chunk.choices[0].delta.content
        if part is not None:
            message += part
            yield message

 context.append({'role': 'assistant', 'content': message})

    yield message

def main():
    chat_interface = pn.chat.ChatInterface(
        callback=callback,
        callback_user="OrderBot",
        help_text="Welcome to My Dear Frankfurt! How can I help you with your order today?",
    )
    
    template = pn.template.FastListTemplate(
        title="OpenAI OrderBot",
        header_background="#212121",
        main=[chat_interface]
    )

    template.servable()
    pn.serve(chat_interface, show=True)


if __name__ == "__main__":
    main()

