# Krishimitra-AI-Helper-for-Farmers
 Project Report: Krishimitra – AI Helper for Farmers 
 Dataset link https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

## Project Title
Krishimitra: AI-Based Plant Disease Detection System

## Objective
The objective of this project is to support farmers in early identification of plant diseases through images. By leveraging artificial intelligence (AI), specifically computer vision and deep learning, Krishimitra helps diagnose plant diseases and suggests simple, actionable remedies—ultimately aiming to improve crop yield and reduce loss.

## Problem Statement
Farmers often face difficulties in identifying plant diseases early, leading to reduced crop yield and increased use of harmful pesticides. There is a need for a simple, accessible AI-based tool that helps them detect crop diseases early using images taken with smartphones.

## Proposed Solution
Krishimitra is a simple AI-based web application where farmers can:
•	Upload a picture of the affected plant.
•	The app predicts the disease using a trained deep learning model.
•	It also suggests basic treatment or actions for the diagnosed condition.

## Technologies Used
•  Frontend: Streamlit (Python Web UI)
•  Backend: TensorFlow/Keras, NumPy, OpenCV, PIL
•  Model: Pre-trained CNN model saved as plant_disease_model.h5
•  Programming Language: Python
•  Image Processing: OpenCV, PIL
•  Deployment: Localhost / Streamlit Cloud (optional)

## System Architecture

+-----------------+        +----------------+        +-----------------+
| User Uploads    |  -->   | Image Preprocess|  -->   | Model Predicts  |
| Crop Image      |        | (Resize, Normalize)      | Disease Class   |
+-----------------+        +----------------+        +-----------------+
                                                          |
                                                          v
                                                +----------------------+
                                                | Show Confidence +    |
                                                | Suggested Solution    |
                                                +----------------------+


## Model Details
•  Model Type: CNN (Convolutional Neural Network)
•  Input Size: 128 x 128 pixels
•  Output Classes: 16 Plant Disease categories (including healthy)
•  Training Data: Based on the PlantVillage dataset

Classes Predicted:
Pepper__bell___Bacterial_spot
Pepper__bell___healthy
PlantVillage
Potato___Early_blight
Potato___Late_blight
Potato___healthy
Tomato_Bacterial_spot
Tomato_Early_blight
Tomato_Late_blight
Tomato_Leaf_Mold
Tomato_Septoria_leaf_spot
Tomato_Spider_mites_Two_spotted_spider_mite
Tomato__Target_Spot
Tomato__Tomato_YellowLeaf__Curl_Virus
Tomato__Tomato_mosaic_virus
Tomato_healthy

## Key Features
•	Image Upload: Farmer uploads an image via drag and drop or file picker.
•	Real-Time Prediction: Model predicts disease with confidence score.
•	Suggested Action: Displays basic treatment or management suggestion.
•	Simple UI: Built with Streamlit for accessibility and ease of use.



## Sample Output   


Input Image	Predicted Disease	Confidence	Suggested Action
![Tomato_leaf.jpg]	Tomato_Late_blight	92.34%	Apply fungicides promptly; ensure good field drainage.

## Conclusion
This AI-powered application empowers farmers by helping them identify plant diseases quickly and get immediate recommendations, potentially saving crop yield and reducing chemical misuse. It represents an accessible step toward smart agriculture.










