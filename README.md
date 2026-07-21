# Enterprise AI Assistant

A production-oriented AI Assistant built using **Python**, **LangChain**, and modern LLM engineering practices.

This project is designed to learn and implement Generative AI and Agentic AI concepts by building a real-world application from the ground up. Every component is developed in phases with a focus on clean architecture, modularity, maintainability, and scalability.

---

## Project Goals

- Learn LangChain from fundamentals to advanced concepts.
- Build production-quality AI applications instead of tutorial projects.
- Apply software engineering best practices in AI development.
- Create a modular architecture that supports future expansion.

---

## Features

- Modular project architecture
- Environment-based configuration
- Multiple LLM provider support
- Centralized model management
- Prompt engineering workflow
- Message-based conversations
- Structured outputs
- Memory management
- RAG integration
- Vector Database support
- Agentic AI workflows
- Human-in-the-Loop support
- Middleware architecture
- Logging and debugging
- Production-ready project structure

---

## Project Structure

```text
enterprise-ai-assistant/

├── app/
│
├── agents/
├── llms/
├── memory/
├── middleware/
├── parsers/
├── prompts/
├── rag/
├── tools/
├── utils/
├── vectorstore/
│
├── config.py
└── __init__.py

├── data/
├── notebooks/
├── tests/

├── .env
├── main.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Technology Stack

- Python 3.10
- LangChain
- LangGraph
- Jupyter Notebook
- UV Package Manager
- Pydantic
- Python Dotenv

---

## Learning Roadmap

The project is implemented incrementally.

### Phase 1

- Configuration Layer
- LLM Layer
- Messages
- Prompt Templates
- Chat Prompt Templates
- LCEL
- Output Parsers

### Phase 2

- Memory
- Checkpointer
- Human-in-the-Loop
- Middleware

### Phase 3

- RAG
- Vector Database
- Retrieval Pipeline

### Phase 4

- AI Agents
- LangGraph
- Multi-Agent Systems
- Deep Agents

### Phase 5

- Guardrails
- LLM Evaluation
- Production Deployment

---

## Getting Started

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd enterprise-ai-assistant
```

Create a virtual environment

```bash
uv venv --python 3.10
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
uv pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## Development Principles

This project follows a modular architecture where every component has a single responsibility.

- Configuration is centralized.
- Models are initialized through a factory.
- Business logic is separated from infrastructure.
- Components are reusable and maintainable.
- The project is designed for scalability.

---

## Current Progress

- Configuration Layer
- LLM Factory
- Model Providers
- Environment Management

Additional modules will be implemented in future phases.

---

## Future Enhancements

- Conversation Memory
- Prompt Templates
- Chat Prompt Templates
- LCEL Pipelines
- Output Parsers
- Retrieval-Augmented Generation
- Vector Database Integration
- AI Agents
- LangGraph Workflows
- Human Approval System
- Guardrails
- Evaluation Framework
- Deployment

---

## License

This project is intended for educational and learning purposes.