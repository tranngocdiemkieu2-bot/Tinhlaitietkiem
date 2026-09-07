import streamlit as st
import pandas as pd
from datetime import date
import calendar


# =========================================================
# SMARTSAVE 360
# HỆ THỐNG MÔ PHỎNG NGHIỆP VỤ TIỀN GỬI TIẾT KIỆM
# =========================================================

st.set_page_config(
    page_title="SmartSave 360",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f7f8fb;
}


/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background-color: #eef0f4 !important;
    width: 360px !important;
}

section[data-testid="stSidebar"] > div {
    width: 360px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: 28px 22px 40px 22px !important;
}


/* =========================
   BẢNG ĐIỀU KHIỂN
   ========================= */

.dashboard-box {
    background: linear-gradient(
        135deg,
        #101b50,
        #15588e
    );

    color: white;

    border-radius: 15px;

    padding: 23px 15px;

    margin-bottom: 25px;

    text-align: center;

    box-shadow: 0 8px 22px rgba(16, 35, 75, 0.22);
}

.dashboard-title {
    font-size: 19px;
    font-weight: 800;
    margin-bottom: 7px;
}

.dashboard-subtitle {
    font-size: 11px;
    opacity: 0.9;
}


/* =========================
   SIDEBAR INPUT
   ========================= */

.sidebar-heading {
    font-size: 16px;
    font-weight: 800;
    color: #202a3d;
    margin-top: 8px;
    margin-bottom: 10px;
}

.money-selected {
    background-color: #dceaff;
    color: #135494;
    padding: 12px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    margin: 12px 0 18px 0;
}


/* =========================
   MAIN HERO
   ========================= */

.hero-box {
    background: linear-gradient(
        135deg,
        #10184c 0%,
        #123e70 50%,
        #155d8b 100%
    );

    color: white;

    border-radius: 18px;

    padding: 38px 40px;

    min-height: 270px;

    box-shadow: 0 10px 28px rgba(15, 30, 70, 0.20);

    margin-bottom: 20px;
}

.hero-title {
    font-size: 32px;
    font-weight: 850;
    margin-bottom: 12px;
}

.hero-subtitle {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 24px;
}

.hero-line {
    font-size: 13px;
    margin: 16px 0;
    line-height: 1.6;
}


/* =========================
   CARD
   ========================= */

.card {
    background: white;
    border-radius: 15px;
    padding: 22px;
    border: 1px solid #e4e8ee;
    box-shadow: 0 5px 18px rgba(0,0,0,0.045);
    margin-bottom: 18px;
}

.card-title {
    color: #153d6b;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 12px;
}


/* =========================
   KẾT QUẢ
   ========================= */

.result-card {
    background: linear-gradient(
        135deg,
        #edf6ff,
        #ffffff
    );

    border: 1px solid #d8e7f5;

    border-radius: 15px;

    padding: 22px;

    margin-bottom: 18px;
}

.result-number {
    color: #124b82;
    font-size: 23px;
    font-weight: 850;
}


/* =========================
   METRIC
   ========================= */

.metric-card {
    background: white;
    border: 1px solid #e1e6ed;
    border-radius: 13px;
    padding: 19px 12px;
    text-align: center;
    min-height: 105px;
    box-shadow: 0 4px 13px rgba(0,0,0,0.04);
}

.metric-label {
    font-size: 11px;
    font-weight: 800;
    color: #667085;
}

.metric-value {
    font-size: 19px;
    font-weight: 850;
    color: #123f70;
    margin-top: 8px;
}


/* =========================
   BUTTON
   ========================= */

.stButton > button {
    border-radius: 9px !important;
    font-weight: 700 !important;
}


/* =========================
   PRIMARY BUTTON
   ========================= */

.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        #102052,
        #155e91
    ) !important;

    color: white !important;

    border: none !important;

    min-height: 48px !important;
}


/* =========================
   TAB
   ========================= */

button[data-baseweb="tab"] {
    font-weight: 750 !important;
}


/* =========================
   MOBILE
   ========================= */

