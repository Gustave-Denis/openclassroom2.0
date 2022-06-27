class Camera:
    def take_picture(self):
        print("Say Cheese!")


class MobilePhone:
    def __init__(self, memory):
        self.memory = memory


class CameraPhone(Camera, MobilePhone):
    pass


if __name__ == '__main__':
    cameraphone = CameraPhone("200KB")
    cameraphone.take_picture()
    print(cameraphone.memory)
