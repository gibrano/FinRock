import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuración de página
st.set_page_config(
    page_title="FinRock - AI Trading Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    /* Fondo y colores principales */
    .stApp {
        background-color: #0A0E27;
        color: #E8EAF6;
    }
    
    /* Header personalizado */
    .main-header {
        background: linear-gradient(135deg, #141B3D, #1E2A5E);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid #1E2A5E;
    }
    
    .logo {
        font-size: 2rem;
        font-weight: bold;
        background: linear-gradient(135deg, #00FF88, #1E90FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Signal Cards */
    .signal-card {
        background: linear-gradient(135deg, rgba(255, 71, 87, 0.1), rgba(255, 71, 87, 0.05));
        border: 2px solid rgba(255, 71, 87, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s;
    }
    
    .signal-card-opportunity {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(0, 255, 136, 0.05));
        border: 2px solid rgba(0, 255, 136, 0.3);
    }
    
    .signal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    
    .signal-company {
        font-size: 1.3rem;
        font-weight: 700;
        color: #E8EAF6;
    }
    
    .signal-change-negative {
        font-size: 1.8rem;
        font-weight: 700;
        color: #FF4757;
    }
    
    .signal-change-positive {
        font-size: 1.8rem;
        font-weight: 700;
        color: #00FF88;
    }
    
    .signal-trigger {
        color: #9CA3AF;
        font-style: italic;
        margin: 0.5rem 0;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    .badge-critical {
        background: rgba(255, 71, 87, 0.2);
        color: #FF4757;
        border: 1px solid #FF4757;
    }
    
    .badge-warning {
        background: rgba(255, 165, 2, 0.2);
        color: #FFA502;
        border: 1px solid #FFA502;
    }
    
    .badge-success {
        background: rgba(0, 255, 136, 0.2);
        color: #00FF88;
        border: 1px solid #00FF88;
    }
    
    /* Market Pulse Cards */
    .pulse-card {
        background: linear-gradient(135deg, rgba(30, 144, 255, 0.1), rgba(30, 144, 255, 0.05));
        border: 1px solid rgba(30, 144, 255, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .pulse-label {
        color: #9CA3AF;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .pulse-value {
        font-size: 2rem;
        font-weight: 700;
        color: #E8EAF6;
        margin: 0.5rem 0;
    }
    
    .pulse-change-positive {
        color: #00FF88;
        font-size: 1rem;
        font-weight: 600;
    }
    
    .pulse-change-negative {
        color: #FF4757;
        font-size: 1rem;
        font-weight: 600;
    }
    
    /* Tabla de oportunidades */
    .dataframe {
        background-color: #141B3D !important;
        border-radius: 12px;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Ajustar padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Estilo para métricas de Streamlit */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <span class="logo">⚡ FinRock</span>
    <p style="color: #9CA3AF; margin-top: 0.5rem;">AI-Powered Trading Intelligence Dashboard</p>
</div>
""", unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([2, 1])

# ========== COLUMNA 1: SEÑALES CRÍTICAS ==========
with col1:
    st.markdown("### 🔴 SEÑALES CRÍTICAS")
    st.markdown('<span class="badge badge-critical">3 ACTIVAS</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Señal 1: NVIDIA
    st.markdown("""
    <div class="signal-card">
        <div class="signal-header">
            <span class="signal-company">NVIDIA</span>
            <span class="signal-change-negative">-4.2%</span>
        </div>
        <span class="badge badge-critical">🔥 IMPACTO ALTO</span>
        <div class="signal-trigger">"Taiwan semiconductor export restrictions announced by US Commerce Dept"</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("📊 Ver Análisis", key="nvidia_analysis", use_container_width=True):
            st.info("Análisis causal completo de NVIDIA")
    with col_btn2:
        if st.button("⭐ Watchlist", key="nvidia_watch", use_container_width=True):
            st.success("Agregado a watchlist")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Señal 2: JPMorgan
    st.markdown("""
    <div class="signal-card">
        <div class="signal-header">
            <span class="signal-company">JPMorgan</span>
            <span class="signal-change-negative">-2.8%</span>
        </div>
        <span class="badge badge-warning">⚠️ IMPACTO MEDIO</span>
        <div class="signal-trigger">"Federal Reserve signals potential rate hikes amid inflation concerns"</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn3, col_btn4 = st.columns(2)
    with col_btn3:
        if st.button("📊 Ver Análisis", key="jpmorgan_analysis", use_container_width=True):
            st.info("Análisis causal completo de JPMorgan")
    with col_btn4:
        if st.button("⭐ Watchlist", key="jpmorgan_watch", use_container_width=True):
            st.success("Agregado a watchlist")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Señal 3: Shell
    st.markdown("""
    <div class="signal-card">
        <div class="signal-header">
            <span class="signal-company">Shell</span>
            <span class="signal-change-negative">-3.1%</span>
        </div>
        <span class="badge badge-warning">⚠️ IMPACTO MEDIO</span>
        <div class="signal-trigger">"OPEC+ announces surprise production increase, oil prices drop"</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn5, col_btn6 = st.columns(2)
    with col_btn5:
        if st.button("📊 Ver Análisis", key="shell_analysis", use_container_width=True):
            st.info("Análisis causal completo de Shell")
    with col_btn6:
        if st.button("⭐ Watchlist", key="shell_watch", use_container_width=True):
            st.success("Agregado a watchlist")

# ========== COLUMNA 2: MARKET PULSE ==========
with col2:
    st.markdown("### 📊 MARKET PULSE")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # VIX
    st.markdown("""
    <div class="pulse-card">
        <div class="pulse-label">VIX (Volatilidad)</div>
        <div class="pulse-value">18.2</div>
        <div class="pulse-change-negative">+12.3%</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # S&P 500
    st.markdown("""
    <div class="pulse-card">
        <div class="pulse-label">S&P 500</div>
        <div class="pulse-value">4,782</div>
        <div class="pulse-change-positive">+0.3%</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # NASDAQ
    st.markdown("""
    <div class="pulse-card">
        <div class="pulse-label">NASDAQ</div>
        <div class="pulse-value">15,043</div>
        <div class="pulse-change-negative">-0.8%</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # DOW JONES
    st.markdown("""
    <div class="pulse-card">
        <div class="pulse-label">DOW JONES</div>
        <div class="pulse-value">37,440</div>
        <div class="pulse-change-positive">+0.5%</div>
    </div>
    """, unsafe_allow_html=True)

# ========== TOP OPORTUNIDADES ==========
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("### 🎯 TOP OPORTUNIDADES")
st.markdown('<span class="badge badge-success">5 SEÑALES</span>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Crear DataFrame con oportunidades
opportunities = pd.DataFrame({
    'Sector': ['💊 Pharma', '⚡ Energy', '📱 Tech', '🏦 Banking', '🚗 Automotive'],
    'Empresa': ['Moderna', 'BP', 'Apple', 'Goldman Sachs', 'Tesla'],
    'Señal': ['BUY', 'SELL', 'HOLD', 'BUY', 'HOLD'],
    'Impacto': ['+8.5%', '-6.2%', '+2.1%', '+5.3%', '+1.8%'],
    'Confianza': ['91%', '88%', '76%', '83%', '72%']
})

# Función para colorear las celdas
def color_signal(val):
    if val == 'BUY':
        return 'background-color: rgba(0, 255, 136, 0.2); color: #00FF88; font-weight: bold;'
    elif val == 'SELL':
        return 'background-color: rgba(255, 71, 87, 0.2); color: #FF4757; font-weight: bold;'
    elif val == 'HOLD':
        return 'background-color: rgba(255, 165, 2, 0.2); color: #FFA502; font-weight: bold;'
    return ''

def color_impact(val):
    if '+' in val:
        return 'color: #00FF88; font-weight: bold; font-size: 1.1rem;'
    else:
        return 'color: #FF4757; font-weight: bold; font-size: 1.1rem;'

# Aplicar estilos
styled_df = opportunities.style.applymap(color_signal, subset=['Señal'])\
                                .applymap(color_impact, subset=['Impacto'])\
                                .set_properties(**{
                                    'background-color': '#141B3D',
                                    'color': '#E8EAF6',
                                    'border-color': '#1E2A5E',
                                    'text-align': 'center',
                                    'font-size': '1rem',
                                    'padding': '0.75rem'
                                })

# Mostrar tabla
st.dataframe(
    styled_df,
    use_container_width=True,
    height=280,
    hide_index=True
)

# Footer con timestamp
st.markdown("<br>", unsafe_allow_html=True)
current_time = datetime.now().strftime("%H:%M:%S")
st.markdown(f"""
<div style="text-align: center; color: #9CA3AF; font-size: 0.85rem; padding: 1rem;">
    ⚡ Última actualización: {current_time} • Datos en tiempo real
</div>
""", unsafe_allow_html=True)