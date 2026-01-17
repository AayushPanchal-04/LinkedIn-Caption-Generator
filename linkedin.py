import streamlit as st
import requests
import json

# Page config
st.set_page_config(
    page_title="LinkedIn Caption Generator",
    page_icon="💼",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .caption-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0077b5;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("LinkedIn Caption Generator")
st.markdown("Generate engaging LinkedIn post captions powered by AI")

# Function to call Groq API directly
def generate_caption(api_key, project_details, tone, include_hashtags, caption_length):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    prompt = f"""You are a professional LinkedIn content creator. Generate an engaging LinkedIn post caption based on the following project details.

Project Details: {project_details}

Tone: {tone}
Include Hashtags: {include_hashtags}
Caption Length: {caption_length}

Requirements:
- Make it professional yet engaging
- Start with a hook to grab attention
- Highlight key achievements and learnings
- Use emojis strategically (but not excessively)
- Include a call-to-action at the end
- If hashtags are requested, add 5-7 relevant hashtags at the end
- Match the requested tone and length

Generate the LinkedIn caption:"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1000,
        "top_p": 1,
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            raise Exception(f"Unexpected API response: {result}")
            
    except requests.exceptions.HTTPError as e:
        error_detail = ""
        try:
            error_detail = response.json()
        except:
            error_detail = response.text
        raise Exception(f"API Error ({response.status_code}): {error_detail}")
    except Exception as e:
        raise Exception(f"Error: {str(e)}")

# Sidebar for API key
with st.sidebar:
    st.header("Configuration")
    groq_api_key = st.text_input("Enter Groq API Key", type="password")
    st.markdown("---")
    st.markdown("### About")
    st.info("This tool uses AI to generate professional and catchy LinkedIn captions from your project details.")
    st.markdown("### Tips")
    st.markdown("""
    - Be specific about your project
    - Include key achievements
    - Mention technologies used
    - Add any impact metrics
    """)

# Main content
if groq_api_key:
    # Input section
    st.subheader("Project Details")
    project_details = st.text_area(
        "Describe your project",
        placeholder="Example: Built a machine learning model that predicts customer churn with 92% accuracy using Python and scikit-learn. Reduced customer attrition by 15% in 3 months...",
        height=150
    )
    
    # Options
    col1, col2 = st.columns(2)
    
    with col1:
        tone = st.selectbox(
            "Select Tone",
            ["Professional", "Inspirational", "Casual", "Technical", "Story-telling"]
        )
        
    with col2:
        caption_length = st.selectbox(
            "Caption Length",
            ["Short (2-3 sentences)", "Medium (4-6 sentences)", "Long (7+ sentences)"]
        )
    
    include_hashtags = st.checkbox("Include Hashtags", value=True)
    
    # Generate button
    if st.button("Generate Caption", type="primary"):
        if project_details:
            with st.spinner("Generating your LinkedIn caption..."):
                try:
                    # Generate caption
                    response = generate_caption(
                        groq_api_key,
                        project_details,
                        tone,
                        "Yes" if include_hashtags else "No",
                        caption_length
                    )
                    
                    # Display result
                    st.success("Caption Generated Successfully")
                    st.markdown("### Your LinkedIn Caption:")
                    st.markdown(f'<div class="caption-box">{response}</div>', unsafe_allow_html=True)
                    
                    # Copy button
                    st.code(response, language=None)
                    st.info("Tip: Click the copy icon in the top-right corner of the box above to copy your caption")
                    
                    # Character count
                    char_count = len(response)
                    st.caption(f"Character count: {char_count} (LinkedIn limit: 3000)")
                    
                except Exception as e:
                    st.error(f"Error generating caption: {str(e)}")
                    st.info("Please check your API key and internet connection.")
        else:
            st.warning("Please enter project details first")
    
    # Example projects
    with st.expander("See Example Projects"):
        st.markdown("""
        **Example 1 - Web Development:**
        "Developed a full-stack e-commerce platform using React, Node.js, and MongoDB. Implemented secure payment gateway, real-time inventory management, and achieved 500+ daily active users within first month."
        
        **Example 2 - Data Science:**
        "Created a sentiment analysis model for customer reviews using NLP and deep learning. Processed 100K+ reviews with 89% accuracy, helping the marketing team improve product positioning."
        
        **Example 3 - Mobile App:**
        "Built a fitness tracking mobile app with React Native. Features include workout plans, progress tracking, and social sharing. Reached 10K downloads in first 2 weeks on Play Store."
        """)
        
else:
    st.warning("Please enter your Groq API key in the sidebar to get started")
    st.markdown("---")
    st.markdown("### How to get a Groq API Key:")
    st.markdown("""
    1. Visit [console.groq.com](https://console.groq.com)
    2. Sign up or log in
    3. Navigate to API Keys section
    4. Create a new API key
    5. Copy and paste it in the sidebar
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-weight: bold;'>Built by Aayush Panchal</div>",
    unsafe_allow_html=True
)
