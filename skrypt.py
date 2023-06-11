import numpy as np
from math import *
import argparse

class Transformacje:

    def __init__(self, model: str = "wgs84"):
        if model == "wgs84":
            self.a = 6378137.0
            self.b = 6356752.31424518
        elif model == "grs80":
            self.a = 6378137.0
            self.b = 6356752.31414036
        elif model == "krasowski":
            self.a = 6378245.0
            self.b = 6356863.019
        else:
            raise NotImplementedError(f"{model} model not implemented")
        self.flat = (self.a - self.b) / self.a
        self.e2 = (2 * self.flat - self.flat ** 2)

# 1 XYZ -> BLH
    def hirvonen(self, X, Y, Z):
        p = np.sqrt(X ** 2 + Y ** 2)
        f = np.arctan(Z / (p * (1 - self.e2)))
        while True:
            N = self.Np(f)
            h = (p / np.cos(f)) - N
            fs = f
            f = np.arctan(Z / (p * (1 - self.e2 * N / (N + h))))
            if np.abs(fs - f) < (0.000001 / 206265):
                break
        l = np.arctan2(Y, X)
        return (f, l, h)


    # 2 BLH -> XYZ
    def flh2XYZ(self, f, l, h):
        N = self.Np(f)
        X = (N + h) * np.cos(f) * np.cos(l)
        Y = (N + h) * np.cos(f) * np.sin(l)
        Z = (N * (1 - self.e2) + h) * np.sin(f)
        return (X, Y, Z)


    # 4 BL-> u2000
    def Np(self, f):
        N = self.a/ np.sqrt(1 - self.e2 * np.sin(f) ** 2)
        return (N)


    def Mp(self, f, a):
        M = (self.a * (1 - self.e2)) / np.sqrt((1 - self.e2 * np.sin(f) ** 2) ** 3)
        return (M)


    def u2000(self, f, l):
        m00 = 0.999923
        b2 = self.a ** 2 * (1 - self.e2)
        ep2 = (self.a ** 2 - b2) / b2
        t = np.tan(f)
        n2 = ep2 * np.cos(f) ** 2
        N = self.Np(f)

        l = np.degrees(l)
        ns = 0
        l0 = 0
        if l > 13.5 and l <= 16.5:
            ns = 5
            l0 = 15
        elif l > 16.5 and l <= 19.5:
            ns = 6
            l0 = 18
        elif l > 19.5 and l <= 22.5:
            ns = 7
            l0 = 21
        elif l > 22.5 and l <= 25.5:
            ns = 8
            l0 = 24
        else:
            raise ValueError("u2000 - wrong l value")

        l = np.radians(l)
        l0 = np.radians(l0)
        d_l = l - l0

        A0 = 1 - (self.e2 / 4) - ((3 * (self.e2 ** 2)) / 64) - ((5 * (self.e2 ** 3)) / 256)
        A2 = (3 / 8) * (self.e2 + ((self.e2 ** 2) / 4) + ((15 * (self.e2 ** 3)) / 128))
        A4 = (15 / 256) * (self.e2 ** 2 + ((3 * (self.e2 ** 3)) / 4))
        A6 = (35 * (self.e2 ** 3)) / 3072

        sigma = self.a * ((A0 * f) - (A2 * np.sin(2 * f)) + (A4 * np.sin(4 * f)) - (A6 * np.sin(6 * f)))
        xgk = sigma + ((d_l ** 2) / 2) * N * np.sin(f) * np.cos(f) * (
                    1 + ((d_l ** 2) / 12) * ((np.cos(f)) ** 2) * (5 - t ** 2 + 9 * n2 + 4 * (n2 ** 2)) + (
                        (d_l ** 4) / 360) * ((np.cos(f)) ** 4) * (
                                61 - (58 * (t ** 2)) + (t ** 4) + (270 * n2) - (330 * n2 * (t ** 2))))
        ygk = d_l * N * np.cos(f) * (
                    1 + (d_l ** 2) / 6 * np.cos(f) ** 2 * (1 - t ** 2 + n2) + ((d_l ** 4) / 120) * np.cos(f) ** 4 * (
                        5 - 18 * t ** 2 + t ** 4 + 14 * n2 - 58 * n2 * t ** 2))
        x2000 = xgk * m00
        y2000 = ygk * m00 + ns * 1000000 + 500000
        return (x2000, y2000)


    # BL -> 1992

    def u1992(self, f, l):
        m0 = 0.9993
        b2 = self.a ** 2 * (1 - self.e2)
        ep2 = (self.a ** 2 - b2) / b2
        t = np.tan(f)
        n2 = ep2 * np.cos(f) ** 2
        N = self.Np(f)
        l0 = radians(19)
        dl = l - l0

        A0 = 1 - (self.e2 / 4) - ((3 * (self.e2 ** 2)) / 64) - ((5 * (self.e2 ** 3)) / 256)
        A2 = (3 / 8) * (self.e2 + ((self.e2 ** 2) / 4) + ((15 * (self.e2 ** 3)) / 128))
        A4 = (15 / 256) * (self.e2 ** 2 + ((3 * (self.e2 ** 3)) / 4))
        A6 = (35 * (self.e2 ** 3)) / 3072

        sigma = self.a * ((A0 * f) - (A2 * np.sin(2 * f)) + (A4 * np.sin(4 * f)) - (A6 * np.sin(6 * f)))

        xgk = sigma + (dl ** 2 / 2) * N * np.sin(f) * np.cos(f) * (
                    1 + (dl ** 2 / 12) * np.cos(f) ** 2 * (5 - t ** 2 + 9 * n2 + 4 * n2 ** 2) + (dl ** 4 / 360) * np.cos(
                f) ** 4 * (61 - 58 * t ** 2 + t ** 4 + 270 * n2 - 330 * n2 * t ** 2))
        ygk = dl * N * np.cos(f) * (
                    1 + dl ** 2 / 6 * np.cos(f) ** 2 * (1 - t ** 2 + n2) + (dl ** 4 / 120) * np.cos(f) ** 4 * (
                        5 - 18 * t ** 2 + t ** 4 + 14 * n2 - 58 * n2 * t ** 2))
        x92 = xgk * m0 - 5300000
        y92 = ygk * m0 + 500000
        return (x92, y92)



    #3 XYZ -> neu
    def xyz2neu(self, xa, ya, za, xb, yb, zb, f, l, h):
        N = self.Np(f)
        X0 = (N + h) * np.cos(f) * np.cos(l)
        Y0 = (N + h) * np.cos(f) * np.sin(l)
        Z0 = ((1 - self.e2) * N + h) * np.sin(f)
        
        dxyz = np.array([xb,yb,zb]) - np.array([xa,ya,za])
        X, Y, Z = dxyz - np.array([X0, Y0, Z0])
        
        sin_f = np.sin(f)
        cos_f = np.cos(f)
        sin_l = np.sin(l)
        cos_l = np.cos(l)
        
        R = np.array([[-sin_l, cos_l, 0],
                      [-sin_f*cos_l, -sin_f*sin_l,  cos_f],
                      [ cos_f*cos_l,  cos_f*sin_l,  sin_f]])
        
        NEU = np.dot(R, np.array([X, Y, Z]))
        
        n = NEU[0]
        e = NEU[1]
        u = -NEU[2]
        return(n,e,u)



