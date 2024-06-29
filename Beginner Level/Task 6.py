class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def make_call(self, number):
        print(f"Making a call to {number} using {self.__class__.__name__}.")
    
    def receive_call(self, number):
        print(f"Receiving a call from {number} on {self.__class__.__name__}.")
    
    def take_a_picture(self):
        print(f"Taking a picture with the {self.rear_camera} rear camera on {self.__class__.__name__}.")

class Apple(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=False, front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model
    
    def make_call(self, number):
        print(f"Making a FaceTime call to {number} using {self.model}.")

class Samsung(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=True, front_camera="16MP", rear_camera="32MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model
    
    def make_call(self, number):
        print(f"Making a call to {number} using {self.model} with Samsung Dialer.")

# Creating objects of Apple class with different properties
iphone_12 = Apple(model="iPhone 12", network_type="5G", dual_sim=True, front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB")
iphone_se = Apple(model="iPhone SE", network_type="4G", dual_sim=False, front_camera="7MP", rear_camera="12MP", ram="3GB", storage="64GB")

# Creating objects of Samsung class with different properties
samsung_galaxy_s21 = Samsung(model="Galaxy S21", network_type="5G", dual_sim=True, front_camera="10MP", rear_camera="64MP", ram="8GB", storage="128GB")
samsung_galaxy_a52 = Samsung(model="Galaxy A52", network_type="4G", dual_sim=True, front_camera="32MP", rear_camera="64MP", ram="6GB", storage="128GB")

# Testing functionality
iphone_12.make_call("123-456-7890")
iphone_12.receive_call("987-654-3210")
iphone_12.take_a_picture()

iphone_se.make_call("123-456-7890")
iphone_se.receive_call("987-654-3210")
iphone_se.take_a_picture()

samsung_galaxy_s21.make_call("123-456-7890")
samsung_galaxy_s21.receive_call("987-654-3210")
samsung_galaxy_s21.take_a_picture()

samsung_galaxy_a52.make_call("123-456-7890")
samsung_galaxy_a52.receive_call("987-654-3210")
samsung_galaxy_a52.take_a_picture()
