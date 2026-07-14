# AI Email Assistant

AI Email Assistant is a simple GenAI app that turns short user notes into polished professional emails. It helps users write faster by generating a subject line, a well-structured email, and a cleaner version of the message from a few basic inputs.

## Overview

Users provide:

- Purpose of the email
- Receiver
- Sender role
- Sender name
- Tone
- Key points

The app generates:

- Subject line
- Professional email
- Short version
- Improved version

## Features

- Generate an email from short bullet points
- Rewrite text in a professional tone
- Support different tones:
  - Formal
  - Friendly
  - Professional
  - Apologetic
- Fix grammar and spelling
- Generate a subject line automatically
- Copy generated text with one click
- Download the result as a PDF

## Tech Stack

| Part | Tool |
|---|---|
| Language | Python |
| UI | Streamlit |
| AI | OpenAI API |
| Environment | python-dotenv |

## Example

**Input**

- Purpose: Leave request
- Receiver: Manager
- Sender role: Student
- Sender name: Ayesha
- Tone: Professional
- Key points:
  - Need one day leave
  - Requesting approval in advance
  - Will complete pending work before leaving

**Output**

- Subject line: Leave Request
- Professional email: a polished leave request email
- Short version: a compact version for quick use
- Improved version: a cleaner rewritten version

## How It Works

1. The user enters a short prompt and selects a tone.
2. The app builds a structured prompt.
3. OpenAI generates the email content.
4. The user can copy the output or download it as a PDF.

## Local Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

## Project Structure

```text
ai-email-assistant/
├── app.py
├── preview.html
├── requirements.txt
├── .env.example
└── README.md
```

## Why This Project Matters

- Shows practical prompt engineering
- Demonstrates OpenAI API integration
- Solves a real communication task
- Presents a simple but useful GenAI workflow

## Future Improvements

- Add more tone options
- Save email history
- Add email templates
- Support multiple languages
- Improve PDF styling

