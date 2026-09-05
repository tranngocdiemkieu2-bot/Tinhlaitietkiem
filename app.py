import streamlit as st

st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 TÍNH LÃI TIỀN GỬI TIẾT KIỆM")
st.write("Nhập thông tin tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

st.divider()

# Nhập thông tin
so_tien = st.number_input(
    "💰 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10000000.0,
    step=500000.0
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

st.divider()

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    tien_lai = so_tien * lai_suat / 100 * ky_han / 12
    tong_tien = so_tien + tien_lai

    st.success("Đã tính toán thành công!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💵 Tiền lãi",
            f"{tien_lai:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "💰 Tổng tiền nhận",
            f"{tong_tien:,.0f} VNĐ"
        )

    st.info(
        f"""
        **Thông tin khoản gửi:**

        - Số tiền gửi: **{so_tien:,.0f} VNĐ**
        - Lãi suất: **{lai_suat}%/năm**
        - Kỳ hạn: **{ky_han} tháng**
        - Tiền lãi: **{tien_lai:,.0f} VNĐ**
        - Tổng tiền nhận: **{tong_tien:,.0f} VNĐ**
        """
    )
