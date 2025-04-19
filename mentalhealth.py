import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Model_Caps_2.pkl")

# Fungsi kategori skor
def get_mental_health_category(score):
    if score <= 3.0:
        return "Buruk", "Kesehatan mental berada pada kondisi yang sangat memprihatinkan dan perlu perhatian segera."
    elif score <= 5.0:
        return "Rendah", "Kondisi mental sedang tidak stabil; mungkin kamu sedang menghadapi tekanan atau kelelahan."
    elif score <= 6.0:
        return "Sedang", "Kesehatan mental cukup netral; ada keseimbangan namun juga tantangan yang perlu diwaspadai."
    elif score <= 7.0:
        return "Kurang Baik", "Kamu berada di jalur yang positif, tapi masih ada beberapa hal yang bisa ditingkatkan."
    elif score <= 8.0:
        return "Baik", "Kesehatan mentalmu berada dalam kondisi yang cukup baik dan stabil."
    else:
        return "Sangat Baik", "Kamu menunjukkan kondisi mental yang sehat, stabil, dan produktif secara keseluruhan."

# Judul aplikasi
st.title("Prediksi Skor Kesehatan Mental Mahasiswa (1 - 10)")
st.write("Isi form berikut untuk mendapatkan prediksi dan insight terkait kondisi mentalmu:")

age = st.number_input("Umur", min_value=15, max_value=60)
gender_before = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
study_hours_per_day = st.number_input("Jam Belajar per Hari", min_value=0.0, max_value=24.0)
social_media_hours = st.number_input("Jam Sosial Media per Hari", min_value=0.0, max_value=24.0)
part_time_job_before = st.selectbox("Punya Kerja Sampingan?", ["Tidak", "Ya"])
attendance_percentage	 = st.slider("Persentase Kehadiran Kuliah (%)", min_value=0, max_value=100)
sleep_hours = st.number_input("Jam Tidur per Hari", min_value=0.0, max_value=24.0)
exercise_frequency = st.slider("Frekuensi Olahraga per Minggu", min_value=0, max_value=7)
extracurricular_participation_2 = st.selectbox("Ikut UKM atau Organisasi?", ["Tidak", "Ya"])
exam_score = st.number_input("Nilai Ujian Terbaru", min_value=0.0, max_value=100.0)

# Encoding
gender = 0 if gender_before == "Perempuan" else 1
part_time_job = 1 if part_time_job_before == "Ya" else 0
extracurricular_participation= 1 if extracurricular_participation_2 == "Ya" else 0


# Prediksi
if st.button("Prediksi"):
    fitur = np.array([[age, gender, study_hours_per_day, social_media_hours, part_time_job,
                       attendance_percentage, sleep_hours, exercise_frequency, extracurricular_participation, exam_score]])
    
    prediksi = model.predict(fitur)[0]
    prediksi = round(float(prediksi), 2)

    kategori, deskripsi = get_mental_health_category(prediksi)

    st.subheader(f"Skor Kesehatan Mental: {prediksi} / 10")
    st.write(f"**Kategori:** {kategori}")
    st.info(deskripsi)

