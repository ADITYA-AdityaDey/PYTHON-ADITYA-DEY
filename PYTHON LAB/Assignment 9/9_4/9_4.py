import math

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def main():
    # Test Data
    radius = 6
    height = 4

    # Calculate volume and surface area
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)

    # Display the results
    print(f"Volume is: {volume}")
    print(f"Surface Area is: {surface_area}")

if __name__ == "__main__":
    main()

