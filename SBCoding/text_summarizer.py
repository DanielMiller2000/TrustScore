from transformers import pipeline
import re
import random

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Load the question-answering pipeline
qa_pipeline = pipeline("question-answering")


def generate_summary(text, max_length=130, min_length=30, split_sentences=True):
    """
    Generate a summary for the given text.

    Parameters:
    text (str): Input text to summarize.
    max_length (int): Maximum length of the summary.
    min_length (int): Minimum length of the summary.
    split_sentences (bool): Whether to split text into smaller parts before summarization.

    Returns:
    str: Generated summary.
    """
    # Preprocess the text
    text = re.sub('\s+', ' ', text.strip())
    
    # Split text if specified
    if split_sentences:
        sentences = text.split('. ')
        segments = ['. '.join(sentences[i:i + 3]) for i in range(0, len(sentences), 3)]
    else:
        segments = [text]

    # Generate summaries for each segment and combine them
    summaries = [summarizer(segment, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text'] for segment in segments]
    return ' '.join(summaries)
