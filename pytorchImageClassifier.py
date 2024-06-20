from PIL import Image
from matplotlib.pyplot import imshow
import pandas
import matplotlib.pylab as plt
import os
import glob
import skillsnetwork

def show_data(data_sample, shape = (28, 28)):
    plt.imshow(data_sample[0].numpy().reshape(shape), cmap='gray')
    plt.title('y = ' + data_sample[1])
    
#download data
async def download_data():
    await skillsnetwork.prepare("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0321EN/data/images/concrete_crack_images_for_classification.zip", path = "/resources/data", overwrite=True)

    await download_data()

#examine files
directory="/resources/data"
negative='Negative'

negative_file_path=os.path.join(directory,negative)
negative_file_path

os.listdir(negative_file_path)[0:3]
[os.path.join(negative_file_path,file) for file in  os.listdir(negative_file_path)][0:3]
 
print("test.jpg".endswith(".jpg"))
print("test.mpg".endswith(".jpg"))
negative_files=[os.path.join(negative_file_path,file) for file in  os.listdir(negative_file_path) if file.endswith(".jpg")]
negative_files.sort()
negative_files[0:3]

#load positive files
positive="Positive"
positive_files_path=os.path.join(directory,positive)
positive_files_path
positive_files=[os.path.join(positive_files_path,file) for file in  os.listdir(positive_files_path) if file.endswith(".jpg")]
positive_files.sort()
positive_files[0:3]
firstThree= positive_files[0:3]
firstThree

#display and analyyze images

image1 = Image.open(negative_files[0])
# you can view the image directly 
#image 
plt.imshow(image1)
plt.title("1st Image Without Cracks")
plt.show()

 
 image2 = Image.open(positive_files[1])
plt.imshow(image2)
plt.title(" 2 Image With  Cracks")
plt.show()

image2 = Image.open(positive_files[2])
plt.imshow(image2)
plt.title("3 Image With  Cracks")
plt.show()

image3 = Image.open(positive_files[3])
plt.imshow(image3)
plt.title("4th Image With Cracks")
plt.show()
 

 