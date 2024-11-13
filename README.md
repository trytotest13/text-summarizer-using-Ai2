
# Text Summarizer Using-Ai


This Python application summarizes long text input using a pre-trained model from the Hugging Face `transformers` library. It utilizes the BART or T5 model, which is fine-tuned for text summarization tasks.

## Requirements

Before you run the program, make sure you have the following dependencies installed:

- Python 3.x
- `transformers` library
- `torch` library (for the model to work efficiently)

You can install the required libraries using `pip`:

```bash
pip install transformers torch
```

## Project Structure

The project contains a simple Python script that takes a text input, processes it through the pre-trained summarization model, and returns a summarized version.

### Files:
- `summarizer.py`: The main Python script for text summarization.

## How to Run

1. **Clone this repository** or download the `summarizer.py` file.
2. Install the necessary dependencies as mentioned above.
3. Run the script using Python:

```bash
python summarizer.py
```

4. The program will prompt you to enter text. Provide the text you want to summarize and press **Enter**.
5. The summarized text will be displayed as output.

### Example Usage:

```bash
Welcome to the Text Summarizer!

Please enter the text you want to summarize:

This is a long piece of text. It can be anything that you would like to summarize. The summarization model will shorten it while keeping the most important information.

--- Summary ---

Original Text:
This is a long piece of text. It can be anything that you would like to summarize. The summarization model will shorten it while keeping the most important information.

Summary:
 This is a long piece of text. It can be anything that you would like to summarize.
```

## How it Works

- The program uses Hugging Face's `pipeline` for summarization, which utilizes a pre-trained model like BART or T5 for transforming long text into a concise summary.
- The text input is processed through the model, and the summarizer returns a text that captures the key points.
  
## Notes

- The script currently summarizes text in English. It may not work as effectively with other languages unless a language-specific model is used.
- The `max_length` and `min_length` parameters in the pipeline function control the length of the summary.
  
---

You can customize the sections as needed, but this should cover the basics for your project!
