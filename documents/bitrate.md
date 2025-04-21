# 📺 Bitrate vs Network Bandwidth in Video Streaming

In video streaming, **bitrate** and **network bandwidth** are key factors that directly affect video quality, buffering, and user experience.

---

## 🎚️ Bitrate

**Definition:**  
Bitrate is the amount of data encoded for video per unit of time, usually measured in **kbps (kilobits per second)** or **Mbps (megabits per second)**.

**Purpose:**  
- Determines **video quality**.
- Higher bitrate = **better quality**, but **more data** is required to stream.

**Typical Bitrate Ranges:**

| Video Quality        | Resolution     | Bitrate Range       |
|----------------------|----------------|----------------------|
| Low                  | 480p           | 500 kbps – 1 Mbps    |
| Standard (SD)        | 720p           | 1 Mbps – 2.5 Mbps    |
| High (HD)            | 1080p          | 3 Mbps – 6 Mbps      |
| Full HD (High FPS)   | 1080p @60fps   | 6 Mbps – 10 Mbps     |
| Ultra HD (4K)        | 2160p          | 15 Mbps – 25 Mbps+   |

---

## 🌐 Network Bandwidth

**Definition:**  
Network bandwidth is the **maximum rate** at which data can be transferred over a network connection. It’s usually measured in **Mbps**.

**Usage in Streaming:**  
- Bandwidth must be **higher than the video bitrate** to ensure smooth playback.
- Recommended to have **30–50% more bandwidth** than the bitrate to avoid buffering and support background tasks.

**Typical Bandwidth Requirements:**

| Video Quality        | Recommended Bandwidth | Notes & Common Use Cases                                                                 |
|----------------------|------------------------|-------------------------------------------------------------------------------------------|
| 480p (Low)           | 1.5 – 2 Mbps            | Basic video quality for mobile streaming; also suitable for casual browsing or messaging alongside playback. |
| 720p (SD)            | 3 – 4 Mbps              | Suitable for video calls, online gaming, and general web use while streaming.            |
| 1080p (HD)           | 5 – 8 Mbps              | Good for HD streaming on laptops/TVs; allows moderate multitasking like email, chat apps.|
| 1080p @60fps (HD+)   | 8 – 12 Mbps             | Smooth high-frame-rate viewing; supports background downloads, cloud sync, or gaming.    |
| 4K (Ultra HD)        | 25 – 40 Mbps            | Best for 4K smart TVs or monitors; needs high-speed broadband, especially if multiple users are active. |

---

> ✅ **Tip:** Adaptive streaming protocols like **HLS** and **MPEG-DASH** dynamically adjust video quality based on available bandwidth, helping prevent buffering during slowdowns.