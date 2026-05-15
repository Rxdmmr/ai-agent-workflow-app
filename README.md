# AI Agent Workflow Application

## Overview

This project is a simple AI-powered workflow automation application built using Streamlit and OpenRouter LLM APIs.

The application accepts business requests as input and processes them through multiple workflow stages including:

- Request Classification

- Information Extraction

- Validation

- Priority Assessment

- Recommended Next Action

## Features

- Streamlit-based UI

- LLM-powered request classification

- LLM-powered structured information extraction

- Rule-based validation

- Priority/risk assessment

- Workflow trace display

- Environment variable support for API security

## Tech Stack

- Python

- Streamlit

- OpenRouter API

- GPT-3.5 Turbo

- dotenv

## Setup Instructions

### 1. Clone Repository

```bash

git clone <your_repo_url>

cd ai_workflow_app

```

### 2. Create Virtual Environment

```bash

python3 -m venv venv

source venv/bin/activate

```

### 3. Install Dependencies

```bash

pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create `.env` file:

```env

OPENROUTER_API_KEY=your_api_key_here

```

### 5. Run Application

```bash

streamlit run [app.py](http://app.py)

```

## Sample Workflow

Input Request

→ Classification

→ Information Extraction

→ Validation

→ Priority Assessment

→ Recommended Action

## Notes

- API keys are not committed to the repository.

- `.env.example` is included for reference.