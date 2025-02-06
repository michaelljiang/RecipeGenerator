from django.shortcuts import render
from django.core.files.storage import default_storage
from .models import Recipe, Ingredient
from PIL import Image
import onnxruntime as ort
import numpy as np

def land(request):
    return render(request, 'detection/landing.html')

def upload(request):
    if request.method == 'POST' and request.FILES.get('image'):

        image = request.FILES['image']
        image_path = default_storage.save('uploads/' + image.name, image)
        image = Image.open('media/' + image_path)

        ort_session = ort.InferenceSession('detection/best.onnx')

        # Image preprocessing for inference
        input_image = np.asarray(image.resize((640,640))).transpose(2, 0, 1)
        input_image = np.expand_dims(input_image, axis = 0).astype(np.float32)

        outputs = ort_session.run(None, {ort_session.get_inputs()[0].name: input_image})

        labels = post_process(outputs)

        ingredient_labels = Ingredient.objects.filter(name__in=labels)
        recipes = Recipe.objects.filter(ingredients__in=ingredient_labels)

        return render(request, 'detection/landing.html', {
            'recipes': recipes,
            'labels': labels,
        })
    return render(request, 'detection/landing.html', {
            'recipes': None,
            'labels': None,
    })

model_labels=['apple', 'background', 'beef', 'cabbage', 'carrot', 'chicken', 'chicken_broth', 'chili', 'cilantro', 'coriander',
        'cucumber', 'egg', 'fish', 'garlic', 'ginger', 'honey', 'lemon', 'lime', 'milk', 'mushroom','noodle', 'olive', 
        'onion', 'orange', 'parsley', 'peanut', 'pork', 'potato', 'rice', 'salmon', 'scallion', 'shrimp', 'stock', 'tomato', 'yoghurt']

def post_process(outputs):
    """
        Post processing on Yolov8's output to extract labels

        Args: 
            outputs: The output of Yolov8 onnxruntime.InferenceSession
        Returns:
            list: The detected labels
    """
    # Lists to store detected labels
    labels = []

    #Transpose and squeeze inference output in order extract labels
    outputs = np.transpose(np.squeeze(outputs[0]))

    # Number of rows (# of possible labels)
    rows = outputs.shape[0]

    # Iterate over each row of output
    for i in range(rows):

        # Extract the confidence of each label
        label_confidences = outputs[i][4:]

        # Find the label with greatest confidence
        max_confidence = np.amax(label_confidences)

        # If max confidence is above confidence threshold ( 0.5 )
        if max_confidence >= 0.5:

            # Get index of max confidence
            label_index = np.argmax(label_confidences)

            # Index into model_labels to find label and append into list
            labels.append(model_labels[label_index])

    # return list of labels
    return labels



        

