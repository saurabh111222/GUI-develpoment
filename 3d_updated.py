from Tkinter import *
import pandas as pd
from pandas import DataFrame
import Tkinter
import math
import numpy as np
from sympy import symbols, Eq, solve
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
t = []
d = []
len = []
a = []
b = []
###===========================
dv1 = []
dh1 = []
dn1 = []
de1 = []
v1 = []
h1 = []
n1 = []
e1 = []
###============================
dv2 = []
dh2 = []
dn2 = []
de2 = []
v2 = []
h2 = []
n2 = []
e2 = []
##===========================================
dv3 = []
dh3 = []
dn3 = []
de3 = []
v3 = []
h3 = []
n3 = []
e3 = []
##===========================================
dv4 = []
dh4 = []
dn4 = []
de4 = []
v4 = []
h4 = []
n4 = []
e4 = []
##=================================================
dv5 = []
dh5 = []
dn5 = []
de5 = []
v5 = []
h5 = []
n5 = []
e5 = []

def plot3d(n, e, v,col,well_pro):
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure(figsize=(10, 7))
    ax = fig.gca(projection='3d')
    z = v
    x = n
    y = e
    plt.gca().invert_yaxis()
    plt.gca().invert_zaxis()
    plt.gca().invert_xaxis()
    ax.plot(x, y, z, label='parametric curve',c=col)
    ax.set_xlabel('North')
    ax.set_ylabel('East')
    ax.set_zlabel('Depth')
    style = dict(size=7, color='black')
    ax.text(n[0], e[0], v[0], "KOP", **style)
    ax.text(n[1], e[1], v[1], "MD1", **style)
    ax.text(n[2], e[2], v[2], "MD2", **style)
    ax.text(n[3], e[3], v[3], "MD3", **style)
    ax.text(n[4], e[4], v[4], "MD4", **style)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    ax.tick_params(axis="z", labelsize=8)
    ax.legend([well_pro])
    plt.show()

def drill_survy_calculation():
    pro2 = Tk()
    pro2.geometry("900x400")

    def tengen():
        dv1 = []
        dh1 = []
        dn1 = []
        de1 = []
        v1 = []
        h1 = []
        n1 = []
        e1 = []
        d1 = float(Entry.get(E1))
        d2 = float(Entry.get(E2))
        d3 = float(Entry.get(E3))
        d4 = float(Entry.get(E4))
        d5 = float(Entry.get(E5))
        d6 = float(Entry.get(E6))
        ##==============================================================
        a1 = float(Entry.get(E7))
        a2 = float(Entry.get(E8))
        a3 = float(Entry.get(E9))
        a4 = float(Entry.get(E10))
        a5 = float(Entry.get(E11))
        ##============================================================================
        b1 = float(Entry.get(E12))
        b2 = float(Entry.get(E13))
        b3 = float(Entry.get(E14))
        b4 = float(Entry.get(E15))
        b5 = float(Entry.get(E16))
        kop = d1
        d = [d2, d3, d4, d5, d6]
        l1 = d3 - d2
        l2 = d4 - d3
        l3 = d5 - d4
        l4 = d6 - d5
        phi1 = float((a1 * 100) / (d2 - d1))

        r = 18000 / (math.pi * phi1)
        V1 = kop + r * math.sin(np.radians(a1))
        H1 = r * (1 - math.cos(np.radians(a1)))
        N1 = H1 * math.cos(np.radians(b1))
        Ee1 = H1 * math.sin(np.radians(b1))
        len = [l1, l2, l3, l4]
        a = [a1, a2, a3, a4, a5]
        b = [b1, b2, b3, b4, b5]
        x = 1
        for i in len:
            delv = i * math.cos(np.radians(a[x]))
            delh = i * math.sin(np.radians(a[x]))
            deln = delh * math.cos(np.radians(b[x]))
            dele = delh * math.sin(np.radians(b[x]))
            x = x + 1
            dv1.append(round(delv,2))
            dh1.append(round(delh,2))
            dn1.append(round(deln,2))
            de1.append(round(dele,2))
        ##========================================
        c = 0
        v1.append(round(V1,2))
        for k in dv1:
            f = v1[c] + k
            v1.append(round(f,2))
            c = c + 1
        print("tengen")
        ##========================================
        s = 0
        h1.append(round(H1,2))
        for z in dh1:
            w = h1[s] + z
            h1.append(round(w,2))
            s = s + 1
        print(h1)
        ##========================================
        m = 0
        n1.append(round(N1,2))
        for y in dn1:
            g = n1[m] + y
            n1.append(round(g,2))
            m = m + 1
        print(n1)
        ##========================================
        t = 0
        e1.append(round(Ee1,2))
        for o in de1:
            q = e1[t] + o
            e1.append(round(q,2))
            t = t + 1
        print(e1)
        calculate_traj(v1, h1, n1, e1, dv1, dh1, dn1, de1)
        col = 'r'
        well_pro = "Tengential Method"
        plot3d(n1, e1, v1,col,well_pro)

    def baltengen():
        dv2 = []
        dh2 = []
        dn2 = []
        de2 = []
        v2 = []
        h2 = []
        n2 = []
        e2 = []
        d1 = float(Entry.get(E1))
        d2 = float(Entry.get(E2))
        d3 = float(Entry.get(E3))
        d4 = float(Entry.get(E4))
        d5 = float(Entry.get(E5))
        d6 = float(Entry.get(E6))
        ##==============================================================
        a1 = float(Entry.get(E7))
        a2 = float(Entry.get(E8))
        a3 = float(Entry.get(E9))
        a4 = float(Entry.get(E10))
        a5 = float(Entry.get(E11))
        ##============================================================================
        b1 = float(Entry.get(E12))
        b2 = float(Entry.get(E13))
        b3 = float(Entry.get(E14))
        b4 = float(Entry.get(E15))
        b5 = float(Entry.get(E16))
        kop = d1
        d = [d2, d3, d4, d5, d6]
        l1 = d3 - d2
        l2 = d4 - d3
        l3 = d5 - d4
        l4 = d6 - d5
        phi1 = float((a1 * 100) / (d2 - d1))

        r = 18000 / (math.pi * phi1)
        V1 = kop + r * math.sin(np.radians(a1))
        H1 = r * (1 - math.cos(np.radians(a1)))
        N1 = H1 * math.cos(np.radians(b1))
        Ee1 = H1 * math.sin(np.radians(b1))
        len = [l1, l2, l3, l4]
        a = [a1, a2, a3, a4, a5]
        b = [b1, b2, b3, b4, b5]

        x = 0
        for i in len:
            delv = (i / 2) * (math.cos(np.radians(a[x])) + math.cos(np.radians(a[x + 1])))
            delh = (i / 2) * (math.sin(np.radians(a[x])) + math.sin(np.radians(a[x + 1])))
            deln = (i / 2) * (math.sin(np.radians(a[x])) * math.cos(np.radians(b[x])) + math.sin(
                np.radians(a[x + 1])) * math.cos(np.radians(b[x + 1])))
            dele = (i / 2) * (math.sin(np.radians(a[x])) * math.sin(np.radians(b[x])) + math.sin(
                np.radians(a[x + 1])) * math.sin(np.radians(b[x + 1])))
            x = x + 1
            dv2.append(round(delv,2))
            dh2.append(round(delh,2))
            dn2.append(round(deln,2))
            de2.append(round(dele,2))
        ##========================================
        c = 0
        v2.append(round(V1,2))
        for k in dv2:
            f = v2[c] + k
            v2.append(round(f,2))
            c = c + 1
        print("baltengen")
        print(v2)
        ##========================================
        s = 0
        h2.append(round(H1,2))
        for z in dh2:
            w = h2[s] + z
            h2.append(round(w,2))
            s = s + 1
        print(h2)
        ##========================================
        m = 0
        n2.append(round(N1,2))
        for y in dn2:
            g = n2[m] + y
            n2.append(round(g,2))
            m = m + 1
        print(n2)
        ##========================================
        t = 0
        e2.append(round(Ee1,2))
        for o in de2:
            q = e2[t] + o
            e2.append(round(q,2))
            t = t + 1
        print(e2)
        ######################################################################delv
        calculate_traj(v2, h2, n2, e2, dv2, dh2, dn2, de2)
        col = 'b'
        well_pro = "Balanced Tengential Method"
        plot3d(n2, e2, v2, col, well_pro)

    #######################################################################################
    def avgangl():
        dv3 = []
        dh3 = []
        dn3 = []
        de3 = []
        v3 = []
        h3 = []
        n3 = []
        e3 = []
        d1 = float(Entry.get(E1))
        d2 = float(Entry.get(E2))
        d3 = float(Entry.get(E3))
        d4 = float(Entry.get(E4))
        d5 = float(Entry.get(E5))
        d6 = float(Entry.get(E6))
        ##==============================================================
        a1 = float(Entry.get(E7))
        a2 = float(Entry.get(E8))
        a3 = float(Entry.get(E9))
        a4 = float(Entry.get(E10))
        a5 = float(Entry.get(E11))
        ##============================================================================
        b1 = float(Entry.get(E12))
        b2 = float(Entry.get(E13))
        b3 = float(Entry.get(E14))
        b4 = float(Entry.get(E15))
        b5 = float(Entry.get(E16))
        kop = d1
        d = [d2, d3, d4, d5, d6]
        l1 = d3 - d2
        l2 = d4 - d3
        l3 = d5 - d4
        l4 = d6 - d5
        phi1 = float((a1 * 100) / (d2 - d1))

        r = 18000 / (math.pi * phi1)
        V1 = kop + r * math.sin(np.radians(a1))
        H1 = r * (1 - math.cos(np.radians(a1)))
        N1 = H1 * math.cos(np.radians(b1))
        Ee1 = H1 * math.sin(np.radians(b1))
        len = [l1, l2, l3, l4]
        a = [a1, a2, a3, a4, a5]
        b = [b1, b2, b3, b4, b5]

        x = 0
        for i in len:
            delv = i * math.cos(np.radians((a[x] + a[x + 1]) / 2))
            delh = i * math.sin(np.radians((a[x] + a[x + 1]) / 2))
            deln = delh * math.cos(np.radians((b[x] + b[x + 1]) / 2))
            dele = delh * math.sin(np.radians((b[x] + b[x + 1]) / 2))
            x = x + 1
            dv3.append(round(delv,2))
            dh3.append(round(delh,2))
            dn3.append(round(deln,2))
            de3.append(round(dele,2))
        ##========================================
        c = 0
        v3.append(round(V1,2))
        for k in dv3:
            f = v3[c] + k
            v3.append(round(f,2))
            c = c + 1
        print("avgangl")
        print(v3)
        ##========================================
        s = 0
        h3.append(round(H1,2))
        for z in dh3:
            w = h3[s] + z
            h3.append(round(w,2))
            s = s + 1
        print(h3)
        ##========================================
        m = 0
        n3.append(round(N1,2))
        for y in dn3:
            g = n3[m] + y
            n3.append(round(g,2))
            m = m + 1
        print(n3)
        ##========================================
        t = 0
        e3.append(round(Ee1,2))
        for o in de3:
            q = e3[t] + o
            e3.append(round(q,2))
            t = t + 1
        print(e3)
        ######################################################################delv
        calculate_traj(v3, h3, n3, e3, dv3, dh3, dn3, de3)
        col = 'y'
        well_pro = "Average Angle Method Method"
        plot3d(n3, e3, v3, col, well_pro)
    ##############################################################################################
    def roc():
        dv4 = []
        dh4 = []
        dn4 = []
        de4 = []
        v4 = []
        h4 = []
        n4 = []
        e4 = []
        d1 = float(Entry.get(E1))
        d2 = float(Entry.get(E2))
        d3 = float(Entry.get(E3))
        d4 = float(Entry.get(E4))
        d5 = float(Entry.get(E5))
        d6 = float(Entry.get(E6))
        ##==============================================================
        a1 = float(Entry.get(E7))
        a2 = float(Entry.get(E8))
        a3 = float(Entry.get(E9))
        a4 = float(Entry.get(E10))
        a5 = float(Entry.get(E11))
        ##============================================================================
        b1 = float(Entry.get(E12))
        b2 = float(Entry.get(E13))
        b3 = float(Entry.get(E14))
        b4 = float(Entry.get(E15))
        b5 = float(Entry.get(E16))
        kop = d1
        d = [d2, d3, d4, d5, d6]
        l1 = d3 - d2
        l2 = d4 - d3
        l3 = d5 - d4
        l4 = d6 - d5
        phi1 = float((a1 * 100) / (d2 - d1))

        r = 18000 / (math.pi * phi1)
        V1 = kop + r * math.sin(np.radians(a1))
        H1 = r * (1 - math.cos(np.radians(a1)))
        N1 = H1 * math.cos(np.radians(b1))
        Ee1 = H1 * math.sin(np.radians(b1))
        len = [l1, l2, l3, l4]
        a = [a1, a2, a3, a4, a5]
        b = [b1, b2, b3, b4, b5]

        x = 0
        for i in len:
            delv = ((180 * i) / (math.pi * (a[x + 1] - a[x]))) * (
                    math.sin(np.radians(a[x + 1])) - math.sin(np.radians(a[x])))
            delh = ((180 * i) / (math.pi * (a[x + 1] - a[x]))) * (
                    math.cos(np.radians(a[x])) - math.cos(np.radians(a[x + 1])))

            deln = ((180 * delh) / (math.pi * (b[x + 1] - b[x]))) * (
                    math.sin(np.radians(b[x + 1])) - math.sin(np.radians(b[x])))
            dele = ((180 * delh) / (math.pi * (b[x + 1] - b[x]))) * (
                    math.cos(np.radians(b[x])) - math.cos(np.radians(b[x + 1])))
            x = x + 1
            dv4.append(round(delv,2))
            dh4.append(round(delh,2))
            dn4.append(round(deln,2))
            de4.append(round(dele,2))
        ##========================================
        c = 0
        v4.append(round(V1,2))
        for k in dv4:
            f = v4[c] + k
            v4.append(round(f,2))
            c = c + 1
        print("roc")
        print(v4)
        ##========================================
        s = 0
        h4.append(round(H1,2))
        for z in dh4:
            w = h4[s] + z
            h4.append(round(w,2))
            s = s + 1
        print(h4)
        ##========================================
        m = 0
        n4.append(round(N1,2))
        for y in dn4:
            g = n4[m] + y
            n4.append(round(g,2))
            m = m + 1
        print(n4)
        ##========================================
        t = 0
        e4.append(round(Ee1,2))
        for o in de4:
            q = e4[t] + o
            e4.append(round(q,2))
            t = t + 1
        print(e4)
        ######################################################################delv
        calculate_traj(v4, h4, n4, e4, dv4, dh4, dn4, de4)
        col = 'g'
        well_pro = "Radius of Curvature Method"
        plot3d(n4, e4, v4, col, well_pro)
    def mincurve():
        dv5 = []
        dh5 = []
        dn5 = []
        de5 = []
        v5 = []
        h5 = []
        n5 = []
        e5 = []
        d1 = float(Entry.get(E1))
        d2 = float(Entry.get(E2))
        d3 = float(Entry.get(E3))
        d4 = float(Entry.get(E4))
        d5 = float(Entry.get(E5))
        d6 = float(Entry.get(E6))
        ##==============================================================
        a1 = float(Entry.get(E7))
        a2 = float(Entry.get(E8))
        a3 = float(Entry.get(E9))
        a4 = float(Entry.get(E10))
        a5 = float(Entry.get(E11))
        ##============================================================================
        b1 = float(Entry.get(E12))
        b2 = float(Entry.get(E13))
        b3 = float(Entry.get(E14))
        b4 = float(Entry.get(E15))
        b5 = float(Entry.get(E16))
        kop = d1
        d = [d2, d3, d4, d5, d6]

        phi1 = float((a1 * 100) / (d2 - d1))

        r = 18000 / (math.pi * phi1)
        V1 = kop + r * math.sin(np.radians(a1))
        H1 = r * (1 - math.cos(np.radians(a1)))
        N1 = H1 * math.cos(np.radians(b1))
        Ee1 = H1 * math.sin(np.radians(b1))
        len = [d3 - d2, d4 - d3, d5 - d4, d6 - d5]
        a = [a1, a2, a3, a4, a5]
        b = [b1, b2, b3, b4, b5]

        x = 0
        for i in len:
            dl = round(np.degrees(math.acos(
                math.cos(np.radians(a[x + 1] - a[x])) - math.sin(np.radians(a[x])) * math.sin(np.radians(a[x + 1])) * (
                            1 - math.cos(np.radians(b[x + 1] - b[x]))))), 2)
            rf = (2 / np.radians(dl)) * math.tan(np.radians(dl / 2))
            delv = rf * (i / 2) * (math.cos(np.radians(a[x])) + math.cos(np.radians(a[x + 1])))
            delh = rf * (i / 2) * (math.sin(np.radians(a[x])) + math.sin(np.radians(a[x + 1])))
            deln = rf * (i / 2) * (math.sin(np.radians(a[x])) * math.cos(np.radians(b[x])) + math.sin(
                np.radians(a[x + 1])) * math.cos(np.radians(b[x + 1])))
            dele = rf * (i / 2) * (math.sin(np.radians(a[x])) * math.sin(np.radians(b[x])) + math.sin(
                np.radians(a[x + 1])) * math.sin(np.radians(b[x + 1])))
            x = x + 1
            dv5.append(round(delv,2))
            dh5.append(round(delh,2))
            dn5.append(round(deln,2))
            de5.append(round(dele,2))
        ##========================================
        c = 0
        v5.append(round(V1,2))
        for k in dv5:
            f = v5[c] + k
            v5.append(round(f,2))
            c = c + 1
        print("mincurve")
        print(v5)
        ##========================================
        s = 0
        h5.append(round(H1,2))
        for z in dh5:
            w = h5[s] + z
            h5.append(round(w,2))
            s = s + 1
        print(h5)
        ##========================================
        m = 0
        n5.append(round(N1,2))
        for y in dn5:
            g = n5[m] + y
            n5.append(round(g,2))
            m = m + 1
        print(n5)
        ##========================================
        t = 0
        e5.append(round(Ee1,2))
        for o in de5:
            q = e5[t] + o
            e5.append(round(q,2))
            t = t + 1
        print(e5)
        ######################################################################delv
        calculate_traj(v5, h5, n5, e5, dv5, dh5, dn5, de5)
        col = 'orange'
        well_pro = "Minimum Curvature Method"
        plot3d(n5, e5, v5, col, well_pro)
    ##============================================================================
    L1 = Label(pro2, text="KOP", ).grid(row=1, column=0)
    L2 = Label(pro2, text="MD1", ).grid(row=2, column=0)
    L3 = Label(pro2, text="MD2", ).grid(row=3, column=0)
    L4 = Label(pro2, text="MD3", ).grid(row=4, column=0)
    L5 = Label(pro2, text="MD4", ).grid(row=5, column=0)
    L6 = Label(pro2, text="MD5", ).grid(row=6, column=0)
    U8 = Label(pro2, text="Enter Values Here", ).grid(row=0, column=1)

    E1 = Entry(pro2, bd=5)
    E1.grid(row=1, column=1)
    E2 = Entry(pro2, bd=5)
    E2.grid(row=2, column=1)
    E3 = Entry(pro2, bd=5)
    E3.grid(row=3, column=1)
    E4 = Entry(pro2, bd=5)
    E4.grid(row=4, column=1)
    E5 = Entry(pro2, bd=5)
    E5.grid(row=5, column=1)
    E6 = Entry(pro2, bd=5)
    E6.grid(row=6, column=1)
    ##===========================================================

    L9 = Label(pro2, text="Alpha1", ).grid(row=1, column=2)
    L10 = Label(pro2, text="Alpha2", ).grid(row=2, column=2)
    L11 = Label(pro2, text="Alpha3", ).grid(row=3, column=2)
    L12 = Label(pro2, text="Alpha4", ).grid(row=4, column=2)
    L13 = Label(pro2, text="Alpha5", ).grid(row=5, column=2)
    U9 = Label(pro2, text="Enter Values Here", ).grid(row=0, column=3)

    E7 = Entry(pro2, bd=5)
    E7.grid(row=1, column=3)
    E8 = Entry(pro2, bd=5)
    E8.grid(row=2, column=3)
    E9 = Entry(pro2, bd=5)
    E9.grid(row=3, column=3)
    E10 = Entry(pro2, bd=5)
    E10.grid(row=4, column=3)
    E11 = Entry(pro2, bd=5)
    E11.grid(row=5, column=3)
    ##============================================================================================

    L14 = Label(pro2, text="Beeta1", ).grid(row=1, column=4)
    L15 = Label(pro2, text="Beeta2", ).grid(row=2, column=4)
    L16 = Label(pro2, text="Beeta3", ).grid(row=3, column=4)
    L17 = Label(pro2, text="Beeta4", ).grid(row=4, column=4)
    L18 = Label(pro2, text="Beeta5", ).grid(row=5, column=4)
    U10 = Label(pro2, text="Enter Values Here", ).grid(row=0, column=5)

    E12 = Entry(pro2, bd=5)
    E12.grid(row=1, column=5)
    E13 = Entry(pro2, bd=5)
    E13.grid(row=2, column=5)
    E14 = Entry(pro2, bd=5)
    E14.grid(row=3, column=5)
    E15 = Entry(pro2, bd=5)
    E15.grid(row=4, column=5)
    E16 = Entry(pro2, bd=5)
    E16.grid(row=5, column=5)
    ##==========================================
    L24 = Label(pro2, text="Del V", ).grid(row=0, column=7)
    L24 = Label(pro2, text="Del H", ).grid(row=0, column=8)
    L25 = Label(pro2, text="Del N", ).grid(row=0, column=9)
    L26 = Label(pro2, text="Del E", ).grid(row=0, column=10)
    L27 = Label(pro2, text="V", ).grid(row=6, column=7)
    L29 = Label(pro2, text="N", ).grid(row=6, column=9)
    L28 = Label(pro2, text="H", ).grid(row=6, column=8)
    L30 = Label(pro2, text="E", ).grid(row=6, column=10)
    ##==========================================

    def calculate_traj(v,h,n,e,dv,dh,dn,de):
        L13 = Label(pro2, text=v[0],bg="white").grid(row=7, column=7)
        L14 = Label(pro2, text=v[1],bg="white").grid(row=8, column=7)
        L15 = Label(pro2, text=v[2],bg="white").grid(row=9, column=7)
        L16 = Label(pro2, text=v[3],bg="white").grid(row=10, column=7)
        L17 = Label(pro2, text=v[4],bg="white").grid(row=11, column=7)
        L20 = Label(pro2, text=h[0],bg="white").grid(row=7, column=8)
        L21 = Label(pro2, text=h[1],bg="white").grid(row=8, column=8)
        L22 = Label(pro2, text=h[2],bg="white").grid(row=9, column=8)
        L23 = Label(pro2, text=h[3],bg="white").grid(row=10, column=8)
        L24 = Label(pro2, text=h[4],bg="white").grid(row=11, column=8)
        L27 = Label(pro2, text=n[0],bg="white").grid(row=7, column=9)
        L28 = Label(pro2, text=n[1],bg="white").grid(row=8, column=9)
        L29 = Label(pro2, text=n[2],bg="white").grid(row=9, column=9)
        L30 = Label(pro2, text=n[3],bg="white").grid(row=10, column=9)
        L31 = Label(pro2, text=n[4],bg="white").grid(row=11, column=9)
        L34 = Label(pro2, text=e[0],bg="white").grid(row=7, column=10)
        L35 = Label(pro2, text=e[1],bg="white").grid(row=8, column=10)
        L36 = Label(pro2, text=e[2],bg="white").grid(row=9, column=10)
        L37 = Label(pro2, text=e[3],bg="white").grid(row=10, column=10)
        L38 = Label(pro2, text=e[4],bg="white").grid(row=11, column=10)
        L13 = Label(pro2, text=dv[0],bg="white").grid(row=1, column=7)
        L14 = Label(pro2, text=dv[1],bg="white").grid(row=2, column=7)
        L15 = Label(pro2, text=dv[2],bg="white").grid(row=3, column=7)
        L16 = Label(pro2, text=dv[3],bg="white").grid(row=4, column=7)
        L20 = Label(pro2, text=dh[0],bg="white").grid(row=1, column=8)
        L21 = Label(pro2, text=dh[1],bg="white").grid(row=2, column=8)
        L22 = Label(pro2, text=dh[2],bg="white").grid(row=3, column=8)
        L23 = Label(pro2, text=dh[3],bg="white").grid(row=4, column=8)
        L27 = Label(pro2, text=dn[0],bg="white").grid(row=1, column=9)
        L28 = Label(pro2, text=dn[1],bg="white").grid(row=2, column=9)
        L29 = Label(pro2, text=dn[2],bg="white").grid(row=3, column=9)
        L30 = Label(pro2, text=dn[3],bg="white").grid(row=4, column=9)
        L34 = Label(pro2, text=de[0],bg="white").grid(row=1, column=10)
        L35 = Label(pro2, text=de[1],bg="white").grid(row=2, column=10)
        L36 = Label(pro2, text=de[2],bg="white").grid(row=3, column=10)
        L37 = Label(pro2, text=de[3],bg="white").grid(row=4, column=10)

    B1 = Button(pro2, text="Tengential Method", command=tengen, activebackground="grey",
                activeforeground="yellow").grid(row=1, column=6)
    B2 = Button(pro2, text="Balanced Tengential Method", command=baltengen, activebackground="grey",
                activeforeground="yellow").grid(row=2, column=6)
    B3 = Button(pro2, text="Average Angle Method", command=avgangl, activebackground="grey",
                activeforeground="yellow").grid(row=3, column=6)
    B4 = Button(pro2, text="Radius of Curvature Method", command=roc, activebackground="grey",
                activeforeground="yellow").grid(row=4, column=6)
    B5 = Button(pro2, text="Minimum Curvature Method", command=mincurve, activebackground="grey",
                activeforeground="yellow").grid(row=5, column=6)
    pro2.mainloop()


