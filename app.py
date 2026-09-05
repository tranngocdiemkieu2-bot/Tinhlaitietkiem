import streamlit as st

# ==============================
# GIAO DIỆN - SIDEBAR LỚN
# ==============================
st.markdown("""
<style>

    /* ===== BẢNG ĐIỀU KHIỂN BÊN TRÁI ===== */
    [data-testid="stSidebar"] {
        min-width: 380px !important;
        max-width: 380px !important;
        background: #f7f9fc;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding: 25px 22px;
    }

    /* Tiêu đề BẢNG ĐIỀU KHIỂN */
    .dashboard-title {
        background: linear-gradient(135deg, #102a72, #1769aa);
        color: white;
        padding: 22px 20px;
        border-radius: 18px;
        text-align: center;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(20, 50, 120, 0.20);
    }

    /* Tiêu đề các mục */
    [data-testid="stSidebar"] h3 {
        font-size: 20px !important;
        font-weight: 750 !important;
        margin-top: 20px;
    }

    /* Chữ trong sidebar */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        font-size: 16px !important;
    }

    /* Ô nhập */
    [data-testid="stSidebar"] input {
        font-size: 17px !important;
        padding: 10px !important;
    }

    /* Nút */
    [data-testid="stSidebar"] button {
        min-height: 45px !important;
        font-size: 16px !important;
        border-radius: 12px !important;
    }

    /* ===== PHẦN NỘI DUNG BÊN PHẢI ===== */
    .main .block-container {
        padding-left: 35px;
        padding-right: 35px;
        max-width: 1100px;
    }

</style>
""", unsafe_allow_html=True)


# ==============================
# BẢNG ĐIỀU KHIỂN
# ==============================
with st.sidebar:

    st.markdown("""
    <div class="dashboard-title">
        ⚙️ BẢNG ĐIỀU KHIỂN
        <div style="font-size:14px;font-weight:400;margin-top:8px;">
            Thiết lập khoản tiền gửi
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💰 Số tiền gửi")

    so_tien = st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0.0,
        value=50000000.0,
        step=5000000.0,
        format="%.0f"
    )

    st.info(f"💵 Đang chọn: {so_tien:,.0f} VNĐ")

    st.markdown("### ⚡ Chọn nhanh")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💰 50 triệu", use_container_width=True):
            so_tien = 50_000_000

        if st.button("💰 200 triệu", use_container_width=True):
            so_tien = 200_000_000

        if st.button("💰 500 triệu", use_container_width=True):
            so_tien = 500_000_000

    with col2:
        if st.button("💰 100 triệu", use_container_width=True):
            so_tien = 100_000_000

        if st.button("💰 1 tỷ", use_container_width=True):
            so_tien = 1_000_000_000

        if st.button("💰 2 tỷ", use_container_width=True):
            so_tien = 2_000_000_000

    st.divider()

    st.subheader("📅 Kỳ hạn & lãi suất")

    ky_han = st.selectbox(
        "Kỳ hạn gửi tiền",
        ["1 tháng", "3 tháng", "6 tháng", "9 tháng", "12 tháng", "18 tháng", "24 tháng"]
    )

    lai_suat = st.number_input(
        "📈 Lãi suất có kỳ hạn (%/năm)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    lai_suat_khong_ky_han = st.number_input(
        "📉 Lãi suất không kỳ hạn (%/năm)",
        min_value=0.0,
        value=0.2,
        step=0.1
    )

    lai_vay = st.number_input(
        "🏦 Lãi suất vay cầm cố (%/năm)",
        min_value=0.0,
        value=8.0,
        step=0.1
    )

    st.divider()

    st.subheader("📆 Thời gian")

    ngay_gui = st.date_input(
        "Ngày gửi tiền"
    )

    ngay_rut = st.date_input(
        "Ngày rút tiền"
    )

    st.divider()

    st.subheader("💳 Phương thức nhận lãi")

    phuong_thuc = st.radio(
        "Chọn phương thức",
        [
            "💵 Nhận lãi trước",
            "📅 Nhận lãi hàng tháng",
            "🏦 Nhận lãi cuối kỳ"
        ]
    )

    st.button(
        "🔥 TÍNH TOÁN NGAY",
        use_container_width=True,
        type="primary"
    )
