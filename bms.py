Mr=1.47 #Mass of limiting reactant material in Kilogram
n=56 #Number of electrons per ion produced at an electrode
Mm=56.78 #Molar mass
F=96485 #Faraday's constant
Qt=(0.278*F)*((Mr*n)/Mm) #Calculating Battery capacity using the formula in Ampere-hour
V=12.4 #Terminal Voltage of Battery in Volt
DelT=4 #Time over which the battery is Discharged in hour
C=100 #Rated capacity of the Battery in Ampere-hour
DoD=C/DelT #Discharge rate of the battery
Et=(1000*F*n*Mr*V)/Mm #Ideal Battery Energy In Joules
Pt=V*Qt #Ideal Battery Power in Watts
Mb=2.35 #Mass of the battery in kilogram
Se=(9.65*(10^7)*n*V*Mr)/Mm*Mb #Specific Energy of a battery in Watt per kilogram
Sp=Pt/Mb #Specific power of a battery in Watt per kilogram
print("Battery Capacity", Qt)
print("Rate of Discharge" , DoD)
print("Battery Energy" , Et)
print("Battery Power" , Pt)
print("Specific Energy" , Se)
print("Specific power", Sp)
