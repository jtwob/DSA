class Solution:

    def calcArea(self, points: List[List[int]]) -> float:
        x1 = points[0][0]
        x2 = points[1][0]
        x3 = points[2][0]
        y1 = points[0][1]
        y2 = points[1][1]
        y3 = points[2][1]
        base = 0
        height = 0

        if y1 != y2 or x1 != x2:
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

            height = pow(pow(x_intercept-x3, 2) + pow(y_intercept-y3, 2), 0.5)
        
        if y1 == y2:
            base = abs(x1-x2)
            height = abs(y3-y1)
        if x1 == x2:
            base = abs(y1-y2)
            height = abs(x3-x2)

        area = 0.5 * base * height
        # print(base, height, "p1 (", x1, ",",y1,")", "p2 (", x2, ",",y2,")", "p3 (", x3, ",",y3,")")
        return area
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Prelim algorithm
        # Recursively calculate areas from all points
        # Return max

        max = 0

        for i in range(len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    area = self.calcArea([points[i], points[j], points[k]])
                    if area > max:
                        print("New Max Found: ", area, "p1 (",points[i][0],",",points[i][1],")","p2 (",points[j][0],",",points[j][1],")", "p3 (",points[k][0],",",points[k][1],")")
                        max = area
        return max
    
