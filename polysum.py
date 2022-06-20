import math
def polysum(n, s):

    #Find the area of the polygon with the formula provided
    area = (0.25 * n * s ** 2) / math.tan(math.pi/n)

    #Find the perimeter by multiplying the number
    #of sides and the length of one side
    perimeter = n * s

    #Get the sum by adding the area and the square of the perimeter
    sum = area + perimeter ** 2

    #Return the sum with only four decimal places
    return round(sum, 4)