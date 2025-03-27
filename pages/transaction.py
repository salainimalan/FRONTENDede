import streamlit as st
import pandas as pd
# ✅ Check authentication status
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("⚠️ You must be logged in to access this page.")
    
    # ✅ Redirect back to login page
    st.stop()  # Prevent rendering the rest of the page

# ✅ Only accessible if authenticated
st.title("📊 Transaction Page")
st.write("Welcome to the secured Transaction page!")

# ✅ Example Transaction Data
st.write("Here you can access financial data...")

# Logout button
if st.button("Logout"):
    st.session_state.authenticated = False
    af = pd.DataFrame(st.session_state.all_data, columns=st.session_state.column_names)
    af.merge(st.session_state.df)
    st.warning("⚠️ You have been logged out.")
    st.rerun()


