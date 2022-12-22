import math

# celsius is represented by 'C'
# kelvin is represented by 'K'
# farenheight is represented by 'F'

#simple conversions of temperature

def convertCelsiusToKelvin(celsius):
    temperature = celsius + 273.15
    return str(temperature) + ' K'

def convertCelsiusToFarenheight(celsius):
    temperature = (9/5)*celsius + 32
    return str(temperature) + ' F'

def convertFarenheightToCelsius(farenheight):
    temperature = (5/9)*farenheight - 32
    return str(temperature) + ' C'
    
def convertFarenheightToKelvin(farenheight):
    temperature = (5/9)*farenheight + 241.15
    return str(temperature) + ' K'

def convertKelvinToCelsius(kelvin):
    temperature = kelvin - 273.15
    return str(temperature) + ' C'
    
def convertKelvinToFarenheight(kelvin):
    temperature = (9/5)*(kelvin - 273.15) + 32
    return str(temperature) + ' F'


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

print("This is a calculator for Thermodynamics\n")

print("iv : initial Volume of container\n fv : final volume of container\n it : initial temperature of gas\n ft : final temperature of gas\n ip : initial pressure of gas in container\n")
print("fp : final pressure of gas in container\nb : coefficient of volume expansion\n il: initial length\n fl : final length\n a: coefficient of linear expansion")

value = input("select an option you would like to solve for: \t")     

if(value.lower() == 'iv')

elif(value.lower() == 'fv')

<<<<<<< Updated upstream
elif(value.lower() == 'it')

elif(value.lower() == 'ft')

elif(value.lower() == 'ip')

elif(value.lower() == 'fp')

elif(value.lower() == 'b')


=======
print("\n iv : initial Volume of container | fv : final volume of container\n it : initial temperature of gas | ft : final temperature of gas\n")
print("ip : initial pressure of gas in container | fp : final pressure of gas in container\n b : coefficient of volume expansion | a: coefficient of linear expansion\n")
print("il: initial length | fl : final length\n")

while True:
    value = input("\nselect an option you would like to solve for: \t")
    type = input("\nif there is linear expansion type L\nif there is volume expansion type V\nif the problem gives only a limited number of variables type o (l/v/o): \t")   

    if(type.lower() == 'l'):
        if(value.lower() == 'a'):
            initialLength = input("\nWhat is the initial length of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            initialTemperature = input("\nWhat is the initial temperature of the material?\t")
            finalTemperature = input("\nWhat is the final temerature of the material?\t")
            print("\nThe coefficient of linear expansion = "+coefficientLinearExpansion(float(finalLength), float(initialLength), float(finalTemperature), float(initialTemperature))+"\n")        
    
        elif(value.lower() == 'il'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            print("\nThe initial length of the material = "+initialLengthLinearExpansion(float(alpha), float(finalTemperature), float(initialTemperature), float(finalLength)+"m\n"))

        elif(value.lower() == 'fl'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material?\t")
            initialLength = input("\nwhat is the initial length of the material?\t")
            print("\nThe final length of the material = "+finalLengthLinearExpansion(float(alpha), float(finalTemperature), float(initialTemperature), float(initialLength))+"m\n")

        elif(value.lower() == 'ft'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material?\t")
            initialLength = input("\nwhat is the initial length of the material?\t")
            print("\nThe final temperature = " + finalTemperatureLinearExpansion(float(alpha), float(initialLength), float(finalLength), float(initialTemperature))+"K\n")

        elif(value.lower() == 'it'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material?\t")
            initialLength = input("\nwhat is the initial length of the material?\t")
            print("\nThe initial temperature = "+ initialTemperatureLinearExpansion(float(alpha), float(initialLength), float(finalLength), float(finalTemperature))+"K\n")

    elif(type.lower() == 'v'):
        if(value.lower() == 'iv'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material?\t")
            finalTemperature = input("\nwhat is the final temeprature of the material?\t")
            print("\nThe initial Volume = "+ initialVolumeVolumeExpansion(float(beta), float(finalVolume), float(initialTemperature), float(finalTemperature))+"\n")

        elif(value.lower() == 'fv'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material?\t")
            finalTemperature = input("\nwhat is the final temeprature of the material?\t")
            print("\nThe final volume = " +finalVolumeVolumeExpansion(float(beta), float(initialVolume), float(initialTemperature), float(finalTemperature))+"\n")

        elif(value.lower() == 'it'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            finalTemperature = input("\nwhat is the final temeprature of the material?\t")
            print("\nThe Initial Temperature = "+initialTemperatureVolumeExpansion(float(beta), float(initialVolume), float(finalVolume), float(finalTemperature))+"K\n")        
        elif(value.lower() == 'ft'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temeprature of the material?\t")
            print("\nThe Final Temperature = "+finalTemperatureVolumeExpansion(float(beta), float(initialVolume), float(finalVolume), float(initialTemperature))+"K\n")
        elif(value.lower() == 'b'):
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temeprature of the material?\t")
            finalTemperature = input("\nwhat is the final temeprature of the material?\t")
            print("\nbeta = "+ str(coefficientVolumeExpansion(float(initialVolume), float(finalVolume), float(initialTemperature), float(finalTemperature)))+"\n")
   # elif(type.lower() == 'o'):

    else:
        print("\nplease input valid values.\n")
'''
>>>>>>> Stashed changes
initialTemperature = input("What is the initial temperature of the container? \t")

finalTemperature = input ("\nWhat is the final temperature of the container?\t")

initialPressure = input("\nWhat is the initial pressure of the container? \t")

finalPressure = input("\nWhat is the final pressure of the gas? \t")

initialVolume = input("\nwhat is the initial Volume of the container? \t")

finalVolume = input("\nWhat is the final volume of the container? \t")



