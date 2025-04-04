import tflite_runtime.interpreter as tflite

try:
    delegate = tflite.load_delegate('/usr/lib/aarch64-linux-gnu/libedgetpu.so.1')
    print("Edge TPU is found!")
except Exception as e:
    print("Failed to load Edge TPU delegate:")
    print(e)

