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
    initial_sidebar_state="expanded",
)

# =========================================================
# 2. CSS
# =========================================================
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    width: 420px !important;
}

section[data-testid="stSidebar"] > div {
    width: 420px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1.35rem 3rem 1.35rem;
}

.sidebar-title {
    background: linear-gradient(135deg, #101b4d, #164d87);
    color: white;
    padding: 24px 18px;
    border-radius: 20px;
    margin-bottom: 22px;
    text-align: center;
}

.sidebar-title h2 {
    margin: 0;
    font-size: 28px;
}

.sidebar-title p {
    margin: 7px 0 0 0;
    font-size: 15px;
}

.hero {
    background: linear-gradient(135deg, #101846, #123c70, #155a83);
    padding: 38px 42px;
    border-radius: 25px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(15, 30, 70, 0.18);
}

.hero h1 {
    font-size: 40px;
    margin: 0 0 8px 0;
}

.hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

.hero-info {
    font-size: 14px;
    opacity: .95;
}

.card,
.metric-card,
.result-box {
    background: white;
    border-radius: 20px;
    border: 1px solid #e3e9f2;
    box-shadow: 0 5px 20px rgba(0,0,0,.06);
}

.card {
    padding: 25px;
    margin-bottom: 20px;
}

.card h3 {
    margin-top: 0;
}

.metric-card {
    padding: 24px 15px;
    text-align: center;
    min-height: 125px;
}

.metric-title {
    color: #64748b;
    font-size: 14px;
}

.metric-value {
    color: #123d73;
    font-size: 23px;
    font-weight: 700;
    margin-top: 9px;
}

.result-box {
    background: linear-gradient(135deg, #eef7ff, #ffffff);
    padding: 28px;
    margin-bottom: 18px;
}

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 12px;
    font-weight: 600;
}

div[data-testid="stButton"] button[kind="primary"] {
    min-height: 60px;
    font-size: 18px;
}

button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
}

@media (max-width: 900px) {
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > div {
        width: 340px !important;
    }

    .hero h1 {
        font-size: 29px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 3. HÀM TÍNH TOÁN
# =========================================================
def format_money(value):
    return f"{value:,.0f} VNĐ"


def tinh_lai_don(tien_goc, lai_suat, so_ngay):
    return tien_goc * (lai_suat / 100) * max(so_ngay, 0) / 365


def tinh_lai_hang_thang(tien_goc, lai_suat, ngay_gui, ngay_ket_thuc):
    """
    Tính lãi theo từng khoảng tháng thực tế.
    Dừng đúng ngày rút nếu khách hàng rút trước hạn.
    """
    data = []
    ngay_bat_dau = ngay_gui
    thang = 1

    while ngay_bat_dau < ngay_ket_thuc:

        moc_thang = ngay_gui + relativedelta(months=thang)

        ngay_cuoi = min(
            moc_thang,
            ngay_ket_thuc
        )

        so_ngay = (
            ngay_cuoi - ngay_bat_dau
        ).days

        if so_ngay <= 0:
            break

        tien_lai = tinh_lai_don(
            tien_goc,
            lai_suat,
            so_ngay
        )

        data.append({
            "Tháng": thang,
            "Từ ngày": ngay_bat_dau,
            "Đến ngày": ngay_cuoi,
            "Số ngày": so_ngay,
            "Tiền lãi": tien_lai,
        })

        ngay_bat_dau = ngay_cuoi
        thang += 1

    return pd.DataFrame(data)


# =========================================================
# 4. SESSION STATE
# =========================================================
if "so_tien" not in st.session_state:
    st.session_state.so_tien = 50_000_000.0

if "da_tinh" not in st.session_state:
    st.session_state.da_tinh = False

if "ngay_gui" not in st.session_state:
    st.session_state.ngay_gui = date.today()


def set_money(value):
    st.session_state.so_tien = float(value)


# =========================================================
# 5. SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">

        <h2>🎛️ BẢNG ĐIỀU KHIỂN</h2>

        <p>
            Thiết lập khoản tiền gửi
        </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TIỀN GỬI
    # =====================================================

    st.markdown("### 💰 Số tiền gửi")

    st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0.0,
        step=1_000_000.0,
        format="%.0f",
        key="so_tien"
    )

    st.info(
        f"💵 Đang chọn: "
        f"**{format_money(st.session_state.so_tien)}**"
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

    # =====================================================
    # KỲ HẠN
    # =====================================================

    st.markdown("---")

    st.markdown("### 📅 Kỳ hạn & lãi suất")

    ky_han_map = {

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

    ky_han = st.selectbox(
        "Kỳ hạn gửi tiền",
        list(ky_han_map.keys()),
        index=2
    )

    so_thang = ky_han_map[ky_han]

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

    # =====================================================
    # THỜI GIAN
    # =====================================================

    st.markdown("---")

    st.markdown("### 🗓️ Thời gian")

    ngay_gui = st.date_input(
        "Ngày gửi tiền",
        key="ngay_gui"
    )

    if so_thang > 0:

        ngay_dao_han = (
            ngay_gui
            + relativedelta(months=so_thang)
        )

    else:

        ngay_dao_han = ngay_gui

    if so_thang > 0:

        st.caption(
            f"📌 Ngày đáo hạn dự kiến: "
            f"**{ngay_dao_han.strftime('%d/%m/%Y')}**"
        )

    ngay_rut = st.date_input(
        "Ngày rút tiền",
        value=ngay_dao_han,
        min_value=ngay_gui
    )

    # =====================================================
    # PHƯƠNG THỨC NHẬN LÃI
    # =====================================================

    st.markdown("---")

    st.markdown("### 💵 Phương thức nhận lãi")

    phuong_thuc = st.radio(
        "Chọn phương thức",
        [
            "💵 Nhận lãi trước",
            "📅 Nhận lãi hàng tháng",
            "📆 Nhận lãi cuối kỳ"
        ],
        index=2
    )

    tai_tuc = st.checkbox(
        "🔄 Tự động tái tục khi đáo hạn"
    )

    # =====================================================
    # TÍNH TOÁN
    # =====================================================

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

        st.session_state.ngay_gui = date.today()

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
# 7. XÁC ĐỊNH TRẠNG THÁI
# =========================================================
so_tien = st.session_state.so_tien

so_ngay = (
    ngay_rut - ngay_gui
).days


if so_tien <= 0:

    st.warning(
        "⚠️ Vui lòng nhập số tiền gửi lớn hơn 0."
    )


# =========================================================
# XÁC ĐỊNH LÃI SUẤT
# =========================================================
if so_thang == 0:

    rut_truoc_han = False

    lai_ap_dung = lai_khong_ky_han

    trang_thai = "🔵 Không kỳ hạn"

elif ngay_rut < ngay_dao_han:

    rut_truoc_han = True

    lai_ap_dung = lai_khong_ky_han

    trang_thai = "🔴 Rút trước hạn"

else:

    rut_truoc_han = False

    lai_ap_dung = lai_suat

    trang_thai = "🟢 Đúng hạn"


# =========================================================
# 8. TÍNH LÃI
# =========================================================
tien_lai = tinh_lai_don(
    so_tien,
    lai_ap_dung,
    so_ngay
)


# =========================================================
# 9. LÃI HÀNG THÁNG
# =========================================================
lai_hang_thang = pd.DataFrame()


if (
    phuong_thuc == "📅 Nhận lãi hàng tháng"
    and so_ngay > 0
):

    lai_hang_thang = tinh_lai_hang_thang(
        so_tien,
        lai_ap_dung,
        ngay_gui,
        ngay_rut
    )


if not lai_hang_thang.empty:

    tong_lai_hang_thang = (
        lai_hang_thang["Tiền lãi"].sum()
    )

else:

    tong_lai_hang_thang = 0


# =========================================================
# 10. TỔNG TIỀN NHẬN
# =========================================================
if phuong_thuc == "💵 Nhận lãi trước":

    tien_lai_nhan_truoc = tien_lai

    tong_nhan = so_tien

elif phuong_thuc == "📅 Nhận lãi hàng tháng":

    tong_nhan = so_tien

else:

    tong_nhan = so_tien + tien_lai


if phuong_thuc == "📅 Nhận lãi hàng tháng":

    hien_thi_lai = tong_lai_hang_thang

else:

    hien_thi_lai = tien_lai


if phuong_thuc == "💵 Nhận lãi trước":

    hien_thi_tong = (
        so_tien + tien_lai
    )

elif phuong_thuc == "📅 Nhận lãi hàng tháng":

    hien_thi_tong = (
        so_tien
        + tong_lai_hang_thang
    )

else:

    hien_thi_tong = tong_nhan


# =========================================================
# 11. TABS
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
# TAB 1 - TỔNG QUAN
# =========================================================
with tab1:

    st.markdown("## 📊 Tổng quan")

    if not st.session_state.da_tinh:

        st.info(
            "💡 Nhập thông tin tại "
            "**Bảng điều khiển bên trái** "
            "sau đó bấm "
            "**🔥 TÍNH TOÁN NGAY**."
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.markdown("""
            <div class="card">

                <h3>💰 Tiền gửi</h3>

                <p>
                    Thiết lập số tiền và kỳ hạn
                    phù hợp với nhu cầu.
                </p>

            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown("""
            <div class="card">

                <h3>📈 Lợi nhuận</h3>

                <p>
                    Tự động tính tiền lãi
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
            f"✅ Đã tính toán khoản tiền gửi "
            f"{format_money(so_tien)}"
        )

        c1, c2, c3, c4 = st.columns(4)

        metrics = [

            (
                "💰 TIỀN GỐC",
                format_money(so_tien)
            ),

            (
                "📈 TIỀN LÃI",
                format_money(hien_thi_lai)
            ),

            (
                "💎 TỔNG NHẬN",
                format_money(hien_thi_tong)
            ),

            (
                "📅 SỐ NGÀY",
                f"{so_ngay} ngày"
            )

        ]

        for col, (title, value) in zip(
            [c1, c2, c3, c4],
            metrics
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="metric-card">

                        <div class="metric-title">
                            {title}
                        </div>

                        <div class="metric-value">
                            {value}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


        st.markdown(
            "### 📌 Tình trạng khoản gửi"
        )


        if rut_truoc_han:

            st.warning(
                f"🔴 Khoản tiền đang "
                f"**rút trước hạn**. "
                f"Lãi suất áp dụng: "
                f"**{lai_khong_ky_han:.2f}%/năm**."
            )

        elif so_thang == 0:

            st.info(
                f"🔵 Khoản tiền gửi "
                f"**không kỳ hạn**. "
                f"Lãi suất áp dụng: "
                f"**{lai_khong_ky_han:.2f}%/năm**."
            )

        else:

            st.success(
                f"🟢 Khoản tiền gửi "
                f"**đúng hạn**. "
                f"Lãi suất áp dụng: "
                f"**{lai_suat:.2f}%/năm**."
            )


        if phuong_thuc == "📅 Nhận lãi hàng tháng":

            st.info(
                f"📅 Tổng lãi dự kiến nhận theo tháng: "
                f"**{format_money(tong_lai_hang_thang)}**."
            )

        elif phuong_thuc == "💵 Nhận lãi trước":

            st.info(
                f"💵 Tiền lãi dự kiến nhận trước: "
                f"**{format_money(tien_lai)}**."
            )

        else:

            st.info(
                f"📆 Tiền lãi dự kiến nhận cuối kỳ: "
                f"**{format_money(tien_lai)}**."
            )


# =========================================================
# TAB 2 - CHI TIẾT
# =========================================================
with tab2:

    st.markdown(
        "## 💰 Chi tiết khoản tiền gửi"
    )

    col1, col2 = st.columns(2)


    with col1:

        st.markdown("""
        <div class="result-box">

            <h3>🏦 Thông tin khoản gửi</h3>

        """, unsafe_allow_html=True)


        st.write(
            f"**Số tiền gửi:** "
            f"{format_money(so_tien)}"
        )

        st.write(
            f"**Kỳ hạn:** {ky_han}"
        )

        st.write(
            f"**Lãi suất niêm yết:** "
            f"{lai_suat:.2f}%/năm"
        )

        st.write(
            f"**Lãi suất áp dụng:** "
            f"{lai_ap_dung:.2f}%/năm"
        )

        st.write(
            f"**Ngày gửi:** "
            f"{ngay_gui.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**Ngày đáo hạn:** "
            f"{ngay_dao_han.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**Ngày rút:** "
            f"{ngay_rut.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**Số ngày thực tế:** "
            f"{so_ngay} ngày"
        )

        st.write(
            f"**Trạng thái:** "
            f"{trang_thai}"
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown("""
        <div class="result-box">

            <h3>💵 Kết quả tài chính</h3>

        """, unsafe_allow_html=True)


        if phuong_thuc == "📅 Nhận lãi hàng tháng":

            st.write(
                f"**Tổng tiền lãi:** "
                f"{format_money(tong_lai_hang_thang)}"
            )

            st.write(
                f"**Tiền gốc cuối kỳ:** "
                f"{format_money(so_tien)}"
            )

            st.write(
                f"**Tổng giá trị:** "
                f"{format_money(so_tien + tong_lai_hang_thang)}"
            )


        elif phuong_thuc == "💵 Nhận lãi trước":

            st.write(
                f"**Tiền lãi nhận trước:** "
                f"{format_money(tien_lai)}"
            )

            st.write(
                f"**Tiền gốc cuối kỳ:** "
                f"{format_money(so_tien)}"
            )

            st.write(
                f"**Tổng giá trị:** "
                f"{format_money(so_tien + tien_lai)}"
            )


        else:

            st.write(
                f"**Tiền lãi:** "
                f"{format_money(tien_lai)}"
            )

            st.write(
                f"**Tổng tiền nhận:** "
                f"{format_money(tong_nhan)}"
            )


        ty_suat = (

            tien_lai / so_tien * 100

            if so_tien > 0

            else 0

        )


        st.write(
            f"**Tỷ suất sinh lời:** "
            f"{ty_suat:.2f}%"
        )

        st.write(
            f"**Phương thức nhận lãi:** "
            f"{phuong_thuc}"
        )

        st.write(
            f"**Tự động tái tục:** "
            f"{'Có 🔄' if tai_tuc else 'Không'}"
        )


        if (
            tai_tuc
            and so_thang > 0
            and not rut_truoc_han
        ):

            st.caption(
                "🔄 Khi đáo hạn, khoản tiền "
                "được đánh dấu là có thể tái tục "
                "sang kỳ hạn mới."
            )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # =====================================================
    # BẢNG LÃI HÀNG THÁNG
    # =====================================================

    if (
        phuong_thuc == "📅 Nhận lãi hàng tháng"
        and not lai_hang_thang.empty
    ):

        st.markdown("---")

        st.markdown(
            "### 📅 Lịch nhận tiền lãi hàng tháng"
        )

        bang_lai = lai_hang_thang.copy()

        bang_lai["Từ ngày"] = (
            bang_lai["Từ ngày"]
            .dt.strftime("%d/%m/%Y")
        )

        bang_lai["Đến ngày"] = (
            bang_lai["Đến ngày"]
            .dt.strftime("%d/%m/%Y")
        )

        bang_lai["Tiền lãi"] = (
            bang_lai["Tiền lãi"]
            .apply(format_money)
        )

        st.dataframe(
            bang_lai,
            use_container_width=True,
            hide_index=True
        )


    # =====================================================
    # CÔNG THỨC
    # =====================================================

    st.markdown("---")

    st.markdown(
        "### 📐 Công thức nghiệp vụ"
    )

    st.latex(
        r"""
        Lãi =
        Tiền\ gốc
        \times
        \frac{Lãi\ suất}{100}
        \times
        \frac{Số\ ngày}{365}
        """
    )

    st.info(
        f"{format_money(so_tien)} "
        f"× {lai_ap_dung:.2f}% "
        f"× {so_ngay}/365 "
        f"= **{format_money(tien_lai)}**"
    )


# =========================================================
# TAB 3 - DÒNG TIỀN
# =========================================================
with tab3:

    st.markdown(
        "## 📋 Bảng dòng tiền chi tiết"
    )

    dong_tien_data = []


    # =====================================================
    # NHẬN LÃI HÀNG THÁNG
    # =====================================================

    if (
        phuong_thuc == "📅 Nhận lãi hàng tháng"
        and not lai_hang_thang.empty
    ):

        dong_tien_data.append(

            [
                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"-{format_money(so_tien)}",

                "Khách hàng gửi tiền"

            ]

        )


        for _, row in lai_hang_thang.iterrows():

            dong_tien_data.append(

                [
                    f"Tháng {int(row['Tháng'])}",

                    row["Đến ngày"].strftime(
                        "%d/%m/%Y"
                    ),

                    f"+{format_money(row['Tiền lãi'])}",

                    "Nhận tiền lãi hàng tháng"

                ]

            )


        dong_tien_data.append(

            [
                "Đáo hạn / rút",

                ngay_rut.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(so_tien)}",

                "Nhận lại tiền gốc"

            ]

        )


    # =====================================================
    # NHẬN LÃI TRƯỚC
    # =====================================================

    elif phuong_thuc == "💵 Nhận lãi trước":

        dong_tien_data = [

            [

                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(tien_lai)}",

                "Nhận tiền lãi trước"

            ],

            [

                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"-{format_money(so_tien)}",

                "Gửi tiền gốc"

            ],

            [

                "Đáo hạn / rút",

                ngay_rut.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(so_tien)}",

                "Nhận lại tiền gốc"

            ]

        ]


    # =====================================================
    # NHẬN LÃI CUỐI KỲ
    # =====================================================

    else:

        dong_tien_data = [

            [

                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"-{format_money(so_tien)}",

                "Khách hàng gửi tiền"

            ],

            [

                "Trong kỳ",

                f"{so_ngay} ngày",

                "—",

                "Tiền gửi đang sinh lãi"

            ],

            [

                "Ngày đáo hạn / rút",

                ngay_rut.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(tong_nhan)}",

                "Nhận tiền gốc + lãi"

            ]

        ]


    # =====================================================
    # DATAFRAME
    # =====================================================

    dong_tien = pd.DataFrame(

        dong_tien_data,

        columns=[

            "Thời điểm",

            "Ngày",

            "Dòng tiền",

            "Nội dung"

        ]

    )


    st.dataframe(

        dong_tien,

        use_container_width=True,

        hide_index=True

    )


    # =====================================================
    # BIỂU ĐỒ
    # =====================================================

    st.markdown(
        "### 📊 Biểu đồ khoản tiền"
    )


    if (
        phuong_thuc == "📅 Nhận lãi hàng tháng"
        and not lai_hang_thang.empty
    ):

        chart_data = lai_hang_thang.copy()

        chart_data["Tháng"] = (

            "Tháng "

            + chart_data["Tháng"].astype(str)

        )

        st.bar_chart(

            chart_data.set_index(
                "Tháng"
            )[["Tiền lãi"]]

        )

    else:

        chart_data = pd.DataFrame({

            "Khoản mục":

                [

                    "Tiền gốc",

                    "Tiền lãi",

                    "Tổng nhận"

                ],

            "Giá trị":

                [

                    so_tien,

                    tien_lai,

                    so_tien + tien_lai

                ]

        })


        st.bar_chart(

            chart_data.set_index(
                "Khoản mục"
            )

        )


# =========================================================
# TAB 4 - SO SÁNH THÔNG MINH
# =========================================================
with tab4:

    st.markdown(
        "## 📈 So sánh thông minh"
    )


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


    for ten_ky_han, thang_i in (
        ky_han_so_sanh.items()
    ):

        ngay_end = (

            ngay_gui
            + relativedelta(
                months=thang_i
            )

        )


        ngay_i = (

            ngay_end - ngay_gui

        ).days


        lai_i = tinh_lai_don(

            so_tien,

            lai_suat,

            ngay_i

        )


        tong_i = (

            so_tien + lai_i

        )


        data.append(

            [

                ten_ky_han,

                ngay_i,

                lai_suat,

                lai_i,

                tong_i

            ]

        )


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


    best = comparison.loc[

        comparison["Tiền lãi"].idxmax()

    ]


    st.success(

        f"""

        🏆 Với số tiền

        **{format_money(so_tien)}**,

        kỳ hạn **{best['Kỳ hạn']}**

        đang mang lại mức lãi cao nhất:

        **{format_money(best['Tiền lãi'])}**

        """

    )


    st.markdown(
        "### 📊 So sánh tiền lãi theo kỳ hạn"
    )


    st.bar_chart(

        comparison.set_index(
            "Kỳ hạn"
        )[["Tiền lãi"]]

    )


# =========================================================
# 12. KIẾN THỨC NGHIỆP VỤ
# =========================================================
st.markdown("---")


with st.expander(
    "📚 Kiến thức nghiệp vụ tiền gửi"
):

    st.markdown("""
    ### 1. Tiền gửi có kỳ hạn

    Khách hàng gửi tiền trong một khoảng thời gian
    xác định và được hưởng mức lãi suất theo kỳ hạn.

    ### 2. Rút trước hạn

    Trong mô hình này, nếu khách hàng rút trước
    ngày đáo hạn, hệ thống chuyển sang áp dụng
    **lãi suất không kỳ hạn**.

    ### 3. Nhận lãi hàng tháng

    Tiền lãi được tính theo số ngày thực tế
    của từng khoảng tháng.

    ### 4. Nhận lãi cuối kỳ

    Khách hàng nhận cả tiền gốc và tiền lãi
    khi kết thúc khoản gửi.

    ### 5. Nhận lãi trước

    Tiền lãi dự kiến được nhận ngay từ
    thời điểm bắt đầu gửi.

    ### 6. Tái tục

    Khi khoản tiền đến ngày đáo hạn,
    nếu khách hàng không rút,
    khoản tiền có thể được tiếp tục gửi
    sang kỳ hạn mới.

    ### 7. Cơ sở tính lãi

    Mô hình sử dụng **365 ngày/năm**.
    """)


# =========================================================
# 13. FOOTER
# =========================================================
st.markdown("---")


st.markdown("""
<center>

    🏦 <b>SMARTSAVE 360</b>

    <br><br>

    <small>

        Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm |

        Phục vụ mục đích học tập và mô phỏng

    </small>

</center>
""", unsafe_allow_html=True)
