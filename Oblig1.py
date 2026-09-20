
#kilometer avstand per år
Kilometer=12000

#Forsikring per år

Forsikringbensin= 7500
Forsikring_el=5000

#Trafikkforsikringsavgift per år

Dagsavgift = 8.38
Årsavgift=Dagsavgift*365

#Drivstoffbruk

ForbukBensin = 1.0
ÅrsforbrukBensin=ForbukBensin*Kilometer

ForbukEl = 0.2
StrømPris=2.0
ÅrsforbrukEl=ForbukEl*Kilometer*StrømPris

#Bomavgift kr/km

Bom_Bensin=0.3
Bom_el= 0.1

TotalBomBensin=Bom_Bensin*Kilometer
TotalBomEl=Bom_el*Kilometer

#TotalKostnader

TotalEl=Forsikring_el+ Årsavgift+ÅrsforbrukEl+TotalBomEl
TotalBensin=Forsikringbensin + Årsavgift + ÅrsforbrukBensin + TotalBomBensin

Differanse= TotalBensin-TotalEl

print("Total årskostnader for en Bensinbil er:",TotalBensin,"Kr")

print("Toral årskostnader for en Elektrisk bil er:",TotalEl,"Kr")

print("Differansen mellom Bensinbil og Elektrisk bil er:",Differanse,"Kr")