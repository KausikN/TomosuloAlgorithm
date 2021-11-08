'''
Generate Assembly Code for Image Convolution
'''

# Imports


# Main Functions
def PixelConv_CodeGen(ImgSize, WindowSize, i, j, BA_h, BA_x, BA_y):
    code = []
    for m in range(WindowSize[0]):
        for n in range(WindowSize[1]):
            address_h = BA_h + m*WindowSize[0] + n
            address_x = BA_x + (i+WindowSize[0]-1-m)*ImgSize[0] + (j+WindowSize[1]-1-n)
            r_h = 2 + (m*WindowSize[0] + n)*2
            r_x = 2 + (m*WindowSize[0] + n)*2 + 1
            code.append('Ld F' + str(r_h) + ' ' + str(address_h))
            code.append('Ld F' + str(r_x) + ' ' + str(address_x))

    for m in range(WindowSize[0]):
        for n in range(WindowSize[1]):
            r_h = 2 + (m*WindowSize[0] + n)*2
            r_x = 2 + (m*WindowSize[0] + n)*2 + 1
            r_mul = 2 + ((WindowSize[0])*WindowSize[0] + WindowSize[1])*2 + (m*WindowSize[0] + n)
            code.append('FMUL F' + str(r_mul) + ' F' + str(r_h) + ' F' + str(r_x))
    
    for m in range(WindowSize[0]):
        for n in range(WindowSize[1]):
            r_mul = 2 + ((WindowSize[0])*WindowSize[0] + WindowSize[1])*2 + (m*WindowSize[0] + n)
            code.append('FADD F0 F0 F' + str(r_mul))


    # for m in range(WindowSize[0]):
    #     for n in range(WindowSize[1]):
    #         r_h = 2 + (m*WindowSize[0] + n)*2
    #         r_x = 2 + (m*WindowSize[0] + n)*2 + 1
    #         code.append('MUL R1 R' + str(r_h) + ' R' + str(r_x))
    #         code.append('ADD R0 R0 R1')
    address_store = BA_y + i*ImgSize[0] + j
    code.append('Sd F0 ' + str(address_store))
    return code

def Convolution_CodeGen(ImgSize, WindowSize, BA_h, BA_x, BA_y):
    code = []
    for i in range(ImgSize[0]):
        for j in range(ImgSize[1]):
            code.extend(PixelConv_CodeGen(ImgSize, WindowSize, i, j, BA_h, BA_x, BA_y))
    return code

# Driver Code
path = 'MainCode/FloatingConv.s'
ImgSize = (5, 5)
WindowSize = (3, 3)
BA_h = 0
BA_x = 9
BA_y = 34
Code = Convolution_CodeGen(ImgSize, WindowSize, BA_h, BA_x, BA_y)
open(path, 'w').write('\n'.join(Code))