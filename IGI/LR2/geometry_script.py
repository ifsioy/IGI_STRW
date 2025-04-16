from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
from geometric_lib.square import area as square_area, perimeter as square_perimeter

def main():
    radius = float(input("Enter circle radius: "))
    print(f"Area: {circle_area(radius)}")
    print(f"Perimeter: {circle_perimeter(radius)}")
    
    length = float(input("Enter square size: "))
    print(f"Area: {square_area(length)}")
    print(f"Perimeter: {square_perimeter(length)}")

if __name__ == "__main__":
    main()
