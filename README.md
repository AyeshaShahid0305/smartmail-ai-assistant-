# AI Email Assistant

AI Email Assistant is a simple GenAI-powered app that helps users generate professional emails from short bullet points or brief instructions. It takes a few inputs such as purpose, receiver, tone, and key points, then produces a polished email with a subject line, a short version, and an improved version.

## What It Does

The user enters:

- Purpose of the email
- Receiver
- Tone
- Key points

The AI generates:

- A professional email
- A subject line
- A short version
- An improved version

## Features

### Basic Version

- Generate emails from bullet points
- Rewrite emails professionally
- Change tone to:
  - Formal
  - Friendly
  - Professional
  - Apologetic
- Fix grammar and improve clarity
- Generate subject lines automatically

### Example Use Cases

- Sending a repository update to a supervisor
- Writing a leave request to a manager
- Rephrasing a rough draft into a professional message
- Improving grammar and tone in an existing email

## Tech Stack

| Part | Tool |
|---|---|
| Language | Python |
| UI | Streamlit |
| AI | OpenAI API |
| Environment | python-dotenv |

## How It Works

When the user enters a short request, the backend builds a prompt and sends it to the OpenAI API.

Example:

```text
Write a professional email.

Recipient: Manager

Purpose: Leave Request

Requirements:
- Be polite
- Keep under 150 words
- Include subject
- Include greeting
- Include closing
```

The AI then returns a complete email response based on the selected tone and requirements.

## Example Input

- Purpose: Need one day leave
- Receiver: Manager
- Tone: Professional
- Points:
  - I need leave for one day
  - I am requesting approval in advance
  - I will complete my pending work before leaving
  - Please consider my request
  - Thank you for your understanding

## Example Output

**Subject:** Leave Request

**Email:**

Dear Manager,

I hope you are doing well.

I am writing to request one day leave. I need this leave for personal reasons and would appreciate your approval.

I will make sure to complete my pending tasks before taking the day off.

Thank you for your consideration.

Best regards,  
Your Name

## Why This Shows GenAI Ability

- Prompt engineering
- LLM API integration
- Text generation
- Tone transformation
- Grammar correction
- Structured output generation
- User input handling

## CV Description

Developed an AI Email Assistant using Python, Streamlit, and the OpenAI API to generate professional emails from user-provided bullet points. Implemented prompt engineering techniques to support tone customization, grammar correction, subject line generation, and email rewriting for different communication contexts.

## Folder Structure

```text
ai-email-assistant/
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## Future Improvements

- Add email templates for common scenarios
- Support multiple languages
- Allow downloadable output
- Save generated emails in history
- Add copy-to-clipboard functionality
