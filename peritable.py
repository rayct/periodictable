import periodictable

# Get details of an element by atomic number
Atomic_No = int(input("Enter Element Atomic No :"))
element = periodictable.elements[Atomic_No]
print('Atomic number:', element.number)
print('Symbols:', element.symbol)
print('Name:', element.name)
print('Atomic mass:', element.mass)
print('Density:', element.density)

# rayturner.dev