# Import the required libraries
import streamlit as st
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.google import Gemini
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
import os

st.set_page_config(
    page_title="AI Research Copilot",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Research Copilot")
st.markdown(
    "Research any topic using multiple AI agents that search Hacker News, browse the web, and generate professional research reports."
)

with st.sidebar:
    st.header("⚙️ Settings")

    gemini_api_key = st.text_input(
        "Gemini API Key",
        type="password"
    )

    model_name = st.selectbox(
        "Gemini Model",
        [
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite"
        ]
    )

    research_type = st.selectbox(
        "Research Category",
        [
            "Artificial Intelligence",
            "Technology",
            "Cyber Security",
            "Business",
            "Science",
            "General"
        ]
    )

os.environ["GOOGLE_API_KEY"] = gemini_api_key

if gemini_api_key:
    hn_researcher = Agent(
        name="News Intelligence Agent",
        model=Gemini(id=model_name),
        role="Gets top stories from hackernews.",
        tools=[HackerNewsTools()],
    )

    web_searcher = Agent(
        name="Web Intelligence Agent",
        model=Gemini(id=model_name),
        role="Searches the web for information on a topic",
        tools=[DuckDuckGoTools()],
        add_datetime_to_context=True,
    )

    article_reader = Agent(
        name="Knowledge Extraction Agent",
        model=Gemini(id=model_name),
        role="Reads articles from URLs.",
        tools=[Newspaper4kTools()],
    )

    hackernews_team = Team(
        name="AI Research Team",
        model=Gemini(id=model_name),
        members=[hn_researcher, web_searcher, article_reader],
        instructions=[
            f"You are performing {research_type} research.",
            "Search Hacker News for relevant stories.",
            "Read the linked articles carefully.",
            "Search the web for additional information.",
            "Compare multiple reliable sources.",
            "Summarize the findings professionally.",
            "Provide key insights and important trends.",
            "Include reference links at the end.",
        ],
        markdown=True,
        debug_mode=False,
        show_members_responses=False,
    )

    # Input field for the report query
    query = st.text_area(
        "🔍 Research Topic",
        placeholder="Example: Latest AI Agent Frameworks",
        height=120
    )

    if st.button("🚀 Generate Research Report"):
        if query == "":
            st.warning("Please enter a research topic.")
            st.stop()

        with st.spinner("Researching..."):

            response: RunOutput = hackernews_team.run(
                query,
                stream=False
            )

            st.success("Research Completed!")

            st.markdown(response.content)

            st.download_button(
                "📄 Download Report",
                response.content,
                file_name="research_report.md"
            )