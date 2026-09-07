import streamlit as st
import pandas as pd
from datetime import date
import calendar
from textwrap import dedent


# ============================================================
# SMARTSAVE 360
# HỆ THỐNG MÔ PHỎNG NGHIỆP VỤ TIỀN GỬI TIẾT KIỆM
# ============================================================

st.set_page_config(
    page_title="SmartSave 360",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    dedent("""
    <style>

    /* ==============================
       TOÀN BỘ TRANG
       ============================== */

    .stApp {
        background: #f7f8fb;
    }

    .main .block-container {
        max-width: 1500px;
        padding: 28px 35px 60px 35px;
    }


    /* ==============================
       SIDEBAR
       ============================== */

    section[data-testid="stSidebar"] {
        background: #eef0f4 !important;
        width: 365px !important;
        min-width: 365px !important;
        max-width: 365px !important;
    }

    section[data-testid="stSidebar"] > div {
        width: 365px !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding: 25px 20px 40px 20px !important;
    }


    /* ==============================
       BẢNG ĐIỀU KHIỂN
       ============================== */

    .dashboard-box {
        width: 100%;
        min-height: 125px;

        background: linear-gradient(
            135deg,
            #101b50 0%,
            #185b91 100%
        );

        border-radius: 16px;

        padding: 27px 15px;

        text-align: center;

        color: white;

        box-shadow:
            0 9px 22px rgba(12, 35, 75, 0.22);

        margin-bottom: 27px;
    }

    .dashboard-box h2 {
        color: white !important;

        font-size: 21px !important;

        font-weight: 800 !important;

        margin: 0 !important;

        padding: 0 !important;
    }

    .dashboard-box p {
        color: white !important;

        font-size: 12px !important;

        margin: 13px 0 0 0 !important;
    }


    /* ==============================
       SIDEBAR
       ============================== */

    .side-heading {
        font-size: 17px;

        font-weight: 800;

        color: #202b40;

        margin-top: 13px;

        margin-bottom: 10px;
    }

    .selected-money {
        background: #dceaff;

        border-radius: 9px;

        padding: 13px 12px;

        color: #135596;

        font-size: 12px;

        font-weight: 750;

        margin-top: 10px;

        margin-bottom: 18px;
    }


    /* ==============================
       HERO
       ============================== */

    .hero-box {
        background: linear-gradient(
            135deg,
            #10194d 0%,
            #123c6d 48%,
            #175e8f 100%
        );

        border-radius: 19px;

        padding: 37px 42px;

        min-height: 285px;

        color: white;

        box-shadow:
            0 12px 30px rgba(15, 32, 75, 0.20);

        margin-bottom: 25px;
    }

    .hero-box h1 {
        color: white !important;

        font-size: 32px !important;

        font-weight: 850 !important;

        margin: 0 0 10px 0 !important;
    }

    .hero-box .hero-subtitle {
        color: white;

        font-size: 14px;

        font-weight: 650;

        margin-bottom: 24px;
    }

    .hero-box .hero-item {
        color: white;

        font-size: 13px;

        margin: 15px 0;

        line-height: 1.6;
    }


    /* ==============================
       CARD
       ============================== */

    .white-card {
        background: white;

        border: 1px solid #e1e6ed;

        border-radius: 15px;

        padding: 22px;

        min-height: 200px;

        box-shadow:
            0 5px 17px rgba(0,0,0,0.04);
    }

    .blue-card {
        background: #edf6ff;

        border: 1px solid #d6e7f7;

        border-radius: 15px;

        padding: 22px;

        min-height: 200px;

        box-shadow:
            0 5px 17px rgba(0,0,0,0.04);
    }

    .card-title {
        color: #123f70;

        font-size: 18px;

        font-weight: 800;

        margin-bottom: 16px;
    }


    /* ==============================
       KẾT QUẢ LỚN
       ============================== */

    .big-result {
        background: linear-gradient(
            135deg,
            #edf6ff,
            #ffffff
        );

        border: 1px solid #d7e7f6;

        border-radius: 15px;

        padding: 22px;

        margin-top: 10px;
    }

    .big-result-title {
        color: #123f70;

        font-size: 16px;

        font-weight: 800;
    }

    .big-result-value {
        color: #123f70;

        font-size: 27px;

        font-weight: 850;

        margin-top: 7px;
    }


    /* ==============================
       BUTTON
       ============================== */

    .stButton > button {
        border-radius: 9px !important;

        min-height: 42px !important;

        font-weight: 700 !important;
    }


    /* ==============================
       MOBILE
       ============================== */

    @media (max-width: 900px) {

        section[data-testid="stSidebar"] {
            width: 310px !important;

            min-width: 310px !important;

            max-width: 310px !important;
        }

        section[data-testid="stSidebar"] > div {
            width: 310px !important;
        }

        .hero-box {
            padding: 28px;
        }

        .hero-box h1 {
            font-size: 27px !important;
        }
    }

    </style>
    """),
    unsafe_allow_html=True
)


