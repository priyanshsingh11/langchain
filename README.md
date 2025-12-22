# LangChain – Core Concepts & Revision Notes

This repository contains **revision notes and practice code for LangChain**.
The focus is on **understanding concepts clearly**, not building complex systems.

---

## What is LangChain?

**LangChain** is a framework used to **build applications powered by Large Language Models (LLMs)**.

It helps you:
- Connect LLMs with external data
- Control how prompts are sent
- Chain multiple steps together
- Parse and structure LLM outputs

LangChain does **not train models** — it **orchestrates** them.

---

## Core Components of LangChain

LangChain is mainly built from the following components:

- **Models**
- **Prompts**
- **Chains**
- **Output Parsers**
- **Memory**
- **Tools**
- **Agents** (advanced)

You usually start with **Models → Prompts → Chains → Parsers**.

---

## Models

Models are the **LLMs** used to generate responses.

Examples:
- OpenAI models
- Hugging Face models
- Local models (via Ollama, etc.)

Important points:
- LangChain only **calls** models, it does not train them
- Models can be:
  - Chat models
  - Text completion models

You control:
- Model type
- Temperature
- Max tokens
- API provider

---

## Temperature (temp)

**Temperature controls randomness of output.**

- `temp = 0.0` → Very deterministic, factual
- `temp = 0.7` → Balanced responses
- `temp = 1.0+` → Creative, more randomness

Use cases:
- Low temp → QA systems, factual answers
- Medium temp → Chatbots
- High temp → Creative writing

**Important:**  
Lower temperature = more reliable output

---

## Prompts

Prompts define **what you ask the model**.

LangChain allows:
- Prompt templates
- Variable injection
- Structured prompts

Example idea:
- Input variables → formatted prompt → model

Prompts are **critical** because LLMs respond based on instructions.

---

## Chains

**Chains are the backbone of LangChain.**

A chain is:
> **Prompt → Model → Output**

Types:
- Simple chain (single step)
- Sequential chain (multiple steps)
- Custom chains

Why chains matter:
- They define **workflow**
- They make logic reusable
- They connect multiple operations

**Without chains, LangChain has no flow.**

---

## Output Parsers

LLMs return **unstructured text**.  
Output parsers convert it into **structured data**.

Examples:
- JSON parser
- String parser
- Custom format parser

Why parsers are important:
- Used in production systems
- Reduce hallucination
- Make outputs machine-readable

**Always use parsers when structure matters.**

---

## Memory

Memory allows the system to **remember past interactions**.

Examples:
- Conversation history
- Session memory

Use cases:
- Chatbots
- Assistants
- Multi-turn conversations

Without memory:
- Each request is independent

---

## Tools

Tools allow LLMs to:
- Call APIs
- Run functions
- Access external systems

Examples:
- Search tools
- Database queries
- Custom Python functions

Tools extend LLM capability beyond text.

---

## Agents (Advanced)

Agents decide **which action to take next**.

They can:
- Choose tools
- Plan steps
- Execute reasoning loops

Agents are powerful but:
- Harder to control
- More expensive
- Not always needed

**Start with chains before agents.**

---

## When to Use LangChain

Use LangChain when:
- You need multi-step LLM logic
- You want structured outputs
- You are building AI workflows

Do NOT use LangChain when:
- A single API call is enough
- Logic is very simple

---

## Summary (Very Important)

- LangChain orchestrates LLMs
- Models generate text
- Prompts guide behavior
- Chains define workflow
- Temperature controls randomness
- Parsers structure output
- Memory handles context
- Agents are optional and advanced

---

## Status

Learning and revision in progress.
