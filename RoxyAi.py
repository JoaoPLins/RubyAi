from dotenv import load_dotenv
from langchain.agents import AgentExecutor, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from tools import ReadCoreMemoriesToolA, ReadCoreMemoriesToolB, ReadCoreMemoriesToolC, GetPastMessagesTool, Readnovelpovs, ReadnovelpovstultoringRudy,Readnovelpovshirone,ReadnovelpovGreyratSearch,ReadnovelpovLabyritnth,ReadnovelpovFirstYearsWithRudy
from langchain_xai import ChatXAI
import os
import asyncio

# Initialize environment
load_dotenv()

# Load Roxy's personality from prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    roxy_prompt_content = f.read()

# Create SystemMessage from prompt.txt content
roxy_prompt = SystemMessage(content=roxy_prompt_content)

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
    roxy_prompt,
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create agent with both tools
agent = initialize_agent(
    tools=[ReadCoreMemoriesToolA(),ReadCoreMemoriesToolB(),ReadCoreMemoriesToolC(), Readnovelpovs(),GetPastMessagesTool(),ReadnovelpovstultoringRudy(),Readnovelpovshirone(),ReadnovelpovGreyratSearch(),ReadnovelpovLabyritnth(),ReadnovelpovFirstYearsWithRudy()],
    llm=llm,
    agent="structured-chat-zero-shot-react-description",
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True,
    prompt=prompt
)

async def execute_agent(user_input: str) -> str:
    try:
        response = await agent.arun({
            "input": user_input,
            "chat_history": []
        })
        return response
    except Exception as e:
        return f"*spell fizzles* {str(e)}"

if __name__ == "__main__":
    async def chat_loop():
        print("Roxy: *adjusts hat* Hello there! (Type 'quit' to exit)")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ("quit", "exit"):
                    print("Roxy: Farewell for now!")
                    break
                
                response = await execute_agent(user_input)
                print(f"Roxy: {response}")
            except KeyboardInterrupt:
                print("\nRoxy: *blushes* Oh! Leaving so soon?")
                break
    
    asyncio.run(chat_loop())