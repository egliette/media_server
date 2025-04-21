# 🎥 Stream Quality: Factors, Metrics, and Comparison

---

## 📌 What Impacts Stream Quality?

Several factors influence the visual and playback quality of a video stream:

| Factor                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **Bitrate**               | Higher bitrate improves quality but needs more bandwidth                   |
| **Resolution**            | Defines the video detail (e.g., 480p vs 1080p)                              |
| **Frame rate**            | Higher frame rates (e.g., 60fps) result in smoother motion                  |
| **Compression/Codec**     | Lossy codecs (e.g., H.264) reduce file size but may lower quality           |
| **Network conditions**    | Packet loss, jitter, and latency can cause stuttering or buffering          |
| **Latency**               | Affects real-time applications like video conferencing                      |
| **Device capabilities**   | Some devices may downscale or drop frames for performance                   |

---

## 🧪 Metrics to Measure Stream Quality

| Metric | Description | Ideal Range | Notes |
|--------|-------------|-------------|-------|
| **PSNR (Peak Signal-to-Noise Ratio)** | Measures signal degradation (higher is better) | 35 dB+ (Excellent), 30–35 dB (Good), 25–30 dB (Fair), <25 dB (Poor) | Sensitive to noise and compression artifacts |
| **SSIM (Structural Similarity Index)** | Compares structural similarity (closer to 1 is better) | 0.95 – 1.00 (Excellent), 0.90 – 0.95 (Good), 0.85 – 0.90 (Fair), <0.85 (Poor) | Perceptually more accurate than PSNR |

---

## 🔍 Compare Two Videos Using FFmpeg

You can compare two videos (e.g., original vs. compressed/streamed output) using **PSNR** and **SSIM**:

### 🧾 Command

```bash
ffmpeg -i <original_video> -i <processed_video> -lavfi "[0:v][1:v]psnr;[0:v][1:v]ssim" -f null -
```

This command:

- Loads two video files for comparison.
- Uses FFmpeg's `lavfi` (libavfilter) to apply:
  - `psnr`: calculates Peak Signal-to-Noise Ratio
  - `ssim`: calculates Structural Similarity Index
- Outputs the results (no actual file is generated, hence `-f null -`)

---

## 📊 Example Output

```txt
[Parsed_psnr_0 @ ...] PSNR y:38.12 u:42.33 v:43.02 average:39.45 min:32.10 max:45.90
[Parsed_ssim_1 @ ...] SSIM Y:0.987419 U:0.993862 V:0.994311 All:0.989371 (12.350629)
```

### 🎯 How to Interpret

- **PSNR average: 39.45** → Excellent quality (very little distortion)
- **SSIM All: 0.989371** → Excellent structural similarity

---

> ✅ **Tip:** Always ensure both videos have the same resolution, frame rate, and duration for accurate comparisons.