@media (max-width: 900px) {

    section[data-testid="stSidebar"] {
        width: 310px !important;
    }

    section[data-testid="stSidebar"] > div {
        width: 310px !important;
    }

    .hero-box {
        padding: 27px;
    }

    .hero-title {
        font-size: 27px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HÀM TÍNH TOÁN
# =========================================================

def format_money(number):
    return f"{number:,.0f} VNĐ"


def calculate_interest(principal, rate, days):
    if principal <= 0 or days <= 0:
        return 0
    return principal * rate / 100 * days / 365


def add_months(original_date, months):
    month = original_date.month - 1 + months
    year = original_date.year + month // 12
    month = month % 12 + 1

    day = min(
        original_date.day,
        calendar.monthrange(year, month)[1]
    )

    return date(year, month, day)


def create_monthly_table(
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

        days = (next_date - current).days

        if days <= 0:
            break

        interest = calculate_interest(
            principal,
            rate,
            days
        )

        rows.append({
            "Tháng": month_number,
            "Từ ngày": current,
            "Đến ngày": next_date,
            "Số ngày": days,
            "Tiền lãi": interest
        })

        current = next_date
        month_number += 1

    return pd.DataFrame(rows)


# =========================================================
# SESSION STATE
# =========================================================

if "principal" not in st.session_state:
    st.session_state.principal = 50_000_000.0

if "start_date" not in st.session_state:
    st.session_state.start_date = date.today()

if "calculate" not in st.session_state:
    st.session_state.calculate = False


def change_money(value):
    st.session_state.principal = float(value)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="dashboard-box">

        <div class="dashboard-title">
            🎛️ BẢNG ĐIỀU KHIỂN
        </div>

        <div class="dashboard-subtitle">
            Thiết lập khoản tiền gửi
        </div>

    </div>
    """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # SỐ TIỀN
    # -----------------------------------------------------

    st.markdown(
        '<div class="sidebar-heading">💰 Số tiền gửi</div>',
        unsafe_allow_html=True
    )

    st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0.0,
        step=1_000_000.0,
        format="%.0f",
        key="principal"
    )

    st.markdown(
        f"""
        <div class="money-selected">
            💵 Đang chọn:
            {format_money(st.session_state.principal)}
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # CHỌN NHANH
    # -----------------------------------------------------

    st.markdown(
        '<div class="sidebar-heading">⚡ Chọn nhanh</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.button(
            "💰 50 triệu",
            on_click=change_money,
            args=(50_000_000,)
        )

        st.button(
            "💰 200 triệu",
            on_click=change_money,
            args=(200_000_000,)
        )

        st.button(
            "💰 500 triệu",
            on_click=change_money,
            args=(500_000_000,)
        )

    with c2:

        st.button(
            "💰 100 triệu",
            on_click=change_money,
            args=(100_000_000,)
        )

        st.button(
            "💰 1 tỷ",
            on_click=change_money,
            args=(1_000_000_000,)
        )

        st.button(
            "💰 2 tỷ",
            on_click=change_money,
            args=(2_000_000_000,)
        )


    st.markdown("---")


    # -----------------------------------------------------
    # KỲ HẠN
    # -----------------------------------------------------

    st.markdown(
        '<div class="sidebar-heading">📅 Kỳ hạn & lãi suất</div>',
        unsafe_allow_html=True
    )

    terms = {
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
        "Kỳ hạn gửi tiền",
        list(terms.keys()),
        index=2
    )

    term_months = terms[term_name]

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


    # -----------------------------------------------------
    # NGÀY GỬI
    # -----------------------------------------------------

    st.markdown(
        '<div class="sidebar-heading">🗓️ Thời gian</div>',
        unsafe_allow_html=True
    )

    start_date = st.date_input(
        "Ngày gửi",
        key="start_date"
    )

    if term_months > 0:

        maturity_date = add_months(
            start_date,
            term_months
        )

    else:

        maturity_date = start_date


    if term_months > 0:

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


    # -----------------------------------------------------
    # PHƯƠNG THỨC NHẬN LÃI
    # -----------------------------------------------------

    st.markdown(
        '<div class="sidebar-heading">💵 Phương thức nhận lãi</div>',
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


    auto_rollover = st.checkbox(
        "🔄 Tự động tái tục khi đáo hạn"
    )


    st.markdown("---")


    # -----------------------------------------------------
    # NÚT TÍNH
    # -----------------------------------------------------

    if st.button(
        "🔥 TÍNH TOÁN NGAY",
        type="primary",
        use_container_width=True
    ):

        st.session_state.calculate = True


    if st.button(
        "🔄 Đặt lại",
        use_container_width=True
    ):

        st.session_state.principal = 50_000_000.0
        st.session_state.start_date = date.today()
        st.session_state.calculate = False

        st.rerun()


# =========================================================
# TÍNH KẾT QUẢ
# =========================================================

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


# =========================================================
# BẢNG LÃI HÀNG THÁNG
# =========================================================

monthly_table = pd.DataFrame()

if (
    interest_method == "Nhận lãi hàng tháng"
    and actual_days > 0
):

    monthly_table = create_monthly_table(
        principal,
        applied_rate,
        start_date,
        end_date
    )


if not monthly_table.empty:

    total_monthly_interest = monthly_table[
        "Tiền lãi"
    ].sum()

else:

    total_monthly_interest = 0


# =========================================================
# TỔNG NHẬN
# =========================================================

if interest_method == "Nhận lãi hàng tháng":

    total_received = (
        principal
        + total_monthly_interest
    )

    displayed_interest = total_monthly_interest

else:

    total_received = (
        principal
        + interest
    )

    displayed_interest = interest


# =========================================================
# MAIN HERO
# =========================================================

st.markdown("""
<div class="hero-box">

    <div class="hero-title">
        🏦 SMARTSAVE 360
    </div>

    <div class="hero-subtitle">
        Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm
    </div>

    <div class="hero-line">
        🔴 Rút trước hạn → áp dụng lãi suất không kỳ hạn
    </div>

    <div class="hero-line">
        🟢 Đến hạn → nhận lãi hoặc tái tục
    </div>

    <div class="hero-line">
        📅 Cơ sở tính lãi: 365 ngày/năm
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Tổng quan",
    "💰 Tính tiền gửi",
    "📋 Dòng tiền",
    "📈 So sánh thông minh"
])


# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.markdown("## 📊 Tổng quan")

    if not st.session_state.calculate:

        st.info(
            "💡 Hãy thiết lập thông tin ở "
            "**Bảng điều khiển** bên trái "
            "và nhấn **TÍNH TOÁN NGAY**."
        )


    # -----------------------------------------------------
    # METRIC
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    💰 TIỀN GỐC
                </div>

                <div class="metric-value">
                    {format_money(principal)}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    📈 TIỀN LÃI
                </div>

                <div class="metric-value">
                    {format_money(displayed_interest)}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    💎 TỔNG NHẬN
                </div>

                <div class="metric-value">
                    {format_money(total_received)}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    📅 SỐ NGÀY
                </div>

                <div class="metric-value">
                    {actual_days} ngày
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("")


    # -----------------------------------------------------
    # TRẠNG THÁI
    # -----------------------------------------------------

    if early_withdrawal:

        st.error(
            f"🔴 Rút trước hạn — "
            f"lãi suất áp dụng "
            f"{non_term_rate:.2f}%/năm."
        )

    elif term_months == 0:

        st.info(
            f"🔵 Không kỳ hạn — "
            f"lãi suất áp dụng "
            f"{non_term_rate:.2f}%/năm."
        )

    else:

        st.success(
            f"🟢 Đúng hạn — "
            f"lãi suất áp dụng "
            f"{fixed_rate:.2f}%/năm."
        )


    # -----------------------------------------------------
    # 2 CARD
    # -----------------------------------------------------

    left, right = st.columns(2)


    with left:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    🏦 Thông tin khoản gửi
                </div>

                <p>
                    <b>Số tiền:</b>
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
                    <b>Ngày rút:</b>
                    {end_date.strftime("%d/%m/%Y")}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with right:

        st.markdown(
            f"""
            <div class="result-card">

                <div class="card-title">
                    💵 Kết quả tài chính
                </div>

                <p>
                    <b>Lãi suất áp dụng:</b>
                    {applied_rate:.2f}%/năm
                </p>

                <p>
                    <b>Tiền lãi:</b>
                    {format_money(displayed_interest)}
                </p>

                <p>
                    <b>Tổng tiền nhận:</b>
                    {format_money(total_received)}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.markdown("## 💰 Chi tiết khoản tiền gửi")


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">📌 Thông tin khoản tiền gửi</div>',
            unsafe_allow_html=True
        )

        st.write(
            f"**Số tiền gửi:** "
            f"{format_money(principal)}"
        )

        st.write(
            f"**Kỳ hạn:** {term_name}"
        )

        st.write(
            f"**Lãi suất niêm yết:** "
            f"{fixed_rate:.2f}%/năm"
        )

        st.write(
            f"**Lãi suất áp dụng:** "
            f"{applied_rate:.2f}%/năm"
        )

        st.write(
            f"**Ngày gửi:** "
            f"{start_date.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**Ngày đáo hạn:** "
            f"{maturity_date.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**Ngày rút:** "
            f"{end_date.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**Số ngày thực tế:** "
            f"{actual_days} ngày"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            '<div class="result-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">💰 Kết quả tính toán</div>',
            unsafe_allow_html=True
        )

        st.write(
            f"**Tiền gốc:** "
            f"{format_money(principal)}"
        )

        st.write(
            f"**Tiền lãi:** "
            f"{format_money(displayed_interest)}"
        )

        st.write(
            f"**Tổng tiền nhận:** "
            f"{format_money(total_received)}"
        )

        profit_rate = 0

        if principal > 0:

            profit_rate = (
                displayed_interest
                / principal
                * 100
            )

        st.write(
            f"**Tỷ suất sinh lời:** "
            f"{profit_rate:.2f}%"
        )

        st.write(
            f"**Trạng thái:** {status}"
        )

        st.write(
            f"**Tái tục:** "
            f"{'Có 🔄' if auto_rollover else 'Không'}"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # CÔNG THỨC
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("### 📐 Công thức tính lãi")

    st.latex(
        r"""
        Tiền\ lãi =
        Tiền\ gốc
        \times
        \frac{Lãi\ suất}{100}
        \times
        \frac{Số\ ngày}{365}
        """
    )

    st.info(
        f"{format_money(principal)} × "
        f"{applied_rate:.2f}% × "
        f"{actual_days}/365 = "
        f"**{format_money(interest)}**"
    )


    # -----------------------------------------------------
    # LÃI HÀNG THÁNG
    # -----------------------------------------------------

    if not monthly_table.empty:

        st.markdown("---")

        st.markdown(
            "### 📅 Lịch nhận lãi hàng tháng"
        )

        table_show = monthly_table.copy()

        table_show["Từ ngày"] = (
            table_show["Từ ngày"]
            .dt.strftime("%d/%m/%Y")
        )

        table_show["Đến ngày"] = (
            table_show["Đến ngày"]
            .dt.strftime("%d/%m/%Y")
        )

        table_show["Tiền lãi"] = (
            table_show["Tiền lãi"]
            .apply(format_money)
        )

        st.dataframe(
            table_show,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# TAB 3
# =========================================================

with tab3:

    st.markdown("## 📋 Dòng tiền khoản gửi")


    cashflows = []


    cashflows.append({
        "Thời điểm": "Ngày gửi",
        "Ngày": start_date.strftime("%d/%m/%Y"),
        "Dòng tiền": -principal,
        "Nội dung": "Gửi tiền"
    })


    if (
        interest_method == "Nhận lãi hàng tháng"
        and not monthly_table.empty
    ):

        for _, row in monthly_table.iterrows():

            cashflows.append({

                "Thời điểm":
                    f"Tháng {int(row['Tháng'])}",

                "Ngày":
                    row["Đến ngày"].strftime(
                        "%d/%m/%Y"
                    ),

                "Dòng tiền":
                    row["Tiền lãi"],

                "Nội dung":
                    "Nhận lãi hàng tháng"

            })


        cashflows.append({

            "Thời điểm": "Ngày rút",

            "Ngày":
                end_date.strftime("%d/%m/%Y"),

            "Dòng tiền": principal,

            "Nội dung":
                "Nhận lại tiền gốc"

        })


    else:

        cashflows.append({

            "Thời điểm": "Ngày rút",

            "Ngày":
                end_date.strftime("%d/%m/%Y"),

            "Dòng tiền":
                total_received,

            "Nội dung":
                "Nhận gốc + lãi"

        })


    cashflow_df = pd.DataFrame(
        cashflows
    )


    cashflow_show = cashflow_df.copy()

    cashflow_show["Dòng tiền"] = (
        cashflow_show["Dòng tiền"]
        .apply(format_money)
    )


    st.dataframe(
        cashflow_show,
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        "### 📊 Biểu đồ dòng tiền"
    )


    chart_data = cashflow_df[
        ["Thời điểm", "Dòng tiền"]
    ].copy()


    chart_data = chart_data.set_index(
        "Thời điểm"
    )


    st.bar_chart(
        chart_data
    )


# =========================================================
# TAB 4
# =========================================================

with tab4:

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

        finish = add_months(
            start_date,
            months
        )

        days = (
            finish - start_date
        ).days

        interest_value = calculate_interest(
            principal,
            fixed_rate,
            days
        )

        comparison_rows.append({

            "Kỳ hạn": name,

            "Số ngày": days,

            "Lãi suất":
                fixed_rate,

            "Tiền lãi":
                interest_value,

            "Tổng nhận":
                principal + interest_value

        })


    comparison_df = pd.DataFrame(
        comparison_rows
    )


    show_comparison = comparison_df.copy()


    show_comparison["Lãi suất"] = (
        show_comparison["Lãi suất"]
        .map(lambda x: f"{x:.2f}%")
    )


    show_comparison["Tiền lãi"] = (
        show_comparison["Tiền lãi"]
        .apply(format_money)
    )


    show_comparison["Tổng nhận"] = (
        show_comparison["Tổng nhận"]
        .apply(format_money)
    )


    st.dataframe(
        show_comparison,
        use_container_width=True,
        hide_index=True
    )


    best_index = comparison_df[
        "Tiền lãi"
    ].idxmax()


    best = comparison_df.loc[
        best_index
    ]


    st.success(
        f"🏆 Với số tiền "
        f"{format_money(principal)}, "
        f"kỳ hạn **{best['Kỳ hạn']}** "
        f"cho tiền lãi cao nhất là "
        f"**{format_money(best['Tiền lãi'])}**."
    )


    st.markdown(
        "### 📊 Tiền lãi theo kỳ hạn"
    )


    chart = comparison_df[
        ["Kỳ hạn", "Tiền lãi"]
    ].set_index(
        "Kỳ hạn"
    )


    st.bar_chart(
        chart
    )


# =========================================================
# KIẾN THỨC NGHIỆP VỤ
# =========================================================

st.markdown("---")


with st.expander(
    "📚 KIẾN THỨC NGHIỆP VỤ TIỀN GỬI"
):

    st.markdown(
        """
        **1. Tiền gửi có kỳ hạn**

        Khách hàng gửi tiền trong một khoảng thời gian
        xác định và được hưởng lãi suất tương ứng
        với kỳ hạn.

        **2. Rút trước hạn**

        Khi khách hàng rút tiền trước ngày đáo hạn,
        khoản tiền được mô phỏng theo lãi suất
        không kỳ hạn.

        **3. Nhận lãi hàng tháng**

        Tiền lãi được tính theo số ngày thực tế
        của từng khoảng thời gian.

        **4. Nhận lãi cuối kỳ**

        Khách hàng nhận tiền gốc và tiền lãi
        khi kết thúc khoản tiền gửi.

        **5. Nhận lãi trước**

        Tiền lãi được tính trước dựa trên
        số tiền gửi, lãi suất và thời gian gửi.

        **6. Tái tục**

        Khi đến ngày đáo hạn, khách hàng có thể
        tiếp tục gửi khoản tiền sang kỳ hạn mới.

        **7. Cơ sở tính lãi**

        Mô hình sử dụng cơ sở
        **365 ngày/năm**.
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "🏦 SmartSave 360 | "
    "Hệ thống mô phỏng nghiệp vụ tiền gửi tiết kiệm | "
    "Phục vụ mục đích học tập"
)
