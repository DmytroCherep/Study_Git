class Rhombus:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a


    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError("side_a must be greater than 0")

        if name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("angle_a must be between 0 and 180")

            object.__setattr__(self, "angle_b", 180 - value)

        object.__setattr__(self, name, value)


# створення об'єкта
rhombus1 = Rhombus(10, 60)

print("Side a:", rhombus1.side_a)
print("Angle a:", rhombus1.angle_a)
print("Angle b:", rhombus1.angle_b)