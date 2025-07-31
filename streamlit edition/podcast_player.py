import streamlit as st

st.set_page_config(page_title="Podcast Player", layout="centered")

st.title("🎧 Podcast Player")
st.write("Select a podcast to play:")

# Default Stations
default_stations = {
    "Iran International": "https://stream.radiojar.com/dfnrphnr5f0uv",
    "Radio Farda": "https://n06.radiojar.com/cp13r2cpn3quv?rj-ttl=5",
    "DW Radio 08C": "https://dw.audiostream.io/dw/1027/mp3/64/dw08",
    "DEUTSCH": "https://deutsch.stream.laut.fm/deutsch"
}

# Saved Custom Stations
if "saved_stations" not in st.session_state:
    st.session_state.saved_stations = {}

if "podcast_url" not in st.session_state:
    st.session_state.podcast_url = ""

# Default Stations
st.subheader("🌐 Default Stations")
cols = st.columns(3)
for i, (name, url) in enumerate(default_stations.items()):
    if cols[i % 3].button(name):
        st.session_state.podcast_url = url
        st.session_state.custom_url = ""

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
            st.experimental_rerun()



# User Custom URL Input
st.divider()
st.subheader("🎙 Add a custom podcast URL")
custom_url = st.text_input("Paste a podcast URL here:", key="custom_url")

if custom_url:
    st.session_state.podcast_url = custom_url
    st.success("Custom URL loaded. Click 'Save' to add it to the station list.")

    with st.form("save_form"):
        label = st.text_input("Name for this station", value="My Custom Station")
        save = st.form_submit_button("💾 Save this station")
        if save:
            if label.strip():
                st.session_state.saved_stations[label.strip()] = custom_url
                st.success(f"Saved '{label}' to your station list.")
                st.experimental_rerun()
            else:
                st.warning("Please enter a name for the station before saving.")

# Player
st.divider()
if st.session_state.podcast_url:
    st.audio(st.session_state.podcast_url)
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
st.write("use this link to find stations: [Radio Browser](https://radio-browser.info/) or [StreamURL](https://streamurl.link/)")
