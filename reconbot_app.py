import streamlit as st
import numpy as np
import base64


def play_sound(file_path):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay>
        <source src="data:audio/wav;base64,{b64}" type="audio/wav">
        </audio>
    """
    st.markdown(md, unsafe_allow_html=True)


if "ammo" not in st.session_state:
    st.session_state.ammo = 6
    st.session_state.kills = 0
    st.session_state.camo = "Neutral"
    st.session_state.log = []


st.title("🪖 ReconBot Tactical Simulation")


st.markdown(f"**Ammo:** {st.session_state.ammo}/6 | **Kills:** {st.session_state.kills} | **Camouflage:** {st.session_state.camo}")


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍 Scan Terrain"):
        terrain = np.random.randint(0,255,(128,128,3),dtype=np.uint8)
        avg_color = terrain.mean(axis=0).mean(axis=0)
        if avg_color[1] > 150:
            st.session_state.camo = "Green"
        elif avg_color[0] > 150:
            st.session_state.camo = "Blue"
        else:
            st.session_state.camo = "Dark"
        st.image(terrain, caption=f"Camouflage: {st.session_state.camo}")
        st.session_state.log.append("Scanning terrain... Camouflage adapted.")

with col2:
    if st.button("🔫 Fire"):
        if st.session_state.ammo == 0:
            st.session_state.log.append("Magazine empty! Reload required.")
        else:
            st.session_state.ammo -= 1
            st.session_state.kills += 1
            st.session_state.log.append("Enemy engaged! Kill confirmed.")
            play_sound("423301__u1769092__visceralbulletimpacts.wav")

with col3:
    if st.button("🔄 Reload"):
        st.session_state.ammo = 6
        st.session_state.log.append("Reloading magazine...")
        play_sound("674569__sertonin__browning-hi-power-handgun-being-reloaded-while-empty.wav")


st.subheader("📜 Kill Confirmation Log")
for entry in st.session_state.log[-10:]:
    st.write(entry)

st.markdown(f"**Ammo:** {st.session_state.ammo}/6 | **Kills:** {st.session_state.kills} | **Camouflage:** {st.session_state.camo}")

