``` 
ffmpeg -re -stream_loop -1 -i <video> -c copy -f rtsp <rtsp_url>
```
- CPU% < 4%
- MEM < 20 MiB
- size for 10s = 9419kB 
- bitrate for 10s = 7748.2kbits/s

---

```
ffmpeg -re -stream_loop -1 -i <video> \
    -fflags nobuffer -flags low_delay -max_delay 0 -tune zerolatency \
    -c copy -preset ultrafast \
    -f rtsp <rtsp_url>
```
- CPU% < 4%
- MEM < 21 MiB
- size for 10s = 7163kB  
- bitrate for 10s = 5892.3kbits/s

---

