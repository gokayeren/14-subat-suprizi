import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="Love Jackpot 🎰", page_icon="❤️")

# --- CSS İLE MOBİL AYARI ---
# Bu kısım sütunların telefonda alt alta inmesini engeller
st.markdown("""
<style>
    /* Sütunları zorla yan yana tut ve genişliklerini eşitle */
    [data-testid="column"] {
        width: 33.33% !important;
        flex: 1 1 auto !important;
        min-width: 1px !important;
        padding: 0 !important;
    }
    /* Emojileri ortala */
    .stMarkdown {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.header("🎰 Şansını Dene Sevgilim!")
st.write("3 Kalbi yan yana bulursan büyük ödül senin Selin!")

# Slot makinesindeki emojiler
emojis = ['🍒', '🍋', '🍇', '💎', '7️⃣', '❤️']

# Session state
if 'spin_count' not in st.session_state:
    st.session_state.spin_count = 0
if 'jackpot' not in st.session_state:
    st.session_state.jackpot = False

# Sütunları oluştur
col1, col2, col3 = st.columns([1,1,1], gap="small")
empty1 = col1.empty()
empty2 = col2.empty()
empty3 = col3.empty()

# Emojileri düzgün göstermek için yardımcı fonksiyon
def show_emoji(container, emoji):
    # Header yerine HTML h1 kullanıyoruz ki mobilde satır taşmasın ve tam ortalansın
    container.markdown(f"<h1 style='text-align: center; font-size: 40px; margin:0; padding:0;'>{emoji}</h1>", unsafe_allow_html=True)

# Başlangıç görüntüsü
if st.session_state.spin_count == 0:
    show_emoji(empty1, "❓")
    show_emoji(empty2, "❓")
    show_emoji(empty3, "❓")

# Çevir Butonu
spin_btn = st.button("BAŞLA! 🕹️", use_container_width=True) # Butonu tam genişlik yapalım

if spin_btn:
    st.session_state.spin_count += 1
    
    # Animasyon efekti
    for i in range(12): # Hızlandırmak için döngüyü biraz azalttım
        show_emoji(empty1, random.choice(emojis))
        show_emoji(empty2, random.choice(emojis))
        show_emoji(empty3, random.choice(emojis))
        time.sleep(0.08)

    # --- HİLE KISMI ---
    if st.session_state.spin_count >= 3 or random.random() < 0.3:
        result = ['❤️', '❤️', '❤️']
        st.session_state.jackpot = True
    else:
        result = [random.choice(emojis) for _ in range(3)]
        while result == ['❤️', '❤️', '❤️']:
            result = [random.choice(emojis) for _ in range(3)]
            
    # Sonucu ekrana bas
    show_emoji(empty1, result[0])
    show_emoji(empty2, result[1])
    show_emoji(empty3, result[2])

    # Sonuç Mesajları
    if st.session_state.jackpot:
        st.balloons()
        st.success("🎉 Tebrikler Selin! ÖDÜLÜ KAZANDIN! 🎉")
        st.write("### 🎁 Ödülün:")
        st.info("İstediğin tarihte istediğin bir etkinlik hakkı kazandın Selin aşkım! Bitanesin :)")
        
        # Yeniden başlat butonu için state'i manuel yönetmek gerekebilir ama basitlik için:
        if st.button("Tekrar Oyna"):
            st.session_state.jackpot = False
            st.session_state.spin_count = 0
            st.rerun() # experimental_rerun yerine artık rerun kullanılıyor
            
    else:
        messages = [
            "Az kaldı canım, tekrar dene!",
            "Bir kez daha dene bebeğim...",
            "Pes etme bitanem, olucak :)",
            "Aşkım tekrar dene!"
        ]
        st.warning(random.choice(messages))

st.write("---")
st.caption("Sevgilin kalplerle yaptı 🐍")
