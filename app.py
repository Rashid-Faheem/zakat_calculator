import streamlit as st


def format_number(value):
    """Format numbers with thousand separators and remove decimal places."""
    return f"{int(value):,}"


def calculate_zakat():
    st.title("📊 Zakat Calculator | زکوٰۃ کیلکولیٹر")
    
    # Cash & Bank Balance
    st.header("💰 Cash & Bank Balance | نقدی اور بینک بیلنس")
    cash = st.number_input("📌 Cash at hand (Amount you have in cash) | نقدی (گھر میں رکھی گئی رقم)", min_value=0, format="%d")
    bank = st.number_input("🏦 Bank Balance (Money in bank accounts) | بینک میں موجود رقم", min_value=0, format="%d")
    other_cash = st.number_input("💳 Other Cash (e.g., Mobile Wallet, Digital Accounts) | دیگر نقدی (مثلاً موبائل والٹ، دیگر اکاؤنٹس)", min_value=0, format="%d")
    cash_subtotal = cash + bank + other_cash
    st.info(f"🔢 Total Cash & Bank Balance | کل نقدی {format_number(cash_subtotal)}")

    # Investments
    st.header("📈 Investments | سرمایہ کاری")
    gold = st.number_input("🏆 Gold (Value in grams) | سونا (گرام کے حساب سے مالیت)", min_value=0, format="%d")
    shares = st.number_input("📊 Shares & Stock Market Investment | شیئرز اور اسٹاک مارکیٹ انویسٹمنٹ", min_value=0, format="%d")
    property = st.number_input("🏠 Property (Only for selling purpose) | جائیداد (جو بیچنے کے لیے رکھی گئی ہو)", min_value=0, format="%d")
    investment_subtotal = gold + shares + property
    st.info(f"🔢 Total Investments | کل سرمایہ کاری {format_number(investment_subtotal)}")

    # Business Assets
    st.header("🏢 Business | کاروبار")
    inventory = st.number_input("📦 Business Inventory (Stock value) | کاروباری اسٹاک یا انوینٹری", min_value=0, format="%d")
    receivable = st.number_input("🧾 Receivable Amount (Pending payments from customers) | قابلِ وصول رقم (لوگوں سے لینی ہے)", min_value=0, format="%d")
    business_cash = st.number_input("💵 Business Cash (Money within your business) | کاروبار میں موجود نقد رقم", min_value=0, format="%d")
    business_subtotal = inventory + receivable + business_cash
    st.info(f"🔢 Total Business Assets | کل کاروباری اثاثے {format_number(business_subtotal)}")

    # Liabilities
    st.header("💳 Liabilities & Expenses | قرض اور اخراجات")
    debts = st.number_input("📉 Outstanding Loans | واجب الادا قرضے", min_value=0, format="%d")
    expenses = st.number_input("🛒 Pending Household Expenses | بقایا گھریلو اخراجات", min_value=0, format="%d")
    other_liabilities = st.number_input("📌 Other Liabilities | دیگر ذمہ داریاں", min_value=0, format="%d")
    liabilities_subtotal = debts + expenses + other_liabilities
    st.info(f"🔢 Total Liabilities | کل واجب الادا رقم {format_number(liabilities_subtotal)}")

    # Total Calculations
    total_assets = cash_subtotal + investment_subtotal + business_subtotal
    net_amount = total_assets - liabilities_subtotal

    # Zakat Calculation (2.5% of net wealth if positive)
    zakat_amount = net_amount * 0.025 if net_amount > 0 else 0
    
    if st.button("🧮 Calculate Zakat | زکوٰۃ کا حساب لگائیں"):
        st.subheader("📋 Summary | خلاصہ")
        st.write(f"💰 **Total Assets | کل اثاثے** {format_number(total_assets)}")
        st.write(f"💳 **Total Liabilities | کل قرض اور اخراجات** {format_number(liabilities_subtotal)}")
        st.write(f"🏦 **Net Amount (Assets - Liabilities) | خالص رقم (اثاثے - قرض)** {format_number(net_amount)}")
        st.success(f"📢 **Zakat Payable Amount:** {format_number(zakat_amount)} روپے")
        
        if zakat_amount > 0:
            st.info("Note: This calculator provides an estimate. Consult an Islamic scholar for specific situations.")
        else:
            st.warning("No Zakat is required as net wealth is below the Nisab.")

if __name__ == "__main__":
    calculate_zakat()
