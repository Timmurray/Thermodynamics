import math
import TemperatureUnitConversions.py

# the coefficient of linear expansion may be derived through a formula
# the known coefficients of linear expansion from most materials will exist in a dictionary
# the known  coefficients of volume expanison for most materials will exist in a dictionary

CoefficientLinearExpansion(FinalLength, InitialLength, FinalTemperature, InitialTemperature):
    alpha = ((FinalLength-InitialLength)/(FinaiTemperature-InitialTemperature))/(InitialLength)
    return alpha

CoefficientVolumeExpansion(initialVolume, finalVolume, initialTemperature, finalTemperature):
    beta = (1/initialVolume)*((finalVolume-initialVolume)/(finalTemperature-initialTemperature))
    return beta

