import streamlit as st

# screen configuration
st.set_page_config(page_title="Podcast Player", page_icon="🎧", layout="wide")

# custom CSS with modern fonts and improved styles
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            background-attachment: fixed;
            font-family: 'Poppins', sans-serif;
            color: #e0e0e0;
        }
        /* Streamlit button styles */
        div.stButton > button {
            background: linear-gradient(90deg, #4b5efb 0%, #8a2be2 100%);
            color: white;
            font-weight: 600;
            border-radius: 12px;
            transition: all 0.3s ease;
            width: 160px;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 12px;
            border: none;
            font-size: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        div.stButton > button:hover {
            background: linear-gradient(90deg, #6b7bff 0%, #a44bff 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }
        /* Audio player styles */
        audio {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        /* Expander header styles */
        .expander-header {
            font-size: 1.5rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1rem;
        }
        /* Expander box styles */
        .stExpander {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        /* Input field styles */
        .stTextInput > div > div > input {
            background-color: #2a2a3b;
            color: #e0e0e0;
            border-radius: 8px;
            border: 1px solid #4b5efb;
        }
        .stSelectbox > div > div > select {
            background-color: #2a2a3b;
            color: #e0e0e0;
            border-radius: 8px;
            border: 1px solid #4b5efb;
        }
        /* Message box styles */
        .stInfo, .stSuccess, .stWarning, .stError {
            border-radius: 8px;
            padding: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Default stations data with genres
default_stations = {
    "Iran International": {"url": "https://stream.radiojar.com/dfnrphnr5f0uv", "genre": "News"},
    "Radio Farda": {"url": "https://n06.radiojar.com/cp13r2cpn3quv?rj-ttl=5", "genre": "News"},
    "DW Radio 08C": {"url": "https://dw.audiostream.io/dw/1027/mp3/64/dw08", "genre": "News"},
    "DEUTSCH": {"url": "https://deutsch.stream.laut.fm/deutsch", "genre": "Music"},
    "berlin info": {"url": "http://dispatcher.rndfnk.com/rbb/inforadio/live/mp3/mid", "genre": "News"},
    "Neue Deutsche Welle": {"url": "https://stream.rpr1.de/exndw/mp3-128/", "genre": "Music"},
    "Deutschlandfunk": {"url": "https://st01.sslstream.dlf.de/dlf/01/128/mp3/stream.mp3", "genre": "News"},
    "hr3": {"url": "https://dispatcher.rndfnk.com/hr/hr3-sued/mp3/high", "genre": "Music"},
    "FluxFM": {"url": "http://channels.fluxfm.de/FluxFM/stream.mp3", "genre": "Music"},
}

# Initialize session_state
if "saved_stations" not in st.session_state:
    st.session_state.saved_stations = {}
if "podcast_url" not in st.session_state:
    st.session_state.podcast_url = ""
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False

# Application Header
with st.container():
    st.markdown("<h1 class='text-3xl font-bold text-white text-center mb-6'>🎧 Podcast & Radio Player</h1>", unsafe_allow_html=True)

# Search & Filter Section
with st.expander("🔍 Search & Filter Stations", expanded=True):
    col1, col2 = st.columns([2, 1], gap="medium")
    search_query = col1.text_input("Search stations:", placeholder="Enter station name...")
    genres = ["All"] + sorted(set(st["genre"] for st in default_stations.values()) | set(st.get("genre", "Custom") for st in st.session_state.saved_stations.values()))
    selected_genre = col2.selectbox("Filter by genre:", genres)

# Filter stations based on search and genre
filtered_default_stations = {
    name: info for name, info in default_stations.items()
    if (selected_genre == "All" or info["genre"] == selected_genre) and (search_query.lower() in name.lower() or not search_query)
}
filtered_saved_stations = {
    name: info for name, info in st.session_state.saved_stations.items()
    if (selected_genre == "All" or info.get("genre", "Custom") == selected_genre) and (search_query.lower() in name.lower() or not search_query)
}
# Default Stations
with st.expander("🌐 Default Stations", expanded=True):
    if filtered_default_stations:
        cols = st.columns(min(len(filtered_default_stations), 5))
        for i, (name, info) in enumerate(filtered_default_stations.items()):
            if cols[i % 5].button(name, key=f"default_{name}", help=f"Genre: {info['genre']}"):
                st.session_state.podcast_url = info["url"]
                st.session_state.is_playing = True
    else:
        st.info("No default stations match your search or filter.")

# Saved Stations
with st.expander("💾 Saved Stations", expanded=len(filtered_saved_stations) > 0):
    if filtered_saved_stations:
        for name, info in list(filtered_saved_stations.items()):
            col1, col2 = st.columns([4, 1], gap="small")
            if col1.button(f"▶ {name}", key=f"play_{name}"):
                st.session_state.podcast_url = info["url"]
                st.session_state.is_playing = True
            if col2.button("🗑", key=f"delete_{name}", help="Delete station"):
                del st.session_state.saved_stations[name]
                st.success(f"Deleted station: {name}")
                st.rerun()
    else:
        st.info("No saved stations match your search or filter.")

# Add Custom Station
with st.expander("🎙 Add Custom Station", expanded=True):
    with st.form("save_form"):
        col1, col2 = st.columns([3, 1], gap="medium")
        custom_url = col1.text_input("Paste a podcast/radio URL:", key="custom_url", placeholder="e.g., https://stream.radiojar.com/...")
        custom_genre = col2.selectbox("Genre:", ["Custom"] + sorted(set(st["genre"] for st in default_stations.values())))
        label = st.text_input("Station name:", value="My Custom Station")
        save = st.form_submit_button("💾 Save Station")
        if save:
            if not label.strip():
                st.warning("Please enter a name for the station.")
            elif label.strip() in st.session_state.saved_stations or label.strip() in default_stations:
                st.warning("A station with this name already exists.")
            elif not custom_url:
                st.warning("Please enter a valid URL.")
            else:
                st.session_state.saved_stations[label.strip()] = {"url": custom_url, "genre": custom_genre}
                st.success(f"Saved '{label}' to your station list.")
                st.rerun()

# Audio Player
with st.container():
    st.markdown("<h3 class='text-xl font-semibold text-white mb-4'>Now Playing</h3>", unsafe_allow_html=True)
    if st.session_state.podcast_url:
        try:
            st.audio(st.session_state.podcast_url, autoplay=st.session_state.is_playing)
            col1, col2 = st.columns(2, gap="medium")
            if col1.button("⏯ Pause/Play", key="toggle_play"):
                st.session_state.is_playing = not st.session_state.is_playing
                st.rerun()
            if col2.button("⏹ Stop", key="stop_play"):
                st.session_state.podcast_url = ""
                st.session_state.is_playing = False
                st.rerun()
            current_station = next((name for name, info in {**default_stations, **st.session_state.saved_stations}.items() if info.get("url") == st.session_state.podcast_url), "Custom URL")
            st.markdown(f"<p class='text-white text-lg'>Playing: <b>{current_station}</b></p>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error loading URL: {e}")
    else:
        st.info("Select a station or enter a URL to start listening.")

# Useful Links
st.markdown(
    """
    <p class='text-white text-center mt-6'>
        Find more stations at: 
        <a href='https://radio-browser.info/' class='text-blue-300 hover:underline'>Radio Browser</a> | 
        <a href='https://streamurl.link/' class='text-blue-300 hover:underline'>StreamURL</a>
    </p>
    """,
    unsafe_allow_html=True
)