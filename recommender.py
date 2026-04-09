import pandas as pd
import numpy as np
import  requests
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer



model = SentenceTransformer('all-MiniLM-L6-v2')


def modelling(df):
    embeddings = model.encode(df['text'].tolist(), show_progress_bar=False)
    return embeddings



def job_recommend(user_input, df, embeddings):
    user_embedding = model.encode([user_input])
    similarity = cosine_similarity(user_embedding, embeddings)[0]

    top_matches = np.argsort(similarity)[::-1][:10]

    results = []
    for idx in top_matches:
        job = df.iloc[idx]
        score = similarity[idx]
        results.append((job, score))

    return results