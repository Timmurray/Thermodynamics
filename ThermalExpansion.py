import math
import TemperatureUnitConversions.py

# the coefficient of linear expansion may be derived through a formula
# the known coefficients of linear expansion from most materials will exist in a dictionary
# the known  coefficients of volume expanison for most materials will exist in a dictionary

coefficientLinearExpansion(finalLength, initialLength, finalTemperature, initialTemperature):
    alpha = ((finalLength-initialLength)/(finaiTemperature-initialTemperature))/(initialLength)
    return alpha

#solving initial length of material with known coefficient of linear expansion, final temperature, initial temperature, and final length
initialLengthLinearExpansion(alpha, finalTemperature, initialTemperature, finalLength):
    initialLength = (finalLength)/(alpha*(finalTemperature-initialTemperature)+1)
    return initialLength

#solving the final length of a material with known coefficient of linear expansion, final temperature, initial temperature, and initial length
finalLengthLinearExpansion(alpha, finalTemperature, initialTemperature, initialLength):
    finalLength = (initialLength*alpha*(finalTemperature-initialTemperature)) + 1
    return finalLength

#solving initial temperature in Kelvin with coefficient of linear expansion, initial length, final length, and final temperature

initialTemperatureLinearExpansion(alpha, initialLength, finalLength, finalTemperature):
    initialTemperature = -((finalLength-initialLength)/(alpha*initialLength)) + finalTemperature
    return initialTemperature

#solving final temperature in Kelvin with coefficient of linear expansion, initial length, final length, and initial temperature

finalTemperatureLinearExpansion(alpha, initialLength, finalLength, initialTemperature):
    finalTemperature = (finalLength-initialLength)/(alpha*initialLength) + initialTemperature
    return finalTemperature

# solving for beta the coefficient of volume expansion with known initial volume, final volume, initial temperature, and final temperature

coefficientVolumeExpansion(initialVolume, finalVolume, initialTemperature, finalTemperature):
    beta = (1/initialVolume)*((finalVolume-initialVolume)/(finalTemperature-initialTemperature))
    return beta

#solving for the initial volume using the volume expansion formula with known beta, final volume, initial temperature, and final temperature

initialVolumeVolumeExpansion(beta, finalVolume, initialTemperature, finalTemperature):
    initialVolume = (finalVolume)/(alpha*(finalTemperature-initialTemperature)+1)
    return initialVolume

#solving for final volume using the volume expansion formula with known beta coefficient of volume expansion, initial volume, initial temperature and final temperature

finalVolumeVolumeExpansion(beta, initialVolume, initialTemperature, finalTemperature):
    finalVolume = (initialTemperature*alpha*(finalTemperature-initialTemperature)) + 1
    return finalVolume

#solving for initial temperature using the volume expansion formula with a known beta, initial volume, final volume, and final temperature

initialTemperatureVolumeExpansion(beta, initialVolume, finalVolume, finalTemperature):
    initialTemperature = -((finalVolume-initialVolume) / (beta*initialVolume)) + finalTemperature
    return initialTemperature

#solving for final temperature using the volume expansion formula with known beta, initial volume, final volume, and initial temperature

finalTemperatureVolumeExpansion(beta, initialVolume, finalVolume, initialTemperature):
    finalTemperature = (finalVolume-initialVolume)/(beta*initialVolume) + initialTemperature
    return finalTemperature