if __name__ == '__main__':
    transformationObject = Transformacje()
    parser = argparse.ArgumentParser()
    parser.add_argument("transformation_type", help="type of transformation - choose one"
                                                    " of the following: hirvonen, flh2XYZ, xyz2neu, u2000, u1992")
    parser.add_argument("input_file", help="path to file with data")
    parser.add_argument("output_file", help="where to save the results")
    #dodane
    parser.add_argument("-m", "--model", help="ellipsoid model - choose one of the following: wgs84, grs80, krasowski", default="wgs84")
    args = parser.parse_args()
    #dodane
    transformationObject = Transformacje(model=args.model)

    if args.transformation_type == "hirvonen" or args.transformation_type == "flh2XYZ":

        with open(args.input_file) as f:
            data = f.read().splitlines()
        data = [list(map(float, x.split(','))) for x in data]


        results = []
        for line in data:
            if args.transformation_type == "hirvonen":
                results.append(transformationObject.hirvonen(line[0], line[1], line[2]))
            elif args.transformation_type == "flh2XYZ":
                results.append(transformationObject.flh2XYZ(line[0], line[1], line[2]))

        with open(args.output_file, 'w') as f:
            for line in results:
                f.write(f'{line[0]},{line[1]},{line[2]}\n')

    elif args.transformation_type == "u2000" or args.transformation_type == "u1992":

        with open(args.input_file) as f:
            data = f.read().splitlines()
        data = [list(map(float, x.split(','))) for x in data]

        results = []
        for line in data:
            if args.transformation_type == "u2000":
                results.append(transformationObject.u2000(line[0], line[1]))
            elif args.transformation_type == "u1992":
                results.append(transformationObject.u1992(line[0], line[1]))

        with open(args.output_file, 'w') as f:
            for line in results:
                f.write(f'{line[0]},{line[1]}\n')


    elif args.transformation_type == "xyz2neu":
            
        with open(args.input_file) as f:
            data = f.read().splitlines()
        data = [list(map(float, x.split(','))) for x in data]
            
        results = []
        for line in data:
            if args.transformation_type == "xyz2neu":
                results.append(transformationObject.xyz2neu(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
             
        with open(args.output_file, 'w') as f:
            for line in results:
                f.write(f'{line[0]},{line[1]},{line[2]}\n')  



    else:
        print("Wrong transformation type - run program again"
              " and choose one of the following: hirvonen, flh2XYZ, xyz2neu, u2000, u1992")
