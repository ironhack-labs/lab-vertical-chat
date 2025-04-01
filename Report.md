# Report: Evaluation of GPT-Based Prompts

## Introduction

In this project, we tested three different prompts with OpenAI's GPT-3.5-turbo model to evaluate its ability to handle various tasks. The prompts were designed to simulate real-world applications: an **OrderBot** for a fast food restaurant, a **Flight Ticket Booking Summary**, and a **General Conversation**. Our goal was to assess how effectively GPT can adapt to different contexts and the accuracy of its responses.

## Methodology

We implemented three distinct prompts and utilized the `continue_conversation` function to interact with GPT. Each prompt served a different purpose:

- **OrderBot**: Collecting and finalizing a customer's order.
- **Flight Ticket Booking**: Generating a structured summary for flight bookings.
- **General Conversation**: Engaging in casual, friendly interactions with users.

## Results

### OrderBot:
- **Strengths**: GPT was able to simulate a coherent, friendly conversation and gather information such as food orders, sizes, and drinks. It followed the sequence of collecting orders, confirming, and finalizing payments effectively.
- **Challenges**: Repeated questions and occasional failure to clarify ambiguous requests (e.g., missing toppings) were issues that could affect the user experience.

### Flight Ticket Booking:
- **Strengths**: GPT successfully generated clear, structured summaries for flight bookings, detailing passenger info, flight schedules, and ticket prices as required.
- **Challenges**: There were occasional formatting issues and missing details, such as incomplete JSON or omitted flight information.

### General Conversation:
- **Strengths**: GPT maintained a friendly and concise tone, handling a range of casual queries effectively.
- **Challenges**: Responses were sometimes overly generic or shallow, particularly when faced with vague or broad questions.

## Challenges & Limitations

- **Hallucinations**: GPT occasionally generated incorrect or fabricated details, especially when the prompt was unclear or too complex.
- **Repetitiveness**: In longer conversations or unclear inputs, GPT repeated certain questions or responses, which could lead to frustration.
- **Ambiguity**: When the prompts were not fully specific, GPT struggled to provide precise or detailed answers.

## Conclusion

The experiments revealed that GPT performs well in structured tasks but faces limitations when dealing with ambiguity or complex data. While it adapts well to casual conversations and simple tasks like order-taking, its accuracy diminishes with more intricate details or unclear inputs. To improve performance, prompts should be clear, specific, and detailed.
