import streamlit as st
from utils import recommendation
st.title("📚 Book Recommendation System")

book_name = st.text_input("Enter a book name:")

if st.button("Get Recommendations"):
    if book_name.strip():
        recommendations = recommendation(book_name)
        st.subheader("Recommended Books:")
        for book in recommendations[:5]:
            st.write(f"- {book}")
    else:
        st.error("Please enter a book name.")