from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import os
from src.config import GEMINI_API_KEY
from src.tools import summarize_text, analyze_sentiment, extract_entities, generate_code, translate_text

# Initialize LLM (Google Gemini API via LangChain)
llm = ChatOpenAI(openai_api_key=GEMINI_API_KEY)

# Define memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define tools (Advanced tasks)
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
