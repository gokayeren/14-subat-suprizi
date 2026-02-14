import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="Love Jackpot 🎰", page_icon="❤️")

st.header("🎰 Şansını Dene Sevgilim!")
st.write("3 Kalbi yan yana bulursan büyük ödül senin Selin!")

# Slot makinesindeki emojiler
emojis = ['🍒', '🍋', '🍇', '💎', '7️⃣', '❤️']

# Session state kullanarak durumu takip edelim (kazandı mı, kaç kere denedi vs.)
if 'spin_count' not in st.session_state:
    st.session_state.spin_count = 0
if 'jackpot' not in st.session_state:
    st.session_state.jackpot = False

col1, col2, col3 = st.columns(3)
empty1 = col1.empty()
empty2 = col2.empty()
empty3 = col3.empty()

# Başlangıç görüntüsü
if st.session_state.spin_count == 0:
    empty1.header("❓")
    empty2.header("❓")
    empty3.header("❓")

# Çevir Butonu
spin_btn = st.button("BAŞLA! 🕹️")

if spin_btn:
    st.session_state.spin_count += 1
    
    # Animasyon efekti (sayılar hızlıca değişiyor gibi görünsün)
    for i in range(15):
        empty1.header(random.choice(emojis))
        empty2.header(random.choice(emojis))
        empty3.header(random.choice(emojis))
        time.sleep(0.05) # Dönme hızı

    # --- HİLE KISMI BAŞLIYOR ---
    # 3. denemede veya %30 şansla kesin kazansın (bunu değiştirebilirsin)
    if st.session_state.spin_count >= 3 or random.random() < 0.3:
        result = ['❤️', '❤️', '❤️']
        st.session_state.jackpot = True
    else:
        # Kazanmadıysa rastgele üret ama hepsi kalp olmasın
        result = [random.choice(emojis) for _ in range(3)]
        while result == ['❤️', '❤️', '❤️']: # Tesadüfen kazanırsa boz
            result = [random.choice(emojis) for _ in range(3)]
            
    # Sonucu ekrana bas
    empty1.header(result[0])
    empty2.header(result[1])
    empty3.header(result[2])

    # Sonuç Mesajları
    if st.session_state.jackpot:
        st.balloons() # Konfetiler patlasın!
        st.success("🎉 Tebrikler Selin! ÖDÜLÜ KAZANDIN! 🎉")
        st.write("### 🎁 Ödülün:")
        st.info("İstediğin tarihte istediğin bir etkilik hakkı kazandın Selin aşkım! Bitanesin :)")
        
        # Oyunu sıfırlama butonu
        if st.button("Tekrar Oyna"):
            st.session_state.jackpot = False
            st.session_state.spin_count = 0
            st.experimental_rerun()
            
    else:
        messages = [
            "Az kaldı canım, tekrar dene!",
            "Bir kez daha dene bebeğim...",
            "Pes etme bitanem, olucak :)",
            "Benim aşkım kadar büyük bir ikramiye bu, son kez dene!"
        ]
        st.warning(random.choice(messages))

st.write("---")
st.caption("Yazılımcı sevgilinden kalplerle yapıldı 🐍")
