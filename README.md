# 🍽️ Cooking Ingredient Detection & Recipe Finder

This is a **Django-based web application** that allows users to upload images of ingredients. The application uses a **fine-tuned YOLOv8 model** to detect ingredients from the uploaded image and then queries a **PostgreSQL database** to find matching recipes containing those ingredients. The results are displayed dynamically in expandable boxes.

The model currently is not very accurate in detecting ingredients, for example finding many small ingredients in a big image of a singular ingredient. This is likely due to the lack of training images per label. In a future iterations, the model will be retrained with fewer labels and more images in both the training and validation sets.

---

## 📌 Features

✅ Upload an image containing cooking ingredients  
✅ Runs a **fine-tuned YOLOv8 model** for ingredient detection  
✅ Queries a **PostgreSQL database** to find matching recipes  
✅ Displays recipes in **expandable sections**  
✅ Simple and **responsive UI**  

---

## 🚀 Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **AI Model:** YOLOv8 (fine-tuned on cooking ingredient images)
- **Frontend:** HTML, CSS, JavaScript (Vanilla JS)
- **Deployment:** ONNX Runtime for model inference

---

![image](https://github.com/user-attachments/assets/d2dbb858-3320-43ed-8a3d-9840b792b526)

