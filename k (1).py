import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# === Load your trained model ===
model = load_model("plant_disease_model.h5")

# === Automatically detect model input image size ===
input_shape = model.input_shape  # (None, height, width, channels)
img_height, img_width = input_shape[1], input_shape[2]

# === Class index mapping ===
class_labels = {
    0: 'Pepper__bell___Bacterial_spot',
    1: 'Pepper__bell___healthy',
    2: 'Potato___Early_blight',
    3: 'Potato___Late_blight',
    4: 'Potato___healthy',
    5: 'Tomato_Bacterial_spot',
    6: 'Tomato_Early_blight',
    7: 'Tomato_Late_blight',
    8: 'Tomato_Leaf_Mold',
    9: 'Tomato_Septoria_leaf_spot',
    10: 'Tomato_Spider_mites_Two_spotted_spider_mite',
    11: 'Tomato__Target_Spot',
    12: 'Tomato__Tomato_YellowLeaf__Curl_Virus',
    13: 'Tomato__Tomato_mosaic_virus',
    14: 'Tomato_healthy'
}

# === Suggested actions ===
suggested_actions = {
    'Pepper__bell___Bacterial_spot': "Use copper-based bactericides; avoid overhead irrigation; remove infected leaves.",
    'Pepper__bell___healthy': "Plant looks healthy! Maintain good watering and nutrient practices.",
    'Potato___Early_blight': "Apply fungicides containing chlorothalonil; remove infected foliage.",
    'Potato___Late_blight': "Use fungicides such as chlorothalonil or mancozeb; remove infected plants promptly.",
    'Potato___healthy': "Plant is healthy; continue regular care.",
    'Tomato_Bacterial_spot': "Apply copper-based bactericides; remove infected leaves; avoid overhead watering.",
    'Tomato_Early_blight': "Use fungicides containing chlorothalonil; prune affected leaves.",
    'Tomato_Late_blight': "Apply fungicides promptly; ensure good field drainage.",
    'Tomato_Leaf_Mold': "Use fungicides; improve air circulation around plants.",
    'Tomato_Septoria_leaf_spot': "Apply fungicides like chlorothalonil; practice crop rotation.",
    'Tomato_Spider_mites_Two_spotted_spider_mite': "Use miticides; introduce predatory mites; maintain humidity.",
    'Tomato__Target_Spot': "Apply appropriate fungicides; remove infected leaves.",
    'Tomato__Tomato_YellowLeaf__Curl_Virus': "Remove infected plants; control whitefly vectors.",
    'Tomato__Tomato_mosaic_virus': "Remove infected plants; sanitize tools and hands regularly.",
    'Tomato_healthy': "Plant is healthy; continue regular care and monitoring."
}

# === Prediction function ===
def predict_and_suggest_action_from_upload(uploaded_file, model, class_labels, suggested_actions, threshold=0.5):
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((img_width, img_height))
    img_array = image.img_to_array(img)
    # img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)[0]
    top_indices = preds.argsort()[-3:][::-1]

    top3 = [(class_labels[i], preds[i] * 100) for i in top_indices]
    best_idx = top_indices[0]
    predicted_class = class_labels[best_idx]
    confidence = preds[best_idx]
    action = suggested_actions.get(predicted_class, "No suggestion available.")

    return top3, predicted_class, confidence, action

# === Streamlit UI ===
st.set_page_config(page_title="KRISHIMITRA : Plant Disease Detector", layout="centered")
st.title("🌿 KRISHIMITRA : Plant Disease Detection")
st.markdown("Upload a leaf image from your device:")

uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Predict Disease"):
        top3, pred_class, confidence, action = predict_and_suggest_action_from_upload(
            uploaded_file, model, class_labels, suggested_actions, threshold=0.5
        )

        st.subheader("🔝 Top 3 Predictions:")
        for label, conf in top3:
            st.write(f"- {label}: **{conf:.2f}%**")

        st.markdown("---")
        if confidence >= 0.5:
            st.success(f"✅ **Predicted Class:** {pred_class} ({confidence*100:.2f}%)")
        else:
            st.error(f"⚠️ Low confidence: {pred_class} ({confidence*100:.2f}%) - verify manually.")

        st.warning(f"🧑‍🌾 Suggested Action: {action}")
