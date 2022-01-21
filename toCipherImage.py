import numpy as np
import math
from PIL import Image
count = 9
image = np.array(Image.open('moto_image/vegetable.jpg').convert('L'))
key_url = '18qubit_ryrz_images/key_'+str(count)+'.jpg'
key_image = np.array(Image.open(key_url).convert('L'))


print(type(image))
print(image.shape)


image_lists = image.tolist()
key_lists = key_image.tolist()


##print(image_list[1])
image_list=[item for sublist in image_lists for item in sublist]
key = [item for sublist in key_lists for item in sublist]



sum_pixel=0
cipher=[0]*len(image_list)
for pixel in image_list:
    sum_pixel+=pixel
    
for i,image_pixel in enumerate(image_list):
    sum_pixel-=image_pixel
    if(i == 0):
        tmp=127
    else:
        tmp=cipher[i-1]
    cipher[i]=image_pixel^(tmp+key[i])%256
    ##print(cipher[i])
    k =int((sum_pixel*key[i]*(10**8/256**4))%256)
    ##print(sum_pixel)
    ##print(k)
    ##print(tmp)
    ##print(key[i])
    ##print('-------------------')
    cipher[i]^=k

cipher_matrix=np.reshape(cipher,(image.shape[0],image.shape[1]))
cipher_image=Image.fromarray(cipher_matrix.astype(np.uint8))
cipher_url='cipher_image/cipher_'+str(count)+'.png'
cipher_image.save(cipher_url)
print('fin')
