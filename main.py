import os
import sys

import cv2

"""

Пока что это snippet (заготовка) программы,
поэтому качество кода вскоре будет улучшаться

"""


objects = str(input("Enter object titles (etc. cat dog car): ")).split()
objects_amount = len(objects)
image_per_object = int(input('Enter images amount per object: '))
def get_cap(cam_number=0):
    """
    Функция get_cap() возвращает объект capture для работы с камерой
    Необязательный аргумент cam_number позволяет указать желаемую камеру, если их несколько
    """
    try:
        capture = cv2.VideoCapture(cam_number)
        _ret, _frame = capture.read()
        height, width, _ = _frame.shape
        if not capture.isOpened():  # Проверка открытия камеры
            raise RuntimeError("Camera not found. Check that your camera is connected.")
    except RuntimeError:  # Обработка ситуация отсутствия камеры
        sys.exit(1)
    # logs.log(f"Capture {cam_number} opened", "SUCCESS")
    return capture, height, width

# Инициализация камеры
cap, cam_h, cam_w = get_cap(1)

pause = True

for i in range(1, objects_amount + 1):
    obj_name = objects[i - 1]
    os.mkdir(obj_name)
    ready = str(input(f'Collect {obj_name} images? (type y to continue): '))
    if ready.lower() == 'y':
        pause = False
    if not pause:
        print(f'Collecting {obj_name} images...')
        for j in range(1, image_per_object + 1):
            ret, frame = cap.read()
            cv2.imshow('Video', frame)
            print(f'Saving {obj_name}/{obj_name}_{j}.jpg...')
            cv2.imwrite(f'{obj_name}/{obj_name}_{j}.jpg', frame)
            # cv2.imshow('Video', frame)
            # key = cv2.waitKey(0) & 0xFF
            # if key == ord("q"):
            #     breakф

print(f'Saved images for {objects}')
cap.release()

