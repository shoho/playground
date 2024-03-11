from dotenv import load_dotenv
from langchain.schema  import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

import os

load_dotenv()

def load_google(model_name):
	return ChatGoogleGenerativeAI(
		model=model_name,
		convert_system_message_to_human=True
	)

def load_openai(model_name):
	return ChatOpenAI(
		temperature=0, 
		model_name=model_name
	)

def load_anthropic(model_name):
	return ChatAnthropic(
		temperature=0, 
		model_name=model_name
	)

human_prompt = "くまモンってなに？"
chat_prompt = ChatPromptTemplate.from_messages([
		HumanMessagePromptTemplate.from_template(human_prompt)
])


#3chat = load_anthropic("claude-3-sonnet-20240229")
#3result = chat.invoke(chat_prompt.format_prompt().to_messages())
#3print(result.content)

#chat = load_openai("gpt-4")
#result = chat.invoke(chat_prompt.format_prompt().to_messages())
#print(result.content)

#chat = load_openai("gpt-4-0125-preview")
#result = chat.invoke(chat_prompt.format_prompt().to_messages())
#print(result.content)

#chat = load_google("gemini-pro")
#result = chat.invoke(messages)
#print(result.content)

