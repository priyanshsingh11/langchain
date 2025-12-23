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
- **Runnables**
- **Output Parsers**
- **Memory**
- **Tools**
- **Agents** (advanced)

You usually start with:  
**Models → Prompts → Chains / Runnables → Parsers**

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

## Runnables – Types & Patterns (Important)

Runnables are the **core execution units** in modern LangChain.  
They define **how data flows** through prompts, models, parsers, and functions.

A runnable:
> **Takes input → processes it → returns output**

LangChain provides multiple **runnable patterns** depending on the workflow.

---

## 1. Simple / Sequential Runnables

This is the **most basic runnable pattern**.

Flow:
> **Input → Step 1 → Step 2 → Output**

Example idea:
- Prompt → Model → Output Parser

Key points:
- Executes **step by step**
- Output of one step becomes input of the next
- Easy to understand and debug

Use cases:
- Single-task pipelines
- Prompt → LLM → structured output
- Learning and prototyping

This is similar to a traditional chain but **more flexible**.

---

## 2. Runnable Sequence (`|` Operator)

LangChain allows chaining runnables using the pipe (`|`) operator.

Concept:
> **Runnable A | Runnable B | Runnable C**

Why this matters:
- Clean and readable
- Highly modular
- Replaces many older `Chain` patterns

Each component:
- Receives input
- Produces output
- Automatically passes it forward

This is the **recommended default approach** in modern LangChain.

---

## 3. Parallel Runnables

Parallel runnables allow **multiple operations to execute simultaneously**.

Concept:
> **Same input → Multiple runnables → Combined output**

Example idea:
- One runnable summarizes text
- Another extracts keywords
- Both run at the same time

Key points:
- Faster execution
- Tasks are independent
- Output is usually a dictionary

Use cases:
- Feature extraction
- Multi-view analysis
- Running independent LLM calls

---

## 4. Runnable Map (Fan-Out Pattern)

Runnable maps apply **different runnables to different parts of the input**.

Concept:
> **Structured input → Multiple transformations → Structured output**

Example idea:
- `text` → summarization
- `review` → sentiment analysis

Key points:
- Input is usually a dictionary
- Each key is processed independently
- Output preserves structure

Use cases:
- Document pipelines
- Multi-field processing
- Data preprocessing before LLM calls

---

## 5. Runnable Lambda (Custom Logic)

Runnable Lambda allows you to use **custom Python functions** inside a runnable pipeline.

Concept:
> **Input → Python logic → Output**

Key points:
- No LLM involved
- Used for transformation, validation, formatting
- Lightweight and fast

Use cases:
- Cleaning input
- Post-processing LLM output
- Adding business rules

Runnable Lambdas are often used **between LLM calls**.

---

## 6. Runnable Branch (Conditional Execution)

Runnable Branch allows **conditional routing** based on input.

Concept:
> **If condition → Runnable A  
Else → Runnable B**

Key points:
- Enables decision-making
- Similar to if-else logic
- Keeps workflows clean

Use cases:
- Different prompts for different inputs
- Routing based on user intent
- Error handling paths

---

## 7. Runnable Passthrough

Runnable Passthrough simply **forwards input without changes**.

Concept:
> **Input → Same input**

Why it exists:
- Useful in parallel or branching workflows
- Helps preserve original data

Use cases:
- Keeping raw input alongside processed output
- Debugging pipelines

---

## Key Takeaways (Revision)

- Runnables are **building blocks**, not just chains
- They support **sequential, parallel, and conditional flows**
- `|` operator is the standard way to compose logic
- Prefer runnables over old chain abstractions
- Combine LLMs + Python logic cleanly using runnables

---

**Tip:**  
Start simple → Sequential → Parallel → Conditional  
Do not jump to agents unless required.

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

**Start with chains or runnables before agents.**

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
- Runnables provide flexible composition
- Temperature controls randomness
- Parsers structure output
- Memory handles context
- Agents are optional and advanced

---

## Status

Learning and revision in progress.
