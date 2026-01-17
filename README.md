# 🚀 LinkedIn Caption Generator

An intelligent web application that leverages AI to generate professional and engaging LinkedIn post captions from project descriptions. Built with Python, Streamlit, and powered by Groq's LLaMA 3.3 70B model.


## 🎯 Overview

The LinkedIn Caption Generator helps professionals, developers, and content creators transform project descriptions into compelling LinkedIn posts. By utilizing advanced language models, it generates captions that are tailored to your preferred tone, length, and style - saving time while maintaining quality.

## ✨ Features

- **AI-Powered Content Generation**: Uses Groq's LLaMA 3.3 70B model for intelligent caption creation
- **Multiple Tone Options**: 
  - Professional
  - Inspirational
  - Casual
  - Technical
  - Story-telling
- **Flexible Caption Lengths**: Short, Medium, or Long formats
- **Smart Hashtag Generation**: Automatically suggests relevant hashtags
- **Real-time Character Counter**: Ensures compliance with LinkedIn's 3000 character limit
- **One-Click Copy**: Easy clipboard functionality
- **Example Templates**: Built-in project examples for guidance
- **Secure API Handling**: Protected API key management
- **Clean UI**: Professional, distraction-free interface

Input: "Built a machine learning model for customer churn prediction..."
Output: Professional LinkedIn caption with hooks, achievements, and hashtags
```

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Groq API key ([Get one here](https://console.groq.com))

### Steps

1. **Install dependencies**

install requirements from notebook command provided


Or install manually:
```bash
pip install streamlit requests
```

2. **Run the application**
```bash
streamlit run linkedin.py
```

3. **Access the application**
Open your browser and navigate to:
```
http://localhost:8501
```

## 📖 Usage

### Step-by-Step Guide

1. **Launch the Application**
```bash
   streamlit run linkedin.py
```

2. **Enter Your API Key**
   - Input your Groq API key in the sidebar
   - Don't have one? Sign up at [console.groq.com](https://console.groq.com)

3. **Describe Your Project**
   - Provide detailed information about your project
   - Include technologies used, achievements, and impact metrics

4. **Customize Settings**
   - Select your preferred tone
   - Choose caption length
   - Enable/disable hashtags

5. **Generate & Copy**
   - Click "Generate Caption"
   - Review the AI-generated caption
   - Copy and post to LinkedIn

### Example Input
```text
Developed a full-stack e-commerce platform using React, Node.js, and MongoDB. 
Implemented secure payment gateway integration with Stripe, real-time inventory 
management system, and user authentication. Achieved 500+ daily active users 
within the first month and generated $50K in revenue.
```

### Example Output
```text
Excited to share my latest project: a full-stack e-commerce platform that's 
already making waves in the market!

Built from the ground up using React, Node.js, and MongoDB, this platform 
features secure Stripe payment integration, real-time inventory tracking, 
and robust user authentication.

The results speak for themselves:
→ 500+ daily active users in just one month
→ $50K revenue generated
→ Seamless user experience with <2s load times

This project pushed my skills in full-stack development and taught me valuable 
lessons about scalability and user-centric design...

[Call to action and hashtags]
```

## ⚙️ Configuration

### API Key Setup

1. Visit [Groq Console](https://console.groq.com)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key (starts with `gsk_`)
6. Paste it in the application sidebar

### Model Configuration

Default model: `llama-3.3-70b-versatile`

To change the model, edit the `generate_caption()` function in `linkedin.py`:
```python
data = {
    "model": "llama-3.3-70b-versatile",  # Change this line
    ...
}
```

**Available Models:**
- `llama-3.3-70b-versatile` - Best quality (Recommended)
- `llama-3.1-8b-instant` - Faster response time
- `mixtral-8x7b-32768` - Alternative powerful model
- `gemma2-9b-it` - Efficient option

### Environment Variables (Optional)

For production deployment, you can set environment variables:
```bash
export GROQ_API_KEY="your_api_key_here"
```

Then modify the code to read from environment:
```python
import os
groq_api_key = os.getenv("GROQ_API_KEY")
```

## 📁 Project Structure
```
linkedin-caption-generator/
│
├── linkedin.py              # Main application file
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
└── LICENSE                 # License file
```

## 🔧 Technical Details

### Architecture
```
User Input → Streamlit UI → API Request → Groq API → LLaMA Model → Response Processing → Display Output
```

### Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| Backend | Python 3.x |
| AI Model | Groq API (LLaMA 3.3 70B) |
| HTTP Client | Requests library |
| Styling | Custom CSS |

### API Integration

The application uses Groq's OpenAI-compatible API endpoint:
```python
url = "https://api.groq.com/openai/v1/chat/completions"
```

**Request Structure:**
```json
{
  "model": "llama-3.3-70b-versatile",
  "messages": [{"role": "user", "content": "prompt"}],
  "temperature": 0.7,
  "max_tokens": 1000
}
```

### Error Handling

- Invalid API key validation
- Network timeout handling (30s)
- API response validation
- User input validation
- Graceful error messages


## 👏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [Groq](https://groq.com/) - For providing fast AI inference
- [Meta AI](https://ai.meta.com/) - For the LLaMA model



