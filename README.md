# 🤖 Multi-Agent AI Researcher

A powerful **Multi-Agent AI Research Assistant** built with **Python, Streamlit, and Agno** that automates research by coordinating multiple AI agents. The application researches Hacker News stories, performs live web searches, extracts article content, and generates comprehensive research reports using modern Large Language Models.

---

## 🚀 Features

* 🔍 Multi-Agent AI architecture
* 📰 Research top Hacker News stories
* 🌐 Real-time web search integration
* 📄 Automatic article extraction and summarization
* 🧠 AI-generated research reports
* 💬 Interactive Streamlit user interface
* 🔑 Supports Groq API (Free Tier)
* ⚡ Powered by Agno Agent Framework

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Agno
* Groq API
* DuckDuckGo Search
* Newspaper4k
* Hacker News API

---

## 📂 Project Structure

```text
multi_agent_researcher/
│── research_agent.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-ai-researcher.git

cd multi-agent-ai-researcher
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

Install additional dependencies

```bash
pip install ddgs newspaper4k lxml_html_clean
```

---

## 🔑 Configure Groq API

Create a free Groq API key:

https://console.groq.com/keys

Enter your API key in the application when prompted.

---

## ▶️ Run the Application

```bash
streamlit run research_agent.py
```

---

## 🧠 How It Works

The application creates a team of intelligent AI agents that collaborate to perform research.

### 🔹 HackerNews Researcher

* Finds relevant Hacker News stories
* Retrieves story metadata

### 🔹 Web Search Agent

* Searches the web for additional information
* Collects recent updates and references

### 🔹 Article Reader

* Extracts article content
* Cleans and summarizes webpages

### 🔹 Research Team

Coordinates all agents and generates:

* Research Reports
* Blog Content
* Summaries
* Reference Links

---

## 📸 Demo

Add screenshots of the application here.

---

## Future Improvements

* PDF Export
* Chat History
* Research Memory
* Multi-LLM Support
* RAG-based Document Search
* Report Download
* Citation Generation

---

## License

This project is intended for educational and research purposes.

---

## Acknowledgement

This project is inspired by the excellent **awesome-llm-apps** repository by **Shubham Saboo**. It has been modified and customized with additional setup changes and support for alternate LLM providers.
