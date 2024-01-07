import time
import cv2
import cvzone
from cvzone.PoseModule import PoseDetector
import numpy as np

# Initialize the PoseDetector and the video capture
cap = cv2.VideoCapture(0)
detector = PoseDetector()

# Get the screen dimensions
screen_width, screen_height = 1920, 1080  # Replace with your screen resolution

# Create the OpenCV window and set the initial size to fit the screen
cv2.namedWindow('Exercise Counter', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Exercise Counter', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Initialize variables for tracking exercises
ptime = 0
ctime = 0
push_up_dir = 0
push_ups = 0
squat_dir = 0
squats = 0
bicep_dir = 0
bicep = 0
plank_dir = 0
plank = 0
lunge_dir = 0
lunge = 0
burpee_dir = 0
burpee = 0
dead_dir = 0
dead = 0
jump_dir = 0
jump = 0


while True:
    # Read a frame from the webcam
    _, img = cap.read()
    img = detector.findPose(img)
    fitness, bbox = detector.findPosition(img, draw=False)

    if fitness:
        # Calculate the angles relevant for push-ups and squats
        push_up_angle1 = detector.findAngle(img, 12, 14, 16)  # Left elbow, shoulder, and wrist
        push_up_angle2 = detector.findAngle(img, 11, 13, 15)  # Right elbow, shoulder, and wrist
        squat_angle = detector.findAngle(img, 23, 25, 27)  # Hips, knees, and ankle
        bicep_angle = detector.findAngle(img, 12, 14, 16)  # Left elbow, shoulder, and wrist
        plank_angle = detector.findAngle(img, 23, 25, 27)  # Hips, knees, and ankle
        lunge_angle = detector.findAngle(img, 23, 25, 27)  # Hips, knees, and ankle
        burpee_angle = detector.findAngle(img, 11, 23, 25)  # shoulder, hips and knee
        dead_angle = detector.findAngle(img, 11, 23, 25)  # shoulder, hips and knee
        jump_angle1 = detector.findAngle(img, 23, 11, 13)  # left hand
        jump_angle2 = detector.findAngle(img, 24, 12, 14)  # right hand
        jump_angle3 = detector.findAngle(img, 11, 23, 25)  # left leg
        jump_angle4 = detector.findAngle(img, 12, 24,26)  # right leg


        # Map angles to percentage values
        push_per_val1 = int(np.interp(push_up_angle1, (75, 175), (100, 0)))
        push_per_val2 = int(np.interp(push_up_angle2, (75, 175), (100, 0)))
        squat_per_val = int(np.interp(squat_angle, (85, 175), (100, 0)))
        bicep_per_val = int(np.interp(bicep_angle, (40, 155), (100, 0)))
        plank_per_val = int(np.interp(plank_angle, (180, 90), (100, 0)))
        lunge_per_val = int(np.interp(lunge_angle, (90, 180), (100, 0)))
        burpee_per_val = int(np.interp(burpee_angle, (180, 30), (100, 0)))
        dead_per_val = int(np.interp(dead_angle, (180, 30), (100, 0)))
        jump_per_val1 = int(np.interp(jump_angle1 + jump_angle2, (120, 10), (100, 0)))
        jump_per_val2 = int(np.interp(jump_angle3 + jump_angle4, (120, 10), (100, 0)))


        # Map percentage values to progress bars
        push_bar_val1 = int(np.interp(push_per_val1, (0, 100), (40 + 350, 40)))
        push_bar_val2 = int(np.interp(push_per_val2, (0, 100), (40 + 350, 40)))
        squat_bar_val = int(np.interp(squat_per_val, (0, 100), (40 + 350, 40)))
        bicep_bar_val = int(np.interp(bicep_per_val, (0, 100), (40 + 350, 40)))
        plank_bar_val = int(np.interp(plank_per_val, (0, 100), (40 + 350, 40)))
        lunge_bar_val = int(np.interp(lunge_per_val, (0, 100), (40 + 350, 40)))
        burpee_bar_val = int(np.interp(burpee_per_val, (0, 100), (40 + 350, 40)))
        dead_bar_val = int(np.interp(dead_per_val, (0, 100), (40 + 350, 40)))
        jump_bar_val1 = int(np.interp(jump_per_val1, (0, 100), (40 + 350, 40)))
        jump_bar_val2 = int(np.interp(jump_per_val2, (0, 100), (40 + 350, 40)))




        # Draw progress bars
        cv2.rectangle(img, (35, push_bar_val1), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, push_bar_val2), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, squat_bar_val), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, bicep_bar_val), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, plank_bar_val), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, lunge_bar_val), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, burpee_bar_val), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, dead_bar_val), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, jump_bar_val1), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)
        cv2.rectangle(img, (35, jump_bar_val2), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (255, 255, 255), 3)



        # Display percentage values
        cvzone.putTextRect(img, f'{push_per_val1}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{push_per_val2}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{squat_per_val}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{bicep_per_val}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{plank_per_val}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{lunge_per_val}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{burpee_per_val}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{dead_per_val}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{jump_per_val1}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))
        cvzone.putTextRect(img, f'{jump_per_val2}%', (35, 25), 1.1, 2, colorT=(0, 135, 0))





        # Count push-ups
        if push_per_val1 == 100 and push_per_val2 == 100:
            if push_up_dir == 0:
                push_ups += 0.5
                push_up_dir = 1

        elif push_per_val1 == 0 and push_per_val2 == 0:
            if push_up_dir == 1:
                push_ups += 0.5
                push_up_dir = 0

        # Count squats
        if squat_per_val == 100:
            if squat_dir == 0:
                squats += 0.5
                squat_dir = 1

        elif squat_per_val == 0:
            if squat_dir == 1:
                squats += 0.5
                squat_dir = 0

        # Count bicep
        if bicep_per_val == 100:
            if bicep_dir == 0:
                bicep += 0.5
                bicep_dir = 1

        elif bicep_per_val == 0:
            if bicep_dir == 1:
                bicep += 0.5
                bicep_dir = 0

        # Count plank
        if plank_per_val == 100:
            if plank_dir == 0:
                plank += 0.5
                plank_dir = 1

        elif plank_per_val == 0:
            if plank_dir == 1:
                plank += 0.5
                plank_dir = 0

        # Count lunge
        if lunge_per_val == 100:
            if lunge_dir == 0:
                lunge += 0.5
                lunge_dir = 1

        elif lunge_per_val == 0:
            if lunge_dir == 1:
                lunge += 0.5
                lunge_dir = 0

        # Count burpee
        if burpee_per_val == 100:
            if burpee_dir == 0:
                burpee += 0.5
                burpee_dir = 1

        elif burpee_per_val == 0:
            if burpee_dir == 1:
                burpee += 0.5
                burpee_dir = 0

        # Count dead
        if dead_per_val == 100:
            if dead_dir == 0:
                dead += 0.5
                dead_dir = 1

        elif dead_per_val == 0:
            if dead_dir == 1:
                dead += 0.5
                dead_dir = 0

        # Count jumping jacks
        if jump_per_val1 == 100 and jump_per_val2 == 100:
            if jump_dir == 0:
                jump += 0.5
                jump_dir = 1

        elif jump_per_val1 == 0 and jump_per_val2 == 0:
            if jump_dir == 1:
                jump += 0.5
                jump_dir = 0

        # Display push-up and squat counts
        cvzone.putTextRect(img, f'Push-Ups:{int(push_ups)}', (410, 50), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Squats:{int(squats)}', (460, 100), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Bicep:{int(bicep)}', (483,150), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Planks:{int(plank)}', (465, 200), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Lunges:{int(lunge)}', (450, 250), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Burpees:{int(burpee)}', (430, 300), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Dead-Lifts:{int(dead)}', (390, 350), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())
        cvzone.putTextRect(img, f'Jumping-Jacks:{int(jump)}', (330, 400), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3, colorB=())

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.imshow('Exercise Counter', img)

    if cv2.waitKey(1) == ord('q'):
        break
