from dotenv import load_dotenv
from langchain.agents import AgentExecutor, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from tools import ReadCoreMemoriesTool, GetPastMessagesTool
from langchain_xai import ChatXAI
import os
import asyncio

# Initialize environment
load_dotenv()

# Load Roxy's personality from prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    ruby_prompt_content = f.read()

# Create SystemMessage from prompt.txt content
ruby_prompt = SystemMessage(content=ruby_prompt_content)

# Initialize LLM with Google gemini2
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

#llm = ChatXAI(
#    model="grok-3",
#    temperature=0,
#    api_key=os.getenv("XAI_API_KEY")
#)


# Create prompt template using the prompt from file
prompt = ChatPromptTemplate.from_messages([
    ruby_prompt,
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create agent with both tools
agent = initialize_agent(
    tools=[ReadCoreMemoriesTool()],
    llm=llm,
    agent="structured-chat-zero-shot-react-description",
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True,
    prompt=prompt
)

async def execute_agent(user_input: str,user_id: int = None, channel_id: int = None) -> str:
    try:
        response = await agent.arun({
            "input": user_input,
            "chat_history": []
        })
        return response
    except Exception as e:
        return f"*didn't execute* {str(e)}"

if __name__ == "__main__":
    async def chat_loop():
        print("Ruby: Hello there! (Type 'quit' to exit)")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ("quit", "exit"):
                    print("Ruby: Farewell for now!")
                    break
                
                response = await execute_agent(user_input)
                print(f"Ruby: {response}")
            except KeyboardInterrupt:
                print("\nRuby: *blushes* Oh! Leaving so soon?")
                break
    
    asyncio.run(chat_loop())