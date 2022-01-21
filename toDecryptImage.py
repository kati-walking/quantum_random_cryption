import numpy as np
import math
from PIL import Image

cipher_image = np.array(Image.open('cipher_image/cipher_0.png').convert('L'))
key_image = np.array(Image.open('18qubit_ryrz_images/key_0.jpg').convert('L'))

cipher_lists=cipher_image.tolist()
key_lists=key_image.tolist()

cipher=[item for sublist in cipher_lists for item in sublist]
key = [item for sublist in key_lists for item in sublist]

sum_all = 0
decrypt=[0]*len(cipher)
for i in reversed(range(len(cipher))):
    tmp=int((sum_all*key[i]*(10**8/256**4))%256)

    if(i==0):
        decrypt[i]=cipher[i]^(127+key[i])%256^tmp
        break
    decrypt[i]=cipher[i]^(cipher[i-1]+key[i])%256^tmp
    sum_all+=decrypt[i]


decrypt_matrix = np.reshape(decrypt,(cipher_image.shape[0],cipher_image.shape[1]))
decrypt_image=Image.fromarray(decrypt_matrix.astype(np.uint8))
decrypt_image.save('decrypt_image/decrypt_0.jpg')
print('fin')
