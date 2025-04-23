``` 
ffmpeg -re -stream_loop -1 -i <video> -c copy -f rtsp <rtsp_url>
```
- CPU% < 4%
- MEM < 20 MiB

---

```
ffmpeg -re -stream_loop -1 -i <video> \
    -fflags nobuffer -flags low_delay -max_delay 0 -tune zerolatency \
    -c copy -preset ultrafast \
    -f rtsp <rtsp_url>
```
- CPU% < 4%
- MEM < 21 MiB

---

```
gst-launch-1.0 \
  filesrc location=<video> ! \
  avidemux name=demux demux.video_0 ! \
  mpeg4videoparse ! \ 
  mpegtsmux ! \
  filesink location=output.ts

gst-launch-1.0 \
  multifilesrc location=/videos/output.ts loop=true ! \
  tsdemux name=demux demux.video_0_0041 ! \
  queue ! \
  mpeg4videoparse ! \
  rtspclientsink location=<rtsp_url> latency=0 protocols=tcp
```
- CPU% < 4%
- MEM < 166 MiB

---