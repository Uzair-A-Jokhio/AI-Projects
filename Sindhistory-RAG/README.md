# Sindh History RAG

This project is a specialized Retrieval-Augmented Generation (RAG) system focused on the history of the Sindh region.

## Overview

This system allows users to ask questions about the history of Sindh and receive answers based on a knowledge base of historical documents. It's built upon the general RAG framework but is specifically tailored for historical information about Sindh.

## Dataset

The primary data source is the "History of Sindh" PDF document, which is processed and stored in a vector database for efficient retrieval.

## Usage

1.  Install the required dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2.  The `history_of_sindh.pdf` file needs to be in the `data` directory.
3.  Run the main application to start querying the Sindh history knowledge base.

## Example

```
Question: Who was the first ruler of the Talpur dynasty?
```

The system will retrieve relevant information from the "History of Sindh" document and generate an answer.