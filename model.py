import os
from simplet5 import SimpleT5

current_dir = os.path.dirname(os.path.abspath(__file__))
model_folder_path = os.path.join(current_dir, "simpleT5_model")

if not os.path.exists(model_folder_path):
    print("Model Not Found!!")
    exit()

# Instantiation
model = SimpleT5()

try:
    model.from_pretrained("t5", "t5-base")
except Exception as e:
    print("Error loading pretrained model:", e)
    exit()

# Loading the model
try:
    model.load_model("t5", model_folder_path, use_gpu=False)
except Exception as e:
    print("Error loading fine-tuned model:", e)
    exit()


async def summarizer(text):
    try:
        print("model",text)
        prediction = model.predict(text)
        return prediction
    except Exception as e:
        print("Error during prediction:", e)
        return None