import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pickle

# Read the preprocessed dataframe.
with open("book_models/processed_df.pkl", "rb") as file:
    book_df = pickle.load(file)

#Read the saved similarty score file
with open("book_models/similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

# Lish of all books name form dataframe
list_of_books = book_df['book_name'].tolist()

# function for recommendation system
def recommendation(book_name:str):
    # finding 4 close macth with threshold value 0.5 to the user entered book name 
    find_close_match = difflib.get_close_matches(book_name, list_of_books, n=4, cutoff=0.5)

    # select first one
    close_match = find_close_match[0]

    # The function finds the index of this best-matching book in the book_df DataFrame.
    index_of_the_book = book_df[book_df.book_name == close_match].index.values[0]

    # retrieve the similarity scores of the best-matching book with all other books.
    similarity_score = list(enumerate(similarity[index_of_the_book]))

    # sort then in descending order
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

    # list top 5 similar books
    top_sim = sorted_similar_movies[:6]
    res = []
    for i, book in enumerate(top_sim):
        index = book[0]
        book_name_from_index = book_df.loc[index, 'book_name'] if index in book_df.index else "no similar book available"
        # print(i+1, "-", book_name_from_index)
        res.append(book_name_from_index)
    return res


book_name = "The Hero Factor"
recommendation(book_name)


  
