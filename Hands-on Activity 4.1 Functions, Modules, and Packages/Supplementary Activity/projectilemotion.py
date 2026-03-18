import math

def projectilemotion_solver(velocity, angle):
    g = 9.8  # this is the costant gravity on the earth (I learned this in physics)

    angle_rad = math.radians(angle)

    # The range
    R = (velocity**2 * math.sin(2 * angle_rad)) / g

    # The max height
    h = (velocity**2 * (math.sin(angle_rad))**2) / (2 * g)

    return R, h