def help():
    help = Tk()
    h = Label(help, text="Saurabh is working on these calculation. Please try after some time.", width=300, height=300,
              font=('arial 20 bold')).pack()
    help.mainloop()




def roc(phi):
    R = round(18000 / (math.pi * phi), 2)
    return R


def targetHandBeta(Et, Es, Nt, Ns):
    Ht = round(((Et - Es) ** 2 + (Nt - Ns) ** 2) ** 0.5, 2)
    beta = np.arctan((Et - Es) / (Nt - Ns))
    return Ht, beta


def proces1():
    top = Tk()
    top.geometry("650x330")
    top.title("TYPE 1 PROFILE")

    L1 = Label(top, text="TYPE 1 PROFILE", bd=7, relief=RAISED, padx=15).grid(row=0, column=0)
    L2 = Label(top, text="Ns", ).grid(row=1, column=0)
    L3 = Label(top, text="Nt", ).grid(row=2, column=0)
    L4 = Label(top, text="Es", ).grid(row=3, column=0)
    L5 = Label(top, text="Et", ).grid(row=4, column=0)
    L6 = Label(top, text="Vb", ).grid(row=5, column=0)
    L7 = Label(top, text="Vt", ).grid(row=6, column=0)
    L8 = Label(top, text="Phi", ).grid(row=7, column=0)
    # l9 = Label(top, text="Press Submit...", ).grid(row=8, column=1)
    L9 = Label(top, text="A", ).grid(row=1, column=2)
    L10 = Label(top, text="B", ).grid(row=2, column=2)
    L11 = Label(top, text="C", ).grid(row=3, column=2)
    L12 = Label(top, text="T", ).grid(row=4, column=2)
    L13 = Label(top, text="V", ).grid(row=0, column=3)
    L14 = Label(top, text="H", ).grid(row=0, column=4)
    L15 = Label(top, text="MD", ).grid(row=0, column=5)
    L16 = Label(top, text="Enter Values Here").grid(row=0, column=1)

    e1 = Entry(top, bd=5)
    e1.grid(row=1, column=1)
    e2 = Entry(top, bd=5)
    e2.grid(row=2, column=1)
    e3 = Entry(top, bd=5)
    e3.grid(row=3, column=1)
    e4 = Entry(top, bd=5)
    e4.grid(row=4, column=1)
    e5 = Entry(top, bd=5)
    e5.grid(row=5, column=1)
    e6 = Entry(top, bd=5)
    e6.grid(row=6, column=1)
    e7 = Entry(top, bd=5)
    e7.grid(row=7, column=1)

    def getData():
        Ns = float(Entry.get(e1))
        Nt = float(Entry.get(e2))
        Es = float(Entry.get(e3))
        Et = float(Entry.get(e4))
        Vb = float(Entry.get(e5))
        Vt = float(Entry.get(e6))
        phi = float(Entry.get(e7))
        Hb = 0
        MDb = Vb
        R = roc(phi)
        Ht, beta = targetHandBeta(Et, Es, Nt, Ns)
        X = round(np.degrees(np.arctan((Ht - R) / (Vt - Vb))), 2)
        c = math.cos(math.radians(X))
        Yrad = np.arcsin(R * c / (Vt - Vb))
        Y = round(np.degrees(Yrad), 2)
        # round(Y, 2)
        alpha = round(X + Y)
        Vc = round(Vb + (R * math.sin(np.radians(alpha))), 2)
        Hc = round(R * (1 - math.cos(np.radians(alpha))), 2)
        MDc = round(Vb + ((alpha / phi) * 100), 2)
        MDt = round(MDc + (Vt - Vc) / math.cos(math.radians(alpha)), 2)

        return Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc

    def calcTrajectory(measuredDepth):
        Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
        h = []
        v = []
        nx = []
        ex = []
        for d in measuredDepth:
            if d < Vb:
                alpha1 = 0
                Vx = d
                Hx = 0
                Nx = Ns
                Ex = Es
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif Vb <= d and d <= MDc:
                L = d - Vb
                x = math.radians(L * phi / 100)
                Vx = round(Vb + R * math.sin(x), 2)
                Hx = round(R * (1 - math.cos(x)), 2)
                Nx = round(Ns + Hx * math.cos(beta), 2)
                Ex = round(Es + Hx * math.sin(beta), 2)
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDc < d and d <= MDt:
                L = d - MDc
                y = math.radians(alpha)
                vx = round(Vc + L * math.cos(y), 2)
                hx = round(Hc + L * math.sin(y), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDt < d:
                s = "out of range"
                v.append(s)
                h.append(s)
                nx.append(s)
                ex.append(s)

        return h, v, nx, ex

    def proces2():
        Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
        L19 = Label(top, text=str(0)).grid(row=1, column=3)
        L20 = Label(top, text=str(0)).grid(row=1, column=4)
        L21 = Label(top, text=str(0)).grid(row=1, column=5)

        L22 = Label(top, text=str(Vb)).grid(row=2, column=3)
        L23 = Label(top, text=str(0)).grid(row=2, column=4)
        L24 = Label(top, text=str(Vb)).grid(row=2, column=5)

        L25 = Label(top, text=str(Vc)).grid(row=3, column=3)
        L26 = Label(top, text=str(Hc)).grid(row=3, column=4)
        L27 = Label(top, text=str(MDc)).grid(row=3, column=5)

        L34 = Label(top, text=str(Vt)).grid(row=4, column=3)
        L35 = Label(top, text=str(Ht)).grid(row=4, column=4)
        L36 = Label(top, text=str(MDt)).grid(row=4, column=5)

    def showgraph():
        Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        h2 = []
        v2 = []
        # print(np.linspace(0, MDt, num = 50))
        Ha = 0
        Va = 0
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        h1 = [Ha, Hb, Hc, Ht]
        v1 = [Va, Vb, Vc, Vt]
        data = np.array([h1, v1])
        data_trans = data.transpose()
        df = DataFrame(data_trans)
        print(df)

        a.plot(h2, list(np.negative(v2)))
        a.scatter(df[0], np.negative(df[1]), color='g')
        # a1.annotate('Well Head',xy=(Hb,Vb))
        style = dict(size=10, color='black')
        a.text(Ha + 50, np.negative(Va), "(A) Well Head", **style)
        a.text(Hb + 50, np.negative(Vb), "(B) Kick off point", **style)
        a.text(Hc + 50, np.negative(Vc), "(C) Drop off point", **style)
        a.text(Ht - 55, np.negative(Vt), "Targate point (T)", **style)
        a.legend(['Well Trajectory', 'Points'])
        a.set_xlabel('Horizontal Distance')
        a.set_ylabel('True Vertical Depth')
        a.set_title('Build and Hold Profile')
        graph = Tk()
        graph.title('Well Trajectory')
        graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        # ============================================================

    def show3d():
        Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
        Ha = 0
        Va = 0
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure(figsize=(10, 7))
        ax = fig.gca(projection='3d')
        z = v2
        x = nx
        y = ex
        plt.gca().invert_yaxis()
        plt.gca().invert_zaxis()
        ax.plot(x, y, z, label='parametric curve')
        ax.set_xlabel('North')
        ax.set_ylabel('East')
        ax.set_zlabel('Depth')
        Ha = 0
        Va = 0
        Nb = round(Ns + Hb * math.cos(beta), 2)
        Eb = round(Es + Hb * math.sin(beta), 2)
        Nc = round(Ns + Hc * math.cos(beta), 2)
        Ec = round(Es + Hc * math.sin(beta), 2)
        Nt = round(Ns + Ht * math.cos(beta), 2)
        Et = round(Es + Ht * math.sin(beta), 2)
        style = dict(size=7, color='black')
        ax.text(Ns, Es, Va, "(A) Well Head", **style)
        ax.text(Nb, Eb, Vb, "(B) Kick off point", **style)
        ax.text(Nc, Ec, Vc, "(C) Drop off point", **style)
        ax.text(Nt, Et, Vt, "Targate point (T)", **style)
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="z", labelsize=8)
        ax.legend(['Well Profile'])
        plt.show()
        # ============================================================

    def proces3():
        pro2 = Tk()
        pro2.geometry("600x400")
        # print('here')

        L1 = Label(pro2, text="Vx").grid(row=0, column=2)
        L2 = Label(pro2, text="MDx1").grid(row=1, column=0)
        L3 = Label(pro2, text="MDx2").grid(row=2, column=0)
        L4 = Label(pro2, text="MDx3").grid(row=3, column=0)
        L5 = Label(pro2, text="MDx4").grid(row=4, column=0)
        L6 = Label(pro2, text="MDx5").grid(row=5, column=0)
        L7 = Label(pro2, text="MDx6").grid(row=6, column=0)
        L8 = Label(pro2, text="MDx7").grid(row=7, column=0)
        Ll = Label(pro2, text="(MDx should be less than MDt)").grid(row=8, column=0)
        L9 = Label(pro2, text="Enter Values Here").grid(row=0, column=1)
        L10 = Label(pro2, text="Hx").grid(row=0, column=3)
        L11 = Label(pro2, text="Nx").grid(row=0, column=4)
        L12 = Label(pro2, text="Ex").grid(row=0, column=5)

        # L9 = Label(top, text="<----Press Here", ).grid(row=18, column=1)

        E1 = Entry(pro2, bd=5)
        E1.grid(row=1, column=1)
        E2 = Entry(pro2, bd=5)
        E2.grid(row=2, column=1)
        E3 = Entry(pro2, bd=5)
        E3.grid(row=3, column=1)
        E4 = Entry(pro2, bd=5)
        E4.grid(row=4, column=1)
        E5 = Entry(pro2, bd=5)
        E5.grid(row=5, column=1)
        E6 = Entry(pro2, bd=5)
        E6.grid(row=6, column=1)
        E7 = Entry(pro2, bd=5)
        E7.grid(row=7, column=1)

        def getMD():
            #           print('inside')

            d1 = float(Entry.get(E1))
            d2 = float(Entry.get(E2))
            d3 = float(Entry.get(E3))
            d4 = float(Entry.get(E4))
            d5 = float(Entry.get(E5))
            d6 = float(Entry.get(E6))
            d7 = float(Entry.get(E7))

            depth = [d1, d2, d3, d4, d5, d6, d7]
            return depth

        def submit():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
            L13 = Label(pro2, text=v[0]).grid(row=1, column=2)
            L14 = Label(pro2, text=v[1]).grid(row=2, column=2)
            L15 = Label(pro2, text=v[2]).grid(row=3, column=2)
            L16 = Label(pro2, text=v[3]).grid(row=4, column=2)
            L17 = Label(pro2, text=v[4]).grid(row=5, column=2)
            L18 = Label(pro2, text=v[5]).grid(row=6, column=2)
            L19 = Label(pro2, text=v[6]).grid(row=7, column=2)

            L20 = Label(pro2, text=h[0]).grid(row=1, column=3)
            L21 = Label(pro2, text=h[1]).grid(row=2, column=3)
            L22 = Label(pro2, text=h[2]).grid(row=3, column=3)
            L23 = Label(pro2, text=h[3]).grid(row=4, column=3)
            L24 = Label(pro2, text=h[4]).grid(row=5, column=3)
            L25 = Label(pro2, text=h[5]).grid(row=6, column=3)
            L26 = Label(pro2, text=h[6]).grid(row=7, column=3)

            L27 = Label(pro2, text=nx[0]).grid(row=1, column=4)
            L28 = Label(pro2, text=nx[1]).grid(row=2, column=4)
            L29 = Label(pro2, text=nx[2]).grid(row=3, column=4)
            L30 = Label(pro2, text=nx[3]).grid(row=4, column=4)
            L31 = Label(pro2, text=nx[4]).grid(row=5, column=4)
            L32 = Label(pro2, text=nx[5]).grid(row=6, column=4)
            L33 = Label(pro2, text=nx[6]).grid(row=7, column=4)

            L34 = Label(pro2, text=ex[0]).grid(row=1, column=5)
            L35 = Label(pro2, text=ex[1]).grid(row=2, column=5)
            L36 = Label(pro2, text=ex[2]).grid(row=3, column=5)
            L37 = Label(pro2, text=ex[3]).grid(row=4, column=5)
            L38 = Label(pro2, text=ex[4]).grid(row=5, column=5)
            L39 = Label(pro2, text=ex[5]).grid(row=6, column=5)
            L40 = Label(pro2, text=ex[6]).grid(row=7, column=5)

            B1 = Button(pro2, text="Save Data", command=final, activebackground="grey", activeforeground="yellow").grid(
                row=10, column=1)

        def final():
            Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)

            data = np.array(
                [[0, 0, 0, '', 'MDx1', v[0], h[0], nx[0], ex[0]], [Vb, Hb, MDb, '', 'MDx2', v[1], h[1], nx[1], ex[1]],
                 [Vc, Hc, MDc, '', 'MDx3', v[2], h[2], nx[2], ex[2]],
                 [Vt, Ht, MDt, '', 'MDx4', v[3], h[3], nx[3], ex[3]],
                 ['', '', '', '', 'MDx5', v[4], h[4], nx[4], ex[4]], ['', '', '', '', 'MDx6', v[5], h[5], nx[5], ex[5]],
                 ['', '', '', '', 'MDx7', v[6], h[6], nx[6], ex[6]]])
            finaldata = DataFrame(data, columns=['V', 'H', 'MD', '', 'Entered MD', 'V', 'H', 'N', 'E'],
                                  index=['A', 'B', 'C', 'T', '', '', ''])
            # np.savetxt('C:\Users\sk314\Documents\Profile_1_text.txt', data, delimiter=',')
            finaldata.to_csv('C:\Users\sk314\Documents\Profile_1.csv', index_label='Points')
            L40 = Label(pro2, text="Data has been Saved\n Check Document File").grid(row=11, column=1)
            print('finaldata')
            print(finaldata)

        def showgf():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            Ns, Es, Vb, Hb, MDb, Vt, phi, R, Ht, beta, alpha, Vc, Hc, MDt, MDc = getData()
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a1 = f.add_subplot(111)
            h1 = []
            v1 = []
            h2 = []
            v2 = []
            # print(np.linspace(0, MDt, num = 50))
            h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
            h1, v1, nx, ex = calcTrajectory(list(np.linspace(depth[0], depth[6], num=7)))
            data = np.array([h1, v1])
            data_trans = data.transpose()
            df = DataFrame(data_trans)
            print(df)

            a.plot(h2, list(np.negative(v2)))
            a1.scatter(df[0], np.negative(df[1]), color='r')
            style = dict(size=10, color='black')
            a1.text(h1[0] + 80, np.negative(v1[0]), "MDx1", **style)
            a1.text(h1[1] + 80, np.negative(v1[1]), "MDx2", **style)
            a1.text(h1[2] + 80, np.negative(v1[2]), "MDx3", **style)
            a1.text(h1[3] + 80, np.negative(v1[3]), "MDx4", **style)
            a1.text(h1[4] + 80, np.negative(v1[4]), "MDx5", **style)
            a1.text(h1[5] + 80, np.negative(v1[5]), "MDx6", **style)
            a1.text(h1[6] + 80, np.negative(v1[6]), "MDx7", **style)

            a1.legend(['Well Trajectory', 'Entered MDx'])
            a.set_xlabel('Horizontal Distance')
            a.set_ylabel('True Vertical Depth')
            a.set_title('Build and Hold Profile')
            graph = Tk()
            graph.title('Well Trajectory')
            graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))

            canvas = FigureCanvasTkAgg(f, graph)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

            # toolbar = NavigationToolbar2TkAgg(canvas, self)
            # toolbar.update()
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        B = Button(pro2, text="Submit", command=submit, activebackground="grey", activeforeground="yellow").grid(row=8,
                                                                                                                 column=1)
        B = Button(pro2, text="Show Graph", command=showgf, activebackground="grey", activeforeground="yellow").grid(
            row=9, column=1)

        pro2.mainloop()

    B1 = Button(top, text="Submit", command=proces2, activebackground="grey", activeforeground="yellow").grid(row=8,
                                                                                                              column=1)
    B2 = Button(top, text="Press to calculate trajectory at different depths", command=proces3, activebackground="grey",
                activeforeground="yellow").grid(row=12, column=1)
    B3 = Button(top, text="Show 2D Graph", command=showgraph, activebackground="grey", activeforeground="yellow").grid(
        row=11, column=1)
    B3 = Button(top, text="Show 3D Graph", command=show3d, activebackground="grey", activeforeground="yellow").grid(
        row=10, column=1)
    top.mainloop()


