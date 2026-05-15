import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

st.title("AI Agent Workflow Application")

request_text = st.text_area("Enter Business Request")


def classify_request(text):

    prompt = f"""
    Classify this request into one category:
    - Refund Request
    - Support Issue
    - Contract Review
    - Invoice Query
    - Other

    Request:
    {text}

    Return only the category name.
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:

        return f"LLM Error: {str(e)}"


def extract_information(text):

    prompt = f"""
    Extract the following fields from this request:

    - customer_name
    - invoice_id
    - payment_reference
    - amount
    - email
    - issue_summary

    Return ONLY valid JSON.

    Request:
    {text}
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        cleaned_text = response.choices[0].message.content.strip()

        cleaned_text = cleaned_text.replace("```json", "").replace("```", "")

        data = json.loads(cleaned_text)

        return data

    except Exception as e:

        return {"error": str(e)}


def validate_information(data):

    required_fields = ["customer_name", "email"]

    missing = []

    for field in required_fields:

        if field not in data or not data[field]:

            missing.append(field)

    if missing:

        return f"Incomplete Request. Missing: {', '.join(missing)}"

    return "Request Complete"


def assess_priority(data):

    amount = data.get("amount", "")
    issue = str(data.get("issue_summary", "")).lower()

    try:

        amount_number = int(
            ''.join(filter(str.isdigit, str(amount)))
        )

        if amount_number > 40000:
            return "High Priority"

    except:
        pass

    urgent_keywords = [
        "urgent",
        "failed",
        "outage",
        "critical"
    ]

    for word in urgent_keywords:

        if word in issue:
            return "High Priority"

    return "Normal Priority"

def recommend_action(request_type):

    actions = {
        "Refund Request": "Forward to Finance Team",
        "Support Issue": "Assign to Technical Support",
        "Contract Review": "Forward to Legal Team",
        "Invoice Query": "Forward to Billing Team",
        "Other": "Manual Review Required"
    }

    return actions.get(
        request_type,
        "Manual Review Required"
    )


if st.button("Process Request"):

    request_type = classify_request(request_text)

    extracted_data = extract_information(request_text)

    validation_result = validate_information(extracted_data)

    priority = assess_priority(extracted_data)

    action = recommend_action(request_type)

    st.subheader("Workflow Result")

    st.write("### Request Type")
    st.write(request_type)

    st.write("### Extracted Information")
    st.json(extracted_data)

    st.write("### Validation")
    st.write(validation_result)

    st.write("### Priority")
    st.write(priority)

    st.write("### Recommended Action")
    st.write(action)

    st.write("### Workflow Trace")

    st.write("""
    Input Received
    → Request Classified
    → Information Extracted
    → Validation Completed
    → Priority Assessed
    → Action Recommended
    """)