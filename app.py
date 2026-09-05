import streamlit as st
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

# =========================================================
# 1. CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="SmartSave 360",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CSS - LÀM BẢNG ĐIỀU KHIỂN TO HƠN
# =========================================================

st.markdown("""
<style>

/* ==============================
   SIDEBAR
   ============================== */

section[data-testid="stSidebar"] {
    width: 390px !important;
}

section[data-testid="stSidebar"] > div {
    width: 390px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.4rem 3rem 1.4rem;
}

/* Tiêu đề sidebar */

.sidebar-title {
    background: linear-gradient(135deg, #101b4d, #164d87);
    color: white;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    text-align: center;
}

.sidebar-title h2 {
    margin: 0;
    font-size: 25px;
}

.sidebar-title p {
    margin: 6px 0 0 0;
    font-size: 14px;
}

/* ==============================
   HEADER
   ============================== */

.hero {
    background: linear-gradient(
        135deg,
        #101846,
        #123c70,
        #155a83
    );
    padding: 35px 40px;
    border-radius: 24px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(15, 30, 70, 0.18);
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 17px;
    margin-bottom: 20px;
}

.hero-info {
    font-size: 14px;
    opacity: 0.95;
}

/* ==============================
   CARD
   ============================== */

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e5eaf2;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.card h3 {
    margin-top: 0;
}

/* ==============================
   METRIC
   ============================== */

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e3e9f2;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    text-align: center;
}

.metric-title {
    color: #64748b;
    font-size: 14px;
}

.metric-value {
    color: #123d73;
    font-size: 25px;
    font-weight: 700;
    margin-top: 8px;
}

/* ==============================
   RESULT
   ============================== */

.result-box {
    background: linear-gradient(
        135deg,
        #eef7ff,
        #ffffff
    );
    padding: 28px;
    border-radius: 20px;
    border: 1px solid #dbeafe;
}

/* ==============================
   BUTTON
   ============================== */

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 12px;
    font-weight: 600;
}

/* Nút tính toán */

div[data-testid="stButton"] button[kind="primary"] {
    min-height: 58px;
    font-size: 18px;
}

/* ==============================
   TAB
   ============================== */

button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
}

/* ==============================
   MOBILE
   ============================== */

@media (max-width: 900px) {

    section[data-testid="stSidebar"] {
        width: 330px !important;
    }

    section[data-testid="stSidebar"] > div {
        width: 330px !important;
    }

    .hero h1 {
        font-size: 28px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. HÀM
# =========================================================

def format_money(value):
    return f"{value:,.0f} VNĐ"


def tinh_lai_don(
    tien_goc,
    lai_suat,
    so_ngay
):
    return tien_goc * (lai_suat / 100) * so_ngay / 365


# =========================================================
# 4. SESSION STATE
# =========================================================

if "so_tien" not in st.session_state:
    st.session_state.so_tien = 50_000_000.0

if "da_tinh" not in st.session_state:
    st.session_state.da_tinh = False


def set_money(value):
    st.session_state.so_tien = value


# =========================================================
# 5. BẢNG ĐIỀU KHIỂN
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">
        <h2>🎛️ BẢNG ĐIỀU KHIỂN</h2>
        <p>Thiết lập khoản tiền gửi</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------
    # TIỀN GỬI
    # ---------------------------------------------

    st.markdown("### 💰 Số tiền gửi")

    st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0.0,
        step=1_000_000.0,
        format="%.0f",
        key="so_tien"
    )

    st.info(
        f"💵 Đang chọn: **{format_money(st.session_state.so_tien)}**"
    )

    st.markdown("#### ⚡ Chọn nhanh")

    c1, c2 = st.columns(2)

    with c1:
        st.button(
            "💰 50 triệu",
            on_click=set_money,
            args=(50_000_000,)
        )

        st.button(
            "💰 200 triệu",
            on_click=set_money,
            args=(200_000_000,)
        )

        st.button(
            "💰 500 triệu",
            on_click=set_money,
            args=(500_000_000,)
        )

    with c2:
        st.button(
            "💰 100 triệu",
            on_click=set_money,
            args=(100_000_000,)
        )

        st.button(
            "💰 1 tỷ",
            on_click=set_money,
            args=(1_000_000_000,)
        )

        st.button(
            "💰 2 tỷ",
            on_click=set_money,
            args=(2_000_000_000,)
        )

    st.markdown("---")

    # ---------------------------------------------
    # KỲ HẠN
    # ---------------------------------------------

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

    so_thang = {
        "Không kỳ hạn": 0,
        "1 tháng": 1,
        "3 tháng": 3,
        "6 tháng": 6,
        "9 tháng": 9,
        "12 tháng": 12,
        "18 tháng": 18,
        "24 tháng": 24,
        "36 tháng": 36
    }[ky_han]

    lai_suat = st.number_input(
        "📈 Lãi suất có kỳ hạn (%/năm)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    lai_khong_ky_han = st.number_input(
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

    # ---------------------------------------------
    # THỜI GIAN
    # ---------------------------------------------

    st.markdown("---")
    st.markdown("### 🗓️ Thời gian")

    ngay_gui = st.date_input(
        "Ngày gửi tiền",
        value=date.today()
    )

    ngay_dao_han = (
        ngay_gui + relativedelta(months=so_thang)
        if so_thang > 0
        else ngay_gui
    )

    ngay_rut = st.date_input(
        "Ngày rút tiền",
        value=ngay_dao_han
    )

    # ---------------------------------------------
    # PHƯƠNG THỨC
    # ---------------------------------------------

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

    tai_tuc = st.checkbox(
        "🔄 Tự động tái tục khi đáo hạn"
    )

    # ---------------------------------------------
    # TÍNH TOÁN
    # ---------------------------------------------

    st.markdown("---")

    tinh = st.button(
        "🔥 TÍNH TOÁN NGAY",
        type="primary"
    )

    if tinh:
        st.session_state.da_tinh = True

    if st.button("🔄 Đặt lại"):
        st.session_state.so_tien = 50_000_000.0
        st.session_state.da_tinh = False
        st.rerun()


# =========================================================
# 6. HEADER
# =========================================================

st.markdown("""
<div class="hero">

<h1>🏦 SMARTSAVE 360</h1>

<p>
<b>Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm</b>
</p>

<div class="hero-info">

🔴 Rút trước hạn → áp dụng lãi suất không kỳ hạn
&nbsp;&nbsp; | &nbsp;&nbsp;

🟢 Đến hạn → nhận lãi hoặc tái tục
&nbsp;&nbsp; | &nbsp;&nbsp;

📅 Cơ sở tính lãi: 365 ngày/năm

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 7. TÍNH TOÁN
# =========================================================

so_tien = st.session_state.so_tien

so_ngay = (ngay_rut - ngay_gui).days

rut_truoc_han = (
    so_thang > 0
    and ngay_rut < ngay_dao_han
)

if rut_truoc_han:
    lai_ap_dung = lai_khong_ky_han
    trang_thai = "🔴 Rút trước hạn"
else:
    lai_ap_dung = lai_suat
    trang_thai = "🟢 Đúng hạn"


if so_ngay < 0:
    st.error("❌ Ngày rút không được trước ngày gửi.")
    st.stop()


tien_lai = tinh_lai_don(
    so_tien,
    lai_ap_dung,
    so_ngay
)


# =========================================================
# 8. TÍNH TỔNG TIỀN
# =========================================================

if phuong_thuc == "💵 Nhận lãi trước":

    tong_nhan = so_tien

elif phuong_thuc == "📅 Nhận lãi hàng tháng":

    tong_nhan = so_tien + tien_lai

else:

    tong_nhan = so_tien + tien_lai


# =========================================================
# 9. TAB
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Tổng quan",
        "💰 Tính tiền gửi",
        "📋 Dòng tiền",
        "📈 So sánh thông minh"
    ]
)


# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.markdown("## 📊 Tổng quan")

    if not st.session_state.da_tinh:

        st.info(
            "💡 Nhập thông tin tại **Bảng điều khiển bên trái** "
            "sau đó bấm **🔥 TÍNH TOÁN NGAY**."
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("""
            <div class="card">
            <h3>💰 Tiền gửi</h3>
            <p>
            Thiết lập số tiền và kỳ hạn gửi
            phù hợp với nhu cầu.
            </p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card">
            <h3>📈 Lợi nhuận</h3>
            <p>
            Tự động tính tiền lãi dự kiến
            theo số ngày thực tế.
            </p>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="card">
            <h3>🧠 Phân tích</h3>
            <p>
            So sánh kỳ hạn và đánh giá
            hiệu quả khoản tiền gửi.
            </p>
            </div>
            """, unsafe_allow_html=True)

    else:

        st.success(
            f"✅ Đã tính toán khoản tiền gửi {format_money(so_tien)}"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown("""
            <div class="metric-card">
            <div class="metric-title">💰 TIỀN GỐC</div>
            """, unsafe_allow_html=True)

            st.markdown(
                f'<div class="metric-value">{format_money(so_tien)}</div>',
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="metric-card">
            <div class="metric-title">📈 TIỀN LÃI</div>
            """, unsafe_allow_html=True)

            st.markdown(
                f'<div class="metric-value">{format_money(tien_lai)}</div>',
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="metric-card">
            <div class="metric-title">💎 TỔNG NHẬN</div>
            """, unsafe_allow_html=True)

            st.markdown(
                f'<div class="metric-value">{format_money(tong_nhan)}</div>',
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        with c4:
            st.markdown("""
            <div class="metric-card">
            <div class="metric-title">📅 SỐ NGÀY</div>
            """, unsafe_allow_html=True)

            st.markdown(
                f'<div class="metric-value">{so_ngay} ngày</div>',
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 📌 Tình trạng khoản gửi")

        if rut_truoc_han:
            st.warning(
                "🔴 Khoản tiền đang **rút trước hạn**. "
                f"Lãi suất áp dụng: **{lai_khong_ky_han:.2f}%/năm**."
            )
        else:
            st.success(
                f"🟢 Khoản tiền gửi **đúng hạn**. "
                f"Lãi suất áp dụng: **{lai_suat:.2f}%/năm**."
            )


# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.markdown("## 💰 Chi tiết khoản tiền gửi")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="result-box">
        <h3>🏦 Thông tin khoản gửi</h3>
        """, unsafe_allow_html=True)

        st.write(f"**Số tiền gửi:** {format_money(so_tien)}")
        st.write(f"**Kỳ hạn:** {ky_han}")
        st.write(f"**Lãi suất niêm yết:** {lai_suat:.2f}%/năm")
        st.write(f"**Lãi suất áp dụng:** {lai_ap_dung:.2f}%/năm")
        st.write(
            f"**Ngày gửi:** {ngay_gui.strftime('%d/%m/%Y')}"
        )
        st.write(
            f"**Ngày đáo hạn:** {ngay_dao_han.strftime('%d/%m/%Y')}"
        )
        st.write(
            f"**Ngày rút:** {ngay_rut.strftime('%d/%m/%Y')}"
        )
        st.write(f"**Trạng thái:** {trang_thai}")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="result-box">
        <h3>💵 Kết quả tài chính</h3>
        """, unsafe_allow_html=True)

        st.write(
            f"**Tiền lãi:** {format_money(tien_lai)}"
        )

        st.write(
            f"**Tổng tiền nhận:** {format_money(tong_nhan)}"
        )

        ty_suat = (
            tien_lai / so_tien * 100
            if so_tien > 0
            else 0
        )

        st.write(
            f"**Tỷ suất sinh lời:** {ty_suat:.2f}%"
        )

        st.write(
            f"**Phương thức nhận lãi:** {phuong_thuc}"
        )

        st.write(
            f"**Tự động tái tục:** "
            f"{'Có 🔄' if tai_tuc else 'Không'}"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📐 Công thức nghiệp vụ")

    st.latex(
        r"Lãi = Tiền\ gốc \times "
        r"\frac{Lãi\ suất}{100} \times "
        r"\frac{Số\ ngày}{365}"
    )

    st.info(
        f"Áp dụng: {format_money(so_tien)} × "
        f"{lai_ap_dung:.2f}% × {so_ngay}/365 "
        f"= **{format_money(tien_lai)}**"
    )


# =========================================================
# TAB 3 - DÒNG TIỀN
# =========================================================

with tab3:

    st.markdown("## 📋 Bảng dòng tiền chi tiết")

    dong_tien = pd.DataFrame({

        "Thời điểm": [
            "Ngày gửi",
            "Trong kỳ",
            "Ngày đáo hạn / rút"
        ],

        "Ngày": [
            ngay_gui.strftime("%d/%m/%Y"),
            f"{so_ngay} ngày",
            ngay_rut.strftime("%d/%m/%Y")
        ],

        "Dòng tiền": [
            f"-{format_money(so_tien)}",
            f"+{format_money(tien_lai)}",
            f"+{format_money(tong_nhan)}"
        ],

        "Nội dung": [
            "Khách hàng gửi tiền",
            "Phát sinh tiền lãi",
            "Khách hàng nhận tiền"
        ]
    })

    st.dataframe(
        dong_tien,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📊 Biểu đồ khoản tiền")

    chart_data = pd.DataFrame({
        "Khoản mục": [
            "Tiền gốc",
            "Tiền lãi",
            "Tổng nhận"
        ],
        "Giá trị": [
            so_tien,
            tien_lai,
            tong_nhan
        ]
    })

    st.bar_chart(
        chart_data.set_index("Khoản mục")
    )


# =========================================================
# TAB 4 - SO SÁNH
# =========================================================

with tab4:

    st.markdown("## 📈 So sánh thông minh")

    ky_han_so_sanh = {
        "1 tháng": 1,
        "3 tháng": 3,
        "6 tháng": 6,
        "9 tháng": 9,
        "12 tháng": 12,
        "18 tháng": 18,
        "24 tháng": 24,
        "36 tháng": 36
    }

    data = []

    for ten_ky_han, thang_i in ky_han_so_sanh.items():

        ngay_end = ngay_gui + relativedelta(
            months=thang_i
        )

        ngay_i = (ngay_end - ngay_gui).days

        lai_i = tinh_lai_don(
            so_tien,
            lai_suat,
            ngay_i
        )

        tong_i = so_tien + lai_i

        data.append([
            ten_ky_han,
            ngay_i,
            lai_suat,
            lai_i,
            tong_i
        ])

    comparison = pd.DataFrame(
        data,
        columns=[
            "Kỳ hạn",
            "Số ngày",
            "Lãi suất (%/năm)",
            "Tiền lãi",
            "Tổng tiền nhận"
        ]
    )

    st.dataframe(
        comparison.style.format({
            "Lãi suất (%/năm)": "{:.2f}",
            "Tiền lãi": "{:,.0f}",
            "Tổng tiền nhận": "{:,.0f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    # Tìm phương án tốt nhất

    best = comparison.loc[
        comparison["Tiền lãi"].idxmax()
    ]

    st.success(
        f"🏆 Với số tiền **{format_money(so_tien)}**, "
        f"kỳ hạn **{best['Kỳ hạn']}** đang mang lại "
        f"mức lãi cao nhất: "
        f"**{format_money(best['Tiền lãi'])}**."
    )

    st.markdown("### 📊 So sánh tiền lãi theo kỳ hạn")

    chart = comparison[
        ["Kỳ hạn", "Tiền lãi"]
    ].set_index("Kỳ hạn")

    st.bar_chart(chart)


# =========================================================
# 10. KIẾN THỨC NGHIỆP VỤ
# =========================================================

st.markdown("---")

with st.expander("📚 Kiến thức nghiệp vụ tiền gửi"):

    st.markdown("""
### 1. Tiền gửi có kỳ hạn

Khách hàng gửi tiền trong một khoảng thời gian
xác định và được hưởng mức lãi suất theo kỳ hạn.

### 2. Rút trước hạn

Nếu khách hàng rút tiền trước ngày đáo hạn,
hệ thống chuyển sang áp dụng **lãi suất không kỳ hạn**
theo mô hình mô phỏng.

### 3. Đáo hạn

Khi đến ngày đáo hạn, khách hàng có thể nhận
tiền gốc và tiền lãi hoặc thực hiện tái tục.

### 4. Tái tục

Nếu khách hàng không rút tiền khi đến hạn,
khoản tiền có thể được tiếp tục gửi sang kỳ hạn mới.

### 5. Cơ sở tính lãi

Hệ thống sử dụng cơ sở:

**365 ngày/năm**

Công thức:

**Lãi = Tiền gốc × Lãi suất × Số ngày / 365**
""")


# =========================================================
# 11. FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <center>
    🏦 <b>SMARTSAVE 360</b><br>
    <small>
    Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm |
    Phục vụ mục đích học tập và mô phỏng
    </small>
    </center>
    """,
    unsafe_allow_html=True
)
