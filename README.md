# LangChain – Core Concepts & Revision Notes

This repository contains **revision notes and practice code for LangChain**.  
The focus is on **clear conceptual understanding**, not building complex or production-heavy systems.

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

**Key Points**
- Output of one step feeds into the next
- Clean and readable
- Recommended default approach
- Internally equivalent to `RunnableSequence`

---

### 7.2 Parallel Runnables

Parallel runnables execute **multiple tasks at the same time**.

**Use Cases**
- Summarization + keyword extraction
- Multi-view analysis

---

### 7.3 Runnable Map (Fan-Out)

Applies different runnables to different input fields.

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
- **Vector Stores / Vector Databases**
- **Retrievers**
- **LLMs**

LangChain orchestrates all these components.

---

## 13. Document Loaders

Document loaders bring **external data into LangChain**.

### Common Loader Types
- **PDF Loaders** – reports, research papers
- **Text Loaders** – `.txt`, logs
- **Web Loaders** – websites, documentation
- **Database Loaders** – SQL / NoSQL
- **API Loaders** – internal services

> Loaders convert raw data into `Document` objects.

---

## 14. Text Splitters (VERY IMPORTANT)

Text splitters divide large documents into **smaller, manageable chunks** before embedding.

> **Good splitting = good retrieval = good RAG answers**

---

### 14.1 Why Text Splitters Are Needed

- LLMs have **context window limits**
- Vector search works better on **focused chunks**
- Large documents reduce retrieval accuracy

Without splitting:
- Poor similarity search
- Higher hallucination
- Context overflow errors

---

### 14.2 What a Text Splitter Does

A text splitter:
- Breaks documents into chunks
- Preserves semantic meaning
- Optionally adds overlap between chunks

**Output:**

Each chunk is embedded separately.

---

### 14.3 Common Text Splitter Types in LangChain

#### 1. Character Text Splitter
- Splits based on fixed character count
- Simple but less semantic

**Use Case:** Small, clean text

---

#### 2. Recursive Character Text Splitter (Most Used)
- Tries to split by:
  - Paragraphs
  - Sentences
  - Words
  - Characters (last fallback)

**Why Best**
- Preserves meaning
- Produces high-quality chunks

> **Recommended default splitter for RAG**

---

#### 3. Token Text Splitter
- Splits based on token count
- Model-aware

**Use Case:** Strict token limits (GPT models)

---

#### 4. Markdown / Code Splitters
- Split based on headers or syntax

**Use Case:** Documentation, README, codebases

---

### 14.4 Chunk Size and Overlap

- **Chunk Size:** Number of characters/tokens per chunk
- **Chunk Overlap:** Shared content between chunks

**Why Overlap Matters**
- Prevents loss of context at boundaries
- Improves answer continuity

**Typical Values**
- Chunk size: `500–1000`
- Overlap: `50–200`

---

### 14.5 Text Splitter Best Practices

- Use **recursive splitter** by default
- Tune chunk size per document type
- Increase overlap for:
  - Legal
  - Technical
  - Research documents
- Smaller chunks ≠ always better

---

### 14.6 Interview Tip

> **Bad RAG answers are often caused by bad text splitting, not bad LLMs.**

---

## 15. Embeddings

Embeddings convert text into **numerical vectors**.

**Key Idea**
> Similar meaning → similar vectors

Used for:
- Semantic search
- Similarity matching

> Embeddings do **not generate text**.

---

## 16. Vector Store vs Vector Database (Very Important)

This distinction is **commonly asked in interviews**.

---

### 16.1 What is a Vector Store?

A **Vector Store** is a **storage + search layer** for embeddings.

Provides:
- Vector storage
- Similarity search
- Basic metadata filtering

**Examples**
- FAISS
- Chroma
- Annoy

Best for:
- Local development
- Prototypes
- Learning

---

### 16.2 What is a Vector Database?

A **Vector Database** is a **production-grade system**.

Provides:
- Horizontal scaling
- High availability
- Authentication
- Monitoring

**Examples**
- Pinecone
- Weaviate
- Milvus
- Qdrant

Best for:
- Enterprise RAG systems

---

### 16.3 Comparison

| Feature | Vector Store | Vector Database |
|------|-------------|----------------|
| Scaling | Limited | Horizontal |
| Security | Minimal | RBAC |
| Deployment | Local | Cloud |
| Use Case | Learning | Production |

---

### 16.4 LangChain Abstraction

LangChain uses a **common interface** for both, enabling easy swapping.

---

## 17. Retrievers (VERY IMPORTANT)

Retrievers are responsible for **finding the most relevant document chunks** from a vector store or vector database **given a user query**.

In simple terms:
> **Retriever = Query → Relevant Chunks**

