import streamlit as st

st.title("Welcome to Scrivener Legal, LLC!")

st.write("If you are a real estate professional previously granted access to our site, please enter your login credentials:")

users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"}
]

username = st.text_input("User Name:", key="username")
password = st.text_input("Password:", type="password", key="password")

if st.button("Login"):
    authenticated_user = None
    for user in users:
        if username == user["username"] and password == user["password"]:
            authenticated_user = user
            break

    if authenticated_user:
        st.markdown(f"<div class='login-message success-message'>🎉 Login successful! Welcome, {authenticated_user['username']}.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='login-message error-message'>❌ Invalid credentials. Please try again.</div>", unsafe_allow_html=True)

st.write("If you are a real estate professional who would like to gain access to our site, please email your request to deeds@myscrivener.com.")

st.write("Thanks for your interest in working with us!")

st.markdown("""
<style>
    .css-1fz3u6l h1 {
        font-size: 36px;
        color: #1E90FF;
    }

    .css-1fz3u6l p {
        font-size: 18px;
        color: #696969;
    }

    .css-1e4rf2i {
        background-color: #F5F5F5;
    }

    .css-1e4rf2i input {
        color: #696969;
    }

    .css-1g6gooi button {
        background-color: #1E90FF;
        color: #FFFFFF;
    }

    .css-1e4rf2i input {
        padding: 10px;
        margin: 10px;
    }

    .css-1g6gooi button {
        padding: 10px;
        margin: 10px;
    }
</style>
""", unsafe_allow_html=True)
