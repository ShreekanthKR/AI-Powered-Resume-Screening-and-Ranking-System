import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_desc, resumes):
    vectorizer = TfidfVectorizer()
    documents = [job_desc] + list(resumes)
    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vector = tfidf_matrix[0].reshape(1, -1)  # Reshape to avoid shape mismatch
    resume_vectors = tfidf_matrix[1:]

    scores = cosine_similarity(job_vector, resume_vectors).flatten()
    ranked_indices = np.argsort(scores)[::-1]

    return [(i, scores[i]) for i in ranked_indices]  # Return index instead of text