def proces5():
    top = Tk()
    top.geometry("660x450")
    top.title("TYPE 2 PROFILE")

    L1 = Label(top, text="TYPE 2 PROFILE", bd=7, relief=RAISED, padx=20, width=10).grid(row=0, column=0)
    L19 = Label(top, text="Ns", ).grid(row=1, column=0)
    L20 = Label(top, text="Es", ).grid(row=2, column=0)
    L21 = Label(top, text="Nt", ).grid(row=3, column=0)
    L22 = Label(top, text="Et", ).grid(row=4, column=0)
    # L2 = Label(top, text="Ht", ).grid(row=5, column=0)
    L3 = Label(top, text="Vt", ).grid(row=5, column=0)
    L4 = Label(top, text="Ve", ).grid(row=6, column=0)
    L5 = Label(top, text="phi1", ).grid(row=7, column=0)
    L6 = Label(top, text="phi2", ).grid(row=8, column=0)
    L7 = Label(top, text="Vb", ).grid(row=9, column=0)
    L8 = Label(top, text="Alpha2", ).grid(row=10, column=0)
    # l9 = Label(top, text="Press Submit...", ).grid(row=8, column=1)
    L9 = Label(top, text="A", ).grid(row=1, column=2)
    L10 = Label(top, text="B", ).grid(row=2, column=2)
    L11 = Label(top, text="C", ).grid(row=3, column=2)
    L12 = Label(top, text="D", ).grid(row=4, column=2)
    L13 = Label(top, text="E", ).grid(row=5, column=2)
    L14 = Label(top, text="T", ).grid(row=6, column=2)

    L15 = Label(top, text="Enter Values Here").grid(row=0, column=1)

    L16 = Label(top, text="V", ).grid(row=0, column=3)
    L17 = Label(top, text="H", ).grid(row=0, column=4)
    L18 = Label(top, text="MD", ).grid(row=0, column=5)

    z8 = Entry(top, bd=5)
    z8.grid(row=1, column=1)
    z9 = Entry(top, bd=5)
    z9.grid(row=2, column=1)
    z10 = Entry(top, bd=5)
    z10.grid(row=3, column=1)
    z11 = Entry(top, bd=5)
    z11.grid(row=4, column=1)

    # z1 = Entry(top, bd=5)
    # z1.grid(row=5, column=1)
    z2 = Entry(top, bd=5)
    z2.grid(row=5, column=1)
    z3 = Entry(top, bd=5)
    z3.grid(row=6, column=1)
    z4 = Entry(top, bd=5)
    z4.grid(row=7, column=1)
    z5 = Entry(top, bd=5)
    z5.grid(row=8, column=1)
    z6 = Entry(top, bd=5)
    z6.grid(row=9, column=1)
    z7 = Entry(top, bd=5)
    z7.grid(row=10, column=1)

    def getData():
        Ns = float(Entry.get(z8))
        Es = float(Entry.get(z9))
        Nt = float(Entry.get(z10))
        Et = float(Entry.get(z11))
        # Ht = float(Entry.get(z1))
        Vt = float(Entry.get(z2))
        Ve = float(Entry.get(z3))
        phi1 = float(Entry.get(z4))
        phi2 = float(Entry.get(z5))
        Vb = float(Entry.get(z6))
        alpha2 = np.radians(float(Entry.get(z7)))
        Ht, beta = targetHandBeta(Et, Es, Nt, Ns)
        R1 = roc(phi1)
        R2 = roc(phi2)
        OQ = round(Ht - R1 - R2 * math.cos(alpha2) - (Vt - Ve) * math.tan(alpha2), 2)
        OP = round(Ve - Vb + R2 * math.sin(alpha2), 2)
        QS = R1 + R2
        PQ = round(math.sqrt(OP ** 2 + OQ ** 2), 2)
        PS = round(math.sqrt(PQ ** 2 - QS ** 2), 2)
        x = round(math.atan(OQ / OP), 2)
        y = round(math.atan(QS / PS), 2)
        alpha1 = x + y
        print((alpha1))
        # alpha1Deg = math.degrees(alpha1)
        CD = PS

        Vc = round(Vb + R1 * math.sin(alpha1), 2)
        Hc = round(R1 * (1 - math.cos(alpha1)), 2)
        MDc = round((np.degrees(alpha1) / phi1) * 100 + Vb, 2)
        Vd = round(Vc + CD * math.cos(alpha1), 2)
        Hd = round(Hc + CD * math.sin(alpha1), 2)
        MDd = round(MDc + CD, 2)
        He = round(Hd + R2 * (math.cos(alpha2) - math.cos(alpha1)), 2)
        MDe = round(MDd + ((np.degrees(alpha1) - np.degrees(alpha2)) / phi2) * 100, 2)
        MDt = round(MDe + (Vt - Ve) / math.cos(alpha2), 2)

        return Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et

    def calcTrajectory(measuredDepth):
        Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et = getData()
        h = []
        v = []
        nx = []
        ex = []

        for d in measuredDepth:
            if d <= Vb:
                # alpha1 = 0
                Vx = d
                Hx = 0
                Nx = Ns
                Ex = Es
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif Vb < d and d <= MDc:  # buildup
                L = d - Vb
                x = math.radians(L * phi1 / 100)
                Vx = round(Vb + R1 * math.sin(x), 2)
                Hx = round(R1 * (1 - math.cos(x)), 2)
                Nx = round(Ns + Hx * math.cos(beta), 2)
                Ex = round(Es + Hx * math.sin(beta), 2)
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDc < d and d <= MDd:  # holdup
                L = d - MDc
                # y = alpha1
                vx = round(Vc + L * math.cos(alpha1), 2)
                hx = round(Hc + L * math.sin(alpha1), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDd < d and d <= MDe:  # dropup
                L = d - MDd
                z = math.radians(L * phi2 / 100)
                vx = round(Vd + R2 * (math.sin(alpha1) - math.sin(alpha1 - z)), 2)
                hx = round(Hd + R2 * (math.cos(alpha1 - z) - math.cos(alpha1)), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDe < d and d <= MDt:
                L = d - MDe
                vx = round(Ve + L * (math.cos(alpha2)), 2)
                hx = round(He + L * (math.sin(alpha2)), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)
            elif MDt < d:
                s = "out of range"
                v.append(s)
                h.append(s)
                nx.append(s)
                ex.append(s)
        return h, v, nx, ex

    def process2():
        Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et = getData()

        L19 = Label(top, text=str(0)).grid(row=1, column=3)
        L20 = Label(top, text=str(0)).grid(row=1, column=4)
        L21 = Label(top, text=str(0)).grid(row=1, column=5)

        L22 = Label(top, text=str(Vb)).grid(row=2, column=3)
        L23 = Label(top, text=str(0)).grid(row=2, column=4)
        L24 = Label(top, text=str(Vb)).grid(row=2, column=5)

        L25 = Label(top, text=str(Vc)).grid(row=3, column=3)
        L26 = Label(top, text=str(Hc)).grid(row=3, column=4)
        L27 = Label(top, text=str(MDc)).grid(row=3, column=5)

        L28 = Label(top, text=str(Vd)).grid(row=4, column=3)
        L29 = Label(top, text=str(Hd)).grid(row=4, column=4)
        L30 = Label(top, text=str(MDd)).grid(row=4, column=5)

        L31 = Label(top, text=str(Ve)).grid(row=5, column=3)
        L32 = Label(top, text=str(He)).grid(row=5, column=4)
        L33 = Label(top, text=str(MDe)).grid(row=5, column=5)

        L34 = Label(top, text=str(Vt)).grid(row=6, column=3)
        L35 = Label(top, text=str(Ht)).grid(row=6, column=4)
        L36 = Label(top, text=str(MDt)).grid(row=6, column=5)

    def showgraph():
        Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et = getData()
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a1 = f.add_subplot(111)
        h2 = []
        v2 = []
        # print(np.linspace(0, MDt, num = 50))
        Ha = 0
        Hb = 0
        Va = 0
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        h1 = [Ha, Hb, Hc, Hd, He, Ht]
        v1 = [Va, Vb, Vc, Vd, Ve, Vt]
        data = np.array([h1, v1])
        data_trans = data.transpose()
        df = DataFrame(data_trans)
        print(df)
        a.plot(h2, list(np.negative(v2)))
        a1.scatter(df[0], np.negative(df[1]), color='g')
        # a1.annotate('Well Head',xy=(Hb,Vb))
        style = dict(size=10, color='black')
        a1.text(Ha, np.negative(Va), "(A) Well Head", **style)
        a1.text(Hb, np.negative(Vb), "(B) Kick off point", **style)
        a1.text(Hc, np.negative(Vc), "(C) Drop off point", **style)
        a1.text(Hd, np.negative(Vd), "(D) Drop up point", **style)
        a1.text(He, np.negative(Ve), "(E) Drop off point", **style)
        a1.text(Ht, np.negative(Vt), "Targate point (T)", **style)
        a1.legend(['Well Trajectory', 'Points'])
        a.set_xlabel('Horizontal Distance')
        a.set_ylabel('True Vertical Depth')
        a.set_title('Build,Hold and Drop Profile')
        graph = Tk()
        graph.title('Well Trajectory')
        graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))

        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        # =========================================================

    def show3d():
        Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et = getData()
        Ha = 0
        Hb = 0
        Va = 0
        h2 = []
        v2 = []
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure(figsize=(10, 7))
        ax = fig.gca(projection='3d')
        z = v2
        x = nx
        y = ex
        plt.gca().invert_yaxis()
        plt.gca().invert_zaxis()
        ax.plot(x, y, z, label='parametric curve')
        ax.set_xlabel('North')
        ax.set_ylabel('East')
        ax.set_zlabel('Depth')
        Ha = 0
        Va = 0
        Nb = round(Ns + Hb * math.cos(beta), 2)
        Eb = round(Es + Hb * math.sin(beta), 2)
        Nc = round(Ns + Hc * math.cos(beta), 2)
        Ec = round(Es + Hc * math.sin(beta), 2)
        Nd = round(Ns + Hd * math.cos(beta), 2)
        Ed = round(Es + Hd * math.sin(beta), 2)
        Ne = round(Ns + He * math.cos(beta), 2)
        Ee = round(Es + He * math.sin(beta), 2)
        Nt = round(Ns + Ht * math.cos(beta), 2)
        Et = round(Es + Ht * math.sin(beta), 2)
        style = dict(size=7, color='black')
        ax.text(Ns, Es, Va, "(A) Well Head", **style)
        ax.text(Nb, Eb, Vb, "(B) Kick off point", **style)
        ax.text(Nc, Ec, Vc, "(C) Drop off point", **style)
        ax.text(Nd, Ed, Vd, "(D) Drop up point", **style)
        ax.text(Ne, Ee, Ve, "(E) Drop off point", **style)
        ax.text(Nt, Et, Vt, "Targate point (T)", **style)

        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="z", labelsize=8)
        ax.legend(['Well Profile'])
        plt.show()

    def process3():
        pro2 = Tk()
        pro2.geometry("600x450")
        # print('here')

        L1 = Label(pro2, text="Vx").grid(row=0, column=2)
        L2 = Label(pro2, text="MDx1").grid(row=1, column=0)
        L3 = Label(pro2, text="MDx2").grid(row=2, column=0)
        L4 = Label(pro2, text="MDx3").grid(row=3, column=0)
        L5 = Label(pro2, text="MDx4").grid(row=4, column=0)
        L6 = Label(pro2, text="MDx5").grid(row=5, column=0)
        L7 = Label(pro2, text="MDx6").grid(row=6, column=0)
        L8 = Label(pro2, text="MDx7").grid(row=7, column=0)
        Ll8 = Label(pro2, text="(MDx should be less than MDt)").grid(row=8, column=0)
        L9 = Label(pro2, text="Enter Values Here").grid(row=0, column=1)
        L10 = Label(pro2, text="Hx").grid(row=0, column=3)
        L11 = Label(pro2, text="Nx").grid(row=0, column=4)
        L12 = Label(pro2, text="Ex").grid(row=0, column=5)

        # L9 = Label(top, text="<----Press Here", ).grid(row=18, column=1)

        E1 = Entry(pro2, bd=5)
        E1.grid(row=1, column=1)
        E2 = Entry(pro2, bd=5)
        E2.grid(row=2, column=1)
        E3 = Entry(pro2, bd=5)
        E3.grid(row=3, column=1)
        E4 = Entry(pro2, bd=5)
        E4.grid(row=4, column=1)
        E5 = Entry(pro2, bd=5)
        E5.grid(row=5, column=1)
        E6 = Entry(pro2, bd=5)
        E6.grid(row=6, column=1)
        E7 = Entry(pro2, bd=5)
        E7.grid(row=7, column=1)

        def getMD():
            #           print('inside')

            d1 = float(Entry.get(E1))
            d2 = float(Entry.get(E2))
            d3 = float(Entry.get(E3))
            d4 = float(Entry.get(E4))
            d5 = float(Entry.get(E5))
            d6 = float(Entry.get(E6))
            d7 = float(Entry.get(E7))

            depth = [d1, d2, d3, d4, d5, d6, d7]
            return depth

        def submit():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            L13 = Label(pro2, text=v[0]).grid(row=1, column=2)
            L14 = Label(pro2, text=v[1]).grid(row=2, column=2)
            L15 = Label(pro2, text=v[2]).grid(row=3, column=2)
            L16 = Label(pro2, text=v[3]).grid(row=4, column=2)
            L17 = Label(pro2, text=v[4]).grid(row=5, column=2)
            L18 = Label(pro2, text=v[5]).grid(row=6, column=2)
            L19 = Label(pro2, text=v[6]).grid(row=7, column=2)

            L20 = Label(pro2, text=h[0]).grid(row=1, column=3)
            L21 = Label(pro2, text=h[1]).grid(row=2, column=3)
            L22 = Label(pro2, text=h[2]).grid(row=3, column=3)
            L23 = Label(pro2, text=h[3]).grid(row=4, column=3)
            L24 = Label(pro2, text=h[4]).grid(row=5, column=3)
            L25 = Label(pro2, text=h[5]).grid(row=6, column=3)
            L26 = Label(pro2, text=h[6]).grid(row=7, column=3)

            L27 = Label(pro2, text=nx[0]).grid(row=1, column=4)
            L28 = Label(pro2, text=nx[1]).grid(row=2, column=4)
            L29 = Label(pro2, text=nx[2]).grid(row=3, column=4)
            L30 = Label(pro2, text=nx[3]).grid(row=4, column=4)
            L31 = Label(pro2, text=nx[4]).grid(row=5, column=4)
            L32 = Label(pro2, text=nx[5]).grid(row=6, column=4)
            L33 = Label(pro2, text=nx[6]).grid(row=7, column=4)

            L34 = Label(pro2, text=ex[0]).grid(row=1, column=5)
            L35 = Label(pro2, text=ex[1]).grid(row=2, column=5)
            L36 = Label(pro2, text=ex[2]).grid(row=3, column=5)
            L37 = Label(pro2, text=ex[3]).grid(row=4, column=5)
            L38 = Label(pro2, text=ex[4]).grid(row=5, column=5)
            L39 = Label(pro2, text=ex[5]).grid(row=6, column=5)
            L40 = Label(pro2, text=ex[6]).grid(row=7, column=5)

            B1 = Button(pro2, text="Save Data", command=final, activebackground="grey", activeforeground="yellow").grid(
                row=12, column=1)

        def final():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            Hb = 0

            Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et = getData()
            MDb = Vb
            data = np.array(
                [[0, 0, 0, '', 'MDx1', v[0], h[0], nx[0], ex[0]], [Vb, Hb, MDb, '', 'MDx2', v[1], h[1], nx[1], ex[1]],
                 [Vc, Hc, MDc, '', 'MDx3', v[2], h[2], nx[2], ex[2]],
                 [Vd, Hd, MDd, '', 'MDx4', v[3], h[3], nx[3], ex[3]],
                 [Ve, He, MDe, '', 'MDx5', v[4], h[4], nx[4], ex[4]],
                 [Vt, Ht, MDt, '', 'MDx6', v[5], h[5], nx[5], ex[5]],
                 ['', '', '', '', 'MDx7', v[6], h[6], nx[6], ex[6]]])
            finaldata = DataFrame(data, columns=['V', 'H', 'MD', '', 'Entered MD', 'V', 'H', 'N', 'E'],
                                  index=['A', 'B', 'C', 'D', 'E', 'T', ''])
            # np.savetxt('C:\Users\sk314\Documents\Profile_1_text.txt', data, delimiter=',')
            finaldata.to_csv('C:\Users\sk314\Documents\Profile_2.csv', index_label='Points')
            L40 = Label(pro2, text="Data has been Saved\n Check Document File").grid(row=13, column=1)
            print('finaldata')
            print(finaldata)

        def showgf():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            Ht, Vt, Ve, phi1, phi2, Vb, alpha2, R1, R2, alpha1, Vc, Vd, Hc, Hd, He, MDc, MDe, MDd, MDt, beta, Ns, Nt, Es, Et = getData()
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a1 = f.add_subplot(111)
            h1 = []
            v1 = []
            h2 = []
            v2 = []
            # print(np.linspace(0, MDt, num = 50))
            h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
            h1, v1, nx, ex = calcTrajectory(list(np.linspace(depth[0], depth[6], num=7)))
            data = np.array([h1, v1])
            data_trans = data.transpose()
            df = DataFrame(data_trans)
            print(df)
            a.plot(h2, list(np.negative(v2)))
            a1.scatter(df[0], np.negative(df[1]), color='r')
            style = dict(size=10, color='black')
            a1.text(h1[0] + 80, np.negative(v1[0]), "MDx1", **style)
            a1.text(h1[1] + 80, np.negative(v1[1]), "MDx2", **style)
            a1.text(h1[2] + 80, np.negative(v1[2]), "MDx3", **style)
            a1.text(h1[3] + 80, np.negative(v1[3]), "MDx4", **style)
            a1.text(h1[4] + 80, np.negative(v1[4]), "MDx5", **style)
            a1.text(h1[5] + 80, np.negative(v1[5]), "MDx6", **style)
            a1.text(h1[6] + 80, np.negative(v1[6]), "MDx7", **style)

            a1.legend(['Well Trajectory', 'Entered MDx'])
            a.set_xlabel('Horizontal Distance')
            a.set_ylabel('True Vertical Depth')
            a.set_title('Build, Hold and Drop Profile')
            graph = Tk()
            graph.title('Well Trajectory')
            graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))

            canvas = FigureCanvasTkAgg(f, graph)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

            # toolbar = NavigationToolbar2TkAgg(canvas, self)
            # toolbar.update()
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        B = Button(pro2, text="Submit", command=submit, activebackground="grey", activeforeground="yellow").grid(row=8,
                                                                                                                 column=1)
        B4 = Button(pro2, text="Show Graph", command=showgf, activebackground="grey", activeforeground="yellow").grid(
            row=9, column=1)
        pro2.mainloop()

    B1 = Button(top, text="Submit", command=process2, activebackground="grey", activeforeground="yellow").grid(row=11,
                                                                                                               column=1)
    B2 = Button(top, text="Press to calculate trajectory at different depths", command=process3,
                activebackground="grey", activeforeground="yellow").grid(row=14, column=1, )
    B3 = Button(top, text="Show 2D Graph", command=showgraph, activebackground="grey", activeforeground="yellow").grid(
        row=13, column=1)
    B3 = Button(top, text="Show 3D Graph", command=show3d, activebackground="grey", activeforeground="yellow").grid(
        row=12, column=1)
    top.mainloop()


