import streamlit as st
from datetime import date

st.set_page_config(page_title="Tính lãi tiền gửi", page_icon="💰")

st.title("💰 TÍNH TIỀN GỬI TIẾT KIỆM")

# ==========================
# Nhập dữ liệu
# ==========================

so_tien = st.number_input(
    "Nhập số tiền gửi (triệu đồng)",
    min_value=0.0,
    value=500.0,
    step=10.0
)

lai_suat = st.number_input(
    "Nhập lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

ngay_gui = st.date_input(
    "Ngày gửi",
    value=date.today()
)

ngay_dao_han = st.date_input(
    "Ngày đến hạn",
    value=date.today()
)

# ==========================
# Tính toán
# ==========================

if st.button("Tính toán"):

    # Kiểm tra ngày hợp lệ
    if ngay_dao_han <= ngay_gui:
        st.error("Ngày đến hạn phải lớn hơn ngày gửi.")
    else:

        # Số ngày gửi thực tế
        so_ngay = (ngay_dao_han - ngay_gui).days

        i = lai_suat / 100

        # Lãi đơn
        tien_lai_don = so_tien * (1 + (i / 365) * so_ngay)

        # Lãi kép
        tien_lai_kep = so_tien * ((1 + i / 365) ** so_ngay)

        st.success("Kết quả tính toán")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Tổng tiền theo lãi đơn",
                f"{tien_lai_don:,.2f} triệu đồng"
            )

        with col2:
            st.metric(
                "Tổng tiền theo lãi kép",
                f"{tien_lai_kep:,.2f} triệu đồng"
            )

        st.write("---")

        st.write(f"**Ngày gửi:** {ngay_gui.strftime('%d/%m/%Y')}")
        st.write(f"**Ngày đến hạn:** {ngay_dao_han.strftime('%d/%m/%Y')}")
        st.write(f"**Số ngày gửi thực tế:** {so_ngay} ngày")

        st.write("---")

        st.subheader("Chi tiết")

        st.write(f"**Số tiền gốc:** {so_tien:,.2f} triệu đồng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Tiền lãi (lãi đơn):** {tien_lai_don - so_tien:,.2f} triệu đồng")
        st.write(f"**Tiền lãi (lãi kép):** {tien_lai_kep - so_tien:,.2f} triệu đồng")
