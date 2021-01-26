from torch.utils.data import Dataset, DataLoader
import torchvision
import os
from PIL import Image
import matplotlib.pyplot as plt

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


class customDatasetClass(Dataset):

    def __init__(self, path):

        """

        Custom Dataset Iterator class using Pytorch DataLoader
        :param path: Path to the directory containing the images
        Data
        ├───Class0
        │       image0.png
        │       image1.png
        │       image2.png
        │       image3.png
        │
        ├───Class1
        │       image0.png
        │       image1.png
        │       image2.png
        │       image3.png
        │
        ├───Class2
        │       image0.png
        │       image1.png
        │       image2.png
        │       image3.png
        │
        └───Class3
                image0.png
                image1.png
                image2.png
                image3.png

        """

        self.path = path
        self.allImagePaths = []
        self.allTargets = []
        self.targetToClass = sorted(os.listdir(self.path))

        for targetNo, targetI in enumerate(self.targetToClass):
            for imageI in sorted(os.listdir(self.path + '/' + targetI)):
                self.allImagePaths.append(self.path + '/' + targetI + '/' + imageI)
                self.allTargets.append(targetNo)

        self.transforms = torchvision.transforms.Compose([
            torchvision.transforms.RandomCrop((256, 256)),
            torchvision.transforms.ToTensor()
        ])

    def __getitem__(self, item):

        image = Image.open(self.allImagePaths[item]).convert('RGB')
        target = self.allTargets[item]

        image = self.transforms(image)

        return image, target

    def __len__(self):

        return len(self.allImagePaths)


if __name__ == "__main__":

    customDataLoaderObject = DataLoader(
        customDatasetClass('C:/Users/0000402250/Desktop/Personal/Content/Internship/Data'),
        batch_size=4,
        num_workers=8,
        shuffle=True
    )

    for no, (images, targets) in enumerate(customDataLoaderObject):

        print(images.shape, targets.shape)
        # [4, 3, 256, 256], [4]
