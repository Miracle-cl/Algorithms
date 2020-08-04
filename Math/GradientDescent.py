import math, random
from typing import List

# Problem: BestPositionServiceCentre
# Optim Algo: Adam > (Montenmum, RMSprop) > (GD, SGD)
# important params: alpha, decay, beta


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def gradient(xc, yc, start, end):
        dx = dy = 0
        for i in range(start, end):
            xi, yi = positions[i]
            tmp = math.sqrt((xc-xi)*(xc-xi) + (yc-yi)*(yc-yi))
            if tmp == 0:
                continue
            dx += (xc - xi) / tmp
            dy += (yc - yi) / tmp
        return dx, dy

    @staticmethod
    def get_distance(xc, yc, positions):
        dist = sum(((xc-xi)**2 + (yc-yi)**2)**0.5 for xi, yi in positions)
        return dist

    def getMinDistSum_GD(self, positions: List[List[int]]) -> float:
        eps = 1e-7
        alpha = 1
        decay = 1e-3
        n = len(positions)
        batch_size = n
        epoch = 1
        if n < 2:
            return 0

        xc = sum(x for x, _ in positions) / n
        yc = sum(y for _, y in positions) / n
        xp, yp = xc, yc

        batches = max(1, n - batch_size)
        while True:
            random.shuffle(positions)
            for i in range(batches):
                dx, dy = self.gradient(xc, yc, i, i+batch_size)
                xc -= alpha * dx
                yc -= alpha * dy

            if math.sqrt((xc-xp)**2 + (yc-yp)**2) < eps:
                break
            xp, yp = xc, yc
            alpha *= (1-decay)
            epoch += 1
        print(epoch) # 15640
        return self.get_distance(xc, yc, positions)

    def getMinDistSum_Monmentum(self, positions: List[List[int]]) -> float:
        eps = 1e-7
        alpha = 1
        beta = 0.99 # 0.9
        beta_1 = 1 - beta
        vdx = vdy = 0
        decay = 1e-3 # Learning rate decay small so slower, if faster then local optimum
        epoch = 1
        n = len(positions)
        batch_size = n
        if n < 2:
            return 0
        
        xc = sum(x for x, _ in positions) / n
        yc = sum(y for _, y in positions) / n
        xp, yp = xc, yc

        # batches = max(1, n - batch_size)
        while True:
            # random.shuffle(positions)
            # for i in range(batches):
            #     dx, dy = gradient(xc, yc, i, i+batch_size)
            dx, dy = self.gradient(xc, yc, 0, batch_size)
            vdx = beta * vdx + beta_1 * dx
            vdy = beta * vdy + beta_1 * dy
            xc -= alpha * vdx
            yc -= alpha * vdy

            if math.sqrt((xc-xp)**2 + (yc-yp)**2) < eps:
                break
            xp, yp = xc, yc
            alpha *= (1-decay)
            epoch += 1
        print(epoch) # 9582
        return self.get_distance(xc, yc, positions)

    def getMinDistSum_RMSprop(self, positions: List[List[int]]) -> float:
        eps = 1e-7
        alpha = 1
        beta = 0.99
        beta_1 = 1 - beta
        sdx = sdy = 0
        decay = 1e-2 # larger, so faster
        epoch = 1
        n = len(positions)
        batch_size = n
        if n < 2:
            return 0
        
        xc = sum(x for x, _ in positions) / n
        yc = sum(y for _, y in positions) / n
        xp, yp = xc, yc

        while True:
            dx, dy = self.gradient(xc, yc, 0, batch_size)
            sdx = beta * sdx + beta_1 * dx * dx 
            sdy = beta * sdy + beta_1 * dy * dy
            xc -= alpha * dx / (math.sqrt(sdx) + 1e-8)
            yc -= alpha * dy / (math.sqrt(sdy) + 1e-8)

            if math.sqrt((xc-xp)**2 + (yc-yp)**2) < eps:
                break
            xp, yp = xc, yc
            alpha *= (1-decay)
            epoch += 1
        print(epoch) # 1563
        return self.get_distance(xc, yc, positions)

    def getMinDistSum_Adam(self, positions: List[List[int]]) -> float:
        eps = 1e-7
        alpha = 1
        vbeta, vbeta_1 = 0.9, 0.1
        sbeta, sbeta_1 = 0.999, 0.001
        vdx = vdy = 0
        sdx = sdy = 0
        decay = 1e-2
        epoch = 1
        n = len(positions)
        batch_size = n
        if n < 2:
            return 0
        
        xc = sum(x for x, _ in positions) / n
        yc = sum(y for _, y in positions) / n
        xp, yp = xc, yc

        while True:
            dx, dy = self.gradient(xc, yc, 0, batch_size)
            
            vcorr = 1 #- math.pow(vbeta, epoch+20) # in here if correct the vdx is too large
            vdx = (vbeta * vdx + vbeta_1 * dx) / vcorr
            vdy = (vbeta * vdy + vbeta_1 * dy) / vcorr
            
            scorr = 1 #- math.pow(sbeta, epoch+20)
            sdx = (sbeta * sdx + sbeta_1 * dx * dx) / scorr
            sdy = (sbeta * sdy + sbeta_1 * dy * dy) /  scorr
            # print(xp, yp, dx, dy) # vdx, math.sqrt(sdx), vdy, math.sqrt(sdy))
            xc -= alpha * vdx / (math.sqrt(sdx) + 1e-8)
            yc -= alpha * vdy / (math.sqrt(sdy) + 1e-8)

            if math.sqrt((xc-xp)**2 + (yc-yp)**2) < eps:
                break
            xp, yp = xc, yc
            alpha *= (1-decay)
            epoch += 1
        print(epoch) # 1305
        return self.get_distance(xc, yc, positions)

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # ternary search : slowest (same as unoptimized gradient descent)
        if len(positions) < 2:
            return 0
            
        eps = 1e-7

        def get_distance(xc, yc, positions):
            dist = sum(((xc-xi)**2 + (yc-yi)**2)**0.5 for xi, yi in positions)
            return dist

        def searchY(xc):
            # if xc fixed, find the best yc to make distance minimum
            yl, yr = 0, 100
            while yr - yl > eps:
                y1 = yl + (yr - yl) / 3
                y2 = y1 + (yr - yl) / 3
                dist1 = get_distance(xc, y1, positions)
                dist2 = get_distance(xc, y2, positions)
                if dist1 < dist2:
                    yr = y2
                elif dist1 == dist2:
                    yl, yr = y1, y2
                else:
                    yl = y1
            return yl
            
        def searchX(xl=0, xr=100):
            while xr - xl > eps:
                x1 = xl + (xr - xl) / 3
                x2 = x1 + (xr - xl) / 3
                y1 = searchY(x1)
                y2 = searchY(x2)
                dist1 = get_distance(x1, y1, positions)
                dist2 = get_distance(x2, y2, positions)
                if dist1 < dist2:
                    xr = x2
                elif dist1 == dist2:
                    xl, xr = x1, x2
                else:
                    xl = x1
            return xl, searchY(xl)

        xc, yc = searchX()
        dist = get_distance(xc, yc, positions)
        return dist


if __name__ == '__main__':
    positions = [[55,91],[83,86],[48,8],[71,31],[50,28],[28,52],[89,18],[61,5],[100,100],
                 [63,94],[93,49],[82,72],[17,9],[63,48],[83,96],[47,2],[43,50],[95,32],
                 [87,74],[39,80],[57,15],[98,95],[37,53]] # 871.35101
    # positions = [[27,90],[99,75],[99,38]]
    # positions = [[44,23],[18,45],[6,73],[0,76],[10,50],[30,7],[92,59],[44,59],[79,45],[69,37],[66,63],[10,78],[88,80],[44,87]]
    # positions = [[9,9],[31,1],[28,61],[14,42],[95,98],[37,69]]
    # positions = [[16,56],[4,87],[80,26],[76,68],[89,23],[8,55]]
    ss = Solution()
    # res_gd = ss.getMinDistSum_GD(positions) # 499.28078 , 109.30317 224.7675, 871.35101
    # res_monmentum = ss.getMinDistSum_Monmentum(positions)
    # res_RMSprop = ss.getMinDistSum_RMSprop(positions)
    res_Adam = ss.getMinDistSum_Adam(positions)
    print(res_Adam)