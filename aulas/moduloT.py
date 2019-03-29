# modulo para transpor matrices
def transpor(matriz):
    nlinhas = len(matriz)
    ncols = len(matriz[0])
    mtransp = []
    for i in range(0,ncols):
        colunai=[]
        for j in range(0,nlinhas):
            colunai.append(matriz[j][i])
        mtransp.append(colunai)
    return mtransp

if __name__=='__main__':
   B=[[0,1,0],[3,5,8],[12,15,55]]
   print(B)
   print(transpor(B))
