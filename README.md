# Intelligent Library Management System

## Overview
This project is a Python-based application that manages basic library inventory (Add, Search, View) and integrates a **Rule-Based AI Module**. This module is designed to demonstrate the core concept of **Prediction and Classification** based on user input, which satisfies the requirements for the AI/ML course.

## Key AI Features
* **Model Type:** Rule-Based Classification System
* **Prediction Goal:** To classify a user's primary reading interest (e.g., Tech Enthusiast, Fiction Lover).
* **Process:** The system analyzes input keywords (reading history) using conditional logic to make a prediction.

## Standard Features
* **Modular Design:** Code is organized into `main.py`, `book_ops.py`, and `data_file.py`.
* **Data Persistence:** Uses CSV file handling (`library.csv`) to save all book records permanently.
* **Smart Search:** Allows users to find books using partial keywords in the Title or Author fields.

## Technologies Used
* **Language:** Python 3.x
* **Concepts:** Rule-Based AI, Modular Programming, File I/O.

## How to Run the AI Feature
1.  Download the repository files.
2.  Run the main script: `python main.py`
3.  From the menu, select **Option 4** ("AI User Classification").
4.  Enter reading topics (e.g., `python, code, ai`) to see the system classify your user profile.