# ============================================================
# HÀM HỖ TRỢ
# ============================================================

def format_money(value):
    return f"{value:,.0f} VNĐ"


def calculate_interest(principal, rate, days):
    if principal <= 0 or days <= 0:
        return 0

    return principal * (rate / 100) * days / 365


def add_months(original_date, months):
    total_month = (
        original_date.year * 12
        + original_date.month
        - 1
        + months
    )

    year = total_month // 12

    month = total_month % 12 + 1

    day = min(
        original_date.day,
        calendar.monthrange(year, month)[1]
    )

    return date(year, month, day)


def monthly_interest_table(
    principal,
    rate,
    start_date,
    end_date
):

    rows = []

    current = start_date

    month_number = 1

    while current < end_date:

        next_date = add_months(
            start_date,
            month_number
        )

        if next_date > end_date:
            next_date = end_date

        days = (
            next_date - current
        ).days

        if days <= 0:
            break

        interest = calculate_interest(
            principal,
            rate,
            days
        )

        rows.append(
            {
                "Tháng": month_number,
                "Từ ngày": current.strftime(
                    "%d/%m/%Y"
                ),
                "Đến ngày": next_date.strftime(
                    "%d/%m/%Y"
                ),
                "Số ngày": days,
                "Tiền lãi": interest
            }
        )

        current = next_date

        month_number += 1

    return pd.DataFrame(rows)


# ============================================================
# SESSION STATE
# ============================================================

if "principal" not in st.session_state:

    st.session_state.principal = 50_000_000.0


