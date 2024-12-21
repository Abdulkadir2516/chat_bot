import streamlit as st
import chat
#import ceviri

# Başlık
st.title("Chatbot Uygulaması")

# Form başlatma
with st.form("my_form"):
    st.header("Aşağıdaki alana input giriniz")

    # Form alanları
    message = st.text_input("İleti Gönder")

    # Form gönderim butonu
    submitted = st.form_submit_button("Gönder")

    # Form verilerinin işlenmesi
    if submitted:
        st.success("Form başarıyla gönderildi!")
        st.write("Girilen Bilgiler:")

        donus = chat.chat_with_ollama(message)
        st.write(f"Çıktı: {donus}")


# Ek bilgi veya mesaj
st.info("Bu bir Streamlit form örneğidir.")
