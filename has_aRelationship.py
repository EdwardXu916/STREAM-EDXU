# Test for class


class X:
    def __init__(self, fuel):
        self.fuel = int(fuel)


class Y:
    def __init__(self, fire):
        self.fire = int(fire)


class Z:
    def __init__(self, index_x, index_y):
        self.x = index_x
        self.y = index_y

    @property
    def outcome(self):
        outcome = self.x.fuel + self.y.fire
        return outcome

class W:
    def __init__(self, index_z):
        self.z = listZs[index_z]

    @property
    def outcome(self):
        outcome = self.z.outcome - 1
        return outcome


class P:
    def __init__(self, listxs):
        self.x = listxs

    @property
    def sumx(self):
        sumx = 0
        int(sumx)
        for x in self.x.values():
            sumx = sumx + int(x.fuel)
        return sumx


listXs = {'x_1': X(10)}
# listXs['x_2'] = X(20)
y_1 = Y(20)

index_X = 'x_1'
index_Y = 'y_1'

listZs = {'z_1': Z(index_X, index_X)}

index_z = 'z_1'

listWs = {'w_1': W(index_z)}












class Wheel(object):
    # would probably have properties like RPM, traction, etc







class TwoWheelDriveInterface(object):
    def __init__(self, *args):
        self.front_left_wheel = Wheel(*args)
        self.front_right_wheel = Wheel(*args)
        self.rear_left_wheel = Wheel(*args)
        self.rear_right_wheel = Wheel(*args)
        self.wheels = [self.front_left_wheel, self.front_right_wheel,
                       self.rear_left_wheel, self.rear_right_wheel]

    def accelerate(self, vector):
        for wheel in [self.front_left_wheel, self.front_right_wheel]:
            wheel.RPM += vector


class FourWheelDriveInterface(object):
    def __init__(self, *args):
        # same as TwoWheelDriveInterface. In fact these could both
        # inherit from a common DriveInterface class and override
        # accelerate! (that is, both TwoWheelDriveInterface and
        # FourWheelDriveInterace ARE-A DriveInterface)

    def accelerate(self, vector):
        for wheel in self.wheels:
            wheel.RPM += vector


class Car(object):
    def __init__(self, color,speed,coolness,two_wheel_drive=False,*wheelargs):
        self.color = color
        self.speed = speed
        self.coolness = coolness
        if two_wheel_drive:
            self.driveinterface = TwoWheelDrive(*wheelargs)
        else:
            self.driveinterface = FourWheelDrive(*wheelargs)
        self.accelerate = self.driveinterface.accelerate # bind the methods together


my_car = Car(color='red',speed='very fast',coolness='very',two_wheel_drive=True)
my_car.accelerate(float('inf')) # runs TwoWheelDriveInterface().accelerate(float('inf'))