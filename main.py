from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool, keyword_showcase

load_dotenv()


class QuestionResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]
    toolUsed: list[str]


llm = ChatAnthropic(model="claude-3.5-sonnet")
parser = PydanticOutputParser(pydantic_object=QuestionResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer user questions using necessary tools. "
                   "Wrap the output in given format without any extra text -> {format_instructions}"),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [
    search_tool,
    wiki_tool,
    save_tool,
]

agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("Enter your question: ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"]) 
    keywords = keyword_showcase(structured_response) 
    save_tool(content=structured_response, keywords=keywords)
except Exception as e:
    print("Error:", e)
