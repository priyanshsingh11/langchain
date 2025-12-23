# LangChain – Core Concepts & Revision Notes

This repository contains **revision notes and practice code for LangChain**.  
The focus is on **understanding concepts clearly**, not building complex systems.

---

## 1. What is LangChain?

**LangChain** is a framework used to **build applications powered by Large Language Models (LLMs)**.

It helps you:
- Connect LLMs with external data
- Control how prompts are sent
- Chain multiple steps together
- Parse and structure LLM outputs

> LangChain does **not train models** — it **orchestrates** them.

---

## 2. Core Components of LangChain

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

**Typical flow:**  
**Models → Prompts → Runnables → Parsers**

---

## 3. Models

Models are the **LLMs** used to generate responses.

### Examples
- OpenAI models
- Hugging Face models
- Local models (via Ollama, etc.)

### Key Points
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

## 4. Temperature

**Temperature controls randomness of output.**

- `0.0` → Deterministic, factual
- `0.7` → Balanced
- `1.0+` → Creative, random

### Use Cases
- Low → QA systems
- Medium → Chatbots
- High → Creative writing

> Lower temperature = more reliable output

---

## 5. Prompts

Prompts define **what you ask the model**.

LangChain supports:
- Prompt templates
- Variable injection
- Structured prompts

> Prompts are critical because **LLMs strictly follow instructions**.

---

## 6. Chains

**Chains define workflow logic.**

A chain is:
> **Prompt → Model → Output**

### Why Chains Matter
- Connect multiple steps
- Define execution order
- Enable reuse

> Modern LangChain prefers **runnables over old chain abstractions**.

---

## 7. Runnables – Core Execution Model

Runnables are the **fundamental building blocks** in modern LangChain.

A runnable:
> **Takes input → processes it → returns output**

They allow:
- Sequential flows
- Parallel execution
- Conditional routing
- Mixing Python logic with LLMs

---

### 7.1 Sequential Runnables (`|` Operator)

Sequential execution using the pipe operator.

**Concept:**

**Key Points**
- Output of one step feeds into the next
- Clean and readable
- Recommended default approach
- Internally equivalent to `RunnableSequence`

---

### 7.2 Parallel Runnables

Parallel runnables execute **multiple tasks at the same time**.

**Concept:**
> Same input → multiple runnables → combined output

**Use Cases**
- Summarization + keyword extraction
- Multi-view analysis

---

### 7.3 Runnable Map (Fan-Out)

Applies different runnables to different input fields.

**Concept:**
> Structured input → multiple transformations → structured output

**Use Cases**
- Document pipelines
- Multi-field processing

---

### 7.4 Runnable Lambda

Allows **custom Python logic** inside pipelines.

**Use Cases**
- Data cleaning
- Validation
- Formatting
- Business rules

> No LLM is required here.

---

### 7.5 Runnable Branch

Enables **conditional execution**.

**Concept:**

**Use Cases**
- Intent-based routing
- Error handling
- Different prompts per input type

---

### 7.6 Runnable Passthrough

Forwards input **without modification**.

**Use Cases**
- Preserving raw input
- Combining original and processed data
- Debugging pipelines

---

## 8. Output Parsers

LLMs return **unstructured text**.  
Output parsers convert it into **structured data**.

### Examples
- String parser
- JSON parser
- Custom parsers

**Why Parsers Matter**
- Reduce hallucination
- Improve reliability
- Critical for production systems

---

## 9. Memory

Memory allows systems to **retain context across interactions**.

### Examples
- Conversation history
- Session memory

Used in:
- Chatbots
- Assistants
- Multi-turn workflows

> Without memory, every request is independent.

---

## 10. Tools

Tools allow LLMs to **interact with external systems**.

### Examples
- APIs
- Databases
- Python functions
- Search engines

> Tools extend LLM capability beyond text generation.

---

## 11. Agents (Advanced)

Agents can:
- Choose tools
- Plan steps
- Execute reasoning loops

### Important Notes
- Harder to control
- More expensive
- Often unnecessary

> **Always start with runnables before agents.**

---

## 12. Retrieval-Augmented Generation (RAG)

**RAG (Retrieval-Augmented Generation)** combines LLMs with **external knowledge sources**.

**In simple terms:**
> **LLM + Your Data = RAG**

LangChain is widely used to build RAG systems.

---

### 12.1 Why RAG is Needed

LLMs:
- Don’t know private data
- Have knowledge cutoffs
- Can hallucinate

RAG solves this by:
- Retrieving relevant documents
- Injecting them into the prompt
- Generating grounded answers

---

### 12.2 High-Level RAG Flow


---

### 12.3 Core Components of RAG in LangChain

- **Document Loaders**
- **Text Splitters**
- **Embeddings**
- **Vector Stores**
- **Retrievers**
- **LLMs**

LangChain orchestrates all these components.

---

### 12.4 Document Loaders (Very Important)

Document loaders bring **external data into LangChain**.

#### Common Loader Types
- **PDF Loaders** – reports, research papers, manuals
- **Text Loaders** – `.txt`, logs, notes
- **Web Loaders** – websites, blogs, documentation
- **Database Loaders** – SQL / NoSQL data
- **API Loaders** – internal services, business APIs

> Loaders convert raw data into structured `Document` objects.

---

### 12.5 Text Splitters

Split large documents into **smaller chunks**.

**Why Needed**
- LLM context window limits
- Better retrieval accuracy

Chunk size and overlap directly affect RAG quality.

---

### 12.6 Embeddings

Embeddings convert text into **numerical vectors**.

**Key Idea**
> Similar meaning → similar vectors

Used for:
- Semantic search
- Similarity matching

> Embeddings do **not generate text**.

---

### 12.7 Vector Stores

Vector stores store embeddings and enable fast similarity search.

**Examples**
- FAISS
- Chroma
- Pinecone

They power the **retrieval step** in RAG.

---

### 12.8 Retrievers

Retrievers fetch the **most relevant document chunks**.

**Flow**

They abstract away vector store logic.

---

### 12.9 Augmentation (Context Injection)

Retrieved documents are injected into the prompt.

The LLM:
- Does not memorize data
- Uses provided context to answer

> This is the core idea of RAG.

---

### 12.10 RAG vs Fine-Tuning

| RAG | Fine-Tuning |
|----|------------|
| Uses external data | Modifies model weights |
| Easy to update | Expensive |
| Dynamic | Static |
| Safer for private data | Risky for sensitive data |

> LangChain primarily focuses on **RAG**, not fine-tuning.

---

## 13. When to Use LangChain

### Use LangChain when:
- You need multi-step LLM logic
- You want structured outputs
- You are building AI workflows
- You need RAG pipelines

### Do NOT use LangChain when:
- A single API call is enough
- Logic is extremely simple

---

## 14. Key Takeaways

- LangChain orchestrates LLM workflows
- Runnables are the core abstraction
- `|` operator is the standard composition method
- RAG enables LLMs to use private data
- Agents are optional and advanced
- Start simple, scale only when needed

---

## 15. Status

Learning and revision in progress.
