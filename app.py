import streamlit as st
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


# ============================================================
# SMARTSAVE 360 - PHIÊN BẢN HOÀN CHỈNH
# ============================================================

st.set_page_config(
    page_title="SmartSave 360",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS - GIAO DIỆN
# ============================================================

st.markdown("""
<style>

/* ---------- Nền ---------- */

.stApp {
    background: #f4f7fb;
}

.main .block-container {
    max-width: 1500px;
    padding: 34px 34px 55px 34px;
}


/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] {
    width: 355px !important;
    min-width: 355px !important;
    max-width: 355px !important;
    background: #eef2f7 !important;
    border-right: 1px solid #dce3ec;
}

section[data-testid="stSidebar"] > div {
    width: 355px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: 18px 18px 30px 18px !important;
}


/* ---------- Tiêu đề bảng điều khiển ---------- */

.sidebar-title {
    background: linear-gradient(
        135deg,
        #101d4e 0%,
        #15568d 100%
    );

    color: #ffffff;

    border-radius: 14px;

    padding: 20px 14px;

    text-align: center;

    margin-bottom: 18px;

    box-shadow:
        0 7px 18px
        rgba(16, 29, 78, .18);
}

.sidebar-title h2 {
    margin: 0;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: .2px;
}

.sidebar-title p {
    margin: 7px 0 0 0;
    font-size: 12px;
}


/* ---------- Sidebar text ---------- */

section[data-testid="stSidebar"] h3 {
    color: #142956 !important;
    font-size: 16px !important;
    margin: 8px 0 9px 0 !important;
}

section[data-testid="stSidebar"] h4 {
    color: #334155 !important;
    font-size: 13px !important;
}

section[data-testid="stSidebar"] label {
    font-size: 12px !important;
}


/* ---------- Input ---------- */

section[data-testid="stSidebar"] input {
    min-height: 40px !important;
    font-size: 13px !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] {
    min-height: 40px !important;
}


/* ---------- Nút ---------- */

section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    min-height: 40px;
    border-radius: 9px;
    font-size: 12px;
    font-weight: 700;
    border: 1px solid #d4dce7;
    background: #ffffff;
    color: #18365c;
}

section[data-testid="stSidebar"] .stButton button:hover {
    border-color: #1d5d92;
    color: #1d5d92;
}


/* ---------- Nút tính toán ---------- */

section[data-testid="stSidebar"]
div[data-testid="stButton"]
button[kind="primary"] {

    min-height: 55px !important;

    font-size: 16px !important;

    color: white !important;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #10204f,
            #155e92
        ) !important;

    box-shadow:
        0 7px 16px
        rgba(16, 32, 79, .20);
}


/* ---------- Hero ---------- */

.hero {

    background:
        linear-gradient(
            135deg,
            #101846 0%,
            #123d71 55%,
            #155d87 100%
        );

    color: white;

    border-radius: 20px;

    padding: 34px 38px;

    margin-bottom: 24px;

    box-shadow:
        0 10px 28px
        rgba(15, 30, 70, .18);
}

.hero-top {
    display: flex;
    align-items: center;
    gap: 12px;
}

.hero-icon {
    font-size: 31px;
}

.hero h1 {
    font-size: 35px;
    margin: 0;
    font-weight: 850;
}

.hero-subtitle {
    font-size: 15px;
    margin-top: 10px;
    margin-bottom: 18px;
}

.hero-info {
    font-size: 12px;
    line-height: 1.9;
    opacity: .96;
}


/* ---------- Card ---------- */

.info-card {

    background: white;

    border: 1px solid #e1e7ef;

    border-radius: 17px;

    padding: 24px;

    min-height: 145px;

    box-shadow:
        0 5px 16px
        rgba(0,0,0,.04);
}

.info-card h3 {

    color: #173c68;

    margin: 0 0 9px 0;

    font-size: 18px;
}

.info-card p {

    color: #64748b;

    font-size: 13px;

    line-height: 1.65;
}


/* ---------- Metric ---------- */

.metric {

    background: white;

    border: 1px solid #e0e6ee;

    border-radius: 15px;

    padding: 20px 10px;

    text-align: center;

    min-height: 112px;

    box-shadow:
        0 4px 15px
        rgba(0,0,0,.04);
}

.metric-label {

    color: #64748b;

    font-size: 11px;

    font-weight: 800;
}

.metric-value {

    color: #123d73;

    font-size: 20px;

    font-weight: 850;

    margin-top: 8px;
}


/* ---------- Result ---------- */

.result-card {

    background:
        linear-gradient(
            135deg,
            #eef7ff 0%,
            #ffffff 100%
        );

    border: 1px solid #d8e6f5;

    border-radius: 17px;

    padding: 24px;

    min-height: 245px;

    box-shadow:
        0 5px 16px
        rgba(0,0,0,.04);
}

.result-card h3 {

    margin: 0 0 14px 0;

    color: #173d6c;

    font-size: 18px;
}


/* ---------- Tabs ---------- */

button[data-baseweb="tab"] {

    font-size: 14px !important;

    font-weight: 800 !important;
}


/* ---------- Mobile ---------- */

@media (max-width: 900px) {

    section[data-testid="stSidebar"] {

        width: 315px !important;

        min-width: 315px !important;

        max-width: 315px !important;
    }

    section[data-testid="stSidebar"] > div {

        width: 315px !important;
    }

    .main .block-container {

        padding:
            22px 18px 40px 18px;
    }

    .hero {

        padding: 27px 24px;
    }

    .hero h1 {

        font-size: 28px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HÀM
# ============================================================

def format_money(value):
    return f"{value:,.0f} VNĐ"


def tinh_lai(tien_goc, lai_suat, so_ngay):

    if tien_goc <= 0 or so_ngay <= 0:
        return 0.0

    return (
        tien_goc
        * (lai_suat / 100)
        * so_ngay
        / 365
    )


def tao_bang_lai_thang(
    tien_goc,
    lai_suat,
    ngay_gui,
    ngay_rut
):

    rows = []

    start = ngay_gui

    i = 1

    while start < ngay_rut:

        end = min(

            ngay_gui
            + relativedelta(
                months=i
            ),

            ngay_rut

        )

        days = (
            end - start
        ).days

        if days <= 0:
            break

        interest = tinh_lai(

            tien_goc,

            lai_suat,

            days

        )

        rows.append({

            "Tháng": i,

            "Từ ngày": start,

            "Đến ngày": end,

            "Số ngày": days,

            "Tiền lãi": interest

        })

        start = end

        i += 1

    return pd.DataFrame(rows)


# ============================================================
# SESSION STATE
# ============================================================

if "so_tien" not in st.session_state:

    st.session_state.so_tien = 50_000_000.0


if "ngay_gui" not in st.session_state:

    st.session_state.ngay_gui = date.today()


if "da_tinh" not in st.session_state:

    st.session_state.da_tinh = False


def set_money(value):

    st.session_state.so_tien = float(value)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">

        <h2>🎛️ BẢNG ĐIỀU KHIỂN</h2>

        <p>
            Thiết lập khoản tiền gửi
        </p>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # SỐ TIỀN
    # --------------------------------------------------------

    st.markdown(
        "### 💰 Số tiền gửi"
    )


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


    st.markdown(
        "#### ⚡ Chọn nhanh"
    )


    q1, q2 = st.columns(2)


    with q1:

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


    with q2:

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


    # --------------------------------------------------------
    # KỲ HẠN
    # --------------------------------------------------------

    st.markdown(
        "### 📅 Kỳ hạn & lãi suất"
    )


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

        list(
            ky_han_map.keys()
        ),

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


    st.markdown("---")


    # --------------------------------------------------------
    # THỜI GIAN
    # --------------------------------------------------------

    st.markdown(
        "### 🗓️ Thời gian"
    )


    ngay_gui = st.date_input(

        "Ngày gửi tiền",

        key="ngay_gui"

    )


    if so_thang > 0:

        ngay_dao_han = (

            ngay_gui
            + relativedelta(
                months=so_thang
            )

        )

    else:

        ngay_dao_han = ngay_gui


    if so_thang > 0:

        st.caption(

            f"📌 Ngày đáo hạn: "
            f"**{ngay_dao_han.strftime('%d/%m/%Y')}**"

        )


    ngay_rut = st.date_input(

        "Ngày rút tiền",

        value=ngay_dao_han,

        min_value=ngay_gui

    )


    st.markdown("---")


    # --------------------------------------------------------
    # PHƯƠNG THỨC NHẬN LÃI
    # --------------------------------------------------------

    st.markdown(
        "### 💵 Phương thức nhận lãi"
    )


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


    st.markdown("---")


    # --------------------------------------------------------
    # NÚT
    # --------------------------------------------------------

    if st.button(

        "🔥 TÍNH TOÁN NGAY",

        type="primary"

    ):

        st.session_state.da_tinh = True


    if st.button(
        "🔄 Đặt lại"
    ):

        st.session_state.so_tien = (
            50_000_000.0
        )

        st.session_state.ngay_gui = (
            date.today()
        )

        st.session_state.da_tinh = False

        st.rerun()


# ============================================================
# TÍNH DỮ LIỆU
# ============================================================

so_tien = st.session_state.so_tien


so_ngay = max(

    (
        ngay_rut
        - ngay_gui
    ).days,

    0

)


if so_thang == 0:

    lai_ap_dung = lai_khong_ky_han

    trang_thai = "🔵 Không kỳ hạn"

    rut_truoc_han = False


elif ngay_rut < ngay_dao_han:

    lai_ap_dung = lai_khong_ky_han

    trang_thai = "🔴 Rút trước hạn"

    rut_truoc_han = True


else:

    lai_ap_dung = lai_suat

    trang_thai = "🟢 Đúng hạn"

    rut_truoc_han = False


tien_lai = tinh_lai(

    so_tien,

    lai_ap_dung,

    so_ngay

)


# ============================================================
# LÃI HÀNG THÁNG
# ============================================================

bang_lai_thang = pd.DataFrame()


if (

    phuong_thuc
    == "📅 Nhận lãi hàng tháng"

    and so_ngay > 0

):

    bang_lai_thang = (

        tao_bang_lai_thang(

            so_tien,

            lai_ap_dung,

            ngay_gui,

            ngay_rut

        )

    )


if not bang_lai_thang.empty:

    tong_lai_thang = (

        bang_lai_thang[
            "Tiền lãi"
        ].sum()

    )

else:

    tong_lai_thang = 0


# ============================================================
# TỔNG NHẬN
# ============================================================

if (

    phuong_thuc
    == "📅 Nhận lãi hàng tháng"

):

    hien_thi_lai = tong_lai_thang

    tong_nhan = (

        so_tien
        + tong_lai_thang

    )

elif (

    phuong_thuc
    == "💵 Nhận lãi trước"

):

    hien_thi_lai = tien_lai

    tong_nhan = (

        so_tien
        + tien_lai

    )

else:

    hien_thi_lai = tien_lai

    tong_nhan = (

        so_tien
        + tien_lai

    )


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-top">

        <div class="hero-icon">
            🏦
        </div>

        <h1>
            SMARTSAVE 360
        </h1>

    </div>


    <div class="hero-subtitle">

        <b>
            Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm
        </b>

    </div>


    <div class="hero-info">

        🔴 Rút trước hạn
        → áp dụng lãi suất không kỳ hạn

        &nbsp;&nbsp; | &nbsp;&nbsp;

        🟢 Đến hạn
        → nhận lãi hoặc tái tục

        &nbsp;&nbsp; | &nbsp;&nbsp;

        📅 Cơ sở tính lãi: 365 ngày/năm

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([

    "📊 Tổng quan",

    "💰 Tính tiền gửi",

    "📋 Dòng tiền",

    "📈 So sánh thông minh"

])


# ============================================================
# TAB 1 - TỔNG QUAN
# ============================================================

with tab1:

    st.markdown(
        "## 📊 Tổng quan"
    )


    if not st.session_state.da_tinh:

        st.info(

            "💡 Thiết lập thông tin trong "
            "**Bảng điều khiển bên trái** "
            "rồi nhấn "
            "**🔥 TÍNH TOÁN NGAY**."

        )


        a, b, c = st.columns(3)


        with a:

            st.markdown("""
            <div class="info-card">

                <h3>
                    💰 Tiền gửi
                </h3>

                <p>
                    Thiết lập số tiền,
                    kỳ hạn, lãi suất
                    và thời gian gửi.
                </p>

            </div>
            """, unsafe_allow_html=True)


        with b:

            st.markdown("""
            <div class="info-card">

                <h3>
                    📈 Lợi nhuận
                </h3>

                <p>
                    Hệ thống tự động tính
                    số tiền lãi theo
                    số ngày thực tế.
                </p>

            </div>
            """, unsafe_allow_html=True)


        with c:

            st.markdown("""
            <div class="info-card">

                <h3>
                    🧠 Phân tích
                </h3>

                <p>
                    So sánh nhiều kỳ hạn
                    để hỗ trợ lựa chọn
                    phương án phù hợp.
                </p>

            </div>
            """, unsafe_allow_html=True)


    else:

        st.success(

            f"✅ Đã tính toán khoản tiền gửi "
            f"{format_money(so_tien)}"

        )


        m1, m2, m3, m4 = st.columns(4)


        metric_data = [

            (

                "💰 TIỀN GỐC",

                format_money(
                    so_tien
                )

            ),

            (

                "📈 TIỀN LÃI",

                format_money(
                    hien_thi_lai
                )

            ),

            (

                "💎 TỔNG NHẬN",

                format_money(
                    tong_nhan
                )

            ),

            (

                "📅 SỐ NGÀY",

                f"{so_ngay} ngày"

            )

        ]


        for col, item in zip(

            [m1, m2, m3, m4],

            metric_data

        ):

            title, value = item


            with col:

                st.markdown(

                    f"""
                    <div class="metric">

                        <div class="metric-label">
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

                f"🔴 Rút trước hạn — "
                f"lãi suất áp dụng "
                f"**{lai_khong_ky_han:.2f}%/năm**."

            )


        elif so_thang == 0:

            st.info(

                f"🔵 Không kỳ hạn — "
                f"lãi suất áp dụng "
                f"**{lai_khong_ky_han:.2f}%/năm**."

            )


        else:

            st.success(

                f"🟢 Đúng hạn — "
                f"lãi suất áp dụng "
                f"**{lai_suat:.2f}%/năm**."

            )


        if (

            phuong_thuc
            == "📅 Nhận lãi hàng tháng"

        ):

            st.info(

                f"📅 Tổng lãi theo lịch tháng: "
                f"**{format_money(tong_lai_thang)}**."

            )


        elif (

            phuong_thuc
            == "💵 Nhận lãi trước"

        ):

            st.info(

                f"💵 Tiền lãi nhận trước: "
                f"**{format_money(tien_lai)}**."

            )


        else:

            st.info(

                f"📆 Tiền lãi nhận cuối kỳ: "
                f"**{format_money(tien_lai)}**."

            )


# ============================================================
# TAB 2 - TÍNH TIỀN GỬI
# ============================================================

with tab2:

    st.markdown(
        "## 💰 Chi tiết khoản tiền gửi"
    )


    left, right = st.columns(2)


    with left:

        st.markdown("""
        <div class="result-card">

            <h3>
                🏦 Thông tin khoản gửi
            </h3>

        """, unsafe_allow_html=True)


        st.write(

            f"**Số tiền gửi:** "
            f"{format_money(so_tien)}"

        )


        st.write(

            f"**Kỳ hạn:** "
            f"{ky_han}"

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


    with right:

        st.markdown("""
        <div class="result-card">

            <h3>
                💵 Kết quả tài chính
            </h3>

        """, unsafe_allow_html=True)


        if (

            phuong_thuc
            == "📅 Nhận lãi hàng tháng"

        ):

            st.write(

                f"**Tổng tiền lãi:** "
                f"{format_money(tong_lai_thang)}"

            )


            st.write(

                f"**Tiền gốc cuối kỳ:** "
                f"{format_money(so_tien)}"

            )


            st.write(

                f"**Tổng giá trị:** "
                f"{format_money(so_tien + tong_lai_thang)}"

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


        st.markdown(

            "</div>",

            unsafe_allow_html=True

        )


    # --------------------------------------------------------
    # BẢNG LÃI HÀNG THÁNG
    # --------------------------------------------------------

    if (

        phuong_thuc
        == "📅 Nhận lãi hàng tháng"

        and not bang_lai_thang.empty

    ):

        st.markdown("---")


        st.markdown(
            "### 📅 Lịch nhận tiền lãi hàng tháng"
        )


        display_df = (
            bang_lai_thang.copy()
        )


        display_df["Từ ngày"] = (

            display_df["Từ ngày"]

            .dt.strftime("%d/%m/%Y")

        )


        display_df["Đến ngày"] = (

            display_df["Đến ngày"]

            .dt.strftime("%d/%m/%Y")

        )


        display_df["Tiền lãi"] = (

            display_df["Tiền lãi"]

            .apply(format_money)

        )


        st.dataframe(

            display_df,

            use_container_width=True,

            hide_index=True

        )


    # --------------------------------------------------------
    # CÔNG THỨC
    # --------------------------------------------------------

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


# ============================================================
# TAB 3 - DÒNG TIỀN
# ============================================================

with tab3:

    st.markdown(
        "## 📋 Bảng dòng tiền"
    )


    cashflow = []


    if (

        phuong_thuc
        == "📅 Nhận lãi hàng tháng"

        and not bang_lai_thang.empty

    ):

        cashflow.append(

            [

                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"-{format_money(so_tien)}",

                "Gửi tiền gốc"

            ]

        )


        for _, row in (
            bang_lai_thang.iterrows()
        ):

            cashflow.append(

                [

                    f"Tháng {int(row['Tháng'])}",

                    row["Đến ngày"].strftime(
                        "%d/%m/%Y"
                    ),

                    f"+{format_money(row['Tiền lãi'])}",

                    "Nhận lãi hàng tháng"

                ]

            )


        cashflow.append(

            [

                "Đáo hạn / rút",

                ngay_rut.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(so_tien)}",

                "Nhận lại tiền gốc"

            ]

        )


    elif (

        phuong_thuc
        == "💵 Nhận lãi trước"

    ):

        cashflow = [

            [

                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(tien_lai)}",

                "Nhận lãi trước"

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

                "Ngày đáo hạn / rút",

                ngay_rut.strftime(
                    "%d/%m/%Y"
                ),

                f"+{format_money(so_tien)}",

                "Nhận lại tiền gốc"

            ]

        ]


    else:

        cashflow = [

            [

                "Ngày gửi",

                ngay_gui.strftime(
                    "%d/%m/%Y"
                ),

                f"-{format_money(so_tien)}",

                "Gửi tiền"

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

                "Nhận gốc + lãi"

            ]

        ]


    cashflow_df = pd.DataFrame(

        cashflow,

        columns=[

            "Thời điểm",

            "Ngày",

            "Dòng tiền",

            "Nội dung"

        ]

    )


    st.dataframe(

        cashflow_df,

        use_container_width=True,

        hide_index=True

    )


    st.markdown(
        "### 📊 Biểu đồ"
    )


    if (

        phuong_thuc
        == "📅 Nhận lãi hàng tháng"

        and not bang_lai_thang.empty

    ):

        chart_df = (
            bang_lai_thang.copy()
        )


        chart_df["Tháng"] = (

            "Tháng "
            + chart_df["Tháng"].astype(str)

        )


        st.bar_chart(

            chart_df.set_index(
                "Tháng"
            )[["Tiền lãi"]]

        )


    else:

        chart_df = pd.DataFrame({

            "Khoản mục": [

                "Tiền gốc",

                "Tiền lãi",

                "Tổng nhận"

            ],

            "Giá trị": [

                so_tien,

                tien_lai,

                so_tien + tien_lai

            ]

        })


        st.bar_chart(

            chart_df.set_index(
                "Khoản mục"
            )

        )


# ============================================================
# TAB 4 - SO SÁNH THÔNG MINH
# ============================================================

with tab4:

    st.markdown(
        "## 📈 So sánh thông minh"
    )


    compare_terms = {

        "1 tháng": 1,

        "3 tháng": 3,

        "6 tháng": 6,

        "9 tháng": 9,

        "12 tháng": 12,

        "18 tháng": 18,

        "24 tháng": 24,

        "36 tháng": 36

    }


    rows = []


    for name, months in (
        compare_terms.items()
    ):

        end_date = (

            ngay_gui
            + relativedelta(
                months=months
            )

        )


        days = (

            end_date
            - ngay_gui

        ).days


        interest = tinh_lai(

            so_tien,

            lai_suat,

            days

        )


        rows.append(

            [

                name,

                days,

                lai_suat,

                interest,

                so_tien + interest

            ]

        )


    comparison = pd.DataFrame(

        rows,

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

        comparison[
            "Tiền lãi"
        ].idxmax()

    ]


    st.success(

        f"🏆 Với số tiền "
        f"{format_money(so_tien)}, "
        f"kỳ hạn **{best['Kỳ hạn']}** "
        f"có mức lãi cao nhất: "
        f"**{format_money(best['Tiền lãi'])}**."

    )


    st.markdown(
        "### 📊 Biểu đồ tiền lãi theo kỳ hạn"
    )


    st.bar_chart(

        comparison.set_index(
            "Kỳ hạn"
        )[["Tiền lãi"]]

    )


# ============================================================
# KIẾN THỨC NGHIỆP VỤ
# ============================================================

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
    ngày đáo hạn, hệ thống áp dụng lãi suất
    không kỳ hạn.

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


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")


st.markdown("""
<div style="
    text-align:center;
    color:#64748b;
    font-size:12px;
    padding-bottom:20px;
">

    🏦 <b>SMARTSAVE 360</b>

    <br><br>

    Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm |

    Phục vụ mục đích học tập và mô phỏng

</div>
""", unsafe_allow_html=True)
