import cv2
import numpy as np
import requests

# Load image from a URL
def load_image_from_url(url):
    try:
        print(f"Attempting to download image from: {url}")
        headers = {
            "User-Agent": "Mozilla/5.0"  # Some sites block requests without this
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        print(f"Successfully downloaded image from: {url}")
        image_array = np.frombuffer(response.content, np.uint8)
        print(f"Downloaded image content size: {len(image_array)} bytes")
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        if image is None:
            print("Error: Image could not be decoded by cv2.")
            return None
        print("Image decoded successfully.")
        return image
    except requests.exceptions.Timeout:
        print(f"Error: Request to {url} timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Image download error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Analyze image
def analyze_crop_image_from_url(image_url):
    image = load_image_from_url(image_url)
    if image is None:
        print("Error: Image not found or invalid.")
        return "unknown"

    try:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        avg_color = np.mean(hsv[:, :, 0])  # average hue

        if avg_color < 30:
            return "yellowing"
        elif avg_color > 90:
            return "overwatered"
        else:
            return "healthy"
    except Exception as e:
        print(f"Error during image analysis: {e}")
        return "unknown"

# Simulate voice input (simple NLP)
def process_voice_input(transcribed_text):
    text = transcribed_text.lower()
    if "yellow" in text or "dry" in text:
        return "yellowing"
    elif "brown spot" in text or "fungus" in text:
        return "fungal infection"
    elif "too wet" in text or "water" in text:
        return "overwatered"
    else:
        return "unknown"

# Basic solution logic
def get_solution(detected_issue):
    solutions = {
        "yellowing": "Apply nitrogen-rich fertilizer and ensure proper watering.",
        "overwatered": "Reduce watering frequency and improve soil drainage.",
        "fungal infection": "Use appropriate fungicide and remove infected leaves.",
        "healthy": "No issue detected. Keep monitoring regularly.",
        "unknown": "Could not determine the issue. Please consult an expert."
    }
    return solutions.get(detected_issue, solutions["unknown"])

# Main function
def ai_helper_main_web(image_url, voice_text):
    print("Analyzing crop image from web...")
    image_issue = analyze_crop_image_from_url(image_url)
    print(f"Image analysis suggests: {image_issue}")

    print("Processing voice input...")
    voice_issue = process_voice_input(voice_text)
    print(f"Voice input suggests: {voice_issue}")

    final_issue = voice_issue if voice_issue != "unknown" else image_issue
    solution = get_solution(final_issue)

    print(f"\nDetected Issue: {final_issue}")
    print(f"Suggested Solution: {solution}")

# === Example Usage ===
if __name__ == "__main__":
    # ✅ Use a working image URL from Wikimedia
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"  # Updated to a valid image URL
    voice_input = "The leaves are turning yellow and dry"

    ai_helper_main_web(image_url, voice_input)