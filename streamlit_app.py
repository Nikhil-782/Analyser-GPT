import streamlit as st
import os
import asyncio
from autogen_agentchat.base import TaskResult
from models.openrouter_model_client import get_model_client
from config.docker_util import *
from teams.analyzer_gpt import *

st.set_page_config(
    page_title="Analyzer GPT",
    page_icon="🤖"
)
st.title("Analyser-GPT")
if "messages" not in st.session_state:
    if os.path.exists("temp"):
        for file in os.listdir("temp"):
            os.remove(os.path.join("temp", file))

    st.session_state.messages = []

if "autogen_team_state" not in st.session_state:
    st.session_state.autogen_team_state = None
file = st.file_uploader("Upload a csv file", type="csv")

task = st.chat_input("Enter your task here.....")


async def run_analyser_gpt(task,docker,model):
    try:
        await start_docker(docker)
        team = getDataAnalyzerTeam(docker,model)
        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)

        async for message in team.run_stream(task=task):
            if not isinstance(message,TaskResult):
                if message.source == "user":
                    with st.chat_message("user", avatar="👤"):
                        st.markdown(message.content)
                elif message.source == "Data_Analyzer_agent":
                    if "STOP" in message.content:
                        with st.chat_message("Data_Analyzer_agent", avatar="👩‍💻"):
                           st.markdown(message.content[:message.content.find("STOP")])

                st.session_state.messages.append({
                    "type": "assistant",
                    "content": message,
                    "images": []
                })



        st.session_state.autogen_team_state = await team.save_state()
    except Exception as e:
        st.error(body=f"error:{e}")

    finally:
        await stop_docker(docker)
if st.session_state.messages:
    for msg in st.session_state.messages:
        if not isinstance(msg,TaskResult):

            if msg["content"].source == "Data_Analyzer_agent":
                if "STOP" in msg["content"].content:
                    with st.chat_message("assistant", avatar="👩‍💻"):
                        content = msg["content"].content
                        content = content[:content.find("STOP")]
                        st.markdown(content)
                        if msg["images"]:
                            for img in msg["images"]:
                                st.image(img)

            elif msg["content"].source == "user":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(msg["content"].content)


if task:
    if not os.path.exists("temp"):
        os.mkdir("temp")
    if file:
        csv_path = os.path.join("temp", file.name)

        if not os.path.exists(csv_path):
            with open(csv_path, "wb") as f:
                f.write(file.getbuffer())
        docker = getDockerCommandLineCodeExecutor()
        model = get_model_client()

        asyncio.run(run_analyser_gpt(task, docker, model))

        check_files = [
                img
                for msg in st.session_state.messages
                if isinstance(msg, dict)
                for img in msg["images"]
            ]
        png_files = [f for f in os.listdir('temp') if (f.endswith('.png') and os.path.join('temp', f) not in check_files)]
        if png_files:
                for png_file in png_files:
                    st.image(os.path.join('temp', png_file))
                    st.session_state.messages[-1]["images"].append(os.path.join('temp', png_file))
    else:
            st.warning("No file Uploaded")