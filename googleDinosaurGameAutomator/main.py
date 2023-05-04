import cv2
import numpy as np
import pyautogui

while True:
    image = pyautogui.screenshot(region=(75, 600, 300, 250))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    black_pixel_count = np.sum(image < 100)
    white_pixel_count = np.sum(image > 100)

    print("Number of black pixels : ", black_pixel_count)
    print("Number of white pixels : ", white_pixel_count)

    if black_pixel_count > 4000 and black_pixel_count < 30000:
        pyautogui.press('up')

    if white_pixel_count > 4000 and white_pixel_count < 30000:
        pyautogui.press('up')

    cv2.imshow('image', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

