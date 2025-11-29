import os
from pathlib import Path
import numpy as np
import librosa
import soundfile as sf
from moviepy.editor import AudioFileClip


# =============== EDIT THESE ===============
INPUT_DIR = "data/rawAudio"
OUTPUT_DIR = "data/cleanMP4"
TARGET_SR = 16000
TARGET_DURATION = 4.0  # seconds
# ==========================================


def standardize_audio_to_mp4(in_path, out_path,
                             sr=TARGET_SR,
                             duration=TARGET_DURATION):
    print(f"Processing: {in_path}")

    # -------- Load audio at fixed SR --------
    y, _ = librosa.load(in_path, sr=sr, mono=True)

    # -------- Trim or pad to EXACT duration --------
    target_len = int(sr * duration)

    if len(y) > target_len:
        # Trim to first 4 seconds
        y = y[:target_len]
    else:
        # Center pad
        pad_total = target_len - len(y)
        pad_left = pad_total // 2
        pad_right = pad_total - pad_left
        y = np.pad(y, (pad_left, pad_right))

    # -------- Save temporary WAV --------
    tmp_wav = out_path.replace(".mp4", "_tmp.wav")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    sf.write(tmp_wav, y, sr)

    # -------- Convert WAV → MP4 (AAC) --------
    audio_clip = AudioFileClip(tmp_wav)
    audio_clip.write_audiofile(
        out_path,
        fps=sr,
        codec="aac",       # MP4 audio codec
        ffmpeg_params=["-ac", "1"]  # force mono
    )
    audio_clip.close()

    # Remove temp WAV
    os.remove(tmp_wav)

    print(f"Saved MP4: {out_path}")


def main():
    input_dir = Path(INPUT_DIR)
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_files = []
    for ext in ("*.mp4", "*.wav", "*.m4a", "*.mp3"):
        audio_files.extend(input_dir.glob(ext))

    if not audio_files:
        print("No audio found in input directory.")
        return

    for file in audio_files:
        out_name = file.stem + "_std.mp4"
        out_path = str(output_dir / out_name)
        standardize_audio_to_mp4(str(file), out_path)


if __name__ == "__main__":
    main()