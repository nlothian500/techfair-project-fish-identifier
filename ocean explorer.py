from PIL import Image
from transformers import pipeline

x = Image.open("Mackerel.webp")
#x.show()
print(x)
classifier  = pipeline("zero-shot-image-classification")

fish = ["Red Snapper", "Mackerel", "Thunnus",
"Mahi-Mahi", "Parrotfish", "Barracuda",
"Crevalle jack"]

prices = {
    "Red Snapper": 2100,
    "Barracuda": 400,
    "Parrotfish": 1150,
    "Mahi-Mahi": 3570,
    "Thunnus": 200,
    "Crevalle jack": 554,
    "Mackerel":  650
}

inputs = classifier(x, candidate_labels=fish)
print("Fish Name:")
print(inputs[0]["label"])
lab = inputs[0]["label"]
print()
score = inputs[0]["score"]*100
print("Confidence:")
o = (round(score,0))
print(str(o)+"%")
print()

print("Estimated Market Value:")
print(str(prices[lab])+ "JMD/lb")
print()


length = {
        "Barracuda": str("5 - 6.5"), 
        "Red Snapper": str("1.5 - 2.5"),
        "Parrotfish": str("4.3 - 4.9"),
        "Mahi-Mahi": str("3 - 7"),
        "Crevalle jack": str("2 - 6.3"), 
        "Thunnus": str("1.6 - 15"),
        "Mackerel": str("1 - 6"),
}

print("Maximum Length:")
print(str(length[lab])+ " feet")
print()

Diet = {
        "Barracuda": str("is a carnivorous fish that eats smaller fish, squids, and crustaceans"), 
        "Red Snapper": str("is a carnivorous that eats various small fish living near the sea bottom Crabs, mantis shrimp (stomatopods), and regular shrimp."),
        "Parrotfish": str("are primarily herbivores that eat algae, coral polyps, and small bits of rock or detritus"),
        "Mahi-Mahi": str("are fast-swimming carnivorous apex predators that feed on small pelagic fish, squid, and crustaceans"),
        "Crevalle jack": str("is a carnivorous predator whose diet consists mainly of smaller schooling fish, shrimp, crabs, and squid"), 
        "Thunnus": str("Thunnus are active, meat-eating predators that feed on smaller fish, squid, and crustaceans"),
        "Mackerel": str("Mackerel fish eats Small Crustaceans: Feed heavily on tiny swimming animals like copepods, krill, and small shrimp."),
}


print("Fish diet and what bait to use to catch the Fish:")
print(Diet[lab])
print()






#barracuda is a carnivorous fish that eats smaller fish, squids, and crustaceans
#red snapper:
#Small Fish: is a carnivorous that eats various small fish living near the sea bottom.
#Crustaceans: Crabs, mantis shrimp (stomatopods), and regular shrimp.

#parrotfish are primarily herbivores that eat algae, coral polyps, and small bits of rock or detritus
#Mahi-mahi are fast-swimming carnivorous apex predators that feed on small pelagic fish, squid, and crustaceans
#Crevalle jack is a carnivorous predator whose diet consists mainly of smaller schooling fish, shrimp, crabs, and squid
#Thunnus are active, meat-eating predators that feed on smaller fish, squid, and crustaceans
#Mackerel fish eats Small Crustaceans: Feed heavily on tiny swimming animals like copepods, krill, and small shrimp.



#JMD $270 to JMD $650 per pound barracuda
#$($3,570 JMD) per pound mahi mahi

#$1,980 JMD to $2,300 JMD per pound red snapper

#JMD $900 to JMD $1,400 per pound parrotfish

#JMD 145.19 and JMD 257.13 per pound(lb) Thunnus
#$390 – $945 per lb
#JMD $390 and JMD $944 Crevalle jack