def set_money(value):

    st.session_state.principal = float(value)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # -----------------------------------------
    # BẢNG ĐIỀU KHIỂN
    # -----------------------------------------

    dashboard_html = dedent("""
    <div class="dashboard-box">
        <h2>🎛️ BẢNG ĐIỀU KHIỂN</h2>
        <p>Thiết lập khoản tiền gửi</p>
    </div>
    """)

    st.markdown(
        dashboard_html,
        unsafe_allow_html=True
    )


    # -----------------------------------------
    # SỐ TIỀN
    # -----------------------------------------

    st.markdown(
        '<div class="side-heading">💰 Số tiền gửi</div>',
        unsafe_allow_html=True
    )

    st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0.0,
        step=1_000_000.0,
        format="%.0f",
        key="principal"
    )

    selected_money_html = dedent(
        f"""
        <div class="selected-money">
            💵 Đang chọn: {format_money(
                st.session_state.principal
            )}
        </div>
        """
    )

    st.markdown(
        selected_money_html,
        unsafe_allow_html=True
    )


    # -----------------------------------------
    # CHỌN NHANH
    # -----------------------------------------

    st.markdown(
        '<div class="side-heading">⚡ Chọn nhanh</div>',
        unsafe_allow_html=True
    )

    col_a, col_b = st.columns(2)

    with col_a:

        st.button(
            "💰 50 triệu",
            use_container_width=True,
            on_click=set_money,
            args=(50_000_000,)
        )

        st.button(
            "💰 200 triệu",
            use_container_width=True,
            on_click=set_money,
            args=(200_000_000,)
        )

        st.button(
            "💰 500 triệu",
            use_container_width=True,
            on_click=set_money,
            args=(500_000_000,)
        )

    with col_b:

        st.button(
            "💰 100 triệu",
            use_container_width=True,
            on_click=set_money,
            args=(100_000_000,)
        )

        st.button(
            "💰 1 tỷ",
            use_container_width=True,
            on_click=set_money,
            args=(1_000_000_000,)
        )

        st.button(
            "💰 2 tỷ",
            use_container_width=True,
            on_click=set_money,
            args=(2_000_000_000,)
        )


    st.markdown("---")


    # -----------------------------------------
    # KỲ HẠN
    # -----------------------------------------

    st.markdown(
        '<div class="side-heading">📅 Kỳ hạn</div>',
        unsafe_allow_html=True
    )

    term_options = {
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

    term_name = st.selectbox(
        "Chọn kỳ hạn",
        list(term_options.keys()),
        index=2
    )

    term_months = term_options[term_name]


    # -----------------------------------------
    # LÃI SUẤT
    # -----------------------------------------

    st.markdown(
        '<div class="side-heading">📈 Lãi suất</div>',
        unsafe_allow_html=True
    )

    fixed_rate = st.number_input(
        "Lãi suất có kỳ hạn (%/năm)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    non_term_rate = st.number_input(
        "Lãi suất không kỳ hạn (%/năm)",
        min_value=0.0,
        value=0.2,
        step=0.1
    )


    st.markdown("---")


    # -----------------------------------------
    # NGÀY GỬI
    # -----------------------------------------

    st.markdown(
        '<div class="side-heading">🗓️ Thời gian</div>',
        unsafe_allow_html=True
    )

    start_date = st.date_input(
        "Ngày gửi",
        value=date.today()
    )

    if term_months > 0:

        maturity_date = add_months(
            start_date,
            term_months
        )

    else:

        maturity_date = start_date


    st.caption(
        "📌 Ngày đáo hạn: "
        + maturity_date.strftime("%d/%m/%Y")
    )


    end_date = st.date_input(
        "Ngày rút tiền",
        value=maturity_date,
        min_value=start_date
    )


    st.markdown("---")


    # -----------------------------------------
    # PHƯƠNG THỨC NHẬN LÃI
    # -----------------------------------------

    st.markdown(
        '<div class="side-heading">💵 Phương thức nhận lãi</div>',
        unsafe_allow_html=True
    )

    interest_method = st.radio(
        "Chọn phương thức",
        [
            "Nhận lãi trước",
            "Nhận lãi hàng tháng",
            "Nhận lãi cuối kỳ"
        ],
        index=2
    )

    rollover = st.checkbox(
        "🔄 Tự động tái tục khi đáo hạn"
    )


# ============================================================
# TÍNH TOÁN
# ============================================================

principal = st.session_state.principal

actual_days = max(
    (end_date - start_date).days,
    0
)


if term_months == 0:

    applied_rate = non_term_rate

    status = "🔵 Không kỳ hạn"

    early_withdrawal = False


elif end_date < maturity_date:

    applied_rate = non_term_rate

    status = "🔴 Rút trước hạn"

    early_withdrawal = True


else:

    applied_rate = fixed_rate

    status = "🟢 Đúng hạn"

    early_withdrawal = False


interest = calculate_interest(
    principal,
    applied_rate,
    actual_days
)


# ============================================================
# HERO
# ============================================================

hero_html = dedent("""
<div class="hero-box">

    <h1>🏦 SMARTSAVE 360</h1>

    <div class="hero-subtitle">
        Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm
    </div>

    <div class="hero-item">
        🔴 Rút trước hạn → áp dụng lãi suất không kỳ hạn
    </div>

    <div class="hero-item">
        🟢 Đến hạn → nhận lãi hoặc tái tục
    </div>

    <div class="hero-item">
        📅 Cơ sở tính lãi: 365 ngày/năm
    </div>

</div>
""")

st.markdown(
    hero_html,
    unsafe_allow_html=True
)


# ============================================================
# TABS
# ============================================================

tab_overview, tab_calculate, tab_cashflow, tab_compare = st.tabs(
    [
        "📊 Tổng quan",
        "💰 Tính tiền gửi",
        "📋 Dòng tiền",
        "📈 So sánh thông minh"
    ]
)


# ============================================================
# TAB 1 - TỔNG QUAN
# ============================================================

with tab_overview:

    st.markdown(
        "## 💰 Chi tiết khoản tiền gửi"
    )


    # -----------------------------------------
    # 3 CHỈ SỐ
    # -----------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💵 TIỀN GỐC",
            format_money(principal)
        )

    with col2:

        st.metric(
            "📈 TIỀN LÃI",
            format_money(interest)
        )

    with col3:

        st.metric(
            "💎 TỔNG NHẬN",
            format_money(
                principal + interest
            )
        )


    # -----------------------------------------
    # TRẠNG THÁI
    # -----------------------------------------

    if early_withdrawal:

        st.error(
            "🔴 Rút trước hạn → "
            f"áp dụng lãi suất "
            f"{non_term_rate:.2f}%/năm."
        )

    elif term_months == 0:

        st.info(
            "🔵 Không kỳ hạn → "
            f"áp dụng lãi suất "
            f"{non_term_rate:.2f}%/năm."
        )

    else:

        st.success(
            "🟢 Đúng hạn → "
            f"áp dụng lãi suất "
            f"{fixed_rate:.2f}%/năm."
        )


    # -----------------------------------------
    # HAI CARD
    # -----------------------------------------

    left_col, right_col = st.columns(2)


    with left_col:

        left_html = dedent(
            f"""
            <div class="white-card">

                <div class="card-title">
                    🏦 Thông tin khoản gửi
                </div>

                <p>
                    <b>Số tiền gửi:</b>
                    {format_money(principal)}
                </p>

                <p>
                    <b>Kỳ hạn:</b>
                    {term_name}
                </p>

                <p>
                    <b>Ngày gửi:</b>
                    {start_date.strftime("%d/%m/%Y")}
                </p>

                <p>
                    <b>Ngày đáo hạn:</b>
                    {maturity_date.strftime("%d/%m/%Y")}
                </p>

                <p>
                    <b>Ngày rút:</b>
                    {end_date.strftime("%d/%m/%Y")}
                </p>

                <p>
                    <b>Số ngày thực tế:</b>
                    {actual_days} ngày
                </p>

            </div>
            """
        )

        st.markdown(
            left_html,
            unsafe_allow_html=True
        )


    with right_col:

        right_html = dedent(
            f"""
            <div class="blue-card">

                <div class="card-title">
                    💰 Kết quả tài chính
                </div>

                <p>
                    <b>Lãi suất áp dụng:</b>
                    {applied_rate:.2f}%/năm
                </p>

                <p>
                    <b>Tiền lãi:</b>
                    {format_money(interest)}
                </p>

                <p>
                    <b>Tổng tiền nhận:</b>
                    {format_money(principal + interest)}
                </p>

                <p>
                    <b>Trạng thái:</b>
                    {status}
                </p>

                <p>
                    <b>Tái tục:</b>
                    {"Có 🔄" if rollover else "Không"}
                </p>

            </div>
            """
        )

        st.markdown(
            right_html,
            unsafe_allow_html=True
        )


