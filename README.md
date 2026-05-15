# AI Agent Workflow Application

## Overview

This project is a simple AI-powered workflow automation system built using Streamlit and OpenRouter LLM APIs.

The application accepts business requests as input and processes them through multiple workflow stages including:

- Request Classification

- Information Extraction

- Validation

- Priority Assessment

- Recommended Next Action

The system combines LLM-based natural language understanding with rule-based workflow automation.

---

## Features

- Streamlit-based user interface

- LLM-powered request classification

- LLM-powered structured information extraction

- Rule-based validation

- Priority and risk assessment

- Recommended workflow actions

- Workflow trace visualization

- Environment variable support for API security

- Basic error handling

---

## Supported Request Types

The application can process requests such as:

- Refund Requests

- Support Issues

- Contract Review Requests

- Invoice Queries

- General Business Requests

---

## Workflow Architecture

```text

User Input

   ↓

Request Classification (LLM)

   ↓

Information Extraction (LLM)

   ↓

Validation

   ↓

Priority Assessment

   ↓

Recommended Action

   ↓

Workflow Result Display

```

---

## Tech Stack

- Python

- Streamlit

- OpenRouter API

- GPT-3.5 Turbo

- python-dotenv

---

## Setup Instructions

### 1. Clone Repository

```bash

git clone [https://github.com/Rxdmmr/ai-agent-workflow-app.git](https://github.com/Rxdmmr/ai-agent-workflow-app.git)

cd ai-agent-workflow-app

```

---

### 2. Create Virtual Environment

```bash

python3 -m venv venv

source venv/bin/activate

```

---

### 3. Install Dependencies

```bash

pip install -r requirements.txt

```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env

OPENROUTER_API_KEY=your_api_key_here

```

---

### 5. Run Application

```bash

streamlit run [app.py](http://app.py)

```

---

## Sample Workflow

Input Request

→ Request Classification

→ Information Extraction

→ Validation

→ Priority Assessment

→ Recommended Action

→ Workflow Result Display

---

## Security Notes

- API keys are not committed to the repository

- `.env.example` is included for reference

- Sensitive credentials are managed using environment variables

---

## Future Improvements

Possible future enhancements include:

- Database integration

- Multi-user authentication

- File upload support

- Dashboard analytics

- Advanced risk scoring

- Workflow history tracking

- Email notification integration

