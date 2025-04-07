import streamlit as st
from job_scraper import scrape_job_description
from cv_extractor import extract_text_from_pdf
from email_generator import generate_cold_email
from chromadb import Client
from chromadb.config import Settings
import datetime

chroma_client = Client(Settings(
    persist_directory="./chromadb_storage",
    anonymized_telemetry=False
))

collection_name = "previous_cold_emails"
email_collection = chroma_client.get_or_create_collection(collection_name)

st.title("Cold Emails")

job_url = st.text_input("Enter Job URL:")
portfolio_link = st.text_input("Enter CV Link:")
user_name = st.text_input("Enter Your Name:")
driver_path = "C:/Users/HP/Downloads/chromedriver-win64/chromedriver.exe"

def store_cold_email(email_content, job_title):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = f"{job_title}_{timestamp}"
    email_collection.add(
        documents=[email_content],
        metadatas=[{"job_title": job_title, "timestamp": timestamp}],
        ids=[unique_id]
    )

def fetch_previous_emails():
    try:
        all_emails = email_collection.get(include=["documents", "metadatas"])
        previous_emails = [{"content": doc, "metadata": meta} for doc, meta in zip(all_emails["documents"], all_emails["metadatas"])]
        return previous_emails
    except Exception as e:
        st.error(f"Error fetching previous emails: {e}")
        return []

if job_url and portfolio_link and user_name:
    st.write("Fetching data")
    job_description, job_title = scrape_job_description(job_url, driver_path)
    cv_text = extract_text_from_pdf(portfolio_link)

    if job_description and cv_text:
        cold_email = generate_cold_email(job_title, job_description, cv_text)
        cold_email = cold_email.replace("[Your Name]", user_name)
        store_cold_email(cold_email, job_title)
        st.text_area("Cold Email", cold_email, height=250)
    else:
        st.error("ERROR!")
else:
    st.info("Please fill out all the fields to proceed.")

st.subheader("Previous Cold Emails")
previous_emails = fetch_previous_emails()

if previous_emails:
    selected_email = st.selectbox(
        "Select a previously generated email:",
        options=[f"{email['metadata']['job_title']} - {email['metadata']['timestamp']}" for email in previous_emails]
    )

    for email in previous_emails:
        if f"{email['metadata']['job_title']} - {email['metadata']['timestamp']}" == selected_email:
            st.text_area("Previously Generated Cold Email", email["content"], height=250)
else:
    st.info("No previous cold emails found.")