def proces7():
    top = Tk()
    top.geometry("650x450")
    top.title("TYPE 4 PROFILE")

    L1 = Label(top, text="TYPE 4 PROFILE", bd=7, relief=RAISED, padx=35, width=20).grid(row=0, column=0)
    L2 = Label(top, text="Ns", ).grid(row=1, column=0)
    L17 = Label(top, text="Es", ).grid(row=2, column=0)
    L18 = Label(top, text="Nt", ).grid(row=3, column=0)
    L19 = Label(top, text="Et", ).grid(row=4, column=0)
    L3 = Label(top, text="Vt", ).grid(row=5, column=0)
    L4 = Label(top, text="MDb", ).grid(row=6, column=0)
    L5 = Label(top, text="Alpha1", ).grid(row=7, column=0)
    L6 = Label(top, text="Phi", ).grid(row=8, column=0)
    L9 = Label(top, text="A", ).grid(row=1, column=2)
    L10 = Label(top, text="B", ).grid(row=2, column=2)
    L11 = Label(top, text="C", ).grid(row=3, column=2)
    L12 = Label(top, text="T", ).grid(row=4, column=2)
    L13 = Label(top, text="V", ).grid(row=0, column=3)
    L14 = Label(top, text="H", ).grid(row=0, column=4)
    L15 = Label(top, text="MD", ).grid(row=0, column=5)
    L16 = Label(top, text="Enter Values Here").grid(row=0, column=1)

    zl1 = Entry(top, bd=5)
    zl1.grid(row=1, column=1)
    zl2 = Entry(top, bd=5)
    zl2.grid(row=2, column=1)
    zl3 = Entry(top, bd=5)
    zl3.grid(row=3, column=1)
    zl4 = Entry(top, bd=5)
    zl4.grid(row=4, column=1)
    zl5 = Entry(top, bd=5)
    zl5.grid(row=5, column=1)
    zl6 = Entry(top, bd=5)
    zl6.grid(row=6, column=1)
    zl7 = Entry(top, bd=5)
    zl7.grid(row=7, column=1)
    zl8 = Entry(top, bd=5)
    zl8.grid(row=8, column=1)

    def getData():
        Ns = float(Entry.get(zl1))
        Es = float(Entry.get(zl2))
        Nt = float(Entry.get(zl3))
        Et = float(Entry.get(zl4))
        Vt = float(Entry.get(zl5))
        MDb = float(Entry.get(zl6))
        alph1 = float(Entry.get(zl7))
        phi = float(Entry.get(zl8))

        Ht, beta = targetHandBeta(Et, Es, Nt, Ns)
        R = round(roc(phi), 2)
        alpha1 = np.radians(alph1)
        ON = math.tan(alpha1) * Vt
        NT = round(Ht - ON, 2)
        Ht_dash = QT = NT * math.cos(alpha1)
        QN = NT * math.sin(alpha1)
        AN = Vt / math.cos(alpha1)
        Vt_dash = AQ = round(AN + QN, 2)
        Vb = round(MDb * math.cos(alpha1), 2)
        X = np.degrees(np.arctan((Ht_dash - R) / (Vt_dash - Vb)))
        Y = np.degrees(np.arcsin(R * math.cos(np.radians(alpha1)) / (Vt_dash - MDb)))
        alpha2 = np.radians(X + Y)

        dash_values = {'Vt_dash': Vt_dash, 'Ht_dash': Ht_dash}
        vt_dash = dash_values['Vt_dash']
        ht_dash = dash_values['Ht_dash']

        Hb = round(MDb * math.sin(alpha1), 2)
        AM = MDb + R * math.sin(alpha2)
        Vc = round(AM * math.cos(alpha1), 2)
        CM = R * (1 - math.cos(alpha2)) / math.cos(alpha1)
        Hc = round(AM * math.sin(alpha1) + CM, 2)
        MDc = round(MDb + (np.degrees(alpha2) / phi) * 100, 2)
        CT = (Vt - Vc) / math.cos(alpha1 + alpha2)
        MDt = round(MDc + CT, 2)
        return Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et

    def calcTrajectory(measuredDepth):
        Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et = getData()
        h = []
        v = []
        nx = []
        ex = []
        for d in measuredDepth:
            if d <= MDb:
                L = d
                Vx = round(L * math.cos(alpha1), 2)
                Hx = round(L * math.sin(alpha1), 2)
                Nx = round(Ns + Hx * math.cos(beta), 2)
                Ex = round(Es + Hx * math.sin(beta), 2)
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDb <= d and d <= MDc:
                L = d - MDb
                x = math.radians(L * phi / 100)
                AMx = MDb + R * math.sin(x)
                CMx = R * (1 - math.cos(x)) / math.cos(alpha1)
                Vx = round(AMx * math.cos(alpha1), 2)
                Hx = round(AMx * math.sin(alpha1) + CMx, 2)
                Nx = round(Ns + Hx * math.cos(beta), 2)
                Ex = round(Es + Hx * math.sin(beta), 2)
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDc < d and d <= MDt:
                L = d - MDc
                alpha_t = alpha1 + alpha2
                vx = round(Vc + L * math.cos(alpha_t), 2)
                hx = round(Hc + L * math.sin(alpha_t), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDt < d:
                s = "out of range"
                v.append(s)
                h.append(s)
                nx.append(s)
                ex.append(s)

        return h, v, nx, ex

    def proces2():
        Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et = getData()
        L19 = Label(top, text=str(0)).grid(row=1, column=3)
        L20 = Label(top, text=str(0)).grid(row=1, column=4)
        L21 = Label(top, text=str(0)).grid(row=1, column=5)

        L22 = Label(top, text=str(Vb)).grid(row=2, column=3)
        L23 = Label(top, text=str(Hb)).grid(row=2, column=4)
        L24 = Label(top, text=str(MDb)).grid(row=2, column=5)

        L25 = Label(top, text=str(Vc)).grid(row=3, column=3)
        L26 = Label(top, text=str(Hc)).grid(row=3, column=4)
        L27 = Label(top, text=str(MDc)).grid(row=3, column=5)

        L34 = Label(top, text=str(Vt)).grid(row=4, column=3)
        L35 = Label(top, text=str(Ht)).grid(row=4, column=4)
        L36 = Label(top, text=str(MDt)).grid(row=4, column=5)

    def showgraph():
        Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et = getData()
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a1 = f.add_subplot(111)
        h2 = []
        v2 = []
        Ha = 0
        Va = 0
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        h1 = [Ha, Hb, Hc, Ht]
        v1 = [Va, Vb, Vc, Vt]
        data = np.array([h1, v1])
        data_trans = data.transpose()
        df = DataFrame(data_trans)
        print(df)
        a.plot(h2, list(np.negative(v2)))
        a1.scatter(df[0], np.negative(df[1]), color='g')
        style = dict(size=10, color='black')
        a1.text(Ha, np.negative(Va), "(A) Well Head", **style)
        a1.text(Hb, np.negative(Vb), "(B) Kick off point", **style)
        a1.text(Hc, np.negative(Vc), "(C) Drop off point", **style)
        a1.text(Ht - 1200, np.negative(Vt), "Targate point (T)", **style)
        a1.legend(['Well Trajectory', 'Points'])
        a.set_xlabel('Horizontal Distance')
        a.set_ylabel('True Vertical Depth')
        a.set_title('Slanted Well Profile')
        graph = Tk()
        graph.title('Well Trajectory')
        graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    def show3d():
        Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et = getData()
        Ha = 0
        Va = 0
        h2 = []
        v2 = []
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure(figsize=(10, 7))
        ax = fig.gca(projection='3d')
        z = v2
        x = nx
        y = ex
        plt.gca().invert_yaxis()
        plt.gca().invert_zaxis()
        ax.plot(x, y, z, label='parametric curve')
        ax.set_xlabel('North')
        ax.set_ylabel('East')
        ax.set_zlabel('Depth')
        Ha = 0
        Va = 0
        Nb = round(Ns + Hb * math.cos(beta), 2)
        Eb = round(Es + Hb * math.sin(beta), 2)
        Nc = round(Ns + Hc * math.cos(beta), 2)
        Ec = round(Es + Hc * math.sin(beta), 2)
        Nt = round(Ns + Ht * math.cos(beta), 2)
        Et = round(Es + Ht * math.sin(beta), 2)
        style = dict(size=7, color='black')
        ax.text(Ns, Es, Va, "(A) Well Head", **style)
        ax.text(Nb, Eb, Vb, "(B) Kick off point", **style)
        ax.text(Nc, Ec, Vc, "(C) Drop off point", **style)
        ax.text(Nt, Et, Vt, "Targate point (T)", **style)
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="z", labelsize=8)
        ax.legend(['Well Profile'])
        plt.show()

    def proces3():
        pro2 = Tk()
        pro2.geometry("550x450")
        L1 = Label(pro2, text="Vx").grid(row=0, column=2)
        L11 = Label(pro2, text="Nx").grid(row=0, column=4)
        L12 = Label(pro2, text="Ex").grid(row=0, column=5)
        L2 = Label(pro2, text="MDx1").grid(row=1, column=0)
        L3 = Label(pro2, text="MDx2").grid(row=2, column=0)
        L4 = Label(pro2, text="MDx3").grid(row=3, column=0)
        L5 = Label(pro2, text="MDx4").grid(row=4, column=0)
        L6 = Label(pro2, text="MDx5").grid(row=5, column=0)
        L7 = Label(pro2, text="MDx6").grid(row=6, column=0)
        L8 = Label(pro2, text="MDx7").grid(row=7, column=0)
        ll8 = Label(pro2, text="(MDx should be less than MDt)").grid(row=8, column=0)
        L9 = Label(pro2, text="Enter Values Here").grid(row=0, column=1)
        L10 = Label(pro2, text="Hx").grid(row=0, column=3)
        E1 = Entry(pro2, bd=5)
        E1.grid(row=1, column=1)
        E2 = Entry(pro2, bd=5)
        E2.grid(row=2, column=1)
        E3 = Entry(pro2, bd=5)
        E3.grid(row=3, column=1)
        E4 = Entry(pro2, bd=5)
        E4.grid(row=4, column=1)
        E5 = Entry(pro2, bd=5)
        E5.grid(row=5, column=1)
        E6 = Entry(pro2, bd=5)
        E6.grid(row=6, column=1)
        E7 = Entry(pro2, bd=5)
        E7.grid(row=7, column=1)

        def getMD():
            d1 = float(Entry.get(E1))
            d2 = float(Entry.get(E2))
            d3 = float(Entry.get(E3))
            d4 = float(Entry.get(E4))
            d5 = float(Entry.get(E5))
            d6 = float(Entry.get(E6))
            d7 = float(Entry.get(E7))
            depth = [d1, d2, d3, d4, d5, d6, d7]
            return depth

        def submit():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            L13 = Label(pro2, text=v[0]).grid(row=1, column=2)
            L14 = Label(pro2, text=v[1]).grid(row=2, column=2)
            L15 = Label(pro2, text=v[2]).grid(row=3, column=2)
            L16 = Label(pro2, text=v[3]).grid(row=4, column=2)
            L17 = Label(pro2, text=v[4]).grid(row=5, column=2)
            L18 = Label(pro2, text=v[5]).grid(row=6, column=2)
            L19 = Label(pro2, text=v[6]).grid(row=7, column=2)

            L20 = Label(pro2, text=h[0]).grid(row=1, column=3)
            L21 = Label(pro2, text=h[1]).grid(row=2, column=3)
            L22 = Label(pro2, text=h[2]).grid(row=3, column=3)
            L23 = Label(pro2, text=h[3]).grid(row=4, column=3)
            L24 = Label(pro2, text=h[4]).grid(row=5, column=3)
            L25 = Label(pro2, text=h[5]).grid(row=6, column=3)
            L26 = Label(pro2, text=h[6]).grid(row=7, column=3)

            L27 = Label(pro2, text=nx[0]).grid(row=1, column=4)
            L28 = Label(pro2, text=nx[1]).grid(row=2, column=4)
            L29 = Label(pro2, text=nx[2]).grid(row=3, column=4)
            L30 = Label(pro2, text=nx[3]).grid(row=4, column=4)
            L31 = Label(pro2, text=nx[4]).grid(row=5, column=4)
            L32 = Label(pro2, text=nx[5]).grid(row=6, column=4)
            L33 = Label(pro2, text=nx[6]).grid(row=7, column=4)

            L34 = Label(pro2, text=ex[0]).grid(row=1, column=5)
            L35 = Label(pro2, text=ex[1]).grid(row=2, column=5)
            L36 = Label(pro2, text=ex[2]).grid(row=3, column=5)
            L37 = Label(pro2, text=ex[3]).grid(row=4, column=5)
            L38 = Label(pro2, text=ex[4]).grid(row=5, column=5)
            L39 = Label(pro2, text=ex[5]).grid(row=6, column=5)
            L40 = Label(pro2, text=ex[6]).grid(row=7, column=5)

            B1 = Button(pro2, text="Save Data", command=final, activebackground="grey", activeforeground="yellow").grid(
                row=12, column=1)

        def final():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et = getData()
            data = np.array([[0, 0, 0, '', 'MDx1', v[0], h[0]], [Vb, Hb, MDb, '', 'MDx2', v[1], h[1]],
                             [Vc, Hc, MDc, '', 'MDx3', v[2], h[2]], [Vt, Ht, MDt, '', 'MDx4', v[3], h[3]],
                             ['', '', '', '', 'MDx5', v[4], h[4]], ['', '', '', '', 'MDx6', v[5], h[5]],
                             ['', '', '', '', 'MDx7', v[6], h[6]]])
            finaldata = DataFrame(data, columns=['V', 'H', 'MD', '', 'Entered MD', 'V', 'H'],
                                  index=['A', 'B', 'C', 'T', '', '', ''])
            finaldata.to_csv('C:\Users\sk314\Documents\Profile_4.csv', index_label='Points')
            L40 = Label(pro2, text="Data has been Saved\n Check Document File").grid(row=13, column=1)
            print('finaldata')
            print(finaldata)

        def showgf():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            Vb, Vc, Hb, Hc, MDc, MDt, R, phi, alpha1, alpha2, MDb, Vt, Ht, beta, Ns, Es, Nt, Et = getData()
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a1 = f.add_subplot(111)
            h1 = []
            v1 = []
            h2 = []
            v2 = []
            h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
            h1, v1, nx, ex = calcTrajectory(list(np.linspace(depth[0], depth[6], num=7)))
            data = np.array([h1, v1])
            data_trans = data.transpose()
            df = DataFrame(data_trans)
            a.plot(h2, list(np.negative(v2)))
            a1.scatter(df[0], np.negative(df[1]), color='r')
            style = dict(size=10, color='black')
            a1.text(h1[0] + 80, np.negative(v1[0]), "MDx1", **style)
            a1.text(h1[1] + 80, np.negative(v1[1]), "MDx2", **style)
            a1.text(h1[2] + 80, np.negative(v1[2]), "MDx3", **style)
            a1.text(h1[3] + 80, np.negative(v1[3]), "MDx4", **style)
            a1.text(h1[4] + 80, np.negative(v1[4]), "MDx5", **style)
            a1.text(h1[5] + 80, np.negative(v1[5]), "MDx6", **style)
            a1.text(h1[6] + 80, np.negative(v1[6]), "MDx7", **style)
            a1.legend(['Well Trajectory', 'Entered MDx'])
            a.set_xlabel('Horizontal Distance')
            a.set_ylabel('True Vertical Depth')
            a.set_title('Slanted Well Profile')
            graph = Tk()
            graph.title('Well Trajectory')
            graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
            canvas = FigureCanvasTkAgg(f, graph)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        B = Button(pro2, text="Submit", command=submit, activebackground="grey", activeforeground="yellow").grid(row=8,
                                                                                                                 column=1)
        B4 = Button(pro2, text="Show Graph", command=showgf, activebackground="grey", activeforeground="yellow").grid(
            row=9, column=1)
        pro2.mainloop()

    B1 = Button(top, text="Submit", command=proces2, activebackground="grey", activeforeground="yellow").grid(row=9,
                                                                                                              column=1)
    B2 = Button(top, text="Press to calculate trajectory at different depths", command=proces3, activebackground="grey",
                activeforeground="yellow").grid(row=12, column=1, )
    B3 = Button(top, text="Show 2D Graph", command=showgraph, activebackground="grey", activeforeground="yellow").grid(
        row=10, column=1)
    B3 = Button(top, text="Show 3D Graph", command=show3d, activebackground="grey", activeforeground="yellow").grid(
        row=11, column=1)
    top.mainloop()


