import streamlit as st
from deepface import DeepFace
from PIL import Image
import tempfile

songs_by_mood = {
    "happy": [
        ("Happy – Pharrell Williams", "https://www.youtube.com/watch?v=y6Sxv-sUYtM"),
        ("Uptown Funk – Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
        ("Can't Stop The Feeling – Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Best Day Of My Life – American Authors", "https://www.youtube.com/watch?v=Y66j_BUCBMY"),
        ("Gone, Gone, Gone – Phillip Phillips", "https://www.youtube.com/watch?v=F7Zs3j1I6a4"),
        ("Hymn for the Weekend – Coldplay", "https://www.youtube.com/watch?v=YykjpeuMNEk"),
        ("What Makes You Beautiful – One Direction", "https://www.youtube.com/watch?v=QJO3ROT-A4E")
    ],
    "sad": [
        ("Someone Like You – Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Fix You – Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("Let Her Go – Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("When I Was Your Man – Bruno Mars", "https://www.youtube.com/watch?v=ekzHIouo8Q4"),
        ("Somebody That I Used To Know – Gotye", "https://www.youtube.com/watch?v=8UVNT4wvIGY"),
        ("Story of My Life – One Direction", "https://www.youtube.com/watch?v=W-TE_Ys4iwM")
    ],
    "angry": [
        ("Lose Yourself – Eminem", "https://www.youtube.com/watch?v=_Yhyp-_hX2s"),
        ("Break Stuff – Limp Bizkit", "https://www.youtube.com/watch?v=ZpUYjpKg9KY"),
        ("Numb – Linkin Park", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
        ("Killing In The Name – Rage Against The Machine", "https://www.youtube.com/watch?v=bWXazVhlyxQ"),
        ("Drag Me Down – One Direction", "https://www.youtube.com/watch?v=zrKzPO0vFO0")
    ],
    "surprise": [
        ("Wake Me Up – Avicii", "https://www.youtube.com/watch?v=IcrbM1l_BoI"),
        ("Feel Good Inc – Gorillaz", "https://www.youtube.com/watch?v=HyHNuVaZJ-k"),
        ("Titanium – David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg"),
        ("Believer – Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc")
    ],
    "fear": [
        ("Everybody Hurts – R.E.M.", "https://www.youtube.com/watch?v=ijZRCIrTgQc"),
        ("Creep – Radiohead", "https://www.youtube.com/watch?v=XFkzRNyygfk"),
        ("Mad World – Tears For Fears", "https://www.youtube.com/watch?v=4N3N1MlvVc4"),
        ("The Sound Of Silence – Disturbed", "https://www.youtube.com/watch?v=u9Dg-g7t2l4")
    ],
    "neutral": [
        ("Shape Of You – Ed Sheeran", "https://www.youtube.com/watch?v=JGwWNGJdvx8"),
        ("Counting Stars – OneRepublic", "https://www.youtube.com/watch?v=hT_nvWreIhg"),
        ("Viva La Vida – Coldplay", "https://www.youtube.com/watch?v=dvgZkm1xWPE"),
        ("Closer – The Chainsmokers", "https://www.youtube.com/watch?v=PT2_F-1esPk")
    ],
    "disgust": [
        ("Boulevard Of Broken Dreams – Green Day", "https://www.youtube.com/watch?v=Soa3gO7tL-c"),
        ("Smells Like Teen Spirit – Nirvana", "https://www.youtube.com/watch?v=hTWKbfoikeg"),
        ("In The End – Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4"),
        ("Bring Me To Life – Evanescence", "https://www.youtube.com/watch?v=3YxaaGgTQYM")
    ]
}

st.title("Moodify - Mood-Based Song Recommender")
st.write("Upload a photo of yourself and let AI guess your mood!")

uploaded_file = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img = img.convert("RGB")
    img = img.resize((400, 400))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        img.save(temp_file.name)
        image_path = temp_file.name

    st.image(img, caption="Uploaded Image", use_column_width=True)

    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend='opencv'
        )
        mood = result[0]['dominant_emotion']

        mood_colors = {
            "happy": "#FFC107",
            "sad": "#1976D2",
            "angry": "#D32F2F",
            "surprise": "#F57C00",
            "fear": "#7B1FA2",
            "neutral": "#757575",
            "disgust": "#388E3C"
        }

        color = mood_colors.get(mood.lower(), "#000000")
        st.markdown(
            f"<div style='padding:10px; background-color:{color}; border-radius:5px;'><h3 style='color:white;'>Detected mood: {mood}</h3></div>",
            unsafe_allow_html=True
        )

    except Exception:
        mood = "unknown"
        st.error("Error analyzing the image. Try another photo!")

    if mood.lower() in songs_by_mood:
        st.write("Here are some songs for you based on your mood:")
        for song_name, youtube_url in songs_by_mood[mood.lower()]:
            st.markdown(f"- [{song_name}]({youtube_url})")
    elif mood == "unknown":
        st.write("Sorry, we couldn't detect your mood. Try another photo!")
    else:
        st.write("Sorry, no recommendations for this mood yet.")
