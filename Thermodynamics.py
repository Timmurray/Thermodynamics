import math

# celsius is represented by 'C'
# kelvin is represented by 'K'
# farenheight is represented by 'F'

#simple conversions of temperature

def convertCelsiusToKelvin(celsius):
    temperature = celsius + 273.15
    return temperature + ' K'

def convertCelsiusToFarenheight(celsius):
    temperature = (9/5)*celsius + 32
    return temperature + ' F'

def convertFarenheightToCelsius(farenheight):
    temperature = (5/9)*farenheight - 32
    return temperature + ' C'
    
def convertFarenheightToKelvin(farenheight):
    temperature = (5/9)*farenheight + 241.15
    return temperature + ' K'

def convertKelvinToCelsius(kelvin):
    temperature = kelvin - 273.15
    return temperature + ' C'
    
def convertKelvinToFarenheight(kelvin):
    temperature = (9/5)*(kelvin - 273.15) + 32
    return temperature + ' F'


# the coefficient of linear expansion may be derived through a formula
# the known coefficients of linear expansion from most materials will exist in a dictionary
# the known  coefficients of volume expanison for most materials will exist in a dictionary

def coefficientLinearExpansion(finalLength, initialLength, finalTemperature, initialTemperature):
    alpha = ((finalLength-initialLength)/(finalTemperature-initialTemperature))/(initialLength)
    return alpha

#solving initial length of material with known coefficient of linear expansion, final temperature, initial temperature, and final length
def initialLengthLinearExpansion(alpha, finalTemperature, initialTemperature, finalLength):
    initialLength = (finalLength)/(alpha*(finalTemperature-initialTemperature)+1)
    return initialLength

#solving the final length of a material with known coefficient of linear expansion, final temperature, initial temperature, and initial length
def finalLengthLinearExpansion(alpha, finalTemperature, initialTemperature, initialLength):
    finalLength = (initialLength*alpha*(finalTemperature-initialTemperature)) + 1
    return finalLength

#solving initial temperature in Kelvin with coefficient of linear expansion, initial length, final length, and final temperature

def initialTemperatureLinearExpansion(alpha, initialLength, finalLength, finalTemperature):
    initialTemperature = -((finalLength-initialLength)/(alpha*initialLength)) + finalTemperature
    return initialTemperature

#solving final temperature in Kelvin with coefficient of linear expansion, initial length, final length, and initial temperature

def finalTemperatureLinearExpansion(alpha, initialLength, finalLength, initialTemperature):
    finalTemperature = (finalLength-initialLength)/(alpha*initialLength) + initialTemperature
    return finalTemperature

# solving for beta the coefficient of volume expansion with known initial volume, final volume, initial temperature, and final temperature

def coefficientVolumeExpansion(initialVolume, finalVolume, initialTemperature, finalTemperature):
    beta = (1/initialVolume)*((finalVolume-initialVolume)/(finalTemperature-initialTemperature))
    return beta

#solving for the initial volume using the volume expansion formula with known beta, final volume, initial temperature, and final temperature

def initialVolumeVolumeExpansion(beta, finalVolume, initialTemperature, finalTemperature):
    initialVolume = (finalVolume)/(beta*(finalTemperature-initialTemperature)+1)
    return initialVolume

#solving for final volume using the volume expansion formula with known beta coefficient of volume expansion, initial volume, initial temperature and final temperature

def finalVolumeVolumeExpansion(beta, initialVolume, initialTemperature, finalTemperature):
    finalVolume = (initialTemperature*beta*(finalTemperature-initialTemperature)) + 1
    return finalVolume

#solving for initial temperature using the volume expansion formula with a known beta, initial volume, final volume, and final temperature

def initialTemperatureVolumeExpansion(beta, initialVolume, finalVolume, finalTemperature):
    initialTemperature = -((finalVolume-initialVolume) / (beta*initialVolume)) + finalTemperature
    return initialTemperature

#solving for final temperature using the volume expansion formula with known beta, initial volume, final volume, and initial temperature

def finalTemperatureVolumeExpansion(beta, initialVolume, finalVolume, initialTemperature):
    finalTemperature = (finalVolume-initialVolume)/(beta*initialVolume) + initialTemperature
    return finalTemperature

Rj = 8.314

Rl = .0821

Na = 6.022*math.pow(10,23)

print("This is a calculator for Thermodynamics\n")


print("\niv : initial Volume of container\n fv : final volume of container\n it : initial temperature of gas\n ft : final temperature of gas\n ip : initial pressure of gas in container\n")
print("fp : final pressure of gas in container\nb : coefficient of volume expansion\n il: initial length\n fl : final length\n a: coefficient of linear expansion")

