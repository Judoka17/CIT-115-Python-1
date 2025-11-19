#differnt gravity numbers
fMERCURY = 0.38
fVENUS= 0.91
fMOON = 0.165
fMARS = 0.38
fJUPITER = 2.34
fSATURN = 0.93
fURANUS = 0.92
fNEPTUNE = 1.12
fPLUTO = 0.066

#NAME
Name = input('What is your name')



#weights on other planets
Fweight = float(input("What is your weight in earth pounds"))
 


print(' ')
print(f"{Name}, this is your weight on different planets")

#weight calculation for user
mars_pounds = fMARS * Fweight         
moon_pounds = fMOON * Fweight             
mercury_pounds = fMERCURY * Fweight       
venus_pounds = fVENUS * Fweight                      
jupiter_pounds = fJUPITER * Fweight              
saturn_pounds = fSATURN * Fweight             
uranus_pounds = fURANUS * Fweight
neptune_pounds = fNEPTUNE * Fweight
pluto_pounds = fPLUTO * Fweight              

#print statments of weight
print(f"Weight on Mars       {mars_pounds:>12,.2f}")
print(f"Weight on Moon       {moon_pounds:>12,.2f}")
print(f"Weight on Mercury    {mercury_pounds:>12,.2f}")
print(f"Weight on Venus      {venus_pounds:>12,.2f}")
print(f"Weight on Jupiter    {jupiter_pounds:>12,.2f}")
print(f"Weight on Saturn     {saturn_pounds:>12,.2f}")
print(f"Weight on Uranus     {uranus_pounds:>12,.2f}")
print(f"Weight on Neptune    {neptune_pounds:>12,.2f}")
print(f"Weight on Pluto      {pluto_pounds:>12,.2f}")

