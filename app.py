import streamlit as st
from datetime import date
import pandas as pd

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="🏦",
    layout="wide"
)

# =========================================================
# CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.header-box {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111a4a, #143d75);
    color: white;
    margin-bottom: 25px;
}

.header-title {
    font-size: 32px;
    font-weight: 700;
}

.header-sub {
    font-size: 16px;
    opacity: 0.9;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.result-card {
    background: linear-gradient(135deg, #eef7ff, #ffffff);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #dbeafe;
}

.big-number {
    font-size: 30px;
    font-weight: 700;
    color: #123c73;
}

.small-label {
    color: #64748b;
    font-size: 14px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 17px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown("""
<div class="header-box">
    <div class="header-title">🏦 Trung tâm tính tiền gửi tiết kiệm</div>
    <div class="header-sub">
        Mô phỏng gửi - lãi - đáo hạn - rút trước hạn - tự động tái tục
    </div>
    <br>
    🔴 Rút trước hạn → lãi suất không kỳ hạn
    &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
    🟢 Đến hạn không rút → tự động tái tục
    &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
    🟡 Cơ sở tính lãi: 365 ngày/năm
</div>
""", unsafe_allow_html=True)

# =========================================================
# HÀM TÍNH TOÁN
# =========================================================

def tinh_lai(so_tien, lai_suat, so_ngay):
    return so_tien * (lai_suat / 100) * so_ngay / 365


def dinh_dang_tien(x):
    return f"{x:,.0f} VNĐ"


# =========================================================
# SIDEBAR - BẢNG ĐIỀU KHIỂN
# =========================================================

with st.sidebar:

    st.markdown("## 🎛️ BẢNG ĐIỀU KHIỂN")

    st.markdown("### 💰 Số tiền gửi")

    so_tien = st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0.0,
        value=50_000_000.0,
        step=1_000_000.0,
        format="%.0f"
    )

    st.caption(
        f"Đang chọn: **{dinh_dang_tien(so_tien)}**"
    )

    st.markdown("#### Chọn nhanh")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("50 triệu"):
            so_tien = 50_000_000

        if st.button("200 triệu"):
            so_tien = 200_000_000

        if st.button("500 triệu"):
            so_tien = 500_000_000

    with col2:
        if st.button("100 triệu"):
            so_tien = 100_000_000

        if st.button("1 tỷ"):
            so_tien = 1_000_000_000

        if st.button("2 tỷ"):
            so_tien = 2_000_000_000

    st.markdown("---")

    st.markdown("### 📅 Kỳ hạn & lãi suất")

    ky_han = st.selectbox(
        "Kỳ hạn gửi tiền",
        [
            "Không kỳ hạn",
            "1 tháng",
            "3 tháng",
            "6 tháng",
            "9 tháng",
            "12 tháng",
            "18 tháng",
            "24 tháng",
            "36 tháng"
        ],
        index=2
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

    st.markdown("---")

    st.markdown("### ⏰ Thời gian")

    ngay_gui = st.date_input(
        "Ngày gửi tiền",
        value=date.today()
    )

    # Xác định số tháng
    mapping_thang = {
        "Không kỳ hạn": 0,
        "1 tháng": 1,
        "3 tháng": 3,
        "6 tháng": 6,
        "9 tháng": 9,
        "12 tháng": 12,
        "18 tháng": 18,
        "24 tháng": 24,
        "36 tháng": 36
    }

    thang = mapping_thang[ky_han]

    # Tính ngày đáo hạn
    if thang > 0:
        try:
            from dateutil.relativedelta import relativedelta
            ngay_dao_han = ngay_gui + relativedelta(months=thang)
        except:
            ngay_dao_han = ngay_gui
    else:
        ngay_dao_han = ngay_gui

    ngay_rut = st.date_input(
        "Ngày rút tiền",
        value=ngay_dao_han
    )

    st.markdown("---")

    st.markdown("### 💵 Phương thức nhận lãi")

    phuong_thuc = st.radio(
        "Chọn phương thức",
        [
            "💵 Nhận lãi trước",
            "📅 Nhận lãi hàng tháng",
            "📆 Nhận lãi cuối kỳ"
        ]
    )

    st.markdown("---")

    tai_tuc = st.checkbox(
        "🔄 Tự động tái tục khi đến hạn",
        value=False
    )

    st.markdown("---")

    tinh_toan = st.button(
        "🔥 TÍNH TOÁN NGAY",
        type="primary"
    )

    reset = st.button(
        "🔄 Đặt lại số tiền mặc định"
    )


# =========================================================
# XỬ LÝ TÍNH TOÁN
# =========================================================

if reset:
    st.rerun()


if tinh_toan:

    # Số ngày thực tế
    so_ngay = (ngay_rut - ngay_gui).days

    if so_ngay < 0:
        st.error("❌ Ngày rút không được trước ngày gửi.")
        st.stop()

    # Kiểm tra rút trước hạn
    rut_truoc_han = False

    if thang > 0 and ngay_rut < ngay_dao_han:
        rut_truoc_han = True

    # Xác định lãi suất
    if rut_truoc_han:
        lai_ap_dung = lai_suat_khong_ky_han
        trang_thai = "🔴 Rút trước hạn"
    else:
        lai_ap_dung = lai_suat
        trang_thai = "🟢 Đúng hạn"

    # Tính lãi
    tien_lai = tinh_lai(
        so_tien,
        lai_ap_dung,
        so_ngay
    )

    # Nhận lãi trước
    if phuong_thuc == "💵 Nhận lãi trước":

        tien_lai = tinh_lai(
            so_tien,
            lai_ap_dung,
            so_ngay
        )

        tong_nhan = so_tien

    # Nhận lãi cuối kỳ
    elif phuong_thuc == "📆 Nhận lãi cuối kỳ":

        tong_nhan = so_tien + tien_lai

    # Nhận lãi hàng tháng
    else:

        tong_nhan = so_tien + tien_lai

    # =====================================================
    # KẾT QUẢ
    # =====================================================

    st.success("✅ Đã tính toán thành công!")

    st.markdown("## 📊 KẾT QUẢ TÍNH TOÁN")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Tiền gửi",
            dinh_dang_tien(so_tien)
        )

    with col2:
        st.metric(
            "📈 Tiền lãi",
            dinh_dang_tien(tien_lai)
        )

    with col3:
        st.metric(
            "💵 Tổng tiền nhận",
            dinh_dang_tien(tong_nhan)
        )

    with col4:
        st.metric(
            "📅 Số ngày gửi",
            f"{so_ngay} ngày"
        )

    st.markdown("---")

    # =====================================================
    # THÔNG TIN CHI TIẾT
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="result-card">
        <h3>🏦 Thông tin khoản gửi</h3>
        """, unsafe_allow_html=True)

        st.write(f"**Số tiền gửi:** {dinh_dang_tien(so_tien)}")
        st.write(f"**Kỳ hạn:** {ky_han}")
        st.write(f"**Lãi suất:** {lai_ap_dung:.2f}%/năm")
        st.write(f"**Ngày gửi:** {ngay_gui.strftime('%d/%m/%Y')}")
        st.write(f"**Ngày đáo hạn:** {ngay_dao_han.strftime('%d/%m/%Y')}")
        st.write(f"**Ngày rút:** {ngay_rut.strftime('%d/%m/%Y')}")
        st.write(f"**Trạng thái:** {trang_thai}")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="result-card">
        <h3>💵 Kết quả tài chính</h3>
        """, unsafe_allow_html=True)

        st.write(
            f"**Tiền lãi:** {dinh_dang_tien(tien_lai)}"
        )

        st.write(
            f"**Tổng tiền nhận:** {dinh_dang_tien(tong_nhan)}"
        )

        if so_tien > 0:
            ty_suat = tien_lai / so_tien * 100
        else:
            ty_suat = 0

        st.write(
            f"**Tỷ suất sinh lời:** {ty_suat:.2f}%"
        )

        st.write(
            f"**Phương thức:** {phuong_thuc}"
        )

        st.write(
            f"**Tái tục:** {'Có 🔄' if tai_tuc else 'Không'}"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # BẢNG DÒNG TIỀN
    # =====================================================

    st.markdown("## 📋 Bảng dòng tiền chi tiết")

    dong_tien = pd.DataFrame({
        "Thời điểm": [
            "Ngày gửi",
            "Trong thời gian gửi",
            "Ngày đáo hạn / rút"
        ],
        "Ngày": [
            ngay_gui.strftime("%d/%m/%Y"),
            f"{so_ngay} ngày",
            ngay_rut.strftime("%d/%m/%Y")
        ],
        "Dòng tiền": [
            f"-{dinh_dang_tien(so_tien)}",
            f"+{dinh_dang_tien(tien_lai)}",
            f"+{dinh_dang_tien(tong_nhan)}"
        ],
        "Nội dung": [
            "Gửi tiền",
            "Tiền lãi",
            "Nhận tiền"
        ]
    })

    st.dataframe(
        dong_tien,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # CÔNG THỨC
    # =====================================================

    with st.expander("📐 Công thức tính lãi"):

        st.write(
            "Lãi tiền gửi = Tiền gốc × Lãi suất năm × Số ngày / 365"
        )

        st.latex(
            r"Lãi = P \times \frac{r}{100} \times \frac{n}{365}"
        )

        st.write(
            f"Trong đó:"
        )

        st.write(
            f"- P = {dinh_dang_tien(so_tien)}"
        )

        st.write(
            f"- r = {lai_ap_dung:.2f}%/năm"
        )

        st.write(
            f"- n = {so_ngay} ngày"
        )

    # =====================================================
    # SO SÁNH
    # =====================================================

    st.markdown("## 📊 So sánh thông minh")

    lai_ky_han = tinh_lai(
        so_tien,
        lai_suat,
        so_ngay
    )

    lai_khong_ky_han = tinh_lai(
        so_tien,
        lai_suat_khong_ky_han,
        so_ngay
    )

    chenhlech = lai_ky_han - lai_khong_ky_han

    comparison = pd.DataFrame({
        "Phương án": [
            "Có kỳ hạn",
            "Không kỳ hạn"
        ],
        "Lãi suất (%/năm)": [
            lai_suat,
            lai_suat_khong_ky_han
        ],
        "Tiền lãi": [
            lai_ky_han,
            lai_khong_ky_han
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        f"💡 Chênh lệch tiền lãi giữa hai phương án: "
        f"**{dinh_dang_tien(chenhlech)}**"
    )

else:

    # =====================================================
    # MÀN HÌNH CHỜ
    # =====================================================

    st.markdown("## 📊 Tổng quan")

    st.info(
        "💡 Nhập thông tin ở **Bảng điều khiển bên trái** "
        "rồi bấm **🔥 TÍNH TOÁN NGAY** để xem kết quả."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>💰 Tiền gửi</h3>
        <p>Nhập số tiền bạn muốn gửi tiết kiệm.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>📅 Kỳ hạn</h3>
        <p>Lựa chọn kỳ hạn và lãi suất phù hợp.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📊 Kết quả</h3>
        <p>Xem tiền lãi và tổng tiền nhận được.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    ### 📌 Hướng dẫn sử dụng

    **Bước 1:** Nhập số tiền gửi.

    **Bước 2:** Chọn kỳ hạn gửi.

    **Bước 3:** Nhập lãi suất.

    **Bước 4:** Chọn ngày gửi và ngày rút.

    **Bước 5:** Chọn phương thức nhận lãi.

    **Bước 6:** Bấm **🔥 TÍNH TOÁN NGAY**.
    """)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "🏦 Hệ thống mô phỏng tính tiền gửi tiết kiệm | "
    "Streamlit | Cơ sở tính lãi 365 ngày/năm"
)
