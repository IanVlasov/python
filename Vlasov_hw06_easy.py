# coding: utf-8

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Считаем, что фигуры плоские


from math import sqrt


class Triangle:
    def __init__(self, point1, point2, point3):
        try:
            # Проверяем, что точки не лежат на одной прямой
            det = (
                    (point2[0] - point1[0]) * (point3[1] - point1[1]) -
                    (point2[1] - point1[1]) * (point3[0] - point1[0])
            )
            if det != 0:
                self.point1 = point1
                self.point2 = point2
                self.point3 = point3
                self._len_a = self.length(point1, point2)
                self._len_b = self.length(point1, point3)
                self._len_c = self.length(point2, point3)
            else:
                print("Точки лежат на одной прямой!")
        except TypeError:
            print("Вы ввели точки в неправильном формате,\n"
                  "Введите точки в формате (x1, y1), (x2, y2), (x3, y3)")

    @property
    def len_a(self):
        return self._len_a

    @property
    def len_b(self):
        return self._len_b

    @property
    def len_c(self):
        return self._len_c

    @staticmethod
    def length(point1, point2):
        length = sqrt(
            (point1[0] - point2[0])**2 +
            (point1[1] - point2[1])**2
        )
        return length

    def area(self):
        p = (self._len_a + self._len_b + self._len_c) / 2
        area = sqrt(
            p * (p - self._len_a) * (p - self._len_b) * (p - self._len_c)
        )
        return area

    # Для определения высоты необходимо указать вершину, из которой она опущена (1, 2 или 3)
    def height(self, point):
        if point == 1:
            height = (2 * self.area()) / self._len_c
            return height
        elif point == 2:
            height = (2 * self.area()) / self._len_b
            return height
        elif point == 3:
            height = (2 * self.area()) / self._len_a
            return height
        else:
            print("Укажите номер вершины, из которой опущена высота (1, 2 или 3)")

    def perimeter(self):
        perimeter = self._len_a + self._len_b + self._len_c
        return perimeter


if __name__ == "__main__":
    a = Triangle((0, 0), (1, 1), (0, 2))
    print(a.area(), a.perimeter(), a.height(2))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrap:
    def __init__(self, point1, point2, point3, point4):
        try:
            # Считаем, что точки введены в порядке их соедения (по вершинам ABCD)
            # Сначала проверяем, что данные точки вообще задают трапецию
            # Для этого необходимо проверить параллельность противоположных сторон (AB-CD или (BC-AD)
            # Проверку будем производить по угловым коэффициентам уравнений прямых через две соседние точки

            coefs = []
            all_points = [point1, point2, point3, point4]

            for i, item in enumerate(all_points):
                if i != len(all_points) - 1:
                    new_coef = (all_points[i + 1][1] - all_points[i][1]) / (all_points[i + 1][0] - all_points[i][0])
                    coefs.append(abs(new_coef))
                else:
                    new_coef = (all_points[0][1] - all_points[i][1]) / (all_points[0][0] - all_points[i][0])
                    coefs.append(abs(new_coef))

            len_a = self.length(point1, point2)
            len_b = self.length(point2, point3)
            len_c = self.length(point3, point4)
            len_d = self.length(point4, point1)

            # проверяем параллельность и равенство двух других сторон друг другу
            if (
                    (coefs[0] == coefs[2] and len_b == len_d and len_a != len_c) or
                    (coefs[1] == coefs[3] and len_a == len_c and len_b != len_d)
            ):

                # Если одна из пар прямых оказалась параллельна, то необходимо проверить,
                # что любые три точки не лежат на одной прямой
                det = (
                        (point2[0] - point1[0]) * (point3[1] - point1[1]) -
                        (point2[1] - point1[1]) * (point3[0] - point1[0])
                )

                # Если все проверки прошли успешно, создаем объект
                if det != 0:
                    self.point1 = point1
                    self.point2 = point2
                    self.point3 = point3
                    self.point4 = point4
                    self._len_a = len_a
                    self._len_b = len_b
                    self._len_c = len_c
                    self._len_d = len_d
                else:
                    print("Точки лежат на одной прямой!")
            else:
                print("Это не равнобедренная трапеция!")
        except TypeError:
            print("Вы ввели точки в неправильном формате,\n"
                  "Введите точки в формате (x1, y1), (x2, y2), (x3, y3), (x4, y4)")


    @property
    def len_a(self):
        return self._len_a

    @property
    def len_b(self):
        return self._len_b

    @property
    def len_c(self):
        return self._len_c

    @property
    def len_d(self):
        return self._len_d

    @staticmethod
    def length(point1, point2):
        length = sqrt(
            (point1[0] - point2[0])**2 +
            (point1[1] - point2[1])**2
        )
        return length

    def perimeter(self):
        perimeter = self._len_a + self._len_b + self._len_c + self._len_d
        return perimeter


if __name__ == "__main__":
    ABCD = IsoscelesTrap((0, 0), (2, 2), (4, 2), (6, 0))
    print(ABCD.perimeter())
