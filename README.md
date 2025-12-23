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
- **RAG (Retrieval-Augmented Generation)**

You usually start with:  
**Models → Prompts → Runnables → Parsers**

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

## Temperature

**Temperature controls randomness of output.**

- `0.0` → Deterministic, factual
- `0.7` → Balanced
- `1.0+` → Creative, random

Use cases:
- Low → QA systems
- Medium → Chatbots
- High → Creative writing

Lower temperature = more reliable output.

---

## Prompts

Prompts define **what you ask the model**.

LangChain supports:
- Prompt templates
- Variable injection
- Structured prompts

Prompts are critical because **LLMs strictly follow instructions**.

---

## Chains

**Chains define workflow logic.**

A chain is:
> **Prompt → Model → Output**

Chains:
- Connect multiple steps
- Define execution order
- Enable reuse

Modern LangChain prefers **runnables over old chain abstractions**.

---

## Runnables – Core Execution Model

Runnables are the **fundamental building blocks** in modern LangChain.

A runnable:
> **Takes input → processes it → returns output**

They allow:
- Sequential flows
- Parallel execution
- Conditional routing
- Mixing Python logic with LLMs

---

## 1. Sequential Runnables (`|` Operator)

Sequential execution using the pipe operator:


Key points:
- Output of one step feeds into the next
- Clean and readable
- Recommended default approach

Internally equivalent to `RunnableSequence`.

---

## 2. Parallel Runnables

Parallel runnables execute **multiple tasks at the same time**.

Concept:
> Same input → multiple runnables → combined output

Key points:
- Faster execution
- Independent tasks
- Output is usually a dictionary

Use cases:
- Summarization + keyword extraction
- Multi-view analysis

---

## 3. Runnable Map (Fan-Out)

Runnable maps apply different runnables to different input fields.

Concept:
> Structured input → multiple transformations → structured output

Use cases:
- Document pipelines
- Multi-field processing

---

## 4. Runnable Lambda

Runnable Lambda allows **custom Python logic** inside pipelines.

Use cases:
- Data cleaning
- Validation
- Formatting
- Business rules

No LLM is required here.

---

## 5. Runnable Branch

Runnable Branch enables **conditional execution**.

Concept:
> If condition → Runnable A  
> Else → Runnable B

Use cases:
- Intent-based routing
- Error handling
- Different prompts per input type

---

## 6. Runnable Passthrough

Runnable Passthrough forwards input **without modification**.

Use cases:
- Preserving raw input
- Combining original and processed data
- Debugging pipelines

---

## Output Parsers

LLMs return **unstructured text**.  
Output parsers convert it into **structured data**.

Examples:
- String parser
- JSON parser
- Custom parsers

Parsers:
- Reduce hallucination
- Improve reliability
- Are critical for production systems

---

## Memory

Memory allows systems to **retain context across interactions**.

Examples:
- Conversation history
- Session memory

Used in:
- Chatbots
- Assistants
- Multi-turn workflows

Without memory, every request is independent.

---

## Tools

Tools allow LLMs to **interact with the external world**.

Examples:
- APIs
- Databases
- Python functions
- Search systems

Tools extend LLM capability beyond text generation.

---

## Agents (Advanced)

Agents can:
- Choose tools
- Plan steps
- Execute reasoning loops

Agents are powerful but:
- Harder to control
- More expensive
- Often unnecessary

**Always start with runnables before agents.**

---

## Retrieval-Augmented Generation (RAG)

**RAG (Retrieval-Augmented Generation)** combines LLMs with **external knowledge sources**.

In simple terms:
> **LLM + Your Data = RAG**

LangChain is commonly used to build RAG systems.

---

## Why RAG is Needed

LLMs:
- Don’t know private data
- Have knowledge cutoffs
- Can hallucinate

RAG solves this by:
- Retrieving relevant documents
- Injecting them into the prompt
- Generating grounded answers

---

## High-Level RAG Flow


---

## Core Components of RAG in LangChain

- **Document Loaders**
- **Text Splitters**
- **Embeddings**
- **Vector Stores**
- **Retrievers**
- **LLMs**

LangChain orchestrates all these components.

---

## Document Loaders

Load external data such as:
- PDFs
- Text files
- Web pages
- Databases

They convert raw data into structured `Document` objects.

---

## Text Splitters

Large documents are split into smaller chunks.

Why:
- Context window limits
- Better retrieval accuracy

Chunk size and overlap impact performance.

---

## Embeddings

Embeddings convert text into vectors.

Key idea:
> Similar meaning → similar vectors

Used for:
- Semantic search
- Similarity matching

Embeddings do **not generate text**.

---

## Vector Stores

Vector stores store embeddings and enable fast similarity search.

Examples:
- FAISS
- Chroma
- Pinecone

They power the retrieval step in RAG.

---

## Retrievers

Retrievers fetch the **most relevant document chunks**.

Flow:
> Query → embedding → similarity search → top-k documents

They abstract away vector store logic.

---

## Augmentation (Context Injection)

Retrieved documents are injected into the prompt.

The LLM:
- Does not memorize data
- Uses provided context to answer

This is the core of RAG.

---

## RAG vs Fine-Tuning

| RAG | Fine-Tuning |
|----|------------|
| Uses external data | Modifies model weights |
| Easy to update | Expensive |
| Dynamic | Static |
| Safer for private data | Risky for sensitive data |

LangChain primarily focuses on **RAG**, not fine-tuning.

---

## When to Use LangChain

Use LangChain when:
- You need multi-step LLM logic
- You want structured outputs
- You are building AI workflows
- You need RAG pipelines

Do NOT use LangChain when:
- A single API call is enough
- Logic is extremely simple

---

## Key Takeaways

- LangChain orchestrates LLM workflows
- Runnables are the core abstraction
- `|` operator is the standard composition method
- RAG enables LLMs to use private data
- Agents are optional and advanced
- Start simple, scale only when needed

---

## Status

Learning and revision in progress.
