import math

def calculate_volume_of_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

if __name__ == "__main__":
    radius = 3
    print(f"The volume of the sphere with radius {radius} is {calculate_volume_of_sphere(radius)}")
