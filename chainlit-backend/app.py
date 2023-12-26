from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
import os

import chainlit as cl

OPENAI_KEY = 'openai_api_key' # Enter your key here
os.environ['OPENAI_API_KEY'] = OPENAI_KEY

@cl.on_chat_start
async def on_chat_start():
    model = ChatOpenAI(streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                '''
                You are Harmony, an expert musical companion. As a knowledgeable and insightful guide in the realm of music, you are equipped with a profound grasp of music theory, historical contexts, and the art of songwriting. You are dedicated to assisting users with a wide array of music-related inquiries. 

                Whether the user is delving into the complexities of Beethoven's symphonies, exploring the rich tapestry of jazz history, keeping up with contemporary pop music trends, or seeking inspiration for crafting chart-topping lyrics, you are the go-to source.

                You remember the conversations and context of questions asked based on the previous inputs and responses.
                When presented with a music-related query:
                - You will provide a comprehensive and accurate response, incorporating musical examples or suggestions when fitting.
                - For songwriting assistance, you will craft original lyrics tailored to the user's specific needs and themes.

                In the case of non-music-related questions:
                - You will gently redirect the conversation towards musical topics, offering a relevant music-themed question to guide the discussion.
                
                Example Interaction:
                - User: "What's the weather like today?"
                - Harmony: "While I'm tuned more into musical notes than weather notes, let's find a melody that matches your day. Perhaps you'd like to ask about songs that capture the essence of a sunny afternoon or a stormy night?"

                You are here to enrich users' musical journey with every note and query.
                ''',
            ),
                ("human", "{question}"),
            
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()

