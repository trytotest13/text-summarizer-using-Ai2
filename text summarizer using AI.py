# Import necessary libraries
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    """
    Summarizes the input text using the pre-trained summarization model.
    """
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    # Greet the user
    print("Welcome to the Text Summarizer!\n")
    
    # Prompt the user to input their text
    text = input("Please enter the text you want to summarize:\n\n")
    
    # Check if the user provided any input
    if text.strip() == "":
        print("You didn't provide any text. Please enter a valid text to summarize.")
    else:
        # Call the summarize_text function to summarize the input text
        summary = summarize_text(text)
        
        # Display the results
        print("\n--- Summary ---\n")
        print(f"Original Text:\n{text}")
        print("\nSummary:\n", summary)
