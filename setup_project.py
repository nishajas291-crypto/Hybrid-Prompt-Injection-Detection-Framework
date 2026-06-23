import os

# Folder structure
folders = [
    "secure_llm_assistant",
    "secure_llm_assistant/templates",
    "secure_llm_assistant/static"
]

# Files with basic content
files = {
    "secure_llm_assistant/app.py": "",
    "secure_llm_assistant/security.py": "",
    "secure_llm_assistant/logger.py": "",
    "secure_llm_assistant/requirements.txt": "flask\nopenai\n",
    "secure_llm_assistant/templates/index.html": "",
    "secure_llm_assistant/static/style.css": "",
    "secure_llm_assistant/static/script.js": ""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ secure_llm_assistant project structure created successfully!")
