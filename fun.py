# import module
import random
import datetime

print("-----------------------------|DAS - Python Online Class|-----------------------------------")



# setting vars and asking questions
myname = input("what is your name? ")
myage = input("what year where you born?  ")
thisyear = datetime.datetime.now().year
# print("It is now the year", thisyear)
mygender = input("what gender are you? ")
YearNow = thisyear
DOBYear = int(YearNow) - int(myage)
myname = myname
myage = myage
mygender = mygender

print("-------------------------------------------------------------------------------------------")
# creating text message
print("My name is " + myname.upper() + "," "I was born in " + myage + " and I am a  " + mygender.upper() + " that is "
      , end='')
print(DOBYear, end=' ')
print("years old")

# vars for year the chinese zodiac
dragon = "1928", "1940", "1952", "1964", "1976", "1988", "2000", "2012", "2024"
rat = "1924", "1936", "1948", "1960", "1972", "1984", "1996", "2008", "2020"
ox = "1925", "1937", "1949", "1961", "1973", "1985", "1997", "2009", "2021"
tiger = "1926", "1938", "1950", "1962", "1974", "1986", "1998", "2010", "2022"
rabbit = "1927", "1939", "1951", "1963", "1975", "1987", "1999", "2011", "2023"
snake = "1929", "1941", "1953", "1965", "1977", "1989", "2001", "2013", "2025"
horse = "1930", "1942", "1954", "1966", "1978", "1990", "2002", "2014", "2026"
goat = "1931", "1943", "1955", "1967", "1979", "1991", "2003", "2015", "2027"
monkey = "1932", "1944", "1956", "1968", "1980", "1992", "2004", "2016", "2028"
rooster = "1933", "1945", "1957", "1969", "1981", "1993", "2005", "2017", "2029"
dog = "1934", "1946", "1958", "1970", "1982", "1994", "2006", "2018", "2030"
pig = "1935", "1947", "1959", "1971", "1983", "1995", "2007", "2019", "2031"

# print the year for chinese zodiac based on the year born
if myage in dragon:
    print("I am a Dragon- Confident, intelligent, enthusiastic")

if myage in rat:
    print("I am a Rat- Quick-witted, resourceful, versatile, kind")

if myage in ox:
    print("I am a Ox- Diligent, dependable, strong, determined")

if myage in tiger:
    print("I am a Tiger- Brave, confident, competitive")

if myage in rabbit:
    print("I am a Rabbit-  Quiet, elegant, kind, responsible")

if myage in snake:
    print("I am a Snake- Enigmatic, intelligent, wise")

if myage in horse:
    print("I am a Horse- Animated, active, energetic")

if myage in goat:
    print("I am a Goat- Calm, gentle, sympathetic")

if myage in monkey:
    print("I am a Monkey- Sharp, smart, curiosity")

if myage in rooster:
    print("I am a Rooster- Observant, hardworking, courageous")

if myage in dog:
    print("I am a Dog- Lovely, honest, prudent")

if myage in pig:
    print("I am a Pig -Compassionate, generous, diligent")


print("-------------------------------------------------------------------------------------------")

# Initializing list
li = random.sample(range(1,99), 6)
lx = random.sample(range(1,99), 6)
ly = random.sample(range(1,99), 6)
lz = random.sample(range(1,99), 6)
la = random.sample(range(1,99), 6)
lb = random.sample(range(1,99), 6)


# using shuffle() to shuffle the list
random.shuffle(li)
random.shuffle(lx)
random.shuffle(ly)
random.shuffle(lz)
random.shuffle(la)
random.shuffle(lb)


# Printing list after shuffling
print("My lucky Lottery numbers right now are based on my infomation   : ")

print("------ Row A ------")
for i in range(0, len(li)):
	print( li[i], end=" ")
print("\r")

print("------ Row B ------")
for x in range(0, len(li)):
	print(lx[x], end=" ")
print("\r")

print("------ Row C ------")
for y in range(0, len(li)):
	print(ly[y], end=" ")
print("\r")

print("------ Row D ------")
for z in range(0, len(li)):
	print(lz[z], end=" ")
print("\r")

print("------ Row E ------")
for a in range(0, len(li)):
	print(la[a], end=" ")
print("\r")

print("------ Row F ------")
for b in range(0, len(li)):
	print(lb[b], end=" ")
print("\r")


print("-------------------------------------------------------------------------------------------")
