import torch
import cv2
import matplotlib.pyplot as plt

from mainapp.car.src.Models import Unet

class Car_View :

    def __init__(self,img_data):
        self.initModel()
        self.imageLoad(img_data)
        self.runModel()


    def initModel(self):
        self.labels = ['Breakage_3', 'Crushed_2', 'Scratch_0', 'Seperated_1']
        self.models = []
        n_classes = 2
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        for label in self.labels:
            model_path = f'./mainapp/car/models/[DAMAGE][{label}]Unet.pt'

            model = Unet(encoder='resnet34', pre_weight='imagenet', num_classes=n_classes).to(self.device)
            model.model.load_state_dict(torch.load(model_path, map_location=torch.device(self.device)))
            model.eval()

            self.models.append(model)

    def imageLoad(self, img_data):
        img_path = './mainapp/car/img/0000177_sc-153567.jpg'
        # 이미지 읽기 
        # img = cv2.imread(img_data)
        # 이미지 채널변환 ( BLUE, GREEN , RED) -> (RED , GREEN , BLUE)
        img = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
        # 이미지 싸이즈 변환
        img = cv2.resize(img, (256, 256))
        # 이미지 값 정규화
        img_input = img / 255.
        # img_input 이미지의 행열변환, 
        img_input = img_input.transpose([2, 0, 1])
        # img_input를 NumPy 배열을 PyTorch Tensor로 변환 이후 float 형태로 변환 CPU or GPU 사용할지 선택
        self.img_input = torch.tensor(img_input).float().to(self.device)
        # 차원하나 늘림 [3, 256, 256] -> [1, 3, 256, 256]
        self.img_input = self.img_input.unsqueeze(0)
        self.outputs = []

    def runModel(self):
        for model in self.models:
            # 모델 돌리기 
            output = model(self.img_input)

            img_output = torch.argmax(output, dim=1).detach().cpu().numpy()
            img_output = img_output.transpose([1, 2, 0])

            self.outputs.append(img_output)

    def result(self):
        price_table = [
            100,  # Breakage_3
            200,  # Crushed_2
            50,   # Scratch_0
            120   # Seperated_1
        ]   

        total = 0
        for i, price in enumerate(price_table):
            area = self.outputs[i].sum()
            total += area * price
        return total

        
                
