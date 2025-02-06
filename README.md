# 🍽️ Cooking Ingredient Detection & Recipe Finder

This is a **Django-based web application** that allows users to upload images of ingredients. The application uses a **fine-tuned YOLOv8 model** to detect ingredients from the uploaded image and then queries a **PostgreSQL database** to find matching recipes containing those ingredients. The results are displayed dynamically in expandable boxes.

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
