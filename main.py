from utils import (read_video,
                   save_video)

def main():
    video_frames = read_video("input_video/input_video.mp4")
    if not video_frames:
        print("Error: No frames were processed. Check if the input video file exists and is readable.")
        return
    save_video(video_frames, "output/output_video.avi")
    
if __name__ == "__main__":
    main()

