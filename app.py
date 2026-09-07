# =========================================================
# CSS GIAO DIỆN SMARTSAVE 360
# =========================================================

st.markdown("""
<style>

/* =====================================================
   TOÀN BỘ ỨNG DỤNG
   ===================================================== */

.stApp {
    background: #f5f7fb;
}


/* =====================================================
   SIDEBAR - BẢNG ĐIỀU KHIỂN
   ===================================================== */

[data-testid="stSidebar"] {
    min-width: 390px !important;
    max-width: 390px !important;
    width: 390px !important;
    background: #eef1f6 !important;
    border-right: 1px solid #dfe4ec !important;
}


/* Nội dung bên trong sidebar */

[data-testid="stSidebar"] > div:first-child {
    width: 390px !important;
}


[data-testid="stSidebar"] .block-container {
    padding: 22px 20px 35px 20px !important;
}


/* =====================================================
   TIÊU ĐỀ BẢNG ĐIỀU KHIỂN
   ===================================================== */

.sidebar-title {

    width: 100%;

    background:
        linear-gradient(
            135deg,
            #101d50,
            #174f89
        );

    color: white;

    padding: 25px 18px;

    border-radius: 12px;

    margin-bottom: 24px;

    text-align: center;

    box-shadow:
        0 6px 18px
        rgba(16, 29, 80, .20);
}


.sidebar-title h2 {

    margin: 0;

    font-size: 22px;

    font-weight: 700;
}


.sidebar-title p {

    margin: 9px 0 0 0;

    font-size: 13px;

    opacity: .95;
}


/* =====================================================
   TIÊU ĐỀ TRONG SIDEBAR
   ===================================================== */

[data-testid="stSidebar"] h3 {

    font-size: 17px !important;

    font-weight: 700 !important;

    color: #172554 !important;

    margin-top: 10px !important;

    margin-bottom: 10px !important;
}


[data-testid="stSidebar"] h4 {

    font-size: 14px !important;

    color: #334155 !important;
}


/* =====================================================
   INPUT
   ===================================================== */

[data-testid="stSidebar"] input {

    font-size: 14px !important;

    height: 43px !important;
}


[data-testid="stSidebar"] [data-baseweb="select"] {

    min-height: 43px !important;
}


/* =====================================================
   THÔNG BÁO ĐANG CHỌN
   ===================================================== */

[data-testid="stSidebar"] [data-testid="stAlert"] {

    border-radius: 8px !important;

    padding: 10px 12px !important;

    font-size: 13px !important;
}


/* =====================================================
   NÚT NHANH
   ===================================================== */

[data-testid="stSidebar"] .stButton button {

    width: 100% !important;

    min-height: 43px !important;

    border-radius: 9px !important;

    font-size: 13px !important;

    font-weight: 600 !important;

    border: 1px solid #d6dce7 !important;

    background: white !important;

    color: #1e3a5f !important;

    transition: .2s;
}


[data-testid="stSidebar"] .stButton button:hover {

    border-color: #174f89 !important;

    color: #174f89 !important;
}


/* =====================================================
   NÚT TÍNH TOÁN
   ===================================================== */

[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"] {

    height: 58px !important;

    min-height: 58px !important;

    border-radius: 11px !important;

    font-size: 17px !important;

    font-weight: 700 !important;

    background:
        linear-gradient(
            135deg,
            #102052,
            #155a91
        ) !important;

    color: white !important;

    border: none !important;

    box-shadow:
        0 5px 15px
        rgba(16, 32, 82, .20);
}


/* =====================================================
   RADIO
   ===================================================== */

[data-testid="stSidebar"] label {

    font-size: 13px !important;
}


/* =====================================================
   CHECKBOX
   ===================================================== */

[data-testid="stSidebar"] [data-testid="stCheckbox"] {

    padding-top: 3px !important;

    padding-bottom: 3px !important;
}


/* =====================================================
   ĐƯỜNG KẺ
   ===================================================== */

[data-testid="stSidebar"] hr {

    margin: 18px 0 !important;

    border-color: #d6dce6 !important;
}


/* =====================================================
   KHU VỰC CHÍNH
   ===================================================== */

.main .block-container {

    max-width: 1450px !important;

    padding:

        45px 45px 60px 45px !important;

}


/* =====================================================
   HEADER SMARTSAVE 360
   ===================================================== */

.hero {

    width: 100%;

    background:

        linear-gradient(
            135deg,
            #101846,
            #123c70,
            #155a83
        );

    color: white;

    padding: 42px 45px;

    border-radius: 18px;

    margin-bottom: 30px;

    box-shadow:
        0 10px 30px
        rgba(15, 30, 70, .18);
}


.hero h1 {

    font-size: 38px;

    font-weight: 750;

    margin: 0 0 10px 0;

    letter-spacing: .3px;
}


.hero p {

    font-size: 16px;

    margin: 0 0 20px 0;
}


.hero-info {

    font-size: 13px;

    line-height: 1.8;

    opacity: .95;
}


/* =====================================================
   CARD
   ===================================================== */

.card {

    background: white;

    padding: 28px;

    border-radius: 16px;

    border: 1px solid #e3e8f0;

    box-shadow:
        0 5px 18px
        rgba(0, 0, 0, .05);

    min-height: 150px;

    margin-bottom: 20px;
}


.card h3 {

    color: #153d6b;

    margin-top: 0;

    font-size: 19px;
}


/* =====================================================
   METRIC
   ===================================================== */

.metric-card {

    background: white;

    padding: 25px 14px;

    border-radius: 15px;

    border: 1px solid #e1e7ef;

    box-shadow:
        0 5px 18px
        rgba(0, 0, 0, .05);

    text-align: center;

    min-height: 125px;
}


.metric-title {

    color: #64748b;

    font-size: 13px;

    font-weight: 600;
}


.metric-value {

    color: #123d73;

    font-size: 23px;

    font-weight: 750;

    margin-top: 10px;
}


/* =====================================================
   RESULT BOX
   ===================================================== */

.result-box {

    background:

        linear-gradient(
            135deg,
            #f0f7ff,
            #ffffff
        );

    padding: 28px;

    border-radius: 17px;

    border: 1px solid #d9e6f5;

    box-shadow:
        0 5px 18px
        rgba(0,0,0,.04);
}


/* =====================================================
   TAB
   ===================================================== */

button[data-baseweb="tab"] {

    font-size: 15px !important;

    font-weight: 700 !important;

    padding-top: 13px !important;

    padding-bottom: 13px !important;
}


/* =====================================================
   DATAFRAME
   ===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 10px;

    overflow: hidden;
}


/* =====================================================
   EXPANDER
   ===================================================== */

[data-testid="stExpander"] {

    border-radius: 12px !important;

    border: 1px solid #dfe5ee !important;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 1000px) {

    [data-testid="stSidebar"] {

        min-width: 320px !important;

        max-width: 320px !important;

        width: 320px !important;
    }

    [data-testid="stSidebar"] > div:first-child {

        width: 320px !important;
    }

    .main .block-container {

        padding:
            25px 20px 40px 20px !important;
    }

    .hero {

        padding: 30px 25px;
    }

    .hero h1 {

        font-size: 29px;
    }

}

</style>
""", unsafe_allow_html=True)
