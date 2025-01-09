class Solution:

    def calcArea(self, points: List[List[int]]) -> float:
        x1 = points[0][0]
        x2 = points[1][0]
        x3 = points[2][0]
        y1 = points[0][1]
        y2 = points[1][1]
        y3 = points[2][1]
        m_base = 0
        m_height = 0
        x_intercept = 0

        base = pow(pow(x1-x2, 2) + pow(y1-y2, 2), 0.5)
        if x1 != x2:
            m_base = (y1-y2)/(x1-x2)
        else:
            m_height = 0
        b_base = y1 - m_base * x1
        if m_base != 0:
            m_height = -1/m_base
        b_height = y3 - m_height * x3
        if x1 == x2:
            x_intercept = x1
            y_intercept = y3
        else:
            if m_base != m_height:
                x_intercept = (b_height - b_base) / (m_base - m_height)
            y_intercept = m_base * x_intercept + b_base

        h = pow(pow(x_intercept-x3, 2) + pow(y_intercept-y3, 2), 0.5)

        area = 0.5 * base * h
        print(base, h, "p1 (", x1, ",",y1,")", "p2 (", x2, ",",y2,")", "p3 (", x3, ",",y3,")", area)
        return area
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Prelim algorithm
        # Recursively calculate areas from all points
        # Return max

        max = 0

        for i in range(len(points)-2):
            for j in range(i, len(points)-1):
                for k in range(j, len(points)):
                    area = self.calcArea([points[i], points[j], points[k]])
                    if area > max:
                        max = area
        return max
    
