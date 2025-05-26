# 🎥 Video Compression Terms and Stream Mechanics

## 🔑 Key Terms

### I-frame (Intra-coded Frame)

* An **I-frame** is a full image, encoded independently without reference to other frames.
* It provides a random-access point; playback can start cleanly at an I-frame.

### P-frame (Predicted Frame)

* A **P-frame** is encoded by referencing a previous I- or P-frame.
* It stores only the differences (motion or changes) from the previous reference frame.
* More efficient than I-frames but cannot stand alone.

### B-frame (Bidirectional Predicted Frame)

* A **B-frame** uses both past and future frames (I or P) to encode differences.
* Offers the highest compression efficiency.
* Requires more computational effort to decode and cannot be used as a reference for other frames.

### IDR Frame (Instantaneous Decoder Refresh)

* A special type of I-frame that *resets* the decoder.
* Guarantees no frames after it reference frames before it.

### GOP (Group of Pictures)

* A **GOP** is a sequence of frames in a video bound by keyframes (IDR/I-frames).
* It defines how many frames rely on previous reference frames before the next full intra-coded frame.
* Typical notation: **GOP size = N** means one I-frame every N frames.

---

## 🔄 Stream Mechanics: Sending and Receiving Frames

When streaming (e.g., RTSP):

1. **Encoding**: Source video is encoded into H.264/HEVC frames (I, P, B).
2. **Packetization**: Encoded frames are packetized into RTP/RTSP packets.
3. **Transmission**: Packets are sent over the network to the server or client.
4. **Decoding**: Client/server reconstructs frames by decoding packets, relying on I-frames as entry points.

> **Note**: Without an IDR to start on, a decoder cannot begin decoding until it sees the first keyframe.

---

## 📏 Impact of GOP Size

* **GOP Too Large** (e.g., 300 frames):

  * **Pros**:

    * Better compression efficiency (fewer I-frames).
    * Smoother bitrate profile over time.
    * Plays smoothly on strong, stable networks.

  * **Cons**:

    * Long wait for the next I-frame — affects random access, seeking, and features like DeepStream smart-record.
    * In DeepStream, if your record window contains no IDR, you'll see errors like:

      > `** ERROR: <RunUserCallback:123>: No video stream found `

    * Artifacts span longer if packet loss occurs.
    * On weak or lossy networks, frames depending on missing packets can’t be decoded, leading to **prolonged visual glitches or freezing**.
    * Playback or seeking may **stall until the next I-frame** is received.

* **GOP Too Small** (e.g., 1–15 frames):

  * **Pros**:

    * Frequent random-access points; robust to packet loss; precise segmenting.
    * Ideal for **unstable or slow networks** — I-frames are frequent, so the stream can recover quickly from loss.
    * Helps features like smart-recording, live preview, and segmenting work reliably.

  * **Cons**:

    * Higher bitrate and larger file size (more I-frames increase data).
    * Slightly reduced compression efficiency.
    * May cause **bitrate spikes** due to frequent large I-frames, which can overwhelm limited bandwidth and cause **jitter or frame drops**.

---

## 🔍 Inspecting GOP with FFmpeg (ffprobe)

### A. Direct Analysis of a File

```bash
ffprobe -v error \
  -select_streams v:0 \
  -show_frames \
  -show_entries frame=pkt_pts_time,pict_type \
  -of csv=p=0 input.mp4 \
| awk -F, '
    $2=="I" {
        if (last_idx) print "GOP:", NR-last_idx-1, "frames (", $1-prev_t, "s )";
        last_idx=NR; prev_t=$1
    }'
```

* Dumps each frame’s PTS and type.
* `awk` computes frames and seconds between I-frames.

### B. Live RTSP Stream

First **record a short sample clip**, then analyze the GOP structure from that saved file.

```bash
# 1) Grab 15 seconds of the RTSP feed and save locally
ffmpeg -rtsp_transport tcp -i rtsp://your.server/stream \
       -t 15 -c copy -y clip15s.mp4

# 2) Analyze GOP structure in the recorded clip
ffprobe -v error \
  -select_streams v:0 \
  -show_frames \
  -show_entries frame=pkt_pts_time,pict_type \
  -of csv=p=0 \
  clip15s.mp4 \
| awk -F, '
    $2=="I" {
      if (last_idx) {
        print "GOP:", NR-last_idx-1, "frames (", $1-prev_t, "s )"
      }
      last_idx = NR; prev_t = $1
    }'
```

---

### ⚙️ Changing GOP with FFmpeg

To re-encode and force a fixed GOP (e.g., 24 frames) and disable scene-change insertion:

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 \     # use x264 encoder
  -preset medium \   # speed-quality tradeoff
  -g 24 \            # maximum interval between IDR frames = 24
  -keyint_min 24 \   # minimum interval between IDR frames = 24
  -sc_threshold 0 \  # disable scene-change insertion of extra I-frames
  -c:a copy \        # copy audio
  output_gop24.mp4
```

* `-g 24`: sets **max** distance (frames) between keyframes.
* `-keyint_min 24`: sets **min** distance between keyframes.
* `-sc_threshold 0`: prevents additional keyframes on scene cuts, locking GOP exactly at 24 frames.

**Scene cut** is a sudden change between scenes or camera angles in a video, where the encoder usually inserts an extra I-frame to improve quality. The `-sc_threshold` option controls this behavior: setting it to 0 disables these extra I-frames, forcing keyframes only at fixed GOP intervals. This helps keep GOP size consistent but may reduce visual quality at abrupt scene changes.
