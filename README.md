---
title: MetaXScaler
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: docker
app_file: main.py
pinned: false
---

MetaXScaler — Hidden Assumption Discovery Environment
Overview
MetaXScaler is an intelligent environment designed to analyze arguments and uncover hidden assumptions in reasoning. It simulates how an AI agent evaluates claims, identifies implicit assumptions, and progresses step-by-step through logical analysis.

Problem Statement
Many AI systems and humans accept arguments without identifying the hidden assumptions behind them. This can lead to flawed reasoning and incorrect conclusions.

Solution
MetaXScaler provides an interactive environment where:

Arguments are analyzed

Claims are evaluated

Hidden assumptions are surfaced

Logical reasoning is simulated step-by-step

Tech Stack
Python

FastAPI

Uvicorn

Docker (for deployment)

Project Structure
Plaintext
metaXscaler/
│
├── main.py                  # FastAPI application
├── my_env_environment.py   # Core environment logic
├── requirements.txt        # Dependencies
├── Dockerfile              # Deployment configuration
└── README.md               # Project documentation
How to Run Locally
1. Install dependencies
Bash
pip install -r requirements.txt
2. Run the server
Bash
uvicorn main:app --reload
3. Open in browser
Access the local server at: http://127.0.0.1:8000

API Endpoints
Root
GET /

Response:

JSON
{"status": "ok"}
Health Check
GET /health

Reset Environment
POST /reset

Step Execution
POST /step

Example Input:

JSON
{
  "action": "test"
}
Workflow
Input argument or action

System processes the request

Environment updates state

Returns observation, reward, and status

Key Features
Lightweight and fast

Modular environment design

Easy API interaction

Suitable for AI reasoning experiments

Demo
Run locally using FastAPI and test endpoints via:

Browser

FastAPI Docs (/docs)

Future Improvements
Integrate advanced reasoning models

Improve assumption detection accuracy

Deploy fully on cloud platforms

Add UI for visualization

Authors
Medicharla Shanmukheswar
kale Viswa Sanjay
Sripati Mohith

Conclusion
MetaXScaler demonstrates a structured approach to analyzing reasoning and uncovering hidden assumptions, helping improve decision-making and AI interpretability.