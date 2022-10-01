import math

# celsius is represented by 'C'
# kelvin is represented by 'K'
# farenheight is represented by 'F'

#simple conversions of temperature

convertCelsiusToKelvin(celsius):
    temperature = celsius + 273.15
    return temperature

convertCelsiusToFarenheight(celsius):
    temperature = (9/5)*celsius + 32
    return temperature

convertFarenheightToCelsius(farenheight):
    temperature = (5/9)*farenheight - 32
    return temperature
    
convertFarenheightToKelvin(farenheight):
    temperature = (5/9)*farenheight + 241.15
    return temperature

convertKelvinToCelsius(kelvin):
    temperature = kelvin - 273.15
    return temperature 
    
convertKelvinToFarenheight(kelvin):
    temperature = (9/5)*(kelvin - 273.15) + 32
    return temperature
