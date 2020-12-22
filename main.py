from shapely.geometry import Point
import rasterio
from rasterio.windows import Window


def input_coordinates():
    try:
        input_e = float(input("Input British National Grid coordinate ""\n""Easting:"))
        input_n = float(input("Northing:"))
        pt = Point(input_e, input_n)
        if 430000 <= input_e <= 465000 and 80000 <= input_n <= 95000:
            return pt
        else:
            print ("The input location is out of range!")
            raise SystemExit
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        return input_coordinates()

dataset = rasterio.open("/Users/yolanda/Downloads/Material/elevation/SZ.asc")
print (dataset.crs)

#
# def highest_p:
#     window()


#input_coordinates()

