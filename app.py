import streamlit as st
from datetime import timedelta

# Tiêu đề
st.title("💰 Tính tiền gửi tiết kiệm")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền gửi (triệu đồng)",
    min_value=0.0,
    value=500.0,
    step=10.0
)

i = st.number_input(
    "Nhập lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1
) / 100

ngay_gui = st.date_input("Chọn ngày gửi")

# Nhập thời gian theo tháng
thang = st.number_input(
    "Nhập thời gian gửi (tháng)",
    min_value=1,
    value=3,
    step=1
)

if st.button("Tính toán"):

    # Quy đổi tháng sang ngày
    n = thang * (365 / 12)

    # Lãi đơn
    An = C * (1 + (i / 365) * n)

    # Lãi kép
    Bn = C * ((1 + (i / 365)) ** n)

    # Ngày đáo hạn
    ngay_dao_han = ngay_gui + timedelta(days=int(n))

    st.subheader("📊 Kết quả")

    st.write(f"**Ngày gửi:** {ngay_gui.strftime('%d/%m/%Y')}")
    st.write(f"**Thời gian gửi:** {thang} tháng")
    st.write(f"**Ngày đáo hạn:** {ngay_dao_han.strftime('%d/%m/%Y')}")

    st.success(f"Tổng số tiền theo lãi đơn: {An:.2f} triệu đồng")
    st.success(f"Tổng số tiền theo lãi kép: {Bn:.2f} triệu đồng")

    st.info(f"Tiền lãi (lãi đơn): {An - C:.2f} triệu đồng")
    st.info(f"Tiền lãi (lãi kép): {Bn - C:.2f} triệu đồng")
    st.success(f"Tổng số tiền theo **lãi kép**: {Bn:.2f} triệu đồng")

    st.info(f"Tiền lãi (lãi đơn): {An - C:.2f} triệu đồng")
    st.info(f"Tiền lãi (lãi kép): {Bn - C:.2f} triệu đồng")
