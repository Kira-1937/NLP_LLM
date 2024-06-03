# AI Assignment

## Overview

This project analyzes a sample blood test report, searches the internet for relevant health articles, and provides health recommendations based on the findings.

## Setup

1. Clone the repository.
2. Navigate to the project directory:
    ```bash
    cd AI_Assignment
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Create a `.env` file in the project directory and add your Gemini API key:
    ```txt
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Usage

To run the project, execute the following command:

```bash
python main.py