while True:
    type = input("if there is linear expansion type L if there is volume expansion type V if the problem gives only a limited number of variables type o (l/v/o): \t")

    value = input("\nselect an option you would like to solve for: \t")     

    if(value.lower() == 'a' & type.lower() == 'l'):
        initialLength = input("What is the initial length of the material?\n")
        finalLength = input("what is the final length of the material?\n")
        initialTemperature = input("What is the initial temperature of the material?\n")
        finalTemperature = input("What is the final temerature of the material?\n")
        print(coefficientLinearExpansion(finalLength, initialLength, finalTemperature, initialTemperature))        
    
    elif(value.lower() == 'il' & type.lower() == 'l'):
        alpha = input("what is the coefficient of linear expansion of the material?\n")
        finalTemperature = input("what is the final temperature of the material?\n")
        initialTemperature = input("what is the initial temperature of the material?\n")
        finalLength = input("what is the final length of the material?\n")
        print(initialLengthLinearExpansion(alpha, finalTemperature, initialTemperature, finalLength))

    elif(value.lower() == 'fl' & type.lower() == 'l'):
        alpha = input("what is the coefficient of linear expansion of the material?\n")
        finalTemperature = input("what is the final temperature of the material?\n")
        initialTemperature = input("what is the initial temperature of the material?\n")
        initialLength = input("what is the initial length of the material?\n")
        print(finalLengthLinearExpansion(alpha, finalTemperature, initialTemperature, initialLength))

    elif(value.lower() == 'ft' & type.lower() == 'l'):
        alpha = input("what is the coefficient of linear expansion of the material?\n")
        finalLength = input("what is the final length of the material?\n")
        initialTemperature = input("what is the initial temperature of the material?\n")
        initialLength = input("what is the initial length of the material?\n")
        print(finalTemperatureLinearExpansion(alpha, initialLength, finalLength, initialTemperature))

    elif(value.lower() == 'it' & type.lower() == 'l'):
        alpha = input("what is the coefficient of linear expansion of the material?\n")
        finalLength = input("what is the final length of the material?\n")
        finalTemperature = input("what is the final temperature of the material?\n")
        initialLength = input("what is the initial length of the material?\n")
        print(initialTemperatureLinearExpansion(alpha, initialLength, finalLength, finalTemperature))

    elif(value.lower() == 'iv' & type.lower() == 'v'):
        beta = input("what is the coefficient of volume expansion?\n")
        finalVolume = input("what is the final volume of the material?\n")
        initialTemperature = input("what is the initial temperature of the material?\n")
        finalTemperature = input("what is the final temeprature of the material?\n")
        print(initialVolumeVolumeExpansion(beta, finalVolume, initialTemperature, finalTemperature))

    elif(value.lower() == 'fv' & type.lower() == 'v'):
        beta = input("what is the coefficient of volume expansion?\n")
        initialVolume = input("what is the initial volume of the material?\n")
        initialTemperature = input("what is the initial temperature of the material?\n")
        finalTemperature = input("what is the final temeprature of the material?\n")
        print(finalVolumeVolumeExpansion(beta, initialVolume, initialTemperature, finalTemperature))

    elif(value.lower() == 'it' & type.lower() == 'v'):
        beta = input("what is the coefficient of volume expansion?\n")
        finalVolume = input("what is the final volume of the material?\n")
        initialVolume = input("what is the initial volume of the material?\n")
        finalTemperature = input("what is the final temeprature of the material?\n")
        print(initialTemperatureVolumeExpansion(beta, initialVolume, finalVolume, finalTemperature))        
    elif(value.lower() == 'ft' & type.lower() == 'v'):
        beta = input("what is the coefficient of volume expansion?\n")
        finalVolume = input("what is the final volume of the material?\n")
        initialVolume = input("what is the initial volume of the material?\n")
        initialTemperature = input("what is the initial temeprature of the material?\n")
        print(finalTemperatureVolumeExpansion(beta, initialVolume, finalVolume, initialTemperature))
    elif(value.lower() == 'b' & type.lower() == 'v'):
        finalVolume = input("what is the final volume of the material?\n")
        initialVolume = input("what is the initial volume of the material?\n")
        initialTemperature = input("what is the initial temeprature of the material?\n")
        print(coefficientVolumeExpansion(initialVolume, finalVolume, initialTemperature, finalTemperature))
    else:
        print("please input valid values.\n")
'''
initialTemperature = input("What is the initial temperature of the container? \t")

finalTemperature = input ("\nWhat is the final temperature of the container?\t")

initialPressure = input("\nWhat is the initial pressure of the container? \t")

finalPressure = input("\nWhat is the final pressure of the gas? \t")

initialVolume = input("\nwhat is the initial Volume of the container? \t")

finalVolume = input("\nWhat is the final volume of the container? \t")
'''


