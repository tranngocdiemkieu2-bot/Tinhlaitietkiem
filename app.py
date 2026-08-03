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

lai_suat_co_ky_han = st.number_input(
    "Lãi suất có kỳ hạn (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

lai_suat_khong_ky_han = st.number_input(
    "Lãi suất không kỳ hạn (%/năm)",
    min_value=0.0,
    value=0.2,
    step=0.1
)

ngay_gui = st.date_input(
    "Ngày gửi",
    value=date.today()
)

ngay_den_han = st.date_input(
    "Ngày đến hạn",
    value=date.today()
)

ngay_rut = st.date_input(
    "Ngày rút tiền",
    value=date.today()
)

# ==========================
# Tính toán
# ==========================

if st.button("Tính toán"):

    if ngay_den_han <= ngay_gui:
        st.error("Ngày đến hạn phải sau ngày gửi.")

    elif ngay_rut < ngay_gui:
        st.error("Ngày rút tiền không được trước ngày gửi.")

    else:

        i_ckh = lai_suat_co_ky_han / 100
        i_kkh = lai_suat_khong_ky_han / 100

        # ==========================
        # Rút trước hoặc đúng ngày đáo hạn
        # ==========================
        if ngay_rut <= ngay_den_han:

            so_ngay = (ngay_rut - ngay_gui).days

            tong_tien = so_tien * (1 + (i_kkh / 365) * so_ngay)

            st.warning("Khách hàng rút trước (hoặc đúng) ngày đến hạn → áp dụng lãi suất KHÔNG KỲ HẠN.")

            st.metric(
                "Tổng tiền nhận",
                f"{tong_tien:,.2f} triệu đồng"
            )

            st.write(f"Số ngày gửi: **{so_ngay} ngày**")
            st.write(f"Tiền lãi: **{tong_tien-so_tien:,.2f} triệu đồng**")

        # ==========================
        # Rút sau ngày đáo hạn
        # ==========================
        else:

            ngay_co_ky_han = (ngay_den_han - ngay_gui).days
            ngay_le = (ngay_rut - ngay_den_han).days

            # Tiền đến ngày đáo hạn
            tien_den_han = so_tien * (1 + (i_ckh / 365) * ngay_co_ky_han)

            # Phần ngày lẻ tính lãi không kỳ hạn
            tong_tien = tien_den_han * (1 + (i_kkh / 365) * ngay_le)

            st.success("Khách hàng rút sau ngày đến hạn.")

            st.metric(
                "Tổng tiền nhận",
                f"{tong_tien:,.3f} triệu đồng"
            )

            st.write("### Chi tiết")

            st.write(f"Số ngày có kỳ hạn: **{ngay_co_ky_han} ngày**")
            st.write(f"Số ngày quá hạn: **{ngay_le} ngày**")

            st.write(f"Tiền tại ngày đến hạn: **{tien_den_han:,.2f} triệu đồng**")

            st.write(f"Tổng tiền khi rút: **{tong_tien:,.2f} triệu đồng**")

            st.write(f"Tổng tiền lãi: **{tong_tien-so_tien:,.2f} triệu đồng**")
