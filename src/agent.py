from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import os
from src.config import GEMINI_API_KEY

# Initialize LLM (Google Gemini API via LangChain)
llm = ChatOpenAI(openai_api_key=GEMINI_API_KEY)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define tools (Advanced tasks)
def summarize_text(text):
    return "[Summarized] " + text[:50]  # Mock summarization

def analyze_sentiment(text):
    return "Positive" if "good" in text.lower() else "Negative"

def extract_entities(text):
    return {"Entities": ["AI", "Machine Learning"]}  # Mock entity extraction

def generate_code(prompt):
    return "print('Hello World')" if "Python" in prompt else "Code generation not supported."

def translate_text(text, target_language="fr"):
    return f"Translated ({target_language}): {text}"  # Mock translation

tools = [
    Tool(name="Summarization", func=summarize_text, description="Summarize input text."),
    Tool(name="Sentiment Analysis", func=analyze_sentiment, description="Analyze sentiment of text."),
    Tool(name="Entity Extraction", func=extract_entities, description="Extract named entities from text."),
    Tool(name="Code Generation", func=generate_code, description="Generate code from a prompt."),
    Tool(name="Translation", func=translate_text, description="Translate text into different languages."),
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

def run_agent(user_input):
    return agent.run(user_input)

if __name__ == "__main__":
    print(run_agent("Extract entities from: AI and Machine Learning are evolving fast."))
