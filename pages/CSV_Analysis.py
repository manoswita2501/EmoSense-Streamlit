import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import cleantext
from textblob import TextBlob

# Setting page icon
st.set_page_config(
    page_title="CSV Analysis",  # Setting page title
    page_icon="📊",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="collapsed"    # Expanding sidebar by default    
)

# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    # Clean the text
    cleaned_text = cleantext.clean(text)
    
    # Performing sentiment analysis
    blob = TextBlob(cleaned_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determining sentiment category and color
    if polarity > 0:
        sentiment_category = 'Positive'
        polarity_color = 'green'
        color = 'green'
    elif polarity < 0:
        sentiment_category = 'Negative'
        polarity_color = 'red'
        color = 'red'
    else:
        sentiment_category = 'Neutral'
        polarity_color = 'blue'
        color = 'blue'
    
    # Assigning colors for subjectivity
    subjectivity_color = 'yellow'
    
    return polarity, subjectivity, sentiment_category, polarity_color, subjectivity_color, color

# Page Title
st.title('Sentiment Analysis from CSV Files')

# File Upload
uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:
    # Reading CSV with specified encoding
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        # Trying a different encoding if 'utf-8' fails
        try:
            df = pd.read_csv(uploaded_file, encoding='latin-1')
        except UnicodeDecodeError:
            df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
    
    # Displaying original dataset
    st.write('Original Dataset:')
    st.write(df)
    
    # Getting unique row numbers
    row_numbers = df.index
    
    # Allowing user to choose a specific row number
    selected_row_number = st.selectbox('Select Row Number:', row_numbers)
    
    # Performing sentiment analysis on the selected row's text
    polarity, subjectivity, sentiment_category, color, polarity_color, subjectivity_color = perform_sentiment_analysis(df.iloc[selected_row_number]['text'])
    
    # Displaying sentiment analysis results
    st.write('Sentiment Analysis of Text associated with the row number entered by you:')
    st.write(f'Polarity: {polarity}')
    st.write(f'Subjectivity: {subjectivity}')
    st.write(f'Sentiment Category: <font color="{color}">{sentiment_category}</font>', unsafe_allow_html=True)
    
    # Plotting polarity and subjectivity as bar charts
    fig = go.Figure(data=[
        go.Bar(name='Polarity', x=['Polarity'], y=[polarity], marker_color=polarity_color),
        go.Bar(name='Subjectivity', x=['Subjectivity'], y=[subjectivity], marker_color=subjectivity_color)
    ])
    
    # Adding layout settings
    fig.update_layout(barmode='group', title='Sentiment Analysis', xaxis_title='Sentiment Measure', yaxis_title='Score')
    
    # Displaying the plot
    st.plotly_chart(fig)
