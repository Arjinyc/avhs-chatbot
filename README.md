# AVHS Chatbot

A simple Flask chatbot that answers questions about Amador Valley High School using information collected from the official AVHS website.

## Requirements

- Python 3.10 or newer
- An OpenAI API key

## Run locally

1. Clone this repository and enter the project folder.
2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:

   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

5. Start the app:

   ```bash
   python app.py
   ```

6. Open http://localhost:8080.

## Security

Never place an API key directly in the code or commit a `.env` file. The application reads `OPENAI_API_KEY` from the environment.

## Data note

`school_data.txt` contains a snapshot of publicly available information from the official AVHS website. School information can change, so refresh this file periodically.

## Disclaimer

This is an independent student project and is not an official Amador Valley High School or Pleasanton Unified School District service.
