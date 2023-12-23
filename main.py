import cv2
import requests
import sys
from city import CITY
import time


class Main:
    def __init__(self):
        self.video = None
        self.password = None
        self.ip = None
        self.user_name = None
        self.path_api: str = sys.argv[1]
        self.password_api: str = sys.argv[2]
        self.time_between_screenshot: int = int(sys.argv[3])
        self.number_picture_counter: int = 0
        self.actual_image_url: str = ''
        self.run()

    def update_var_by_city(self, index: int) -> None:
        self.ip: str = CITY[index][1]
        self.user_name: str = CITY[index][2]
        self.password: str = CITY[index][3]
        self.actual_image_url: str = (f'dataset/{CITY[index][0]}'
                                      f'-dataset-{self.number_picture_counter}'
                                      f'.png')

    def take_screenshot(self) -> None:
        self.video = cv2.VideoCapture(f'rtsp://{self.user_name}:'
                                      f'{self.password}@{self.ip}'
                                      f'/h264Preview_01_sub')
        _, frame = self.video.read()
        cv2.imwrite(self.actual_image_url, frame)

    def send_screenshot(self) -> None:
        try:
            with open(self.actual_image_url, 'rb') as file:
                requests.post(self.path_api, files={'file': file},
                              json={'key': self.password_api})
            print(f'Picture {self.actual_image_url} sent')
        except Exception as e:
            print(e)

    def run(self) -> None:
        while True:
            for i in range(len(CITY)):
                self.update_var_by_city(i)
                self.take_screenshot()
                self.send_screenshot()
            self.number_picture_counter += 1
            time.sleep(self.time_between_screenshot)


if __name__ == '__main__':
    Main()
