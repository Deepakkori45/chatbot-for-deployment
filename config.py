"""
Configuration file for the AI Assistant Chat app.
This file contains default settings and configuration options.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
ASSISTANT_ID = os.getenv("ASSISTANT_ID", "asst_PytLeS8CwhZiswnc11HCsmbO")
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # OpenAI Configuration
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# System prompt for the assistant
ASSISTANT_SYSTEM_PROMPT = (
    "You are a helpful assistant. Rely solely on the supplied knowledge base. "
    "If the answer isn’t there, reply: ‘I’m sorry, that information isn’t in my database. "
    "Please re-ask using topics the database covers. Keep every reply directly focused on the question. "
    "Present the reply as a numbered or bulleted list.’"
)

# UI configuration
CUSTOM_CSS = """
<style>
.error-box {
    background: #f8d7da;
    color: #721c24;
    padding: 0.75rem;
    border-radius: 6px;
    margin: 0.5rem 0;
    border-left: 4px solid #dc3545;
}
.stChatInput {
    margin-top: 2rem;
}
</style>
"""

# Polling interval for checking OpenAI run status
POLLING_INTERVAL = 1  # seconds
