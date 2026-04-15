# Morgan CS AI Advising Assistant

## Project Overview
This project is a multi agent AI system designed to support Morgan State University Computer Science students with academic advising, course planning, prerequisite understanding, policy guidance, and student support resources.

The system helps students ask questions about degree planning, prerequisites, advising policies, and available support services. A routing component determines which specialized agent should respond, and the system retrieves relevant information from Morgan State Computer Science materials.

## Problem Statement
Computer Science students at Morgan State University, especially freshmen and sophomores, often face challenges related to academic advising, course planning, prerequisite understanding, and access to support resources. Advising information is spread across multiple sources, including curriculum documents, catalog pages, and departmental guidance, which can make it difficult for students to quickly find accurate and consistent answers.

## Solution
The proposed solution is a multi agent academic support assistant. The system includes specialized agents for different categories of student questions and uses a retrieval based backend to return source grounded responses.

## Agents
- Degree Planning Agent
- Prerequisite Checking Agent
- Advising and Policy Agent
- Student Resources Agent
- General Advising Agent
- Router component for assigning queries to the correct agent

## Features
- Multi agent routing based on question type
- Retrieval based search over Morgan CS advising materials
- Streamlit frontend for interactive question answering
- Source display for retrieved advising information
- Support for academic planning, prerequisites, advising, and resources

## Development Environment
- Python
- Streamlit
- Visual Studio Code
- Terminal
- GitHub

## Data Sources
The project uses Morgan State University Computer Science materials, including curriculum sequence information and a cleaned advising knowledge base prepared for retrieval and demo purposes.

## Example Questions
- What is the prerequisite for COSC 112?
- How many credits are required for the Computer Science degree?
- When do students take COSC 490?
- What courses are in the freshman year sequence?
- Is tutoring available for CS students?
- Should students meet with an advisor before upper level courses?

## Current Progress
The current system includes:
- a working retrieval based backend
- a chunked knowledge base stored in `data/chunks.json`
- routing logic for multiple advising agents
- a Streamlit frontend for user interaction
- source grounded responses using Morgan CS materials

## How to Run
1. Activate the virtual environment
2. Run `python3 src/ingest.py`
3. Run `streamlit run src/app.py`

## Evaluation Approach
The system is evaluated using simulated student advising scenarios. Performance is assessed based on:
- accuracy
- clarity
- relevance
- correct routing to the appropriate agent
- use of source grounded information

## Project Goal
The goal of this project is to create a functional AI advising assistant that improves access to academic guidance for Morgan State University Computer Science students while demonstrating applied artificial intelligence, multi agent system design, retrieval based reasoning, and problem solving skills.
