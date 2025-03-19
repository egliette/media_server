# Media server

## Simple RTSP Server

**Step 1**: Put your videos inside `videos` folder.

**Step 2**: Edit your `USERNAME`, `PASSWORD` inside `docker/.env`.

**Step 3**: To stream your videos, run:
```
docker-compose -f docker/docker-compose.simple_rtsp.yaml up
```

You should see your stream at `rtsp://{USERNAME}:{PASSWORD}@localhost:8554/<video_name>`

For example `rtsp://mediaserver:free4all@localhost:8554/your_camera`
    