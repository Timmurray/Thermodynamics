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

def constantValueReaction(type, variable):
    if(type.lower()=='ib'):
        if(variable.lower() == 'fv'):
            initialTemperature = input(print("\nwhat is the initial temperature? (in Kelvin)\t"))
            finalTemperature = input(print("\nWhat is the final temperature? (in Kelvin)\t"))
            initialVolume = input(print("\nWhat is the initial volume?\t"))
            finalVolume = float(finalTemperature) * float(initialVolume) / float(initialTemperature)
            return finalVolume
        elif(variable.lower() == 'iv'):
            initialTemperature = input(print("\nwhat is the initial temperature? (in Kelvin)\t"))
            finalTemperature = input(print("\nWhat is the final temperature? (in Kelvin)\t"))
            finalVolume = input(print("\nWhat is the final volume?\t"))
            initialVolume = float(finalVolume) * float(initialTemperature) / float(finalTemperature)
            return initialVolume
        elif(variable.lower() == 'ft'):
            initialTemperature = input(print("\nwhat is the initial temperature? (in Kelvin)\t"))
            initialVolume = input(print("\nWhat is the initial Volume? \t"))
            finalVolume = input(print("\nWhat is the final Volume?\t"))
            finalTemperature = float(finalVolume) * float(initialTemperature) / float(initialVolume)
            return finalTemperature
        elif(variable.lower() == 'it'):
            finalTemperature = input(print("\nWhat is the final temperature? (in Kelvin)\t"))
            finalVolume = input(print("\nWhat is the final volume?\t"))
            initialVolume = input(print("\nWhat is the initial Volume? \t"))
            initialTemperature = float(finalVolume)*float(finalTemperature) / float(initialVolume)
            return initialTemperature
        else:
            print("\nwhen the pressure is constant, the ratio of pressures and volumes are what are important so please input valid values.")
    elif(type.lower()=='ith'):
        if(variable.lower() == 'ip'):
            finalPressure = input(print("\nwhat is the final pressure in the containter? \t"))
            initialVolume = input(print("\nwhat is the initial volume of the container?\t"))
            finalVolume = input(print("\nwhat is the final volume in the container?\t"))
            initialPressure = float(finalPressure) * float(finalVolume) / float(initialVolume)
            return initialPressure
        elif(variable.loewr() == 'fp'):
            initialPressure = input(print("\nwhat is the initial pressure of the container?\t"))
            initialVolume = input(print("\nwhat is the initial volume of the container?\t"))
            finalVolume = input(print("\nwhat is the final volume of the container?\t"))
            finalPressure = float(initialPressure) * float(initialVolume) / float(finalVolume)
            return finalPressure
        elif(variable.lower() == 'iv'):
            initialPressure = input(print("\nwhat is the initial pressure?\t"))
            finalPressure = input(print("\nwhat is the final pressure?\t"))
            finalVolume = input(print("\nwhat is the final volume?\t"))
            initialVolume = float(finalVolume) * float(finalPressure) / float(initialPressure)
            return initialVolume
        elif(variable.lower() == 'fv'):
            initialVolume = input(print("\nwhat is the initlal volume of the container?\t"))
            initialPressure = input(print("\nwhat is the initial pressure in the container?\t"))
            finalPreesure = input(print("\nwhat is the final pressure of the container?\t"))
            finalVolume = float(initialPressure) * float(initialVolume) / float(finalPressure)
            return finalVolume
    elif(type.lower()=='ic'):
        if(variable.lower()=='ip'):
            initialTemperature = input(print("\nWhat is the initial temperature of the container?\t"))
            finalTemperature = input(print("\n what is the final tempearture of the container?\t"))
            finalPressure = input(print("\nWhat is the final pressure in thr container?\t"))
            initialPressure = float(finalPressure)*float(initialTemperature) / float(finalPressure)
        elif(variable.lower()=='fp'):
            initialTemperature = input(print("\nWhat is the initial temperature of the container?\t"))
            finalTemperature = input(print("\n what is the final tempearture of the container?\t"))
            initialPressure = input(print("\nWhat is the final pressure in thr container?\t"))
            finalPressure = float(initialPressure)*float(finalTemperature) / float(initialTemperature)
        elif(variable.lower()=='it'):
            initialPressure = input(print("\nwhat is the initial pressure of the container?\t"))
            finalPressure = input(print("\nWhat is the final pressure of the container?\t"))
            finalTemperature = input(print("\nWhat is the final temperature of the conatiner?\t"))
            initialTemperature = float(finalTemperature)*float(initialPressure) / float(finalPressure)
        elif(variable.lower()=='ft'):
            initialPressure = input(print("\nwhat is the initial pressure of the contianer?\t"))
            finalPressure = input(print("what is the final pressure of the container?\t"))
            initialTemperature = input(print("\nwhat is the initial temperature of the container?\t"))
            finalTemperature = float(initialTemperature)*float(finalPressure) / float(initialPressure)
        else:
            print("\ninvalid input, please try again.")
    elif(type.lower()=='ab'):
        Cv = int(input(print("\nhow many degrees of freedom do the particles have?\t")))/2
        Cp = 1 + Cv
        gamma = float(Cp / Cv)
        if(variable.lower()=='it'):
        elif(variable.lower()=='ft'):
        elif(variable.lower()=='iv'):
        elif(variable.lower()=='fv'):
        elif(variable.lower()=='ip'):
        elif(variable.lower()=='fp'):
        
    elif(type.lower()=='e'):
    

