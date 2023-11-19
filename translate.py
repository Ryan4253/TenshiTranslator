import tkinter as tk
from tkinter import filedialog
import requests
import json
import time
import os

# Constants
BATCH_SIZE = 64
SUGOI_URL = '127.0.0.1:14366'
OUTPUT_FILE = 'output.txt'

# Translation function
def send_batch_request(host, lines):
    data = {'message': 'translate array', 'content': lines}
    headers = {'content-type': 'application/json'}
    response = requests.post(f'http://{host}/', data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Translation request failed with status code {response.status_code}")
        return []

# Translation process
def translate_input_file():
    input_file_path = filedialog.askopenfilename(title="Select Input File")
    if not input_file_path:
        return

    output_file_path = filedialog.asksaveasfilename(title="Save Translated Output", defaultextension=".txt")
    if not output_file_path:
        return

    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                lines = []
                n = 0
                start_time = time.time()
                for line in input_file:
                    n += 1
                    lines.append(line.strip())
                    if len(lines) >= BATCH_SIZE:
                        translated_lines = send_batch_request(SUGOI_URL, lines)
                        for original, translation in zip(lines, translated_lines):
                            output_file.write(original + '\n' + translation + '\n\n')
                        lines = []
                        print(f"Translated {n} lines")

                if lines:
                    translated_lines = send_batch_request(SUGOI_URL, lines)
                    for original, translation in zip(lines, translated_lines):
                        output_file.write(original + '\n' + translation + '\n\n')

                end_time = time.time()
                elapsed_time = end_time - start_time
                sps = n / elapsed_time
                print(f"Translation completed. Translated {n} lines, sps = {sps:.3f} ")
                sps_label.config(text=f"Translation speed: {sps:.3f} sps")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Create the GUI
root = tk.Tk()
root.title("Text Translation")
root.geometry("400x250")

translate_button = tk.Button(root, text="Translate", command=translate_input_file)
translate_button.pack(pady=20)

sps_label = tk.Label(root, text="", font=("Arial", 12))
sps_label.pack()

root.mainloop()
