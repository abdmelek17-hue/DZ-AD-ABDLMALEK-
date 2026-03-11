import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="DZ-Ad Pro", layout="centered")

# جلب المفتاح من الإعدادات السرية لـ Streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    st.title("🚀 DZ-Ad Pro - ذكاء اصطناعي لإعلاناتك")
    st.write("صمم إعلانك الاحترافي بالدارجة الجزائرية في ثوانٍ!")

    email = st.text_input("أدخل بريدك الإلكتروني:")
    
    if email:
        uploaded_file = st.file_uploader("ارفع صورة المنتج", type=["jpg", "png", "jpeg"])
        details = st.text_area("تفاصيل إضافية (السعر، المكان...):")
        
        if st.button("توليد الإعلان ✨"):
            with st.spinner("جاري التحليل..."):
                prompt = f"اكتب إعلانين بالدارجة الجزائرية لمنتج. الأول رسمي والثاني جذاب لفيسبوك. الإضافات: {details}"
                if uploaded_file:
                    img = Image.open(uploaded_file)
                    response = model.generate_content([prompt, img])
                else:
                    response = model.generate_content(prompt)
                st.success("تم التوليد بنجاح!")
                st.write(response.text)
else:
    st.error("⚠️ خطأ: لم يتم العثور على مفتاح API. يرجى إضافته في Secrets باسم GEMINI_API_KEY")

# لوحة تحكم بسيطة
with st.expander("🔐 الإدارة"):
    admin_pass = st.text_input("كلمة سر المدير:", type="password")
    if admin_pass == "ENS_2026":
        st.write("مرحباً أيها المدير، يمكنك هنا متابعة إحصائيات التطبيق.")