print("This is a calculator for Thermodynamics\n")

print("\n iv : initial Volume of container | fv : final volume of container\n it : initial temperature of gas | ft : final temperature of gas\n")
print("ip : initial pressure of gas in container | fp : final pressure of gas in container\n b : coefficient of volume expansion | a: coefficient of linear expansion\n")
print("il: initial length | fl : final length\n")

while True:
    value = input("\nselect an option you would like to solve for: \t")
    type = input("\nto solve using linear expansion type 'l'\nto solve using volume expansion type 'v'\notherwise type 'o' (l/v/o): \t")   

    if(type.lower() == 'l'):
        if(value.lower() == 'a'):
            initialLength = input("\nWhat is the initial length of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            initialTemperature = input("\nWhat is the initial temperature of the material? (in Kelvin)\t")
            finalTemperature = input("\nWhat is the final temperature of the material? (in Kelvin)\t")
            print("\nThe coefficient of linear expansion = "+coefficientLinearExpansion(float(finalLength), float(initialLength), float(finalTemperature), float(initialTemperature))+"\n")        
    
        elif(value.lower() == 'il'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material? (in Kelvin)\t")
            initialTemperature = input("\nwhat is the initial temperature of the material? (in Kelvin)\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            print("\nThe initial length of the material = "+initialLengthLinearExpansion(float(alpha), float(finalTemperature), float(initialTemperature), float(finalLength)+"m\n"))

        elif(value.lower() == 'fl'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material? (in Kelvin)\t")
            initialTemperature = input("\nwhat is the initial temperature of the material? (in Kelvin)\t")
            initialLength = input("\nwhat is the initial length of the material?\t")
            print("\nThe final length of the material = "+finalLengthLinearExpansion(float(alpha), float(finalTemperature), float(initialTemperature), float(initialLength))+"m\n")

        elif(value.lower() == 'ft'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material? (in Kelvin)\t")
            initialLength = input("\nwhat is the initial length of the material?\t")
            print("\nThe final temperature = " + finalTemperatureLinearExpansion(float(alpha), float(initialLength), float(finalLength), float(initialTemperature))+"K\n")

        elif(value.lower() == 'it'):
            alpha = input("\nwhat is the coefficient of linear expansion of the material?\t")
            finalLength = input("\nwhat is the final length of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material? (in Kelvin)\t")
            initialLength = input("\nwhat is the initial length of the material?\t")
            print("\nThe initial temperature = "+ initialTemperatureLinearExpansion(float(alpha), float(initialLength), float(finalLength), float(finalTemperature))+"K\n")

    elif(type.lower() == 'v'):
        if(value.lower() == 'iv'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material? (in Kelvin)\t")
            finalTemperature = input("\nwhat is the final temperature of the material? (in Kelvin)\t")
            print("\nThe initial Volume = "+ initialVolumeVolumeExpansion(float(beta), float(finalVolume), float(initialTemperature), float(finalTemperature))+"\n")

        elif(value.lower() == 'fv'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temperature of the material? (in Kelvin)\t")
            finalTemperature = input("\nwhat is the final temperature of the material? (in Kelvin)\t")
            print("\nThe final volume = " +finalVolumeVolumeExpansion(float(beta), float(initialVolume), float(initialTemperature), float(finalTemperature))+"\n")

        elif(value.lower() == 'it'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            finalTemperature = input("\nwhat is the final temperature of the material? (in Kelvin)\t")
            print("\nThe Initial Temperature = "+initialTemperatureVolumeExpansion(float(beta), float(initialVolume), float(finalVolume), float(finalTemperature))+"K\n")        
        elif(value.lower() == 'ft'):
            beta = input("\nwhat is the coefficient of volume expansion?\t")
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temeprature of the material? (in Kelvin)\t")
            print("\nThe Final Temperature = "+finalTemperatureVolumeExpansion(float(beta), float(initialVolume), float(finalVolume), float(initialTemperature))+"K\n")
        elif(value.lower() == 'b'):
            finalVolume = input("\nwhat is the final volume of the material?\t")
            initialVolume = input("\nwhat is the initial volume of the material?\t")
            initialTemperature = input("\nwhat is the initial temeprature of the material? (in Kelvin)\t")
            finalTemperature = input("\nwhat is the final temeprature of the material? (in Kelvin)\t")
            print("\nbeta = "+ str(coefficientVolumeExpansion(float(initialVolume), float(finalVolume), float(initialTemperature), float(finalTemperature)))+"\n")
    
    elif(type.lower() == 'o'):
        newValue = input(print("\nif there is an isochoric simulation (volume is constant) type : ic\t if there is an isothermal reaction (temperature does not change) type : ith\t if the reaction is isobaric (pressure is constant) type : ib\t if the amount of heat is constant (adiabatic) type : ab\t if entropy is constant (isentropic) type: e\t "))
        if(newValue.lower() == 'ib'):
            variable = input(print("\nType 'iv' for the initial volume; Type 'fv' for the final volume; type 'it' for initial temperature; type 'ft' for final temperature"))
            if(variable.lower()=='iv' | variable.lower()=='fv'):
                constantValueReaction(newValue,variable)
            elif(variable.lower()=='it' | variable.lower()=='ft'):
                constantValueReaction(newValue, variable)
            else:
                print("Please input a valid value listed above.\n\n")
        elif(newValue.lower() == 'ith'):
            variable = input(print("\ntype 'fv' to solve for the final volume; type 'iv' to solve for the initial volume; type 'ip' to solve for the initial pressure; type 'fp' to solve for the final pressure:\t"))
            if(variable.lower()=='iv' | variable.lower()=='fv'):
                constantValueReaction(newValue,variable)
            elif(variable.lower()=='ip' | variable.lower()=='fp'):
                constantValueReaction(newValue, variable)
            else:
                print("Please input a valid value listed above.\n\n")
        elif(newValue.lower()=='ic'):
            variable = input(print("\ntype 'fp' to solve for the final pressure; type 'ip' to solve for the initial pressure; type 'it' to solve for the initial temperature; type 'ft' to solve for the final temperature:\t"))
            if(variable.lower()=='ip' | variable.lower()=='fp'):
                constantValueReaction(newValue,variable)
            elif(variable.lower()=='it' | variable.lower()=='ft'):
                constantValueReaction(newValue, variable)
            else:
                print("\nPlease input a valid value listed above.\n\n")
        elif(newValue.lower()=='ab'):
            variable = input(print("\ntype 'i(p/v/t)' in the form 'it' to find the initial pressure, volume, or temperature and 'f(p/v/t)' in the form 'fp' to find the final pressure, volume, or temperature"))
            if(variable.lower() == 'ip' | variable.lower()=='fp'):
                constantValueReaction(newValue, variable)
            elif(variable.lower()=='iv' | variable.loewr() == 'fv'):
                constantValueReaction(newValue,variable)
            elif(variable.lower()=='it' | variable.lower()=='ft'):
                constantValueReaction(newValue,variable)
            else:
                print("\n there were no valid inputs detected, please try again.")
        elif(newValue.lower()=='e'):
            
                        
        else:
            print("\nplease input a valid response.")
    else:
        print("\nplease input valid values.\n")