import distutils  
import distutils.util 

#  True values are y, yes, t, true, on and 1; false values are n, no, f, false, off and 0. Raises ValueError if val is anything else.
#  For more information please check out https://docs.python.org/3/distutils/apiref.html#distutils.util.strtobool

age = bool(distutils.util.strtobool(input("Are you a cigarette addict older than 75 years old? [True/False]")))
chronic = bool(distutils.util.strtobool(input("Do you have a severe chronic disease? [True/False]")))
immune = bool(distutils.util.strtobool(input("Is your immune system too weak? [True/False]")))

if (age and chronic and immune):
    print("COVID-19 poses a great risk of death for you. Stay at your home and pay attention to the social distancing rules.")
elif (age or chronic or immune):
    print("COVID-19 might effect your health negatively. Therefore, to be at the safe side, stay at your home.")
else: 
    print("There is no COVID-19 risk for you. Enjoy the summer.")  