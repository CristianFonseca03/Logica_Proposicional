from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from random import getrandbits
import os

w, h = A4
a = []
b = []
m1 = ''
m2 = []
m3 = []
x_list = []
matriz = []
pdf = 'martriz.pdf'

def main():
    get_conjuntos('conjuntos.txt')
    grid_x_y(7)
    create_PDF()
    # os.popen(pdf)

def fill_matriz(matriz):
    for i in range(5):
        matriz.append([0]*5)
    for i in range(5):
        for j in range(5):
            matriz[i][j] = getrandbits(1)
    print(matriz)

def get_conjuntos(file):
    f = open(file, 'r')
    global a, b, m1, m2, m3
    a = f.readline().replace('\n', '').split(',')
    b = f.readline().replace('\n', '').split(',')
    m1 = f.readline().replace('\n', '')
    m2 = f.readline().replace('\n', '').split(':')
    m3 = f.readline().replace('\n', '').split(':')
    f.close()

def grid_x_y(number):
    a = (w-100)/number
    global x_list
    for i in range(1, number+1):
        x_list.append(a*i)

def table(start, c, matriz, title):
    start_y = start
    y_list = [start_y, start_y-30, start_y-60, start_y -
              90, start_y-120, start_y-150, start_y-180]
    c.grid(x_list, y_list)
    c.drawCentredString(x_list[0]+35, y_list[1]+12, title)
    c.drawCentredString(x_list[1]+35, y_list[1]+12, b[0])
    c.drawCentredString(x_list[2]+35, y_list[1]+12, b[1])
    c.drawCentredString(x_list[3]+35, y_list[1]+12, b[2])
    c.drawCentredString(x_list[4]+35, y_list[1]+12, b[3])
    c.drawCentredString(x_list[5]+35, y_list[1]+12, b[4])

    c.drawCentredString(x_list[0]+35, y_list[2]+12, a[0])
    c.drawCentredString(x_list[1]+35, y_list[2]+12, str(matriz[0][0]))
    c.drawCentredString(x_list[2]+35, y_list[2]+12, str(matriz[0][1]))
    c.drawCentredString(x_list[3]+35, y_list[2]+12, str(matriz[0][2]))
    c.drawCentredString(x_list[4]+35, y_list[2]+12, str(matriz[0][3]))
    c.drawCentredString(x_list[5]+35, y_list[2]+12, str(matriz[0][4]))

    c.drawCentredString(x_list[0]+35, y_list[3]+12, a[1])
    c.drawCentredString(x_list[1]+35, y_list[3]+12, str(matriz[1][0]))
    c.drawCentredString(x_list[2]+35, y_list[3]+12, str(matriz[1][1]))
    c.drawCentredString(x_list[3]+35, y_list[3]+12, str(matriz[1][2]))
    c.drawCentredString(x_list[4]+35, y_list[3]+12, str(matriz[1][3]))
    c.drawCentredString(x_list[5]+35, y_list[3]+12, str(matriz[1][4]))

    c.drawCentredString(x_list[0]+35, y_list[4]+12, a[2])
    c.drawCentredString(x_list[1]+35, y_list[4]+12, str(matriz[2][0]))
    c.drawCentredString(x_list[2]+35, y_list[4]+12, str(matriz[2][1]))
    c.drawCentredString(x_list[3]+35, y_list[4]+12, str(matriz[2][2]))
    c.drawCentredString(x_list[4]+35, y_list[4]+12, str(matriz[2][3]))
    c.drawCentredString(x_list[5]+35, y_list[4]+12, str(matriz[2][4]))

    c.drawCentredString(x_list[0]+35, y_list[5]+12, a[3])
    c.drawCentredString(x_list[1]+35, y_list[5]+12, str(matriz[3][0]))
    c.drawCentredString(x_list[2]+35, y_list[5]+12, str(matriz[3][1]))
    c.drawCentredString(x_list[3]+35, y_list[5]+12, str(matriz[3][2]))
    c.drawCentredString(x_list[4]+35, y_list[5]+12, str(matriz[3][3]))
    c.drawCentredString(x_list[5]+35, y_list[5]+12, str(matriz[3][4]))

    c.drawCentredString(x_list[0]+35, y_list[6]+12, a[4])
    c.drawCentredString(x_list[1]+35, y_list[6]+12, str(matriz[4][0]))
    c.drawCentredString(x_list[2]+35, y_list[6]+12, str(matriz[4][1]))
    c.drawCentredString(x_list[3]+35, y_list[6]+12, str(matriz[4][2]))
    c.drawCentredString(x_list[4]+35, y_list[6]+12, str(matriz[4][3]))
    c.drawCentredString(x_list[5]+35, y_list[6]+12, str(matriz[4][4]))

