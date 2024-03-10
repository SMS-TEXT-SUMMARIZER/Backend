  SMS Text Summarizer

SMS Text Summarizer
===================

This is a service designed to process SMS messages, extract useful information, and generate summaries for each conversation thread. It leverages natural language processing (NLP) techniques to identify key information and provide concise summaries.

Installation
------------

1.  Clone the repository:
    ```bash
    git clone https://github.com/SMS-TEXT-SUMMARIZER/Backend.git
    ```
3.  Navigate to the project directory:
    ```bash
    cd Backend
    ```
5.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
Usage
-----

1.  Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
This will start the server on `http://localhost:8000` by default.

4.  Test the APIs using tools like `curl` or Swagger UI.

```mermaid
graph TD
  A[Incoming SMS Messages] -->|List of Dictionaries| B(Process Messages)
  B -->|Dictionary of Messages| C{Group Messages by Number}
  C -->|Dictionary| D[Task 1: Process and Summarize]
  C -->|Dictionary| E[Task 2: Process and Summarize]
  C -->|Dictionary| F[Task 3: Process and Summarize]
  C -->|Dictionary| G[...]
  D -->|Async Summarization| H(Summary 1)
  E -->|Async Summarization| I(Summary 2)
  F -->|Async Summarization| J(Summary 3)
  G -->|Async Summarization| K(...)
  H -->|Dict: Number - Summary| L{All Summaries Ready}
  I -->|Dict: Number - Summary| L
  J -->|Dict: Number - Summary| L
  K -->|Dict: Number - Summary| L
  L -->|Dict: Number - Summary| M{API Response}
```

Contributing
------------

Contributions are welcome! Please feel free to open issues or submit pull requests to improve the functionality, documentation, or code quality.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
