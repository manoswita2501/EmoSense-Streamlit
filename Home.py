import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go

# Set page
st.set_page_config(
    page_title="EmoSense",  # Setting page title
    page_icon="🧠",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="collapsed"    # Expanding sidebar by default    
)

# Create a Streamlit app title
st.title("EmoSense - A Sentiment Analyzer")
st.image('https://exemplary.ai/img/blog/sentiment-analysis/sentiment-analysis.svg', use_column_width=True)

# Create a text area for user input
user_input = st.text_area("Enter the text you wish to analyze:")

# Define a function for sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    sentiment_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return sentiment_label, polarity, subjectivity

# Function to display raining emojis
def rain_emojis(emoji, font_size, falling_speed, animation_length):
    from streamlit_extras.let_it_rain import rain
    rain( 
        emoji=emoji,
        font_size=font_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )

# Add a button for sentiment analysis
if st.button("Analyze the Sentiment"):
    if user_input:
        sentiment_label, polarity, subjectivity = analyze_sentiment(user_input)
        st.write(f"Sentiment: {sentiment_label}")
        st.write(f"Polarity: {polarity:.2f}")
        st.write(f"Subjectivity: {subjectivity:.2f}")

        # Emoticon representation with raining emojis
        if sentiment_label == "Positive":
            rain_emojis("😃", 20, 2, "infinite")
            st.success("This text is perceived to be generally positive.")
        elif sentiment_label == "Negative":
            rain_emojis("😞", 20, 2, "infinite")
            st.error("This text is perceived to be generally negative.")
        else:
            rain_emojis("😐", 20, 2, "infinite")
            st.info("This text is perceived to be neutral.")

        # Define colors based on sentiment
        if sentiment_label == "Positive":
            polarity_color = "green"
        elif sentiment_label == "Negative":
            polarity_color = "red"
        else:
            polarity_color = "blue"
        
        subjectivity_color = "yellow"

        # Plotting 2D chart
        st.subheader("Sentiment Visualization")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=['Polarity', 'Subjectivity'], y=[polarity, subjectivity], name='Sentiment Scores', marker_color=[polarity_color, subjectivity_color]))
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Please enter some text to analyze.")

st.markdown(
    """
    **EmoSense uses TextBlob to perform sentiment analysis on your entered text. It provides a sentiment label, polarity, subjectivity, emoticon, and explanation; thus sensing your emotion through the input.**
    """)
