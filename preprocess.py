import re
import nltk
from nltk.corpus import stopwords

def clean_text(text):
    nltk.download('stopwords', quiet=True)  # Download in a controlled manner
    stop_words = set(stopwords.words('english'))
    
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = ' '.join(word for word in text.split() if word not in stop_words)

    return text