def create_m2(a, b, matriz):
    mat_2 = []
    m0 = [0, 0, 0, 0, 0]
    m_yes = [0, 0, 0, 0, 0]
    for i in range(5):
        if (matriz[i][a] and matriz[i][b] == 1):
            m_yes[a] = 1
            m_yes[b] = 1
            mat_2.append(m_yes)
        else:
            mat_2.append(m0)
    return mat_2

def create_m3(a, matriz):
    mat_2 = []
    m0 = [0, 0, 0, 0, 0]
    m_yes = [0, 0, 0, 0, 0]
    for i in range(5):
        if (matriz[i][a] == 1):
            m_yes[a] = 1
            mat_2.append(m_yes)
        else:
            mat_2.append(m0)
    return mat_2

def create_m4(a,b,c,matriz):
    mat_2 = []
    m0 = [0, 0, 0, 0, 0]
    m_yes = [0, 0, 0, 0, 0]
    for i in range(5):
        if (matriz[i][a] and matriz[i][b] and matriz[i][c]== 1):
            m_yes[a] = 1
            m_yes[b] = 1
            m_yes[c] = 1
            mat_2.append(m_yes)
        else:
            mat_2.append(m0)
    return mat_2

def create_m5(a,b):
    mat_dif=[]
    for i in range(5):
        mat_dif.append([0]*5)
    for i in range(5):
        for j in range(5):
            if(a[i][j]!=b[i][j]):
                mat_dif[i][j]=1
    print(mat_dif)
    return mat_dif

def create_PDF():
    global x_list, a, b, matriz, m1, m2, m3
    c = canvas.Canvas(pdf)
    # page 1
    c.setFont('Helvetica-Bold', 14)
    c.drawCentredString(w/2, h-60, 'Matematicas discretas')
    c.setFont('Helvetica-Oblique', 12)
    c.drawCentredString(
        w/2, h-80, 'Universidad Pedagogica y Tecnologica de Colombia')
    c.setFont('Helvetica', 12)
    c.drawString(75, h-150, 'A = {'+a[0]+',' +
                 a[1]+','+a[2]+','+a[3]+','+a[4]+'}.')
    c.drawString(75, h-170, 'B = {'+b[0]+',' +
                 b[1]+','+b[2]+','+b[3]+','+b[4]+'}.')
    c.drawString(75, h-190, 'M1(x,y) = '+m1)
    c.drawCentredString(w/2, h-220, 'R1= {(x,y)/x∈A ^ y∈B ^ M1(x,y)}')
    fill_matriz(matriz)
    table(h-240, c, matriz, 'R1')
    c.drawString(75, h-460, 'M2(x,y) = '+m2[0])
    c.drawCentredString(w/2, h-490, 'R2= {(x,y)/x∈A ^ y∈B ^ M2(x,y)}')
    param = m2[1].split(',')
    table(h-510, c, create_m2(int(param[0]), int(param[1]), matriz), 'R2')
    c.showPage()
    # Page 2
    c.setFont('Helvetica-Bold', 14)
    c.drawCentredString(w/2, h-60, 'Matematicas discretas')
    c.setFont('Helvetica-Oblique', 12)
    c.drawCentredString(
        w/2, h-80, 'Universidad Pedagogica y Tecnologica de Colombia')
    c.setFont('Helvetica', 12)
    c.drawString(75, h-150, 'M3 = '+m3[0])
    c.drawCentredString(w/2, h-180, 'R3= {(x,y)/x∈A ^ y∈B ^ M3(x)}')
    table(h-200, c, create_m3(int(m3[1]), matriz), 'R3')
    c.drawString(75, h-440, 'R4 = R2 U R3')
    c.drawCentredString(w/2, h-470, 'R4= {(x,y)/x∈A ^ y∈B ^ (M2(x,y) ^ M3(x))}')
    table(h-500, c, create_m4(int(param[0]), int(param[1]),int(m3[1]), matriz), 'R4')
    c.showPage()
    # Page 3
    c.setFont('Helvetica-Bold', 14)
    c.drawCentredString(w/2, h-60, 'Matematicas discretas')
    c.setFont('Helvetica-Oblique', 12)
    c.drawCentredString(
        w/2, h-80, 'Universidad Pedagogica y Tecnologica de Colombia')
    c.setFont('Helvetica', 12)
    c.drawString(75, h-150, 'R5 = R2 Δ R3')
    c.drawCentredString(w/2, h-180, 'R5= {(x,y)/x∈A ^ y∈B ^ (M2(x,y) v M3(x) ^ ~ (M2(x,y) ^ M3(x)))}')
    table(h-200, c, create_m5(create_m2(int(param[0]), int(param[1]), matriz),create_m3(int(m3[1]), matriz)), 'R5')
    c.save()

if __name__ == "__main__":
    main()
