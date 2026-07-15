# Vertical Chat Lab – Prompt Engineering Report

## Objective

The objective of this lab was to understand how the system prompt influences the behavior of a chatbot using the OpenAI API. I created three different vertical chatbots: a Travel Booking Assistant, a Wellness Support Assistant, and a Parenting Assistant. Although all three used the same GPT model, changing the system prompt resulted in very different conversations and responses.

## Chatbot Variations

### 1. Travel Booking Assistant

The Travel Booking Assistant produced the most structured conversations. It greeted the user, collected the necessary travel information (destination, travel dates, number of travelers, flight class, hotel requirements, and budget), summarized the itinerary, and then asked for confirmation before proceeding. This chatbot closely followed the instructions provided in the prompt and maintained a logical conversation flow.

### 2. Wellness Support Assistant

The Wellness Support Assistant was designed to provide emotional support and general well-being advice. The chatbot was empathetic and asked follow-up questions to better understand the user's concerns before offering suggestions. To reduce the risk of incorrect advice, the prompt instructed the model not to diagnose medical or mental health conditions and to encourage users to seek professional help when appropriate.

### 3. Parenting Assistant

The Parenting Assistant focused on helping parents with common concerns such as discipline, motivation, meal planning, sleep routines, and balancing family life. The chatbot maintained a warm and supportive tone while asking clarifying questions before providing practical parenting suggestions.

## Observations

The quality of the responses depended heavily on how detailed the system prompt was. When the prompt clearly described the chatbot's role, conversation flow, and limitations, the responses were more consistent and relevant. The model also remembered previous messages because the conversation history was stored in the `context` list, allowing it to build on earlier information naturally.

## Variations That Didn't Work Well

Some versions produced less reliable responses when the prompt was too vague or lacked specific instructions. For example, if I did not specify that the chatbot should collect all the necessary information before answering, it sometimes skipped important questions and made assumptions about the user's request.

I also noticed that GPT could occasionally generate information that was not verified, such as suggesting travel details or recommendations without confirming enough information first. Adding instructions like "If you don't know something, do not assume" and "Do not invent prices or availability" reduced these hallucinations and improved the quality of the responses.

## What I Learned

This lab demonstrated that prompt engineering is one of the most important aspects of building conversational AI. The same GPT model can perform very different tasks depending on the instructions provided in the system prompt. I also learned the importance of defining the chatbot's role, specifying a clear conversation flow, setting constraints, and providing safety instructions when appropriate.

Finally, I learned how conversation memory works. By continuously appending the user's messages and the assistant's responses to the `context` list, the chatbot can maintain coherent multi-turn conversations and provide more personalized interactions.
