import streamlit as st
import os
import re
import base64
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

# Set page configurations
st.set_page_config(
    page_title="Anime Recommender",
    page_icon="🎌",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

# Inject Custom Elegant Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

/* Main font overrides */
html, body, [data-testid="stAppViewContainer"], .stApp {
    font-family: 'Inter', sans-serif;
    background-color: #0d0e12;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #12131a;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}

/* Gorgeous Header Banner Title */
.main-title {
    font-size: 2.8rem;
    font-weight: 800;
    margin-top: -20px;
    margin-bottom: 5px;
    background: linear-gradient(135deg, #FF3366 0%, #7928CA 50%, #00DFD8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
}

.sub-title {
    font-size: 1.1rem;
    color: #8A92A6;
    margin-bottom: 25px;
    font-weight: 300;
}

/* Premium anime card style */
.anime-card {
    background: linear-gradient(145deg, rgba(20, 21, 28, 0.9) 0%, rgba(13, 14, 18, 0.95) 100%);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    backdrop-filter: blur(10px);
}

.anime-card:hover {
    transform: translateY(-6px);
    border-color: rgba(0, 223, 216, 0.4);
    box-shadow: 0 20px 40px rgba(0, 223, 216, 0.12);
}

.card-badge {
    display: inline-block;
    background: linear-gradient(90deg, #FF3366 0%, #E22A5B 100%);
    color: white;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 50px;
    margin-bottom: 15px;
    letter-spacing: 0.8px;
    box-shadow: 0 4px 12px rgba(255, 51, 102, 0.3);
}

.card-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 16px;
    letter-spacing: -0.5px;
}

.label-title {
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    color: #00DFD8;
    letter-spacing: 0.8px;
    margin-top: 18px;
    margin-bottom: 6px;
}

.card-text {
    font-size: 1rem;
    color: #C3C7DB;
    line-height: 1.6;
    font-weight: 400;
}

/* Sidebar Custom List */
.sidebar-tech {
    padding: 10px 15px;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 8px;
    margin-bottom: 10px;
    font-size: 0.9rem;
    border-left: 3px solid #7928CA;
}

.sidebar-tech strong {
    color: #00DFD8;
}

/* Divider line */
.divider {
    height: 1px;
    background: rgba(255, 255, 255, 0.08);
    margin: 25px 0;
}
</style>
""", unsafe_allow_html=True)

def add_bg_from_local(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{encoded_string});
                background-size: cover;
                background-position: top center;
                background-attachment: fixed;
                background-repeat: no-repeat;
            }}
            /* Add an overlay to ensure text remains readable */
            .stApp::before {{
                content: "";
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                background-color: rgba(13, 14, 18, 0.85);
                z-index: -1;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Main Screen
banner_path = os.path.join("app", "anime_recommender_banner.png")
add_bg_from_local(banner_path)

# Cache initialization of RAG pipeline
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

try:
    pipeline = init_pipeline()
except Exception as e:
    st.error(f"Error loading vector database. Make sure you run data ingestion first! Detail: {e}")
    st.stop()

# Sidebar Setup
st.sidebar.markdown("<h2 style='text-align: center; color: white; font-family: \"Outfit\"; font-weight:800;'>🎌 Anime Recommender</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #8A92A6; font-size:0.95rem; margin-top:-15px;'>AI-Powered Anime Discovery Engine</p>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.sidebar.subheader("System Stack Details")
st.sidebar.markdown("""
<div class='sidebar-tech'><strong>Vector DB:</strong> ChromaDB</div>
<div class='sidebar-tech'><strong>Embeddings:</strong> HuggingFace (all-MiniLM-L6-v2)</div>
<div class='sidebar-tech'><strong>RAG Framework:</strong> LangChain</div>
<div class='sidebar-tech'><strong>LLM Engine:</strong> Groq (Llama 3.1 8B)</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.sidebar.subheader("Try these suggestions:")
suggestions = [
    "Space western adventure with high action",
    "Mind-bending psychological thrillers with twists",
    "Emotional, slice-of-life romance and drama",
    "High-school sports anime about self-discovery",
]
for sug in suggestions:
    if st.sidebar.button(sug, key=sug):
        st.session_state.search_query = sug

# Main Screen title
st.markdown("<h1 class='main-title'>Anime Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>State-of-the-art semantic search combined with Large Language Model generation to deliver precise recommendations strictly grounded in the database.</p>", unsafe_allow_html=True)

# Query state management
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# Input Field
query = st.text_input(
    "What kind of anime are you looking for today?",
    value=st.session_state.search_query,
    placeholder="e.g. space western action, psychological game survival, lighthearted highschool sports...",
    key="main_search_input"
)

# Robust recommendation parser
def parse_recommendations(text):
    # Regex to find numbered items (e.g., 1. **Title** or 1. **Title:**)
    items = re.split(r'\n(?=\d+\.\s+\*\*)', text.strip())
    parsed_animes = []
    
    for item in items:
        # Extract title
        title_match = re.search(r'\d+\.\s+\*\*(.*?)\*\*', item)
        if not title_match:
            continue
        title = title_match.group(1).replace(":", "").strip()
        
        # Extract Plot Summary
        plot_match = re.search(r'-\s*(?:Short\s+)?Plot\s+Summary:\s*(.*)', item, re.IGNORECASE)
        if not plot_match:
            plot_match = re.search(r'Plot:\s*(.*)', item, re.IGNORECASE)
        plot = plot_match.group(1).strip() if plot_match else ""
        
        # Extract Why it matches
        why_match = re.search(r'-\s*Why\s+it\s+matches\s*(?:your\s+preferences)?:\s*(.*)', item, re.IGNORECASE)
        if not why_match:
            why_match = re.search(r'Why:\s*(.*)', item, re.IGNORECASE)
        why = why_match.group(1).strip() if why_match else ""
        
        # Clean clean tags from markdown
        plot = re.sub(r'\*\*', '', plot)
        why = re.sub(r'\*\*', '', why)
        
        parsed_animes.append({
            "title": title,
            "plot": plot,
            "why": why
        })
    return parsed_animes

# Process and Render Query
if query:
    st.session_state.search_query = query
    with st.spinner("Analyzing semantics, querying local vector store, and running LLM inference..."):
        try:
            response = pipeline.recommend(query)
            
            st.markdown("<h2 style='color: white; font-weight:700; margin-bottom: 20px; font-family: \"Outfit\";'>Semantically Grounded Recommendations</h2>", unsafe_allow_html=True)
            
            parsed_animes = parse_recommendations(response)
            
            if parsed_animes:
                for idx, anime in enumerate(parsed_animes, 1):
                    card_html = f"""<div class='anime-card'>
    <div class='card-badge'>Recommendation #{idx}</div>
    <div class='card-title'>{anime['title']}</div>
    <div class='label-title'>Plot Summary</div>
    <div class='card-text'>{anime['plot'] if anime['plot'] else "No plot details available."}</div>
    <div class='label-title'>Semantic Match Analysis</div>
    <div class='card-text'>{anime['why'] if anime['why'] else "This title matches your preferences semantically based on genre and character themes."}</div>
</div>"""
                    st.markdown(card_html, unsafe_allow_html=True)
            else:
                # If parsing didn't match the expected structure, display the raw markdown
                st.info("Displaying raw RAG response:")
                st.markdown(response)
                
        except Exception as e:
            st.error(f"Failed to generate recommendations: {e}")
