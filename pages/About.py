import streamlit as st

def about_page():
    st.title("About the Developer")
    st.image('static/developer.jpg', width=400)
    
    st.subheader("Introduction")
    st.markdown("This Streamlit app has been developed by **Manoswita Bose (2347238)** of **MCA-B, CHRIST (Deemed to be University)**.", unsafe_allow_html=True)
    
    st.subheader("Things you should probably know about Manoswita")
    st.markdown(
        """
        - She hails from the sweetest part of India - West Bengal.
        - Besides books, she is a full-time Wikipedia reader.
        - She is a great cook, by the way. Not of food, but of stories.
        - She is a staunch believer in retail therapy - shopping makes her heart happy.
        - She writes, codes, and illustrates. But more often than not, she procrastinates.
        """
    )
    
    st.subheader("Contact Information")
    st.markdown("Reach out to her at **manoswita.bose@mca.christuniversity.in**", unsafe_allow_html=True)

# Main function to run the app
def main():
    st.set_page_config(
        page_title="Developer Information",
        page_icon="💟",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    about_page()

if __name__ == "__main__":
    main()


