def rectangles(x1,y1,x2,y2,x3,y3,x4,y4):
    xA,xB = [x1,x2],[x3,x4]
    yA,yB = [y1,y2],[y3,y4]

    max_xA = max(xA)
    min_xB = min(xB)
    max_yA = max(yA)
    min_yB = min(yB)
    min_yA = min(yA)
    max_yB = max(yB)
    min_xA = min(xA)
    max_xB = max(xB)

    if max_xA<min_xB or max_yA <min_yB  or min_yA > max_yB:
        return f'Прямоугольники не пересекаются'
    elif max_xA > min_xB and  min_xA < min_xB:
        s = (max_xA - min_xB) * (max_yA -min_yB)
        return f'Прямоугольники пересекаются, полощадь пересечения равна {s}'
    else:
        s = (max_xB - min_xA) * (max_yB - min_yA)
        return f'Прямоугольники пересекаются, полощадь пересечения равна {s}'

def main():
    print(rectangles(x1=1,y1=1,x2=5,y2=4,x3=3,y3=1,x4=8,y4=1))

if __name__ == '__main__':
    main()