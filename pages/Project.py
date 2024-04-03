import streamlit as st

def project_page():
    st.title("EmoSense: A Sentiment Analysis Web App")
    st.image('https://getthematic.com/assets/img/sentiment-analysis/aspect-based-sentiment-analysis.png', width=800)
    
    st.markdown(
        """
        EmoSense employs TextBlob, a natural language processing library in Python, to conduct sentiment analysis 
        on user-entered text. The workflow of the application begins with the user inputting text into a designated 
        text area. Upon submission, EmoSense utilizes TextBlob's sentiment analysis capabilities to process the input. 
        TextBlob analyzes the text's polarity and subjectivity, providing a sentiment label indicating whether the 
        text is positive, negative, or neutral, along with numerical values representing polarity and subjectivity scores. 
        
        Additionally, EmoSense incorporates a graphical representation of the sentiment analysis results, displaying 
        emoticons corresponding to the detected sentiment (such as 😃 for positive, 😞 for negative, and 😐 for neutral). 
        Furthermore, the application offers a detailed explanation of the sentiment analysis outcome, aiding users in 
        understanding the emotional tone conveyed by the input text.
        """
    )
    
    st.subheader("Technologies Used:")
    st.markdown(
        """
        - **Streamlit**: A Python library for creating interactive web applications.
        - **TextBlob**: A natural language processing library in Python.
        - **Cleantext**: A library for preprocessing and sanitizing text data.
        """
    )

    st.markdown(
        """
        In addition to analyzing sentiment in real-time text input, EmoSense extends its functionality to perform 
        sentiment analysis on data entered via CSV files. Upon uploading a CSV file containing text data, EmoSense 
        automatically processes each entry within the file using the same sentiment analysis techniques employed for 
        real-time text input. Leveraging the TextBlob library, EmoSense computes polarity and subjectivity scores for 
        each entry, categorizing them as positive, negative, or neutral based on the sentiment label derived from the 
        polarity score.
        """
    )

    st.subheader("Features:")
    st.markdown(
        """
        - Real-time sentiment analysis of user-entered text.
        - Graphical representation of sentiment analysis results with emoticons.
        - Explanation of sentiment analysis outcome.
        - Analysis of sentiment in CSV files.
        - Data exploration and visualization.
        """
    )

    st.markdown(
        """
        The integration of sentiment analysis on CSV data further enriches EmoSense's capabilities, empowering users 
        to gain valuable sentiment insights from structured text data sources. By harnessing the power of TextBlob 
        and Streamlit, EmoSense delivers an intuitive and user-friendly interface for efficient sentiment analysis, 
        catering to the needs of users seeking to understand the emotional context embedded within their data.
        """
    )

# Main function to run the app
def main():
    st.set_page_config(
        page_title="EmoSense: A Sentiment Analysis Web App",
        page_icon="😊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    project_page()

if __name__ == "__main__":
    main()
