## 🧠 Agentic AI Example — LangChain + Anthropic + Tools

This project demonstrates an example of **Agentic AI** built with **LangChain** and **Anthropic Claude 3.5 Sonnet**, capable of performing multiple real-world tasks through tool usage.

### 🚀 Features
- 🔍 **Search the web** using **DuckDuckGo**
- 📘 **Query Wikipedia** for factual information
- 💾 **Save responses** automatically to a file
- 🏷️ **Extract top keywords** from any text (excluding common stopwords)

### 🧩 Tech Stack
- **Python**
- **LangChain Community Tools**
- **Anthropic Claude 3.5 Sonnet**
- **Pydantic** for structured responses
- **dotenv** for environment configuration

### 📖 How It Works
The agent:
1. Receives a user question.  
2. Chooses the best tools dynamically (DuckDuckGo, Wikipedia, etc.).  
3. Generates a structured response using the `QuestionResponse` model.  
4. Extracts important keywords and saves everything to a local file.

### ▶️ Tutorial
Full walkthrough and explanation available on YouTube:  
👉 [Agentic AI Tutorial — LangChain + Anthropic](https://www.youtube.com/watch?v=bTMPwUgLZf0&t=2s)