# ============================================================
# TAB 2 - TÍNH TIỀN GỬI
# ============================================================

with tab_calculate:

    st.markdown(
        "## 💰 Tính tiền gửi"
    )


    formula_html = dedent("""
    <div class="white-card">

        <div class="card-title">
            📐 Công thức tính lãi
        </div>

        <p>
            Tiền lãi được tính dựa trên tiền gốc,
            lãi suất và số ngày gửi thực tế.
        </p>

    </div>
    """)

    st.markdown(
        formula_html,
        unsafe_allow_html=True
    )


    st.latex(
        r"""
        I =
        P \times
        \frac{r}{100}
        \times
        \frac{n}{365}
        """
    )


    st.write(
        f"**P - Tiền gốc:** "
        f"{format_money(principal)}"
    )

    st.write(
        f"**r - Lãi suất:** "
        f"{applied_rate:.2f}%/năm"
    )

    st.write(
        f"**n - Số ngày:** "
        f"{actual_days} ngày"
    )


    result_html = dedent(
        f"""
        <div class="big-result">

            <div class="big-result-title">
                💰 TIỀN LÃI
            </div>

            <div class="big-result-value">
                {format_money(interest)}
            </div>

        </div>
        """
    )

    st.markdown(
        result_html,
        unsafe_allow_html=True
    )


    st.markdown("")


    result_html_2 = dedent(
        f"""
        <div class="big-result">

            <div class="big-result-title">
                💎 TỔNG TIỀN NHẬN
            </div>

            <div class="big-result-value">
                {format_money(principal + interest)}
            </div>

        </div>
        """
    )

    st.markdown(
        result_html_2,
        unsafe_allow_html=True
    )


    # -----------------------------------------
    # LÃI HÀNG THÁNG
    # -----------------------------------------

    if interest_method == "Nhận lãi hàng tháng":

        st.markdown("---")

        st.markdown(
            "### 📅 Lịch nhận lãi hàng tháng"
        )

        monthly_df = monthly_interest_table(
            principal,
            applied_rate,
            start_date,
            end_date
        )

        if not monthly_df.empty:

            display_monthly = monthly_df.copy()

            display_monthly["Tiền lãi"] = (
                display_monthly["Tiền lãi"]
                .apply(format_money)
            )

            st.dataframe(
                display_monthly,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "Khoản gửi chưa đủ thời gian để "
                "hiển thị lịch lãi hàng tháng."
            )


