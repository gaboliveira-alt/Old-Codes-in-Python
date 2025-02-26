def bmi(weight, height):
    index = weight / (height  * height)
    return index
    

patient_5 = bmi(61, 1.83)
print("underweight:", patient_5 < 18.5)

patient_6 = bmi(75, 1.74)
print("underweight:", patient_6 < 18.5)
 