# Try new OpenAI API first, fall back to old
try:
    # New OpenAI API (v1.0+)
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(...)
except ImportError:
    # Old OpenAI API (v0.28)
    import openai
    openai.api_key = api_key
    response = openai.ChatCompletion.create(...)
""")
