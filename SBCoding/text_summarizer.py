from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")


def generate_summary(text, max_length=130, min_length=30):
    """
    Generate a summary for the given text.

    Parameters:
    text (str): Input text to summarize.
    max_length (int): Maximum length of the summary.
    min_length (int): Minimum length of the summary.

    Returns:
    str: Generated summary.
    """
    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


# Example usage
if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural 
    intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of 
    intelligent agents: any system that perceives its environment and takes actions that maximize its 
    chance of achieving its goals.
    """

    print("Original Text:")
    print(sample_text)
    print("\nGenerated Summary:")
    print(generate_summary(sample_text))
