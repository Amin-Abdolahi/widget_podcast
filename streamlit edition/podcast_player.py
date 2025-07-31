import streamlit as st

st.set_page_config(page_title="Podcast Player", page_icon="🎧", layout="wide")
col1, col2, col3 = st.columns(3)
col1.title("🎧 Podcast Player")

# Default Stations
default_stations = {
    "Iran International": "https://stream.radiojar.com/dfnrphnr5f0uv",
    "Radio Farda": "https://n06.radiojar.com/cp13r2cpn3quv?rj-ttl=5",
    "DW Radio 08C": "https://dw.audiostream.io/dw/1027/mp3/64/dw08",
    "DEUTSCH": "https://deutsch.stream.laut.fm/deutsch",
    "berlin info": "http://dispatcher.rndfnk.com/rbb/inforadio/live/mp3/mid",
    "Neue Deutsche Welle": "https://stream.rpr1.de/exndw/mp3-128/",
    "Deutschlandfunk" : "https://st01.sslstream.dlf.de/dlf/01/128/mp3/stream.mp3",
    "hr3" : "https://dispatcher.rndfnk.com/hr/hr3-sued/mp3/high"
}

# Saved Custom Stations
if "saved_stations" not in st.session_state:
    st.session_state.saved_stations = {}

if "podcast_url" not in st.session_state:
    st.session_state.podcast_url = ""

# Default Stations
st.subheader("🌐 Default Stations")
cols = st.columns(15)
for i, (name, url) in enumerate(default_stations.items()):
    if cols[i % 5].button(name):
        st.session_state.podcast_url = url
        st.session_state.custom_url = ""

col1, col2, col3 = st.columns(3)
# Saved Stations
if st.session_state.saved_stations:
    st.subheader("💾 Saved Stations")
    for name, url in list(st.session_state.saved_stations.items()):
        col1, col2 = st.columns([4, 1])
        if col1.button(f"▶ {name}", key=f"play_{name}"):
            st.session_state.podcast_url = url
            st.session_state.custom_url = ""
        if col2.button("🗑", key=f"delete_{name}"):
            del st.session_state.saved_stations[name]
            st.success(f"Deleted station: {name}")
            st.rerun()



# User Custom URL Input
st.divider()
st.subheader("🎙 Add a custom podcast URL")
custom_url = st.text_input("Paste a podcast URL here:", key="custom_url", width=500)

if custom_url:
    st.session_state.podcast_url = custom_url
    st.success("Custom URL loaded. Click 'Save' to add it to the station list.")

    with st.form("save_form"):
        label = st.text_input("Name for this station", value="My Custom Station")
        save = st.form_submit_button("💾 Save this station")
        if save:
            if label.strip():
                if label.strip() in st.session_state.saved_stations:
                    st.warning("A station with this name already exists. Please choose a different name.")
                else:
                    st.session_state.saved_stations[label.strip()] = custom_url
                    st.success(f"Saved '{label}' to your station list.")
                    st.rerun()
            else:
                st.warning("Please enter a name for the station before saving.")

        else:
            st.warning("Please enter a name for the station before saving.")
# Player
st.divider()
if st.session_state.podcast_url:
    try:
        st.audio(st.session_state.podcast_url, autoplay=True, width=500)
    except Exception as e:
        st.error(f"Error loading podcast: {e}")
else:
    st.info("Please select a station or enter a URL to start listening.")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://streamurl.link/assets/img/streamurl.link/radio.webp');
        background-size: cover;
        background-position: center;
    }
    .stButton>button {
        background-color: #ffffff33;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.3s ease-in-out;
        display: block;
        width: 100%;
        max-width: 600px;
        height: 75px;

    }
    .stButton>button:hover {
        background-color: #ffffffaa;
        color: black;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Links
st.write("use this links to find stations: [Radio Browser](https://radio-browser.info/) or [StreamURL](https://streamurl.link/)")
