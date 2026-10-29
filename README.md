# CareFlow AI

**An AI-powered healthcare dashboard built with React, TypeScript, FastAPI, and the OpenAI Agents SDK.**

## Overview

CareFlow AI is a full-stack application designed to help hospital care coordinators manage patient discharge workflows, track follow-up appointments, and identify gaps in care.

The project demonstrates how **LLM tool calling, MCP, and multi-agent orchestration** can automate healthcare administrative workflows while keeping humans in control of important decisions.

> **Status:** Work in progress — features are being developed incrementally.

## The Problem

Hospital care coordinators often work across disconnected systems to manage patient records, discharge instructions, medications, and follow-up appointments. These manual processes can lead to missed tasks and delayed follow-up care.

## The Solution

CareFlow AI will provide a centralized dashboard that allows healthcare staff to:

- View patient records and discharge information.
- Monitor follow-up appointments and outstanding tasks.
- Identify incomplete care coordination workflows.
- Ask an AI assistant questions about patient data.
- Generate summaries and AI-assisted task recommendations.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| State Management | Redux Toolkit, RTK Query / Jotai |
| Backend | Python, FastAPI |
| AI | OpenAI Agents SDK |
| Agent Tools | Tool Calling, MCP |
| Database | PostgreSQL |
| Infrastructure | Docker, AWS |
| CI/CD | GitHub Actions |

## AI Architecture

The planned multi-agent system includes:

- **Care Coordinator Agent:** Orchestrates requests and delegates tasks.
- **Patient Records Agent:** Retrieves patient and discharge information.
- **Follow-Up Agent:** Checks appointments and outstanding follow-ups.
- **Task Agent:** Prepares administrative actions for human approval.
- **MCP Server:** Provides standardized access to healthcare data and tools.

The project will also explore **MCP Code Mode** for efficiently orchestrating multiple tool calls.

## Project Roadmap

- [ ] Build FastAPI endpoints and synthetic patient datasets.
- [ ] Develop the React patient dashboard.
- [ ] Integrate state management and API fetching.
- [ ] Implement AI assistant and tool calling.
- [ ] Build MCP integrations.
- [ ] Add multi-agent orchestration and human approval workflows.
- [ ] Implement tests, tracing, and agent evaluations.
- [ ] Containerize and deploy to AWS.

## Getting Started

### Backend

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

API documentation: http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173

## Data & Safety

CareFlow AI uses **synthetic patient data**, potentially generated using [Synthea](https://synthea.mitre.org/), with healthcare interoperability concepts based on [HL7 FHIR](https://www.hl7.org/fhir/).

This is an educational proof of concept, not a production clinical system. It does not provide medical diagnoses or treatment recommendations. AI-assisted actions require human oversight.

## Purpose

CareFlow AI is a portfolio project demonstrating full-stack engineering, AI agent development, healthcare workflow automation, and AWS cloud deployment.