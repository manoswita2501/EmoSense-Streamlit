import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import cleantext
from textblob import TextBlob

# Set page icon
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
    
    # Perform sentiment analysis
    blob = TextBlob(cleaned_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment category and color
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
    
    # Assign colors for subjectivity
    subjectivity_color = 'yellow'
    
    return polarity, subjectivity, sentiment_category, polarity_color, subjectivity_color, color

# Page Title
st.title('Sentiment Analysis from CSV Files')

# File Upload
uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:
    # Read CSV with specified encoding
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        # Try a different encoding if 'utf-8' fails
        try:
            df = pd.read_csv(uploaded_file, encoding='latin-1')
        except UnicodeDecodeError:
            df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
    
    # Display original dataset
    st.write('Original Dataset:')
    st.write(df)
    
    # Clean the dataset
    df['Cleaned Text'] = df['text'].apply(lambda x: cleantext.clean(x) if isinstance(x, str) else '')
    
    # Get unique recipe numbers
    column_numbers = df['recipe_number'].unique()
    
    # Allow user to choose a specific recipe number
    selected_column_number = st.selectbox('Select Column Number:', column_numbers)
    
    # Filter DataFrame based on selected recipe number
    selected_row = df[df['recipe_number'] == selected_column_number].iloc[0]  # Assuming only one row per recipe number
    
    # Perform sentiment analysis on the selected row's text
    polarity, subjectivity, sentiment_category, color, polarity_color, subjectivity_color = perform_sentiment_analysis(selected_row['Cleaned Text'])
    
    # Display sentiment analysis results
    st.write('Sentiment Analysis of Text associated with the column number entered by you:')
    st.write(f'Polarity: {polarity}')
    st.write(f'Subjectivity: {subjectivity}')
    st.write(f'Sentiment Category: <font color="{color}">{sentiment_category}</font>', unsafe_allow_html=True)
    
    # Plotting polarity and subjectivity as bar charts
    fig = go.Figure(data=[
        go.Bar(name='Polarity', x=['Polarity'], y=[polarity], marker_color=polarity_color),
        go.Bar(name='Subjectivity', x=['Subjectivity'], y=[subjectivity], marker_color=subjectivity_color)
    ])
    
    # Add layout settings
    fig.update_layout(barmode='group', title='Sentiment Analysis', xaxis_title='Sentiment Measure', yaxis_title='Score')
    
    # Display the plot
    st.plotly_chart(fig)
