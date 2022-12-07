h_actual = 6.626e-34 #Actual value of plank's costant


def plank_value(V1, V2, x1, x2):
    e = 1.6e-19  # elementary charge value in coulombs
    c = 3e8  # speed of light in metres per second
    k1 = e/c
    l_blue = 4565e-10  # wavelength of blue in metres
    l_green = 5645e-10  # wavelength of green in metres
    l_red = 6125e-10  # wavelength of red in metres

    if (x1 == 'b' and x2 == 'g') or (x1 == 'g' and x2 == 'b'):
        diff = l_green - l_blue  # difference in wavelength of green and blue
        mul = l_green*l_blue  # product of wavelengths of green and blue
    elif (x1 == 'g' and x2 == 'r') or (x1 == 'r' and x2 == 'g'):
        diff = l_red - l_green  # difference in wavelength of green and red
        mul = l_green*l_red  # product of wavelengths of green and red
    elif (x1 == 'r' and x2 == 'b') or (x1 == 'b' and x2 == 'r'):
        diff = l_red - l_blue  # difference in wavelength of red and blue
        mul = l_red*l_blue  # product of wavelengths of red and blue
    else:
        print("ERROR COMBINATION!!!")
        exit()

    vol_diff = V2 - V1
    print(f"k1 = {k1}\nvoltage difference = {vol_diff}\nwavelength products = {mul}\nwavelength difference = {diff}\n")
    h = (k1*vol_diff*mul)/diff
    return h


def experiment_analysis(b, g, r, name='DATASET DEFAULT'):
    print(
        f"######################### {name} ################################################################################################################################")

    print(f"Planks constant combination of blue and green: \n")
    h1 = plank_value(g, b, 'g', 'b')
    print("Planks Contant b+g = ", h1)
    print("----------------------------------------------------------------------------------------------")
    print(f"Planks constant combination of red and green: \n")
    h2 = plank_value(r, g, 'g', 'r')
    print("Planks Contant g+r = ", h2)
    print("----------------------------------------------------------------------------------------------")
    print(f"Planks constant combination of blue and red: \n")
    h3 = plank_value(r, b, 'r', 'b')
    print("Planks Contant r+b = ", h3)
    print("----------------------------------------------------------------------------------------------")
    print("AVERAGE OF ALL PLANKS VALUES: ")
    h_average = (h1 + h2 + h3)/3
    print(h_average)
    error = ((h_actual - h_average)/h_average)*100
    print(f"ERROR IN DATA RESULT IS {error}%")


if __name__ == '__main__':
    experiment_analysis(0.659, 0.428, 0.222, "DATASET 1")
    experiment_analysis(0.668, 0.438, 0.257, "DATASET 2")
    experiment_analysis(0.672, 0.419, 0.364, "DATASET 3")
    experiment_analysis(0.666, 0.428, 0.281, "DATASET 4: Average")
    experiment_analysis(
        1.05, 0.85, 0.54, "DATASET 5: Minimized Error by linear addition")
