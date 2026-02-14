import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Sayfa ayarları (Başlık ve ikon)
st.set_page_config(page_title="Sana Özel Bir Denklem", page_icon="❤️", layout="centered")

# Başlık ve Açıklama
st.title("❤️ Sevgililer Günün Kutlu Olsun!")
st.write("Sözel ifadeler bazen yetersiz kalıyor, ben de hislerimi matematikle anlatmak istedim.")

# Kalp çizim fonksiyonu
def draw_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    fig, ax = plt.subplots(figsize=(6,6))
    
    # Arka planı şeffaf yapalım ki sitenin temasına uysun
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    
    # Kalbi çiz ve içini doldur
    ax.plot(x, y, color='#ff4b4b', linewidth=3) # Streamlit kırmızısı
    ax.fill(x, y, color='#ff4b4b', alpha=0.3)
    
    ax.axis('off') # Eksenleri ve sayıları gizle
    return fig

# Çizimi ekrana bas
st.pyplot(draw_heart())

# Altına formülü ve notu ekle
st.markdown("---")
st.subheader("Bu kalbin formülü:")
st.code("x = 16sin³(t)\ny = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)", language="python")

st.caption("Matematikte buna 'Kardiyoid' deniyor, bende ise sadece 'SEN'.")