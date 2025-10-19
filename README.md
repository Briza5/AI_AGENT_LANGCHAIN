# Smart Todoist Agent

A conversational AI agent for managing Todoist tasks using natural language commands. Built with LangChain, Google Gemini 2.5 Flash, and the Todoist API.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (recommended)
- API keys for Gemini and Todoist

### Installation

1. Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory with your API keys:

```env
TODOIST_API_TOKEN=<YOUR_TODOIST_API_TOKEN>
GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
```

#### How to obtain API keys:

| Key | Purpose | Source |
|-----|---------|--------|
| `GEMINI_API_KEY` | Access to Google Gemini model | [Google AI Studio](https://aistudio.google.com) |
| `TODOIST_API_TOKEN` | Access to your Todoist task list | Todoist Settings → Integrations |

### Running the Agent

Start the interactive chat loop:

```bash
python main.py
```

The program will launch an interactive session. Currently configured for Czech input due to the system prompt.

## 🧠 Agent Capabilities

The agent uses LangChain's `AgentExecutor` to maintain conversation history and interact with Todoist through specialized tools.

### Available Tools

| Function | Description | Usage |
|----------|-------------|-------|
| `add_task(task, desc=None)` | Add a task to your Todoist list | When you want to create a new task |
| `show_tasks()` | Display all tasks from Todoist | When you want to see your current tasks |

### Example Commands

Input is expected in Czech:

| Input | Translation | Agent Action |
|-------|-------------|--------------|
| `Ukaž mi, co mám dnes za úkoly.` | Show me my tasks for today. | Calls `show_tasks()` |
| `Přidej: nakoupit chleba a mléko.` | Add: buy bread and milk. | Calls `add_task()` |
| `Ahoj, jak ti jde přidávání úkolů?` | Hello, how is task adding going? | Conversational response (no tool) |

## 📦 Requirements

All dependencies are specified in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

## 📝 License

[Add your license information here]