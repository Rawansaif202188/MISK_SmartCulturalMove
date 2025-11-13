import streamlit as st

# ==============================
# إعداد واجهة التطبيق
# ==============================
st.set_page_config(page_title="MISK Smart Cultural Move", layout="wide")

st.title("🚗 MISK Smart Cultural Move")
st.subheader("تجربة تنقل ذكية وثقافية داخل مدينة مسك 🇸🇦")
st.markdown("""
مرحباً بك في مشروع **MISK Smart Cultural Move**.  
التطبيق يساعدك على التنقل بسهولة داخل مدينة مسك واكتشاف المعالم الثقافية.
""")

# ==============================
# إدخال نقاط البداية والوجهة
# ==============================
col1, col2 = st.columns(2)
start = col1.text_input("📍 نقطة البداية (Latitude,Longitude)", "26.3043,50.1393")
end = col2.text_input("🏁 الوجهة (Latitude,Longitude)", "26.3059,50.1432")

# ==============================
# زر عرض المسار على Google Maps
# ==============================
if st.button("🔍 عرض المسار على Google Maps"):
    try:
        # تحويل النصوص إلى أرقام
        start_coords = start.replace(" ", "")
        end_coords = end.replace(" ", "")

        # إنشاء رابط Google Maps Directions
        maps_url = f"https://www.google.com/maps/dir/{start_coords}/{end_coords}/"

        # عرض الخريطة في iframe داخل التطبيق
        st.markdown(f'<iframe src="{maps_url}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

        st.success("✅ تم عرض المسار على Google Maps!")
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
