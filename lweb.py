import streamlit as st

st.set_page_config(page_title="For My Love ❤️", page_icon="❤️")

st.title("❤️ To My Favorite Person ❤️")

st.write("Hi Love,")
st.write("I made this little website just for you.")
st.write("Every moment with you is my favorite memory. ❤️")

if st.button("💌 Open My Heart"):
    st.balloons()
    st.success("I love you more than words can ever express. Thank you for being you. ❤️")
    

st.image("w.jpeg", width=500)