# ============================================================
# TAB 3 - DÒNG TIỀN
# ============================================================

with tab_cashflow:

    st.markdown(
        "## 📋 Dòng tiền khoản gửi"
    )


    cashflow_rows = []


    cashflow_rows.append(
        {
            "Thời điểm": "Ngày gửi",
            "Ngày": start_date.strftime(
                "%d/%m/%Y"
            ),
            "Dòng tiền": -principal,
            "Nội dung": "Gửi tiền"
        }
    )


    if interest_method == "Nhận lãi hàng tháng":

        monthly_df = monthly_interest_table(
            principal,
            applied_rate,
            start_date,
            end_date
        )

        if not monthly_df.empty:

            for _, row in monthly_df.iterrows():

                cashflow_rows.append(
                    {
                        "Thời điểm":
                            f"Tháng {int(row['Tháng'])}",

                        "Ngày":
                            row["Đến ngày"],

                        "Dòng tiền":
                            row["Tiền lãi"],

                        "Nội dung":
                            "Nhận lãi hàng tháng"
                    }
                )


        cashflow_rows.append(
            {
                "Thời điểm": "Ngày rút",

                "Ngày": end_date.strftime(
                    "%d/%m/%Y"
                ),

                "Dòng tiền": principal,

                "Nội dung": "Nhận lại tiền gốc"
            }
        )


    else:

        cashflow_rows.append(
            {
                "Thời điểm": "Ngày rút",

                "Ngày": end_date.strftime(
                    "%d/%m/%Y"
                ),

                "Dòng tiền":
                    principal + interest,

                "Nội dung":
                    "Nhận gốc + lãi"
            }
        )


    cashflow_df = pd.DataFrame(
        cashflow_rows
    )


    display_cashflow = cashflow_df.copy()

    display_cashflow["Dòng tiền"] = (
        display_cashflow["Dòng tiền"]
        .apply(format_money)
    )


    st.dataframe(
        display_cashflow,
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        "### 📊 Biểu đồ dòng tiền"
    )


    chart_df = cashflow_df[
        ["Thời điểm", "Dòng tiền"]
    ].copy()

    chart_df = chart_df.set_index(
        "Thời điểm"
    )

    st.bar_chart(
        chart_df
    )


