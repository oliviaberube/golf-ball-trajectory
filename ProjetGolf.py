import cv2, os

from src.detection import detect_ball, convert_pos, detect_movement
from src.video import get_video_info, select_video, open_video



def main():
    path = select_video()
    
    video = open_video(path)

    if video is None:
        return

    fps, frame_count, height, width = get_video_info(video)

    
    read,frame = video.read()

    origin = False
    
    positions = []
    frame_index = 0 
    
    while read:

        result = detect_ball(frame)

        if result is not None: 

            x_p, y_p, radius_p = result

            if origin != True:
                x0_p = x_p
                y0_p = y_p
                radius0_p = radius_p
                origin = True

        
        outside_frame = (
            x_p + radius_p >= width  
            or x_p - radius_p <= 0      
            or y_p + radius_p >= height 
            or y_p - radius_p <= 0 
        )
  
        if outside_frame:
            break


        x, y = convert_pos(
            x_p, y_p, 
            x0_p, y0_p, 
            radius0_p )
        positions.append((frame_index, x, y))

        frame_index += 1
        read,frame = video.read()
   
    
    video.release()

    
    start_frame = detect_movement(positions)

    if start_frame is not None:
        useful_pos = [
            pos for pos in positions
            if pos[0] >= start_frame]




if __name__ == "__main__":
    main()