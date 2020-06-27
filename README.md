# jetson-nano-rtsp

If you really want to learn while enjoying coffee, visit the master: Paul McWhorter -> (https://www.youtube.com/channel/UCfYfK0tzHZTpNFrc_NDKfTA)

This is a test of the rtsp protocol from a Raspberry pi to Jetson Nano and Jetson Xavier:

A: Streaming a RPi Camera video:
    Source: https://helloraspberrypi.blogspot.com/2019/02/raspberry-pi-stream-video-to-vlc-player.html

1. On terminal run this commad: 
    <code>$raspivid -o - -t 0 -n -w 320 -h 240 -fps 30| cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:80/live/stream}' :demux=h264</code>

B: Using ffmpeg.

1. Install ffmpeg:   Instructions here: 
    https://toptechboy.com/low-cost-raspberry-pi-ip-camera/
                  
  Also visit this post if you are going to use the RPi Camera: 
    https://github.com/legotheboss/YouTube-files/wiki/(RPi)-Compile-FFmpeg-with-the-OpenMAX-H.264-GPU-acceleration
    
2. Install node rtsp server, instructions on this Post:
    https://codecalamity.com/raspberry-pi-hardware-accelerated-h264-webcam-security-camera/#compile-ffmpeg-with-hardware-acceleration
    
3. The following commands start the video streaming 
      
      USB Camera (Tested: Logitec C920s) 
      
      <code>ffmpeg -input_format yuyv422 -f video4linux2 -s 800x600 -r 10 -i /dev/video0 -c:v h264_omx -r 10 -b:v 2M -an -f rtsp rtsp://localhost:80/live/stream</code>
      
      RPi Camera (h264 native support)
      
      <code>ffmpeg -input_format h264 -f video4linux2 -video_size 1920x1080 -framerate 30 -i /dev/video0 -c:v copy -an -f rtsp rtsp://localhost:80/live/stream</code>

4. Verify that the rtsp streaming is working:
  
    Used VLC on a PC: Media --> Open Network Stream... --> rtsp://raspberrypi_ip:80/live/stream
    
5. Run the Python program openCV-rtsp.py on your Jetson Nano or Xavier

