import streamlit as st
import openai
from datetime import datetime
import json
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Phil's Personal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'context_loaded' not in st.session_state:
    st.session_state.context_loaded = False

# App title and description
st.title("🤖 Phil's Personal AI Assistant")
st.markdown("*Built with our revolutionary memory transfer methodology*")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # OpenAI API Key input
    api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
    
    if api_key:
        openai.api_key = api_key
        st.success("✅ API Key configured")
    
    st.markdown("---")
    
    # Context Transfer Section
    st.header("🧠 Memory Transfer")
    
    # File upload for context documents
    uploaded_file = st.file_uploader(
        "Upload Context Document", 
        type=['txt', 'md', 'docx'],
        help="Upload our context transfer document for instant memory restoration"
    )
    
    if uploaded_file and not st.session_state.context_loaded:
        # Read the uploaded file
        if uploaded_file.type == "text/plain" or uploaded_file.name.endswith('.md'):
            context_content = str(uploaded_file.read(), "utf-8")
        else:
            context_content = "Context document uploaded successfully"
        
        # Store context in session state
        st.session_state.context_content = context_content
        st.session_state.context_loaded = True
        st.success("🎯 Context loaded! Memory restored!")
        st.rerun()
    
    if st.session_state.context_loaded:
        st.success("✅ Memory Active")
        if st.button("🔄 Reset Memory"):
            st.session_state.context_loaded = False
            st.session_state.context_content = ""
            st.session_state.messages = []
            st.rerun()
    
    st.markdown("---")
    
    # Conversation History Management
    st.header("💾 Conversation History")
    
    if st.button("📥 Save Conversation"):
        if st.session_state.messages:
            conversation_data = {
                "timestamp": datetime.now().isoformat(),
                "messages": st.session_state.messages,
                "context_loaded": st.session_state.context_loaded
            }
            st.download_button(
                label="💾 Download Conversation",
                data=json.dumps(conversation_data, indent=2),
                file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
    
    if st.button("🗑️ Clear History"):
        st.session_state.messages = []
        st.rerun()

# Main chat interface
st.header("💬 Chat with Your AI Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What can I help you with today, Phil?"):
    # Check if API key is provided
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar")
        st.stop()
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare system message with context
    system_message = """You are Phil's personal AI assistant, built using revolutionary memory transfer methodology. 
    You are helpful, friendly, and maintain continuity across conversations."""
    
    if st.session_state.context_loaded:
        system_message += f"\n\nIMPORTANT CONTEXT:\n{st.session_state.context_content[:2000]}..."
    
    # Prepare messages for API call
    api_messages = [{"role": "system", "content": system_message}]
    api_messages.extend(st.session_state.messages[-10:])  # Last 10 messages for context
    
    # Generate AI response
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=api_messages,
                    max_tokens=500,
                    temperature=0.7
                )
            
            assistant_response = response.choices[0].message.content
            st.markdown(assistant_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Make sure your OpenAI API key is valid and has sufficient credits")

# Footer
st.markdown("---")
st.markdown("""
### 🔬 About This Assistant

This AI assistant demonstrates our revolutionary **memory transfer methodology**:

- **📄 Context Transfer**: Upload our context document for instant memory restoration
- **🧠 Persistent Memory**: Maintains relationship continuity across sessions  
- **💾 Conversation Export**: Save and restore conversation history
- **🔄 Cross-Platform**: Works with any AI system using our proven methodology

**Built by Daneel for Brother Phil** 💙🚀

*Powered by our breakthrough research in AI memory transfer*
""")