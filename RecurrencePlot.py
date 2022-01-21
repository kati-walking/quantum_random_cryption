import numpy as np
import math
from PIL import Image

key_count=9

key = '18qubit_ryrz_images/key_'+str(key_count)+'.jpg'
##key='cipher_image/cipher_'+str(count)+'.png'
image = np.array(Image.open(key))
image_lists = image.tolist()
image_list=[item for sublist in image_lists for item in sublist]



for k in range(128):
    result=[[0 for i in range(2048)] for j in range(len(image_list))]
    """
    print(len(result))##262144
    print(len(result[0]))##2048
    result[i][j]について
    0<=i<=262144
    0<=j<=2048
    """
    for i in range(len(image_list)):
        for j in range(2048):
            if(image_list[i]==image_list[j+k*2048]):
                result[i][j]=255
    for i in range(128):
        cut_result=result[2048*i:2048*(i+1)]
        result_image=Image.fromarray(np.array(cut_result).astype(np.uint8))
        image_pass = 'recurrence/'+str(key_count)+'/'+str(k)+'_'+str(i)+'.png'
        result_image.save(image_pass,'PNG')

print('fin')