Retrievers are the **heart of any RAG system**.  
If retrieval is poor, even the best LLM will give bad answers.

---

### 17.1 What Exactly Does a Retriever Do?

A retriever:
- Takes a user query (text)
- Converts it into an embedding
- Searches the vector store
- Returns the **top-K most relevant chunks**

**Flow:**

The LLM only sees what the retriever provides.

---

### 17.2 Why Retrievers Matter So Much

Even with:
- A powerful LLM
- High-quality documents
- Good prompts

❌ **Bad retrieval = bad answers**

Retrievers directly impact:
- Answer correctness
- Hallucination rate
- Context relevance
- User trust

> In most RAG systems, **retrieval quality matters more than model choice**.

---

### 17.3 Retriever vs Vector Store (Common Confusion)

| Vector Store | Retriever |
|-------------|----------|
| Stores embeddings | Fetches relevant chunks |
| Handles similarity search | Controls *how* search happens |
| Low-level storage | High-level retrieval logic |

**Key idea:**  
> A retriever sits **on top of** a vector store.

---

### 17.4 Types of Retrievers in LangChain

LangChain provides multiple retriever strategies.

---

#### 1. Similarity Retriever (Default)

- Fetches chunks based on **vector similarity**
- Uses cosine / dot-product similarity

**Best for:**
- General Q&A
- Semantic search

---

#### 2. Similarity Search with Score Threshold

- Returns chunks only if similarity score > threshold
- Filters out weak matches

**Best for:**
- Reducing noise
- Avoiding irrelevant context

---

#### 3. Max Marginal Relevance (MMR) Retriever

MMR balances:
- Relevance to query
- Diversity among retrieved chunks

**Why important**
- Prevents retrieving many similar chunks
- Improves coverage of different aspects

**Best for:**
- Broad or ambiguous questions
- Long documents

> MMR is often better than pure similarity search.

---

#### 4. Metadata-Based Retriever

Filters chunks using metadata such as:
- Source
- Date
- Category
- Document type

**Example use cases:**
- Only retrieve legal documents
- Only retrieve documents from last year

---

#### 5. Hybrid Retriever

Combines:
- Keyword search (BM25)
- Vector search

**Why useful**
- Handles exact matches + semantic meaning
- Strong for enterprise search

---

### 17.5 Retriever Parameters You Can Tune

Key parameters that affect retrieval quality:

- **k (Top-K):**
  - Number of chunks returned
  - Too small → missing context
  - Too large → noisy prompt

- **Search type:**
  - similarity
  - mmr
  - hybrid

- **Score threshold:**
  - Filters weak matches

- **Metadata filters:**
  - Improves precision

> Retrieval tuning is often an **iterative process**.

---

### 17.6 Retriever + Prompt Relationship

Retrievers and prompts work together.

- Retriever decides **what context** is sent
- Prompt decides **how context is used**

Bad combination:
- Too many chunks + weak prompt → hallucination

Good combination:
- Focused chunks + clear instructions → grounded answers

---

### 17.7 Retriever in the Full RAG Pipeline


The retriever acts as the **gatekeeper of knowledge**.

---

### 17.8 Common Retriever Mistakes

- Using default settings blindly
- Retrieving too many chunks
- No metadata filtering
- Poor text splitting (upstream issue)
- Assuming LLM will “figure it out”

> Many RAG failures are **retrieval problems**, not LLM problems.

---

### 17.9 Interview Tip

If asked:
> *“Why are retrievers important in RAG?”*

**Answer:**
> Retrievers control what knowledge the LLM sees. High-quality retrieval reduces hallucinations, improves relevance, and directly determines answer accuracy.

---

### 17.10 Key Takeaways

- Retrievers fetch relevant chunks for the LLM
- They sit on top of vector stores
- MMR and hybrid retrievers often outperform basic similarity search
- Retrieval quality > model size
- Good RAG starts with good retrieval


## 18. Augmentation (Context Injection)

Retrieved chunks are injected into the prompt.

LLM:
- Does not memorize data
- Answers using only provided context

---

## 19. RAG vs Fine-Tuning

| RAG | Fine-Tuning |
|----|------------|
| External data | Model weights |
| Dynamic | Static |
| Cheap | Expensive |
| Safer | Risky |

---

## 20. When to Use LangChain

### Use LangChain when:
- Multi-step LLM workflows
- RAG pipelines
- Structured outputs

### Avoid LangChain when:
- Single API call is enough

---

## 21. Key Takeaways

- LangChain orchestrates LLM workflows
- Runnables are the core abstraction
- Text splitters heavily affect RAG quality
- Vector stores for local use
- Vector databases for production
- Agents are optional

---

## 22. Status

Learning and revision in progress.