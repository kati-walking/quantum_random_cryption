import numpy as np
import math
from PIL import Image
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import BasicAer, execute
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity 
from copy import deepcopy
q = QuantumRegister(18,'q')
c = ClassicalRegister(18,'c')
circ = QuantumCircuit(q,c)
##鍵となる回転のリスト(範囲は実数)
##todo 18*2 pattern,or 18*n pattern 
##ランダムな鍵のリストを生成する

## 任意のRY変換を行う
np.random.seed(0)
key_list = np.random.rand(10000)
key_list *=2
circ.ry(math.pi*key_list[0],q[0])
circ.ry(math.pi*key_list[1],q[1])
circ.ry(math.pi*key_list[2],q[2])
circ.ry(math.pi*key_list[3],q[3])
circ.ry(math.pi*key_list[4],q[4])
circ.ry(math.pi*key_list[5],q[5])
circ.ry(math.pi*key_list[6],q[6])
circ.ry(math.pi*key_list[7],q[7])
circ.ry(math.pi*key_list[8],q[8])
circ.ry(math.pi*key_list[9],q[9])
circ.ry(math.pi*key_list[10],q[10])
circ.ry(math.pi*key_list[11],q[11])
circ.ry(math.pi*key_list[12],q[12])
circ.ry(math.pi*key_list[13],q[13])
circ.ry(math.pi*key_list[14],q[14])
circ.ry(math.pi*key_list[15],q[15])
circ.ry(math.pi*key_list[16],q[16])
circ.ry(math.pi*key_list[17],q[17])
circ.rz(math.pi*key_list[18],q[0])
circ.rz(math.pi*key_list[19],q[1])
circ.rz(math.pi*key_list[20],q[2])
circ.rz(math.pi*key_list[21],q[3])
circ.rz(math.pi*key_list[22],q[4])
circ.rz(math.pi*key_list[23],q[5])
circ.rz(math.pi*key_list[24],q[6])
circ.rz(math.pi*key_list[25],q[7])
circ.rz(math.pi*key_list[26],q[8])
circ.rz(math.pi*key_list[27],q[9])
circ.rz(math.pi*key_list[28],q[10])
circ.rz(math.pi*key_list[29],q[11])
circ.rz(math.pi*key_list[30],q[12])
circ.rz(math.pi*key_list[31],q[13])
circ.rz(math.pi*key_list[32],q[14])
circ.rz(math.pi*key_list[33],q[15])
circ.rz(math.pi*key_list[34],q[16])
circ.rz(math.pi*key_list[35],q[17])
circ.barrier()
for i in range(10):
    ##各量子ビットのペア間にCNOTを適用
    circ.cx(q[0],q[1])
    circ.cx(q[0],q[2])
    circ.cx(q[0],q[3])
    circ.cx(q[0],q[4])
    circ.cx(q[0],q[5])
    circ.cx(q[0],q[6])
    circ.cx(q[0],q[7])
    circ.cx(q[0],q[8])
    circ.cx(q[0],q[9])
    circ.cx(q[0],q[10])
    circ.cx(q[0],q[11])
    circ.cx(q[0],q[12])
    circ.cx(q[0],q[13])
    circ.cx(q[0],q[14])
    circ.cx(q[0],q[15])
    circ.cx(q[0],q[16])
    circ.cx(q[0],q[17])
    circ.cx(q[1],q[2])
    circ.cx(q[1],q[3])
    circ.cx(q[1],q[4])
    circ.cx(q[1],q[5])
    circ.cx(q[1],q[6])
    circ.cx(q[1],q[7])
    circ.cx(q[1],q[8])
    circ.cx(q[1],q[9])
    circ.cx(q[1],q[10])
    circ.cx(q[1],q[11])
    circ.cx(q[1],q[12])
    circ.cx(q[1],q[13])
    circ.cx(q[1],q[14])
    circ.cx(q[1],q[15])
    circ.cx(q[1],q[16])
    circ.cx(q[1],q[17])
    circ.cx(q[2],q[3])
    circ.cx(q[2],q[4])
    circ.cx(q[2],q[5])
    circ.cx(q[2],q[6])
    circ.cx(q[2],q[7])
    circ.cx(q[2],q[8])
    circ.cx(q[2],q[9])
    circ.cx(q[2],q[10])
    circ.cx(q[2],q[11])
    circ.cx(q[2],q[12])
    circ.cx(q[2],q[13])
    circ.cx(q[2],q[14])
    circ.cx(q[2],q[15])
    circ.cx(q[2],q[16])
    circ.cx(q[2],q[17])
    circ.cx(q[3],q[4])
    circ.cx(q[3],q[5])
    circ.cx(q[3],q[6])
    circ.cx(q[3],q[7])
    circ.cx(q[3],q[8])
    circ.cx(q[3],q[9])
    circ.cx(q[3],q[10])
    circ.cx(q[3],q[11])
    circ.cx(q[3],q[12])
    circ.cx(q[3],q[13])
    circ.cx(q[3],q[14])
    circ.cx(q[3],q[15])
    circ.cx(q[3],q[16])
    circ.cx(q[3],q[17])
    circ.cx(q[4],q[5])
    circ.cx(q[4],q[6])
    circ.cx(q[4],q[7])
    circ.cx(q[4],q[8])
    circ.cx(q[4],q[9])
    circ.cx(q[4],q[10])
    circ.cx(q[4],q[11])
    circ.cx(q[4],q[12])
    circ.cx(q[4],q[13])
    circ.cx(q[4],q[14])
    circ.cx(q[4],q[15])
    circ.cx(q[4],q[16])
    circ.cx(q[4],q[17])
    circ.cx(q[5],q[6])
    circ.cx(q[5],q[7])
    circ.cx(q[5],q[8])
    circ.cx(q[5],q[9])
    circ.cx(q[5],q[10])
    circ.cx(q[5],q[11])
    circ.cx(q[5],q[12])
    circ.cx(q[5],q[13])
    circ.cx(q[5],q[14])
    circ.cx(q[5],q[15])
    circ.cx(q[5],q[16])
    circ.cx(q[5],q[17])
    circ.cx(q[6],q[7])
    circ.cx(q[6],q[8])
    circ.cx(q[6],q[9])
    circ.cx(q[6],q[10])
    circ.cx(q[6],q[11])
    circ.cx(q[6],q[12])
    circ.cx(q[6],q[13])
    circ.cx(q[6],q[14])
    circ.cx(q[6],q[15])
    circ.cx(q[6],q[16])
    circ.cx(q[6],q[17])
    circ.cx(q[7],q[8])
    circ.cx(q[7],q[9])
    circ.cx(q[7],q[10])
    circ.cx(q[7],q[11])
    circ.cx(q[7],q[12])
    circ.cx(q[7],q[13])
    circ.cx(q[7],q[14])
    circ.cx(q[7],q[15])
    circ.cx(q[7],q[16])
    circ.cx(q[7],q[17])
    circ.cx(q[8],q[9])
    circ.cx(q[8],q[10])
    circ.cx(q[8],q[11])
    circ.cx(q[8],q[12])
    circ.cx(q[8],q[13])
    circ.cx(q[8],q[14])
    circ.cx(q[8],q[15])
    circ.cx(q[8],q[16])
    circ.cx(q[8],q[17])
    circ.cx(q[9],q[10])
    circ.cx(q[9],q[11])
    circ.cx(q[9],q[12])
    circ.cx(q[9],q[13])
    circ.cx(q[9],q[14])
    circ.cx(q[9],q[15])
    circ.cx(q[9],q[16])
    circ.cx(q[9],q[17])
    circ.cx(q[10],q[11])
    circ.cx(q[10],q[12])
    circ.cx(q[10],q[13])
    circ.cx(q[10],q[14])
    circ.cx(q[10],q[15])
    circ.cx(q[10],q[16])
    circ.cx(q[10],q[17])
    circ.cx(q[11],q[12])
    circ.cx(q[11],q[13])
    circ.cx(q[11],q[14])
    circ.cx(q[11],q[15])
    circ.cx(q[11],q[16])
    circ.cx(q[11],q[17])
    circ.cx(q[12],q[13])
    circ.cx(q[12],q[14])
    circ.cx(q[12],q[15])
    circ.cx(q[12],q[16])
    circ.cx(q[12],q[17])
    circ.cx(q[13],q[14])
    circ.cx(q[13],q[15])
    circ.cx(q[13],q[16])
    circ.cx(q[13],q[17])
    circ.cx(q[14],q[15])
    circ.cx(q[14],q[16])
    circ.cx(q[14],q[17])
    circ.cx(q[15],q[16])
    circ.cx(q[15],q[17])
    circ.cx(q[16],q[17])
    #任意のRY変換を行う
    circ.barrier()
    circ.ry(math.pi*key_list[0+36*(i+1)],q[0])
    circ.ry(math.pi*key_list[1+36*(i+1)],q[1])
    circ.ry(math.pi*key_list[2+36*(i+1)],q[2])
    circ.ry(math.pi*key_list[3+36*(i+1)],q[3])
    circ.ry(math.pi*key_list[4+36*(i+1)],q[4])
    circ.ry(math.pi*key_list[5+36*(i+1)],q[5])
    circ.ry(math.pi*key_list[6+36*(i+1)],q[6])
    circ.ry(math.pi*key_list[7+36*(i+1)],q[7])
    circ.ry(math.pi*key_list[8+36*(i+1)],q[8])
    circ.ry(math.pi*key_list[9+36*(i+1)],q[9])
    circ.ry(math.pi*key_list[10+36*(i+1)],q[10])
    circ.ry(math.pi*key_list[11+36*(i+1)],q[11])
    circ.ry(math.pi*key_list[12+36*(i+1)],q[12])
    circ.ry(math.pi*key_list[13+36*(i+1)],q[13])
    circ.ry(math.pi*key_list[14+36*(i+1)],q[14])
    circ.ry(math.pi*key_list[15+36*(i+1)],q[15])
    circ.ry(math.pi*key_list[16+36*(i+1)],q[16])
    circ.ry(math.pi*key_list[17+36*(i+1)],q[17])
    circ.rz(math.pi*key_list[18+36*(i+1)],q[0])
    circ.rz(math.pi*key_list[19+36*(i+1)],q[1])
    circ.rz(math.pi*key_list[20+36*(i+1)],q[2])
    circ.rz(math.pi*key_list[21+36*(i+1)],q[3])
    circ.rz(math.pi*key_list[22+36*(i+1)],q[4])
    circ.rz(math.pi*key_list[23+36*(i+1)],q[5])
    circ.rz(math.pi*key_list[24+36*(i+1)],q[6])
    circ.rz(math.pi*key_list[25+36*(i+1)],q[7])
    circ.rz(math.pi*key_list[26+36*(i+1)],q[8])
    circ.rz(math.pi*key_list[27+36*(i+1)],q[9])
    circ.rz(math.pi*key_list[28+36*(i+1)],q[10])
    circ.rz(math.pi*key_list[29+36*(i+1)],q[11])
    circ.rz(math.pi*key_list[30+36*(i+1)],q[12])
    circ.rz(math.pi*key_list[31+36*(i+1)],q[13])
    circ.rz(math.pi*key_list[32+36*(i+1)],q[14])
    circ.rz(math.pi*key_list[33+36*(i+1)],q[15])
    circ.rz(math.pi*key_list[34+36*(i+1)],q[16])
    circ.rz(math.pi*key_list[35+36*(i+1)],q[17])

    #確率の計測
    backend_sim = BasicAer.get_backend('statevector_simulator')
    result = execute(circ, backend_sim).result()
    state = result.get_statevector(circ)
    ##print(state)
    prob = np.empty(2**18)

    for j in range(2**18):
        if j%(2**18)<2**17:
            string='0'
        else:
            string='1'
        if j%(2** 17 )<2** 16 :
            string+='0'
        else:
            string+='1'
        if j%(2** 16 )<2** 15 :
            string+='0'
        else:
            string+='1'
        if j%(2** 15 )<2** 14 :
            string+='0'
        else:
            string+='1'
        if j%(2** 14 )<2** 13 :
            string+='0'
        else:
            string+='1'
        if j%(2** 13 )<2** 12 :
            string+='0'
        else:
            string+='1'
        if j%(2** 12 )<2** 11 :
            string+='0'
        else:
            string+='1'
        if j%(2** 11 )<2** 10 :
            string+='0'
        else:
            string+='1'
        if j%(2** 10 )<2** 9 :
            string+='0'
        else:
            string+='1'
        if j%(2** 9 )<2** 8 :
            string+='0'
        else:
            string+='1'
        if j%(2** 8 )<2** 7 :
            string+='0'
        else:
            string+='1'
        if j%(2** 7 )<2** 6 :
            string+='0'
        else:
            string+='1'
        if j%(2** 6 )<2** 5 :
            string+='0'
        else:
            string+='1'
        if j%(2** 5 )<2** 4 :
            string+='0'
        else:
            string+='1'
        if j%(2** 4 )<2** 3 :
            string+='0'
        else:
            string+='1'
        if j%(2** 3 )<2** 2 :
            string+='0'
        else:
            string+='1'
        if j%(2** 2 )<2** 1 :
            string+='0'
        else:
            string+='1'

        if j%2 < 1:
            string += '0'
        else:
            string += '1'
        prob[j] = state_fidelity(basis_state(string,18),state)*10**8%256
        prob[j] = math.floor(prob[j])
        #print(prob[i])
    #print(prob)
    #確率行列を生成するところまで
    #2qubit増えるごとに次元が2倍になる
    #多くとも5000*5000ならば十分かも
    prob_matrix = np.reshape(prob,[2**9,2**9])

    ##確率分布を画像として出してみる
    pil_image = Image.fromarray(prob_matrix.astype(np.uint8))
    ##print(pil_image.mode)
    image_pass = '18qubit_ryrz_images/key_'+str(i)+'.jpg'
    pil_image.save(image_pass,'jpeg')

##pil_image = Image.fromarray(key_matrix.astype(np.uint8))
##print(pil_image.mode)
##pil_image.save('sample_images/key.jpg','jpeg')
##print(key_matrix)
##print(prob_matrix)
##circ.draw(output='mpl')
print('fin')
