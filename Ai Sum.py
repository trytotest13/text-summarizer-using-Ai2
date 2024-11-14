from transformers import pipeline

# Specify the model and revision you want to use explicitly
model_name = "sshleifer/distilbart-cnn-12-6"
revision = "a4f8f3e"

# Initialize the pipeline with the model name and revision
summarizer = pipeline("summarization", model=model_name, revision=revision)

# Use the pipeline as usual
text = "Your input text here"
summary = summarizer(text)
print(summary)


# Import necessary libraries
from transformers import pipeline

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
