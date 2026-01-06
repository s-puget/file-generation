# 📄 AI File Generator API

Hi! Welcome to my AI File Generator project.  
This project explores how large language models can be used not only to generate content, but also to **produce structured execution plans (tool use)** that drive programmatic file creation.

The goal is to combine:
- **LLM-powered content generation**
- **Tool use via structured execution steps**
- **Programmatic file creation**
- **A simple FastAPI interface**

---

## 🚀 Project Description

The AI File Generator is built around a modular Python backend that leverages OpenAI’s GPT models to transform natural language instructions into structured files such as DOCX and Excel documents.

Instead of directly generating files from raw text, the system uses a **tool-based approach**:

1. An LLM generates structured content (e.g. markdown) from user instructions (specifically for DOCX documents).
2. A second LLM call converts that content into a **structured execution plan** describing which file-generation functions to call and with which arguments.
3. File-specific generators interpret this plan and execute the corresponding **tools** (e.g. add headers, formatted text, bullet points, add sheet, add row) to build the final file programmatically.

The project exposes this functionality through a FastAPI endpoint, allowing users to generate and download files directly via an API call.

---

## 🗂️ Project Structure

```text
src
├─ api
│  ├─ main.py
│  ├─ routes.py
│  └─ schemas.py
├─ generators
│  ├─ base_file_generator.py
│  ├─ docx_file_generator.py
│  └─ excel_file_generator.py
├─ prompts
│  ├─ docx_file_generation_prompts.py
│  └─ excel_file_generation_prompts.py
```

## ⚙️ Running the Project

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/file-generation.git
cd file-generation
```

2️⃣ Create a Virtual Environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Set Up OpenAI API Key
Create a `.env` file in the project root and add:
```python
OPENAI_API_KEY=your_openai_api_key_here
```

## ▶️ Usage

Start the FastAPI server:
```bash
python -m uvicorn src.api.main:app --reload
```
Then open `http://127.0.0.1.8000/docs` on your browser. This will open an interactive API documentation on which users can create documents.

## Example API request

```
{
  "file_type": "excel", --> can be "docx" or "excel"
  "instructions": "Create an Excel file with two sheets: one with values and their squares, and one with countries and capitals." --> intructions for file generation 
}
```

## ✨ Supported File Types

- 📄 DOCX (Word documents)
- 📊 Excel (XLSX)

The architecture is designed to easily support additional file formats.

## 🧠 Possible Extensions

- Add support for **PDF or PowerPoint** generation
- Add **async/background** file generation