# ============================================================
# TAB 4 - SO SÁNH
# ============================================================

with tab_compare:

    st.markdown(
        "## 📈 So sánh thông minh"
    )


    comparison_terms = {
        "1 tháng": 1,
        "3 tháng": 3,
        "6 tháng": 6,
        "9 tháng": 9,
        "12 tháng": 12,
        "18 tháng": 18,
        "24 tháng": 24,
        "36 tháng": 36
    }


    comparison_rows = []


    for name, months in comparison_terms.items():

        finish_date = add_months(
            start_date,
            months
        )

        comparison_days = (
            finish_date - start_date
        ).days

        comparison_interest = (
            calculate_interest(
                principal,
                fixed_rate,
                comparison_days
            )
        )

        comparison_rows.append(
            {
                "Kỳ hạn": name,

                "Số ngày":
                    comparison_days,

                "Lãi suất":
                    fixed_rate,

                "Tiền lãi":
                    comparison_interest,

                "Tổng nhận":
                    principal + comparison_interest
            }
        )


    comparison_df = pd.DataFrame(
        comparison_rows
    )


    display_comparison = comparison_df.copy()


    display_comparison["Lãi suất"] = (
        display_comparison["Lãi suất"]
        .apply(
            lambda x: f"{x:.2f}%"
        )
    )


    display_comparison["Tiền lãi"] = (
        display_comparison["Tiền lãi"]
        .apply(format_money)
    )


    display_comparison["Tổng nhận"] = (
        display_comparison["Tổng nhận"]
        .apply(format_money)
    )


    st.dataframe(
        display_comparison,
        use_container_width=True,
        hide_index=True
    )


    best_index = comparison_df[
        "Tiền lãi"
    ].idxmax()


    best_term = comparison_df.loc[
        best_index
    ]


    st.success(
        f"🏆 Kỳ hạn có tiền lãi cao nhất: "
        f"**{best_term['Kỳ hạn']}** — "
        f"{format_money(best_term['Tiền lãi'])}"
    )


    st.markdown(
        "### 📊 Biểu đồ so sánh tiền lãi"
    )


    comparison_chart = comparison_df[
        ["Kỳ hạn", "Tiền lãi"]
    ].set_index(
        "Kỳ hạn"
    )


    st.bar_chart(
        comparison_chart
    )


# ============================================================
# KIẾN THỨC NGHIỆP VỤ
# ============================================================

st.markdown("---")


with st.expander(
    "📚 Kiến thức nghiệp vụ tiền gửi"
):

    st.markdown(
        """
        ### 1. Tiền gửi có kỳ hạn

        Khách hàng gửi tiền trong một khoảng thời gian
        xác định và được hưởng lãi suất tương ứng
        với kỳ hạn.

        ### 2. Rút trước hạn

        Nếu khách hàng rút tiền trước ngày đáo hạn,
        mô hình áp dụng lãi suất không kỳ hạn.

        ### 3. Nhận lãi cuối kỳ

        Khách hàng nhận tiền gốc và tiền lãi
        khi khoản tiền gửi đến hạn.

        ### 4. Nhận lãi hàng tháng

        Tiền lãi được tính và phân bổ theo
        từng khoảng thời gian trong kỳ gửi.

        ### 5. Tự động tái tục

        Khi khoản tiền gửi đến hạn,
        khách hàng có thể tiếp tục gửi tiền
        sang một kỳ hạn mới.

        ### 6. Cơ sở tính lãi

        Hệ thống sử dụng cơ sở tính lãi
        **365 ngày/năm**.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🏦 SmartSave 360 | "
    "Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm | "
    "Phục vụ mục đích học tập"
)
