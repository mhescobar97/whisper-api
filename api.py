from flask import Flask, request, jsonify
import subprocess
import os
import uuid

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files['audio']
    audio_id = str(uuid.uuid4())
    audio_path = f"/tmp/{audio_id}.wav"
    output_path = f"/tmp/{audio_id}.txt"

    audio.save(audio_path)

    command = [
        "./main", "-m", "models/ggml-base.bin",
        "-f", audio_path,
        "-otxt", "-of", f"/tmp/{audio_id}"
    ]

    subprocess.run(command, check=True)
    
    with open(output_path, "r") as f:
        transcription = f.read()

    # Limpieza opcional
    os.remove(audio_path)
    os.remove(output_path)

    return jsonify({"text": transcription.strip()})
