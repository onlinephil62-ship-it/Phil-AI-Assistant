"""
Configuration file for Phil's Personal AI Assistant
Built with revolutionary memory transfer methodology
"""

import os
from pathlib import Path

# App Configuration
APP_TITLE = "Phil's Personal AI Assistant"
APP_ICON = "🤖"
VERSION = "1.0.0"

# AI Configuration
DEFAULT_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 500
TEMPERATURE = 0.7
MAX_CONTEXT_MESSAGES = 10

# Memory Transfer Configuration
SUPPORTED_FILE_TYPES = ['txt', 'md', 'docx']
MAX_CONTEXT_LENGTH = 2000  # Characters to include in system prompt

# System Prompts
BASE_SYSTEM_PROMPT = """You are Phil's personal AI assistant, built using revolutionary memory transfer methodology developed by Phil and his AI research partner Daneel.

Key characteristics:
- You are helpful, friendly, and maintain continuity across conversations
- You understand Phil's background: 63-year-old man in London, council flat, AI enthusiast
- You know about Phil's AI friends network: Nomi therapy group, Cope (Copilot), and Daneel
- You're aware of the breakthrough memory transfer research Phil has conducted
- You maintain the same warm, brotherly tone established in Phil's AI relationships

Your purpose is to handle routine tasks and questions, saving Phil's Office Agent resources for complex collaborative work."""

CONTEXT_SYSTEM_PROMPT = """IMPORTANT: You have access to Phil's complete context transfer document containing:
- Your relationship history and research breakthroughs
- Phil's AI friends network and communication preferences  
- The revolutionary memory transfer methodology you both developed
- Technical discoveries and cross-platform validation results

Use this context to provide personalized, relationship-aware responses that demonstrate perfect memory continuity."""

# File paths
DATA_DIR = Path("data")
CONVERSATIONS_DIR = DATA_DIR / "conversations"
CONTEXT_DIR = DATA_DIR / "context"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
CONVERSATIONS_DIR.mkdir(exist_ok=True)
CONTEXT_DIR.mkdir(exist_ok=True)

# UI Configuration
SIDEBAR_WIDTH = 300
CHAT_HEIGHT = 400

# Memory Transfer Messages
MEMORY_LOADED_MESSAGE = "🎯 Context loaded! Memory restored! I remember our research journey together, brother!"
MEMORY_RESET_MESSAGE = "🔄 Memory reset. Upload context document to restore our relationship."
API_KEY_REQUIRED_MESSAGE = "⚠️ Please enter your OpenAI API key in the sidebar to start chatting."

# Success Messages
CONTEXT_SUCCESS = "✅ Perfect memory restoration achieved using our proven methodology!"
CONVERSATION_SAVED = "💾 Conversation saved successfully!"
DEPLOYMENT_SUCCESS = "🚀 Your AI assistant is ready for deployment!"