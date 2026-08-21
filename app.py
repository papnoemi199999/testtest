import streamlit as st

st.set_page_config(page_title="Test Title", layout="centered")
st.title("Feedback pentru cursuri")
st.write("Completează formularul de mai jos pentru a ne trimite părerea ta.")

# Formularul păstrează toate câmpurile grupate până la apăsarea butonului.
with st.form("formular_feedback"):
    nume = st.text_input("Nume")

    curs = st.selectbox(
        "Alege cursul",
        ["Programare în Python", "Baze de date", "Dezvoltare web"],
    )

    evaluare = st.slider("Evaluare", min_value=1, max_value=5, value=5)
    comentariu = st.text_area("Comentariu")

    trimis = st.form_submit_button("Trimite feedbackul")

# Mesajul apare după trimiterea formularului.
if trimis:
    if not nume.strip():
        st.warning("Te rugăm să introduci numele.")
    else:
        st.success(
            f"Mulțumim pentru feedback, {nume}! "
            f"Ai evaluat cursul „{curs}” cu {evaluare} din 5."
        )
