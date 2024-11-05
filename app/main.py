import requests
import os
from dotenv import load_dotenv
from app.openai_helper import get_openai_response
from app.m365_helper import authenticate_m365, send_email

load_dotenv()  # Load environment variables

def main():
    m365_auth = authenticate_m365()
    if m365_auth is None:
        print("M365 authentication failed.")
        return

    openai_response = get_openai_response("Write a summary for project updates.")
    print("OpenAI Response:", openai_response)

    email_status = send_email(m365_auth, "example@domain.com", "Project Update", openai_response)
    print("Email sent:", email_status)

if __name__ == "__main__":
    main()