def proces9():
    top = Tk()
    top.geometry("600x400")
    top.title("TYPE 5B PROFILE")

    L1 = Label(top, text="TYPE 5B PROFILE", bd=7, relief=RAISED, padx=20, width=10).grid(row=0, column=0)
    L2 = Label(top, text="Ns", ).grid(row=1, column=0)
    L18 = Label(top, text="Es", ).grid(row=2, column=0)
    L19 = Label(top, text="Nt", ).grid(row=3, column=0)
    L20 = Label(top, text="Et", ).grid(row=4, column=0)
    L3 = Label(top, text="Vt", ).grid(row=5, column=0)
    L4 = Label(top, text="Vb", ).grid(row=6, column=0)
    L5 = Label(top, text="Phi1", ).grid(row=7, column=0)
    L6 = Label(top, text="Phi2", ).grid(row=8, column=0)
    L7 = Label(top, text="Alpha1", ).grid(row=9, column=0)
    L9 = Label(top, text="A", ).grid(row=1, column=2)
    L10 = Label(top, text="B", ).grid(row=2, column=2)
    L11 = Label(top, text="C", ).grid(row=3, column=2)
    L12 = Label(top, text="D", ).grid(row=4, column=2)
    L13 = Label(top, text="E", ).grid(row=5, column=2)
    L14 = Label(top, text="T", ).grid(row=6, column=2)
    L15 = Label(top, text="V", ).grid(row=0, column=3)
    L16 = Label(top, text="H", ).grid(row=0, column=4)
    L17 = Label(top, text="MD", ).grid(row=0, column=5)

    L16 = Label(top, text="Enter Values Here").grid(row=0, column=1)

    e1 = Entry(top, bd=5)
    e1.grid(row=1, column=1)
    e2 = Entry(top, bd=5)
    e2.grid(row=2, column=1)
    e3 = Entry(top, bd=5)
    e3.grid(row=3, column=1)
    e4 = Entry(top, bd=5)
    e4.grid(row=4, column=1)
    e5 = Entry(top, bd=5)
    e5.grid(row=5, column=1)
    e6 = Entry(top, bd=5)
    e6.grid(row=6, column=1)
    e7 = Entry(top, bd=5)
    e7.grid(row=7, column=1)
    e8 = Entry(top, bd=5)
    e8.grid(row=8, column=1)
    e9 = Entry(top, bd=5)
    e9.grid(row=9, column=1)

    def getData():
        Ns = float(Entry.get(e1))
        Es = float(Entry.get(e2))
        Nt = float(Entry.get(e3))
        Et = float(Entry.get(e4))
        Vt = float(Entry.get(e5))
        Vb = float(Entry.get(e6))
        phi1 = float(Entry.get(e7))
        phi2 = float(Entry.get(e8))
        alfa1 = float(Entry.get(e9))
        alpha1 = np.radians(alfa1)
        alpha2 = np.radians(90 - alfa1)
        Ht, beta = targetHandBeta(Et, Es, Nt, Ns)
        R1 = round(roc(phi1), 2)
        R2 = round(roc(phi2), 2)
        Vc = round(Vb + R1 * math.sin(alpha1), 2)
        Hc = round(R1 * (1 - math.cos(alpha1)), 2)
        GE = R2 - R2 * math.cos(alpha2)
        CX = Vt - GE - Vb - R1 * math.sin(alpha1)
        CD = CX / math.cos(alpha1)
        Vd = round(Vc + CX, 2)
        Hd = round(Hc + CD * math.sin(alpha1), 2)
        He = Hd + R2 * math.sin(alpha2)
        Ve = round(Vt, 2)
        MDb = Vb
        MDc = MDb + (np.degrees(alpha1) / phi1) * 100
        MDd = round(MDc + CD, 2)
        MDe = round(MDd + (np.degrees(alpha2) / phi2) * 100, 2)
        L = ET = Ht - R1 * (1 - math.cos(alpha1)) - CD * math.sin(alpha1) - R2 * math.sin(alpha2)
        MDt = round(MDe + ET, 2)
        L = round(L, 2)
        Hb = 0
        He = round(Ht - ET, 2)
        return R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta

    def calcTrajectory(measuredDepth):
        R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta = getData()
        h = []
        v = []
        nx = []
        ex = []
        for d in measuredDepth:
            if d < Vb:
                Vx = d
                Hx = 0
                Nx = Ns
                Ex = Es
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif Vb <= d and d <= MDc:
                L = d - Vb
                x = math.radians(L * phi1 / 100)
                Vx = round(Vb + R1 * math.sin(x), 2)
                Hx = round(R1 * (1 - math.cos(x)), 2)
                Nx = round(Ns + Hx * math.cos(beta), 2)
                Ex = round(Es + Hx * math.sin(beta), 2)
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDc < d and d <= MDd:
                L = d - MDc
                vx = round(Vc + L * math.cos(alpha1), 2)
                hx = round(Hc + L * math.sin(alpha1), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDd < d and d <= MDe:
                L = d - MDd
                z = math.radians(L * phi1 / 100)
                vx = round(Vd + R2 * (math.cos(alpha2 - z) - math.cos(alpha2)), 2)
                hx = round(Hd + R2 * (math.sin(alpha2) - math.sin(alpha2 - z)), 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)
            elif MDe < d and d <= MDt:
                L = d - MDe
                vx = round(Ve, 2)
                hx = round(He + L, 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDt < d:
                s = "Out of range"
                v.append(s)
                h.append(s)
                nx.append(s)
                ex.append(s)

        return h, v, nx, ex

    def proces2():
        R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta = getData()
        L19 = Label(top, text=str(0)).grid(row=1, column=3)
        L20 = Label(top, text=str(0)).grid(row=1, column=4)
        L21 = Label(top, text=str(0)).grid(row=1, column=5)

        L22 = Label(top, text=str(Vb)).grid(row=2, column=3)
        L23 = Label(top, text=str(0)).grid(row=2, column=4)
        L24 = Label(top, text=str(MDb)).grid(row=2, column=5)

        L25 = Label(top, text=str(Vc)).grid(row=3, column=3)
        L26 = Label(top, text=str(Hc)).grid(row=3, column=4)
        L27 = Label(top, text=str(MDc)).grid(row=3, column=5)

        L28 = Label(top, text=str(Vd)).grid(row=4, column=3)
        L29 = Label(top, text=str(Hd)).grid(row=4, column=4)
        L30 = Label(top, text=str(MDd)).grid(row=4, column=5)

        L31 = Label(top, text=str(Ve)).grid(row=5, column=3)
        L32 = Label(top, text=str(He)).grid(row=5, column=4)
        L33 = Label(top, text=str(MDe)).grid(row=5, column=5)

        L34 = Label(top, text=str(Vt)).grid(row=6, column=3)
        L35 = Label(top, text=str(Ht)).grid(row=6, column=4)
        L36 = Label(top, text=str(MDt)).grid(row=6, column=5)

    def showgraph():
        R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta = getData()
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a1 = f.add_subplot(111)
        h2 = []
        v2 = []
        Ha = 0
        Hb = 0
        Va = 0
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        h1 = [Ha, Hb, Hc, Hd, He, Ht]
        v1 = [Va, Vb, Vc, Vd, Ve, Vt]
        data = np.array([h1, v1])
        data_trans = data.transpose()
        df = DataFrame(data_trans)
        a.plot(h2, list(np.negative(v2)))
        a1.scatter(df[0], np.negative(df[1]), color='g')
        style = dict(size=7, color='black')
        a1.text(Ha + 80, np.negative(Va), "(A) Well Head", **style)
        a1.text(Hb + 80, np.negative(Vb), "(B) Kick off point", **style)
        a1.text(Hc + 80, np.negative(Vc), "(C) Drop off point", **style)
        a1.text(Hd + 80, np.negative(Vd), "(D) Build up point", **style)
        a1.text(He + 80, np.negative(Ve - 150), "(E) Drop off point", **style)
        a1.text(Ht - 500, np.negative(Vt - 150), "Targate point (T)", **style)
        a1.legend(['Well Trajectory', 'Points'])
        a.set_xlabel('Horizontal Distance')
        a.set_ylabel('True Vertical Depth')
        a.set_title('Double Buildup Horizontal Profile')
        graph = Tk()
        graph.title('Well Trajectory')
        graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    def show3d():
        R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta = getData()
        Va = 0
        h2 = []
        v2 = []
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure(figsize=(10, 7))
        ax = fig.gca(projection='3d')
        z = v2
        x = nx
        y = ex
        plt.gca().invert_yaxis()
        plt.gca().invert_zaxis()
        ax.plot(x, y, z, label='parametric curve')
        ax.set_xlabel('North')
        ax.set_ylabel('East')
        ax.set_zlabel('Depth')
        Nb = round(Ns + Hb * math.cos(beta), 2)
        Eb = round(Es + Hb * math.sin(beta), 2)
        Nc = round(Ns + Hc * math.cos(beta), 2)
        Ec = round(Es + Hc * math.sin(beta), 2)
        Nd = round(Ns + Hd * math.cos(beta), 2)
        Ed = round(Es + Hd * math.sin(beta), 2)
        Ne = round(Ns + He * math.cos(beta), 2)
        Ee = round(Es + He * math.sin(beta), 2)
        Nt = round(Ns + Ht * math.cos(beta), 2)
        Et = round(Es + Ht * math.sin(beta), 2)
        style = dict(size=7, color='black')
        ax.text(Ns, Es, Va, "(A) Well Head", **style)
        ax.text(Nb, Eb, Vb, "(B) Kick off point", **style)
        ax.text(Nc, Ec, Vc, "(C) Drop off point", **style)
        ax.text(Nd, Ed, Vd, "(D) Drop up point", **style)
        ax.text(Ne, Ee, Ve, "(E) Drop off point", **style)
        ax.text(Nt, Et, Vt, "Targate point (T)", **style)
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="z", labelsize=8)
        ax.legend(['Well Profile'])
        plt.show()

    def proces3():
        pro2 = Tk()
        pro2.geometry("550x400")
        L1 = Label(pro2, text="Vx").grid(row=0, column=2)
        L2 = Label(pro2, text="MDx1").grid(row=1, column=0)
        L3 = Label(pro2, text="MDx2").grid(row=2, column=0)
        L4 = Label(pro2, text="MDx3").grid(row=3, column=0)
        L5 = Label(pro2, text="MDx4").grid(row=4, column=0)
        L6 = Label(pro2, text="MDx5").grid(row=5, column=0)
        L7 = Label(pro2, text="MDx6").grid(row=6, column=0)
        L8 = Label(pro2, text="MDx7").grid(row=7, column=0)
        Ll8 = Label(pro2, text="(MDx should be less then MDt)").grid(row=8, column=0)
        L9 = Label(pro2, text="Enter Values Here").grid(row=0, column=1)
        L10 = Label(pro2, text="Hx").grid(row=0, column=3)
        L1 = Label(pro2, text="Nx").grid(row=0, column=4)
        L1 = Label(pro2, text="Ex").grid(row=0, column=5)

        E1 = Entry(pro2, bd=5)
        E1.grid(row=1, column=1)
        E2 = Entry(pro2, bd=5)
        E2.grid(row=2, column=1)
        E3 = Entry(pro2, bd=5)
        E3.grid(row=3, column=1)
        E4 = Entry(pro2, bd=5)
        E4.grid(row=4, column=1)
        E5 = Entry(pro2, bd=5)
        E5.grid(row=5, column=1)
        E6 = Entry(pro2, bd=5)
        E6.grid(row=6, column=1)
        E7 = Entry(pro2, bd=5)
        E7.grid(row=7, column=1)

        def getMD():
            d1 = float(Entry.get(E1))
            d2 = float(Entry.get(E2))
            d3 = float(Entry.get(E3))
            d4 = float(Entry.get(E4))
            d5 = float(Entry.get(E5))
            d6 = float(Entry.get(E6))
            d7 = float(Entry.get(E7))
            depth = [d1, d2, d3, d4, d5, d6, d7]
            return depth

        def submit():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            L13 = Label(pro2, text=v[0]).grid(row=1, column=2)
            L14 = Label(pro2, text=v[1]).grid(row=2, column=2)
            L15 = Label(pro2, text=v[2]).grid(row=3, column=2)
            L16 = Label(pro2, text=v[3]).grid(row=4, column=2)
            L17 = Label(pro2, text=v[4]).grid(row=5, column=2)
            L18 = Label(pro2, text=v[5]).grid(row=6, column=2)
            L19 = Label(pro2, text=v[6]).grid(row=7, column=2)

            L20 = Label(pro2, text=h[0]).grid(row=1, column=3)
            L21 = Label(pro2, text=h[1]).grid(row=2, column=3)
            L22 = Label(pro2, text=h[2]).grid(row=3, column=3)
            L23 = Label(pro2, text=h[3]).grid(row=4, column=3)
            L24 = Label(pro2, text=h[4]).grid(row=5, column=3)
            L25 = Label(pro2, text=h[5]).grid(row=6, column=3)
            L26 = Label(pro2, text=h[6]).grid(row=7, column=3)

            L27 = Label(pro2, text=nx[0]).grid(row=1, column=4)
            L28 = Label(pro2, text=nx[1]).grid(row=2, column=4)
            L29 = Label(pro2, text=nx[2]).grid(row=3, column=4)
            L30 = Label(pro2, text=nx[3]).grid(row=4, column=4)
            L31 = Label(pro2, text=nx[4]).grid(row=5, column=4)
            L32 = Label(pro2, text=nx[5]).grid(row=6, column=4)
            L33 = Label(pro2, text=nx[6]).grid(row=7, column=4)

            L34 = Label(pro2, text=ex[0]).grid(row=1, column=5)
            L35 = Label(pro2, text=ex[1]).grid(row=2, column=5)
            L36 = Label(pro2, text=ex[2]).grid(row=3, column=5)
            L37 = Label(pro2, text=ex[3]).grid(row=4, column=5)
            L38 = Label(pro2, text=ex[4]).grid(row=5, column=5)
            L39 = Label(pro2, text=ex[5]).grid(row=6, column=5)
            L40 = Label(pro2, text=ex[6]).grid(row=7, column=5)
            B1 = Button(pro2, text="Save Data", command=final, activebackground="grey", activeforeground="yellow").grid(
                row=12, column=1)

        def final():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta = getData()
            data = np.array(
                [[0, 0, 0, '', 'MDx1', v[0], h[0], nx[0], ex[0]], [Vb, Hb, MDb, '', 'MDx2', v[1], h[1], nx[1], ex[1]],
                 [Vc, Hc, MDc, '', 'MDx3', v[2], h[2], nx[2], ex[2]],
                 [Vd, Hd, MDd, '', 'MDx4', v[3], h[3], nx[3], ex[3]],
                 [Ve, He, MDe, '', 'MDx5', v[4], h[4], nx[4], ex[4]],
                 [Vt, Ht, MDt, '', 'MDx6', v[5], h[5], nx[5], ex[5]],
                 ['', '', '', '', 'MDx7', v[6], h[6], nx[6], ex[6]]])
            finaldata = DataFrame(data, columns=['V', 'H', 'MD', '', 'Entered MD', 'V', 'H', 'N', 'E'],
                                  index=['A', 'B', 'C', 'D', 'E', 'T', ''])
            finaldata.to_csv('C:\Users\sk314\Documents\Profile_5B.csv', index_label='Points')
            L40 = Label(pro2, text="Data has been Saved\n Check Document File").grid(row=13, column=1)
            print('finaldata')
            print(finaldata)

        def showgf():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            R1, R2, Vb, Hb, Vc, Hc, Vd, Hd, Ve, He, MDb, MDc, MDd, MDe, MDt, L, phi1, phi2, alpha1, alpha2, Ht, Vt, Ns, Es, Nt, Et, beta = getData()
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a1 = f.add_subplot(111)
            h1 = []
            v1 = []
            h2 = []
            v2 = []
            h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
            h1, v1, nx, ex = calcTrajectory(list(np.linspace(depth[0], depth[6], num=7)))
            data = np.array([h1, v1])
            data_trans = data.transpose()
            df = DataFrame(data_trans)
            a.plot(h2, list(np.negative(v2)))
            a1.scatter(df[0], np.negative(df[1]), color='r')
            style = dict(size=10, color='black')
            a1.text(h1[0] + 80, np.negative(v1[0]), "MDx1", **style)
            a1.text(h1[1] + 80, np.negative(v1[1]), "MDx2", **style)
            a1.text(h1[2] + 80, np.negative(v1[2]), "MDx3", **style)
            a1.text(h1[3] + 80, np.negative(v1[3]), "MDx4", **style)
            a1.text(h1[4] + 80, np.negative(v1[4]), "MDx5", **style)
            a1.text(h1[5] + 80, np.negative(v1[5]), "MDx6", **style)
            a1.text(h1[6] + 80, np.negative(v1[6]), "MDx7", **style)
            a1.legend(['Well Trajectory', 'Entered MDx'])
            a.set_xlabel('Horizontal Distance')
            a.set_ylabel('True Vertical Depth')
            a.set_title('Double Buildup Horizontal Profile')
            graph = Tk()
            graph.title('Well Trajectory')
            graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
            canvas = FigureCanvasTkAgg(f, graph)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        B = Button(pro2, text="Submit", command=submit, activebackground="grey", activeforeground="yellow").grid(row=8,
                                                                                                                 column=1)
        B4 = Button(pro2, text="Show Graph", command=showgf, activebackground="grey", activeforeground="yellow").grid(
            row=9, column=1)
        pro2.mainloop()

    B1 = Button(top, text="Submit", command=proces2, activebackground="grey", activeforeground="yellow").grid(row=10,
                                                                                                              column=1)
    B2 = Button(top, text="Press to calculate trajectory at different depths", command=proces3, activebackground="grey",
                activeforeground="yellow").grid(row=13, column=1, )
    B3 = Button(top, text="Show 2D Graph", command=showgraph, activebackground="grey", activeforeground="yellow").grid(
        row=11, column=1)
    B3 = Button(top, text="Show 3D Graph", command=show3d, activebackground="grey", activeforeground="yellow").grid(
        row=12, column=1)
    top.mainloop()


def proces11():
    top = Tk()
    top.geometry("600x300")
    top.title("TYPE 5A PROFILE")

    L1 = Label(top, text="TYPE 5A PROFILE", bd=7, relief=RAISED, padx=20, width=10).grid(row=0, column=0)
    L2 = Label(top, text="Ns", ).grid(row=1, column=0)
    L3 = Label(top, text="Es", ).grid(row=2, column=0)
    L4 = Label(top, text="Nt", ).grid(row=3, column=0)
    L5 = Label(top, text="Et", ).grid(row=4, column=0)
    L6 = Label(top, text="Vt", ).grid(row=5, column=0)
    L7 = Label(top, text="Phi", ).grid(row=6, column=0)
    L9 = Label(top, text="A", ).grid(row=1, column=2)
    L10 = Label(top, text="B", ).grid(row=2, column=2)
    L11 = Label(top, text="C", ).grid(row=3, column=2)
    L12 = Label(top, text="T", ).grid(row=4, column=2)
    L13 = Label(top, text="V", ).grid(row=0, column=3)
    L14 = Label(top, text="H", ).grid(row=0, column=4)
    L15 = Label(top, text="MD", ).grid(row=0, column=5)
    L16 = Label(top, text="Enter Values Here").grid(row=0, column=1)

    xl1 = Entry(top, bd=5)
    xl1.grid(row=1, column=1)
    xl2 = Entry(top, bd=5)
    xl2.grid(row=2, column=1)
    xl3 = Entry(top, bd=5)
    xl3.grid(row=3, column=1)
    xl4 = Entry(top, bd=5)
    xl4.grid(row=4, column=1)
    xl5 = Entry(top, bd=5)
    xl5.grid(row=5, column=1)
    xl6 = Entry(top, bd=5)
    xl6.grid(row=6, column=1)

    def getData():
        Ns = float(Entry.get(xl1))
        Es = float(Entry.get(xl2))
        Nt = float(Entry.get(xl3))
        Et = float(Entry.get(xl4))
        Vt = float(Entry.get(xl5))
        phi = float(Entry.get(xl6))
        Ht, beta = targetHandBeta(Et, Es, Nt, Ns)
        Va = 0
        Ha = 0
        MDa = 0
        Hb = 0
        R = round(roc(phi), 2)
        Vb = Vt - R
        MDb = Vb
        Vc = Vt
        Hc = R
        MDc = MDb + (90 / phi) * 100
        L = Ht - Hc
        MDt = MDc + L
        return R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta

    def calcTrajectory(measuredDepth):
        R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta = getData()
        h = []
        v = []
        nx = []
        ex = []
        for d in measuredDepth:
            if d <= Vb:
                L = d
                Vx = round(L, 2)
                Hx = round(0, 2)
                Nx = Ns
                Ex = Es
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif Vb < d and d <= MDc:
                L = d - Vb
                x = math.radians(L * phi / 100)
                Vx = round(Vb + R * math.sin(x), 2)
                Hx = round(R * (1 - math.cos(x)), 2)
                Nx = round(Ns + Hx * math.cos(beta), 2)
                Ex = round(Es + Hx * math.sin(beta), 2)
                v.append(Vx)
                h.append(Hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDc < d and d <= MDt:
                L = d - MDc
                vx = round(Vc, 2)
                hx = round(Hc + L, 2)
                Nx = round(Ns + hx * math.cos(beta), 2)
                Ex = round(Es + hx * math.sin(beta), 2)
                v.append(vx)
                h.append(hx)
                nx.append(Nx)
                ex.append(Ex)

            elif MDt < d:
                s = "out of range"
                v.append(s)
                h.append(s)
                nx.append(s)
                ex.append(s)

        return h, v, nx, ex

    def proces2():
        R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta = getData()
        L19 = Label(top, text=str(0)).grid(row=1, column=3)
        L20 = Label(top, text=str(0)).grid(row=1, column=4)
        L21 = Label(top, text=str(0)).grid(row=1, column=5)

        L22 = Label(top, text=str(Vb)).grid(row=2, column=3)
        L23 = Label(top, text=str(Hb)).grid(row=2, column=4)
        L24 = Label(top, text=str(MDb)).grid(row=2, column=5)

        L25 = Label(top, text=str(Vc)).grid(row=3, column=3)
        L26 = Label(top, text=str(Hc)).grid(row=3, column=4)
        L27 = Label(top, text=str(MDc)).grid(row=3, column=5)

        L34 = Label(top, text=str(Vt)).grid(row=4, column=3)
        L35 = Label(top, text=str(Ht)).grid(row=4, column=4)
        L36 = Label(top, text=str(MDt)).grid(row=4, column=5)

    def showgraph():
        R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta = getData()
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a1 = f.add_subplot(111)
        h2 = []
        v2 = []
        Ha = 0
        Va = 0
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        h1 = [Ha, Hb, Hc, Ht]
        v1 = [Va, Vb, Vc, Vt]
        data = np.array([h1, v1])
        data_trans = data.transpose()
        df = DataFrame(data_trans)
        a.plot(h2, list(np.negative(v2)))
        a1.scatter(df[0], np.negative(df[1]), color='g')
        style = dict(size=10, color='black')
        a1.text(Ha, np.negative(Va), "(A) Well Head", **style)
        a1.text(Hb, np.negative(Vb), "(B) Kick off point", **style)
        a1.text(Hc, np.negative(Vc), "(C) Drop off point", **style)
        a1.text(Ht, np.negative(Vt), "Targate point (T)", **style)
        a1.legend(['Well Trajectory', 'Points'])
        a.set_xlabel('Horizontal Distance')
        a.set_ylabel('True Vertical Depth')
        a.set_title('Single Buildup Horizontal Profile')
        graph = Tk()
        graph.title('Well Trajectory')
        graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    def show3d():
        R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta = getData()
        Va = 0
        h2 = []
        v2 = []
        h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure(figsize=(10, 7))
        ax = fig.gca(projection='3d')
        z = v2
        x = nx
        y = ex
        plt.gca().invert_yaxis()
        plt.gca().invert_zaxis()
        ax.plot(x, y, z)
        ax.set_xlabel('North')
        ax.set_ylabel('East')
        ax.set_zlabel('Depth')
        Nb = round(Ns + Hb * math.cos(beta), 2)
        Eb = round(Es + Hb * math.sin(beta), 2)
        Nc = round(Ns + Hc * math.cos(beta), 2)
        Ec = round(Es + Hc * math.sin(beta), 2)
        Nt = round(Ns + Ht * math.cos(beta), 2)
        Et = round(Es + Ht * math.sin(beta), 2)
        x1 = [Ns, Nb, Nc, Nt]
        y1 = [Es, Eb, Ec, Et]
        z1 = [Va, Vb, Vc, Vt]
        ax.scatter(x1, y1, z1, color='g')
        style = dict(size=7, color='black')
        ax.text(Ns, Es, Va, "(A) Well Head", **style)
        ax.text(Nb, Eb, Vb, "(B) Kick off point", **style)
        ax.text(Nc, Ec, Vc, "(C) Drop off point", **style)
        ax.text(Nt, Et, Vt, "Targate point (T)", **style)
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="z", labelsize=8)
        ax.legend(['Well Profile', 'Points'])
        plt.show()

    def proces3():
        pro2 = Tk()
        pro2.geometry("550x400")
        L1 = Label(pro2, text="Vx").grid(row=0, column=7)
        L2 = Label(pro2, text="MDx1").grid(row=1, column=5)
        L3 = Label(pro2, text="MDx2").grid(row=2, column=5)
        L4 = Label(pro2, text="MDx3").grid(row=3, column=5)
        L5 = Label(pro2, text="MDx4").grid(row=4, column=5)
        L6 = Label(pro2, text="MDx5").grid(row=5, column=5)
        L7 = Label(pro2, text="MDx6").grid(row=6, column=5)
        L8 = Label(pro2, text="MDx7").grid(row=7, column=5)
        Ll8 = Label(pro2, text="(MDx should be less than MDt)").grid(row=8, column=5)
        L9 = Label(pro2, text="Enter Values Here").grid(row=0, column=6)
        L10 = Label(pro2, text="Hx").grid(row=0, column=8)
        L11 = Label(pro2, text="Nx").grid(row=0, column=9)
        L12 = Label(pro2, text="Ex").grid(row=0, column=10)

        E1 = Entry(pro2, bd=5)
        E1.grid(row=1, column=6)
        E2 = Entry(pro2, bd=5)
        E2.grid(row=2, column=6)
        E3 = Entry(pro2, bd=5)
        E3.grid(row=3, column=6)
        E4 = Entry(pro2, bd=5)
        E4.grid(row=4, column=6)
        E5 = Entry(pro2, bd=5)
        E5.grid(row=5, column=6)
        E6 = Entry(pro2, bd=5)
        E6.grid(row=6, column=6)
        E7 = Entry(pro2, bd=5)
        E7.grid(row=7, column=6)

        def getMD():
            d1 = float(Entry.get(E1))
            d2 = float(Entry.get(E2))
            d3 = float(Entry.get(E3))
            d4 = float(Entry.get(E4))
            d5 = float(Entry.get(E5))
            d6 = float(Entry.get(E6))
            d7 = float(Entry.get(E7))

            depth = [d1, d2, d3, d4, d5, d6, d7]
            return depth

        def submit():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            L13 = Label(pro2, text=v[0]).grid(row=1, column=7)
            L14 = Label(pro2, text=v[1]).grid(row=2, column=7)
            L15 = Label(pro2, text=v[2]).grid(row=3, column=7)
            L16 = Label(pro2, text=v[3]).grid(row=4, column=7)
            L17 = Label(pro2, text=v[4]).grid(row=5, column=7)
            L18 = Label(pro2, text=v[5]).grid(row=6, column=7)
            L19 = Label(pro2, text=v[6]).grid(row=7, column=7)

            L20 = Label(pro2, text=h[0]).grid(row=1, column=8)
            L21 = Label(pro2, text=h[1]).grid(row=2, column=8)
            L22 = Label(pro2, text=h[2]).grid(row=3, column=8)
            L23 = Label(pro2, text=h[3]).grid(row=4, column=8)
            L24 = Label(pro2, text=h[4]).grid(row=5, column=8)
            L25 = Label(pro2, text=h[5]).grid(row=6, column=8)
            L26 = Label(pro2, text=h[6]).grid(row=7, column=8)

            L27 = Label(pro2, text=nx[0]).grid(row=1, column=9)
            L28 = Label(pro2, text=nx[1]).grid(row=2, column=9)
            L29 = Label(pro2, text=nx[2]).grid(row=3, column=9)
            L30 = Label(pro2, text=nx[3]).grid(row=4, column=9)
            L31 = Label(pro2, text=nx[4]).grid(row=5, column=9)
            L32 = Label(pro2, text=nx[5]).grid(row=6, column=9)
            L33 = Label(pro2, text=nx[6]).grid(row=7, column=9)

            L34 = Label(pro2, text=ex[0]).grid(row=1, column=10)
            L35 = Label(pro2, text=ex[1]).grid(row=2, column=10)
            L36 = Label(pro2, text=ex[2]).grid(row=3, column=10)
            L37 = Label(pro2, text=ex[3]).grid(row=4, column=10)
            L38 = Label(pro2, text=ex[4]).grid(row=5, column=10)
            L39 = Label(pro2, text=ex[5]).grid(row=6, column=10)
            L40 = Label(pro2, text=ex[6]).grid(row=7, column=10)
            B1 = Button(pro2, text="Save Data", command=final, activebackground="grey", activeforeground="yellow").grid(
                row=12, column=1)

        def final():
            depth = getMD()
            h, v, nx, ex = calcTrajectory(depth)
            R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta = getData()
            data = np.array(
                [[0, 0, 0, '', 'MDx1', v[0], h[0], nx[0], ex[0]], [Vb, Hb, MDb, '', 'MDx2', v[1], h[1], nx[1], ex[1]],
                 [Vc, Hc, MDc, '', 'MDx3', v[2], h[2], nx[2], ex[2]],
                 [Vt, Ht, MDt, '', 'MDx4', v[3], h[3], nx[3], ex[3]],
                 ['', '', '', '', 'MDx5', v[4], h[4], nx[4], ex[4]], ['', '', '', '', 'MDx6', v[5], h[5], nx[5], ex[5]],
                 ['', '', '', '', 'MDx7', v[6], h[6], nx[6], ex[6]]])
            finaldata = DataFrame(data, columns=['V', 'H', 'MD', '', 'Entered MD', 'V', 'H', 'N', 'E'],
                                  index=['A', 'B', 'C', 'T', '', '', ''])
            finaldata.to_csv('C:\Users\sk314\Documents\Profile_5A.csv', index_label='Points')
            L40 = Label(pro2, text="Data has been Saved\n Check Document File").grid(row=13, column=1)

        def showgf():
            R, L, Vb, Hb, MDb, Vc, Hc, MDc, MDt, phi, Vt, Ht, Ns, Es, Nt, Et, beta = getData()
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a1 = f.add_subplot(111)
            h1 = []
            v1 = []
            h2 = []
            v2 = []
            h2, v2, nx, ex = calcTrajectory(list(np.linspace(0, MDt, num=50)))  # calctraj([zero,....mdt])
            h1, v1, nx, ex = calcTrajectory(list(np.linspace(depth[0], depth[6], num=7)))
            data = np.array([h1, v1])
            data_trans = data.transpose()
            df = DataFrame(data_trans)
            print(df)
            a.plot(h2, list(np.negative(v2)))
            a1.scatter(df[0], np.negative(df[1]), color='r')
            style = dict(size=10, color='black')
            a1.text(h1[0] + 80, np.negative(v1[0]), "MDx1", **style)
            a1.text(h1[1] + 80, np.negative(v1[1]), "MDx2", **style)
            a1.text(h1[2] + 80, np.negative(v1[2]), "MDx3", **style)
            a1.text(h1[3] + 80, np.negative(v1[3]), "MDx4", **style)
            a1.text(h1[4] + 80, np.negative(v1[4]), "MDx5", **style)
            a1.text(h1[5] + 80, np.negative(v1[5]), "MDx6", **style)
            a1.text(h1[6] + 80, np.negative(v1[6]), "MDx7", **style)
            a1.legend(['Well Trajectory', 'Entered MDx'])
            a.set_xlabel('Horizontal Distance')
            a.set_ylabel('True Vertical Depth')
            a.set_title('Single Buildup Horizontal Profile')
            graph = Tk()
            graph.title('Well Trajectory')
            graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
            canvas = FigureCanvasTkAgg(f, graph)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        B = Button(pro2, text="Submit", command=submit, activebackground="grey", activeforeground="yellow").grid(row=8,
                                                                                                                 column=6)
        B4 = Button(pro2, text="Show Graph", command=showgf, activebackground="grey", activeforeground="yellow").grid(
            row=9, column=6)
        pro2.mainloop()

    B1 = Button(top, text="Submit", command=proces2, activebackground="grey", activeforeground="yellow").grid(row=7,
                                                                                                              column=1)
    B2 = Button(top, text="Press to calculate trajectory at different depths", command=proces3, activebackground="grey",
                activeforeground="yellow").grid(row=10, column=1, )
    B3 = Button(top, text="Show 2D Graph", command=showgraph, activebackground="grey", activeforeground="yellow").grid(
        row=8, column=1)
    B3 = Button(top, text="Show 3D Graph", command=show3d, activebackground="grey", activeforeground="yellow").grid(
        row=9, column=1)
    top.mainloop()


def comp():
    top = Tk()
    top.geometry("1200x300")

    def f1():
        def pro1():
            Ht = float(Entry.get(e1))
            Vt = float(Entry.get(e2))
            Vb = float(Entry.get(e3))
            phi = float(Entry.get(e4))

            R = round(18000 / (math.pi * phi), 2)
            X = round(np.degrees(np.arctan((Ht - R) / (Vt - Vb))), 2)
            c = math.cos(math.radians(X))
            Yrad = np.arcsin(R * c / (Vt - Vb))
            Y = np.degrees(Yrad)
            round(Y, 2)
            alpha = round(X + Y)
            Vc = round(Vb + (R * math.sin(np.radians(alpha))), 2)
            Hc = round(R * (1 - math.cos(np.radians(alpha))), 2)
            MDc = round(Vb + ((alpha / phi) * 100), 2)
            MDt = round(MDc + (Vt - Vc) / math.cos(math.radians(alpha)), 2)
            print("done")
            t.append(MDt)

        def pro2():
            Ht = float(Entry.get(e8))
            Vt = float(Entry.get(e9))
            Ve = float(Entry.get(e10))
            phi1 = float(Entry.get(e11))
            phi2 = float(Entry.get(e12))
            c1 = float(Entry.get(e14))
            c2 = float(Entry.get(e15))

            alpha1 = np.radians(c1)
            alpha2 = np.radians(c2)

            R1 = round(18000 / (math.pi * phi1), 2)
            R2 = round(18000 / (math.pi * phi2), 2)
            OQ = round(Ht - R1 - R2 * math.cos(alpha2), 2)
            QS = R1 + R2
            EM = Vt - Ve
            ET = round(EM / (math.cos((alpha2))), 2)
            MT = round(ET * math.sin((alpha2)), 2)
            Hc = round(R1 * (1 - math.cos(alpha1)), 2)
            CD = round((Ht - Hc - R2 * (math.cos(alpha2) - math.cos(alpha1)) - MT) / math.sin(alpha1), 2)
            PS = CD
            PQ = round(math.sqrt(PS ** 2 + QS ** 2), 2)
            OP = round(math.sqrt(PQ ** 2 - OQ ** 2), 2)
            Vb = round(Ve - OP + R2 * math.sin(alpha2), 2)
            Hd = round(Hc + CD * math.sin(alpha1), 2)
            Vc = round(Vb + R1 * math.sin(alpha1), 2)
            Vd = round(Vc + CD * math.cos(alpha1), 2)
            He = Ht - MT
            MDc = round((np.degrees(alpha1) / phi1) * 100 + Vb, 2)
            MDd = round(MDc + CD, 2)
            MDe = round(MDd + ((np.degrees(alpha1) - np.degrees(alpha2)) / phi2) * 100, 2)
            MDt = round(MDe + (Vt - Ve) / math.cos(alpha2), 2)
            print("done")
            t.append(MDt)

        def pro4():
            Ht = float(Entry.get(ek1))
            Vt = float(Entry.get(ek2))
            MDb = float(Entry.get(ek3))
            alph1 = float(Entry.get(ek4))
            phi = float(Entry.get(ek5))

            R = round(18000 / (math.pi * phi), 2)
            alpha1 = np.radians(alph1)
            ON = math.tan(alpha1) * Vt
            NT = round(Ht - ON, 2)
            Ht_dash = QT = NT * math.cos(alpha1)
            QN = NT * math.sin(alpha1)
            AN = Vt / math.cos(alpha1)
            Vt_dash = AQ = round(AN + QN, 2)
            Vb = round(MDb * math.cos(alpha1), 2)
            X = np.degrees(np.arctan((Ht_dash - R) / (Vt_dash - Vb)))
            Y = np.degrees(np.arcsin(R * math.cos(np.radians(alpha1)) / (Vt_dash - MDb)))
            alpha2 = np.radians(X + Y)

            dash_values = {'Vt_dash': Vt_dash, 'Ht_dash': Ht_dash}
            vt_dash = dash_values['Vt_dash']
            ht_dash = dash_values['Ht_dash']

            Hb = round(MDb * math.sin(alpha1), 2)
            AM = MDb + R * math.sin(alpha2)
            Vc = round(AM * math.cos(alpha1), 2)
            CM = R * (1 - math.cos(alpha2)) / math.cos(alpha1)
            Hc = round(AM * math.sin(alpha1) + CM, 2)
            MDc = round(MDb + (np.degrees(alpha2) / phi) * 100, 2)
            CT = R / math.tan(np.radians(Y))
            MDt = round(MDc + CT, 2)
            print("done")
            t.append(MDt)

        def pro5a():
            Vt = float(Entry.get(el1))
            Ht = float(Entry.get(el2))
            phi = float(Entry.get(el3))
            Va = 0
            Ha = 0
            MDa = 0
            Hb = 0
            # ===================
            R = round(18000 / (math.pi * phi), 2)
            Vb = Vt - R
            MDb = Vb
            Vc = Vt
            Hc = R
            MDc = MDb + (90 / phi) * 100
            L = Ht - Hc
            MDt = round(MDc + L, 2)
            print("done")
            t.append(MDt)

        def pro3():
            y = 0
            return y
            #t.append(y)

        def pro5b():
            Ht = float(Entry.get(ed8))
            Vt = float(Entry.get(ed9))
            Vb = float(Entry.get(ed10))
            phi1 = float(Entry.get(ed11))
            phi2 = float(Entry.get(ed12))
            alph1 = float(Entry.get(ed14))

            alpha1 = np.radians(alph1)
            alph2 = (90.0 - alph1)
            alpha2 = np.radians(alph2)

            R1 = round(18000 / (math.pi * phi1), 2)
            R2 = round(18000 / (math.pi * phi2), 2)
            Vc = round(Vb + R1 * math.sin(alpha1), 2)
            Hc = round(R1 * (1 - math.cos(alpha1)), 2)
            GE = R2 - R2 * math.cos(alpha2)
            CX = Vt - GE - Vb - R1 * math.sin(alpha1)
            CD = CX / math.cos(alpha1)
            Vd = Vc + CX
            Hd = Hc + CD * math.sin(alpha1)
            He = Hd + R2 * math.sin(alpha2)
            Ve = round(Vt, 2)
            MDb = Vb
            MDc = MDb + (np.degrees(alpha1) / phi1) * 100
            MDd = round(MDc + CD, 2)
            MDe = round(MDd + (np.degrees(alpha2) / phi2) * 100, 2)
            ET = Ht - R1 * (1 - math.cos(alpha1)) - CD * math.sin(alpha1) - R2 * math.sin(alpha2)
            MDt = round(MDe + ET, 2)
            He = Ht - ET
            t.append(MDt)
            print(t)


        pro1()
        pro2()
        y=pro3()
        pro4()
        pro5a()
        pro5b()

        Entry.insert(eh8, 0, t[0])
        Entry.insert(eh9, 0, t[1])
        Entry.insert(eh10, 0, y)
        Entry.insert(eh11, 0, t[2])
        Entry.insert(eh12, 0, t[3])
        Entry.insert(eh13, 0, t[4])
        L = Label(top, text="Minimum MDt is " + str(min(t))).grid(row=11, column=13)

    L2 = Label(top, text="Ht", ).grid(row=1, column=0)
    L3 = Label(top, text="Vt", ).grid(row=2, column=0)
    L4 = Label(top, text="Vb", ).grid(row=3, column=0)
    L6 = Label(top, text="Phi", ).grid(row=4, column=0)

    L7 = Label(top, text="Pro1", ).grid(row=0, column=0)

    e1 = Entry(top, bd=5)
    e1.grid(row=1, column=1)
    e2 = Entry(top, bd=5)
    e2.grid(row=2, column=1)
    e3 = Entry(top, bd=5)
    e3.grid(row=3, column=1)
    e4 = Entry(top, bd=5)
    e4.grid(row=4, column=1)

    # ==========================================================
    l1 = Label(top, text="Ht", ).grid(row=1, column=2)
    l2 = Label(top, text="Vt", ).grid(row=2, column=2)
    l3 = Label(top, text="Ve", ).grid(row=3, column=2)
    l4 = Label(top, text="Phi1", ).grid(row=4, column=2)
    l5 = Label(top, text="Phi2", ).grid(row=5, column=2)
    l6 = Label(top, text="Alpha1", ).grid(row=6, column=2)
    l7 = Label(top, text="Alpha2", ).grid(row=7, column=2)

    lr = Label(top, text="Pro2", ).grid(row=0, column=2)

    e8 = Entry(top, bd=5)
    e8.grid(row=1, column=3)
    e9 = Entry(top, bd=5)
    e9.grid(row=2, column=3)
    e10 = Entry(top, bd=5)
    e10.grid(row=3, column=3)
    e11 = Entry(top, bd=5)
    e11.grid(row=4, column=3)
    e12 = Entry(top, bd=5)
    e12.grid(row=5, column=3)
    e14 = Entry(top, bd=5)
    e14.grid(row=6, column=3)
    e15 = Entry(top, bd=5)
    e15.grid(row=7, column=3)

    # =====================================================================

    k2 = Label(top, text="Ht", ).grid(row=1, column=6)
    k3 = Label(top, text="Vt", ).grid(row=2, column=6)
    k4 = Label(top, text="MDb", ).grid(row=3, column=6)
    k5 = Label(top, text="Alpha1", ).grid(row=4, column=6)
    k6 = Label(top, text="Phi", ).grid(row=5, column=6)

    kr = Label(top, text="Pro4", ).grid(row=0, column=6)

    ek1 = Entry(top, bd=5)
    ek1.grid(row=1, column=7)
    ek2 = Entry(top, bd=5)
    ek2.grid(row=2, column=7)
    ek3 = Entry(top, bd=5)
    ek3.grid(row=3, column=7)
    ek4 = Entry(top, bd=5)
    ek4.grid(row=4, column=7)
    ek5 = Entry(top, bd=5)
    ek5.grid(row=5, column=7)

    # ==================================================

    Lk2 = Label(top, text="Ht", ).grid(row=1, column=8)
    Lk3 = Label(top, text="Vt", ).grid(row=2, column=8)
    Lk4 = Label(top, text="Phi", ).grid(row=3, column=8)
    Lk5 = Label(top, text="Pro5A", ).grid(row=0, column=8)
    el1 = Entry(top, bd=5)
    el1.grid(row=1, column=9)
    el2 = Entry(top, bd=5)
    el2.grid(row=2, column=9)
    el3 = Entry(top, bd=5)
    el3.grid(row=3, column=9)
    # =====================================================

    ld1 = Label(top, text="Ht", ).grid(row=1, column=10)
    ld2 = Label(top, text="Vt", ).grid(row=2, column=10)
    ld3 = Label(top, text="Vb", ).grid(row=3, column=10)
    ld4 = Label(top, text="Phi1", ).grid(row=4, column=10)
    ld5 = Label(top, text="Phi2", ).grid(row=5, column=10)
    ld6 = Label(top, text="Alpha1", ).grid(row=6, column=10)

    ldr = Label(top, text="Pro5B", ).grid(row=0, column=10)

    ed8 = Entry(top, bd=5)
    ed8.grid(row=1, column=11)
    ed9 = Entry(top, bd=5)
    ed9.grid(row=2, column=11)
    ed10 = Entry(top, bd=5)
    ed10.grid(row=3, column=11)
    ed11 = Entry(top, bd=5)
    ed11.grid(row=4, column=11)
    ed12 = Entry(top, bd=5)
    ed12.grid(row=5, column=11)
    ed14 = Entry(top, bd=5)
    ed14.grid(row=6, column=11)

    # ====================================================

    lh1 = Label(top, text="Pro1", ).grid(row=1, column=12)
    lh2 = Label(top, text="Pro2", ).grid(row=2, column=12)
    lh3 = Label(top, text="Pro3", ).grid(row=3, column=12)
    lh4 = Label(top, text="Pro4", ).grid(row=4, column=12)
    lh5 = Label(top, text="Pro5A", ).grid(row=5, column=12)
    lh6 = Label(top, text="Pro5B", ).grid(row=6, column=12)
    lh7 = Label(top, text="MDt", ).grid(row=0, column=13)

    eh8 = Entry(top, bd=5)
    eh8.grid(row=1, column=13)
    eh9 = Entry(top, bd=5)
    eh9.grid(row=2, column=13)
    eh10 = Entry(top, bd=5)
    eh10.grid(row=3, column=13)
    eh11 = Entry(top, bd=5)
    eh11.grid(row=4, column=13)
    eh12 = Entry(top, bd=5)
    eh12.grid(row=5, column=13)
    eh13 = Entry(top, bd=5)
    eh13.grid(row=6, column=13)

    B = Button(top, text="Submit", command=f1, activebackground="grey", activeforeground="yellow").grid(row=10,column=13)
    top.mainloop()

def help():
    help = Tk()
    h = Label(help, text="Saurabh is working on these calculation. Please try after some time.", width=300, height=300,
              font=('arial 20 bold')).pack()
    help.mainloop()

root = Tk()
root.title("PETROLEUM ENGINEERING")
# root.geometry("1500x800")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

head = Frame(root, width=1500, height=50, bg="powder blue", relief=SUNKEN)
head.pack(side=TOP)
f2 = Frame(root, width=1500, height=400, relief=SUNKEN)
f2.pack(side=TOP)

bot = Frame(root, width=1500, height=400, relief=SUNKEN)
bot.pack(side=TOP)
# ====================================================

l1 = Label(head, text="DIRECTIONAL DRILLING", font=('arial', 40, 'bold'), fg="dark grey", bd=10)
l1.grid(row=0, column=0, ipady=20)

# ====================================================
l3 = Label(f2, text="TYPE 1 PROFILE", font=('arial', 10, 'bold'))
l3.grid(row=1, column=1, ipadx=60, ipady=20)
l13 = Label(f2, text="WELL PROFILE SELECTION", font=('arial', 15, 'bold'))
l13.grid(row=0, column=2, ipadx=60, ipady=20)
b1 = Button(f2, command=proces1, text="PRESS TO SELECT TYPE 1").grid(row=2, column=1)

l4 = Label(f2, text="TYPE 2 PROFILE", font=('arial', 10, 'bold'))
l4.grid(row=3, column=1, ipadx=60, ipady=20)
b2 = Button(f2, command=proces5, text="PRESS TO SELECT TYPE 2").grid(row=4, column=1)

l5 = Label(f2, text="TYPE 3 PROFILE", font=('arial', 10, 'bold'))
l5.grid(row=5, column=1, ipadx=60, ipady=20)
b3 = Button(f2, command=help, text="PRESS TO SELECT TYPE 3").grid(row=6, column=1)

l6 = Label(f2, text="TYPE 4 PROFILE", font=('arial', 10, 'bold'))
l6.grid(row=1, column=2, ipadx=60, ipady=20)
b4 = Button(f2, command=proces7, text="PRESS TO SELECT TYPE 4").grid(row=2, column=2)

l7 = Label(f2, text="TYPE 5(A) PROFILE", font=('arial', 10, 'bold'))
l7.grid(row=3, column=2, ipadx=120, ipady=20)
b5 = Button(f2, command=proces11, text="PRESS TO SELECT TYPE 5(A)").grid(row=4, column=2)

l8 = Label(f2, text="TYPE 5(B) PROFILE", font=('arial', 10, 'bold'))
l8.grid(row=5, column=2, ipadx=120, ipady=20)
b6 = Button(f2, command=proces9, text="PRESS TO SELECT TYPE 5(B)").grid(row=6, column=2)
l11 = Label(f2, text="OPTIMIZATION", font=('arial', 10, 'bold'))
l11.grid(row=3, column=3, ipady=10)
b = Button(f2, command=help, text="Press to compare the well profiles Part 1 ").grid(row=4, column=3, pady=10)
p = Button(f2, command=comp, text="Press to compare the well profiles Part 2").grid(row=5, column=3, pady=10, padx=10)
l2 = Label(bot, text="DIRECTIONAL SURVEYING", font=('arial', 15, 'bold'))
l2.grid(row=0, column=1, pady=40)
b6 = Button(bot, command=drill_survy_calculation, text="Press to find the Change in Trajectory at different points").grid(row=1,column=1,pady=10,padx=20)
#b7 = Button(bot, command=help, text="Press to find the change in Trajectory between two points").grid(row=1, column=2,pady=10, padx=20)
root.mainloop()
