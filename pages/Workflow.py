import streamlit as st

def workflow_page():
    st.title("Workflow of EmoSense")
    st.image('static/chart.png', width=550)
    
    st.subheader("User Input")
    st.markdown("""
    The process begins with the user inputting text into a designated text area provided by the EmoSense application. 
    This text serves as the input for sentiment analysis.
    """)

    st.subheader("Sentiment Analysis (TextBlob)")
    st.markdown("""
    Upon submission of the user input, EmoSense utilizes TextBlob, a natural language processing library in Python, 
    to perform sentiment analysis. TextBlob analyzes the text's polarity and subjectivity, providing numerical scores 
    representing the text's sentiment.
    """)

    st.subheader("Sentiment Labeling")
    st.markdown("""
    Based on the polarity score computed by TextBlob, EmoSense categorizes the sentiment of the input text into one 
    of three labels: Positive, Negative, or Neutral. This categorization helps users understand the emotional tone 
    conveyed by the text.
    """)

    st.subheader("Polarity and Subjectivity Scores")
    st.markdown("""
    In addition to the sentiment label, EmoSense provides users with the polarity and subjectivity scores computed 
    by TextBlob. These scores offer quantitative insights into the sentiment analysis results, indicating the degree 
    of positivity or negativity and the level of objectivity or subjectivity present in the text.
    """)

    st.subheader("Sentiment Visualization (Emoticons)")
    st.markdown("""
    To enhance user understanding and engagement, EmoSense incorporates a graphical representation of the sentiment 
    analysis results. Emoticons corresponding to the detected sentiment (here, 😃 for positive, 😞 for negative, and 
    😐 for neutral) are displayed, providing users with visual feedback on the emotional tone of the text.
    """)

    st.subheader("Explanation of Sentiment Analysis Result")
    st.markdown("""
    Finally, EmoSense offers a detailed explanation of the sentiment analysis outcome. This explanation aids users in 
    interpreting the sentiment analysis results, providing additional context and insights into the emotional content 
    of the input text. In addition, visualization of the polarity and subjectivity levels enables users to quickly
    grasp the emotional tone of text data and derive actionable insights for informed decision making.
    """)

# Main function to run the app
def main():
    st.set_page_config(
        page_title="EmoSense: Workflow",
        page_icon="⚙️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    workflow_page()

if __name__ == "__main__":
    main()
