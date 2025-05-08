# 🧠 Multi-Agent Financial News System

A modular AI-powered system that leverages multiple LLM agents to deliver real-time market insights for traders and investors. Built using **Agno** and **Agent UI**, the system combines sentiment analysis, financial data retrieval, and web-based market research.

---

## 🚀 Features

- **News Sentiment Analysis**  
  Analyze global financial headlines and rate their sentiment to identify potential trading signals.

- **Real-Time Financial Data**  
  Retrieve live stock prices, financial ratios, and company fundamentals to support investment decisions.

- **Web-Based Market Research**  
  Search and summarize relevant market news and historical data using LLM agents.

- **Integrated Financial Intelligence**  
  A combined agent integrates all services to provide plain-language explanations and strategic market insights.

---

## 🧩 Agent Architecture

Built using the Agno framework, the system follows a modular agent architecture:

- **Agent/Brain**: LLM core responsible for decision-making  
- **Planning**: Task strategy formulation  
- **Memory**: Conversation history and context retention  
- **Tool Use**: Interfacing with external APIs (news, stock market, web)

---

## 🛠 Setup Instructions

### 1️⃣ Backend Setup with Agno

- Clone the project repository.
- Configure your agent in `agent.yaml`.
- Set up environment variables in `.env` (e.g., API keys).

```bash
git clone https://github.com/your-repo/financial-agent-system.git
cd financial-agent-system
cp .env.example .env
# Add your API keys to .env
