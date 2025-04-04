import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image

interpreter = tflite.Interpreter(
    model_path="mobilenet_v1_1.0_224_quant.tflite",
    experimental_delegates=[
        tflite.load_delegate("libedgetpu.so.1")
    ]
)
interpreter.allocate_tensors()

print("? Successfully ran known-good model.")
