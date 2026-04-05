# Install streamlit if not already
# !pip install streamlit

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Initialize session state
# -------------------------------
if "ammo" not in st.session_state:
    st.session_state.ammo = 6
    st.session_state.kills = 0
    st.session_state.camo = "Neutral"
    st.session_state.log = []

# -------------------------------
# App Title
# -------------------------------
st.title("🪖 ReconBot Tactical Simulation")

# -------------------------------
# Status Bar
# -------------------------------
st.markdown(f"**Ammo:** {st.session_state.ammo}/6 | **Kills:** {st.session_state.kills} | **Camouflage:** {st.session_state.camo}")

# -------------------------------
# Buttons
# -------------------------------
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

with col3:
    if st.button("🔄 Reload"):
        st.session_state.ammo = 6
        st.session_state.log.append("Reloading magazine...")

# -------------------------------
# Kill Log
# -------------------------------
st.subheader("📜 Kill Confirmation Log")
for entry in st.session_state.log[-10:]:
    st.write(entry)

# -------------------------------
# Updated Status Bar
# -------------------------------
st.markdown(f"**Ammo:** {st.session_state.ammo}/6 | **Kills:** {st.session_state.kills} | **Camouflage:** {st.session_state.camo}")
