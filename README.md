RAG-based Document Q&A system with AI observability via Arize — tracks hallucination, RAG relevancy, tool calling, and QA accuracy.

Document Q&A System with AI Observability

A Retrieval-Augmented Generation (RAG) application that answers natural language questions over your documents, with built-in observability powered by Arize. The system is instrumented with span-level evaluators to continuously monitor:

Hallucination detection — flags responses not grounded in retrieved context
RAG relevancy — measures how well retrieved chunks match the query
Tool calling accuracy — validates correct tool/function invocation
QA correctness — evaluates overall answer quality against expected responses

This enables real-time visibility into LLM behavior, making it easier to debug retrieval issues, catch hallucinations, and maintain answer quality in production.
