#import cv2
from PIL import Image
from transformers import pipeline
#import requests
#import torch

#OPEN AI load
#patch14 is more memory, better model 
classifier  = pipeline("zero-shot-image-classification", model="openai/clip-vit-large-patch32")

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods = ["POST"])
def upload():
    file = request.files["image"]

    image1 = Image.open(file).convert("RGB")

    x = image1.convert("RGB")

    #x.show()
    print(x)
    

    fish = ["Red Snapper", "Mackerel", "Tuna",
    "Mahi-Mahi", "Parrotfish", "Barracuda",
    "Crevalle Jack"]

    prices = {
        "Red Snapper": 2100,
        "Barracuda": 400,
        "Parrotfish": 1150,
        "Mahi-Mahi": 3570,
        "Tuna": 200,
        "Crevalle Jack": 554,
        "Mackerel":  650
    }

    inputs = classifier(x, candidate_labels=fish, hypothesis_template="a clear photo of a {} fish")
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
            "Crevalle Jack": str("2 - 6.3"), 
            "Tuna": str("3.6 - 15"),
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
            "Crevalle Jack": str("is a carnivorous predator whose diet consists mainly of smaller schooling fish, shrimp, crabs, and squid"), 
            "Tuna": str("Tuna are active, meat-eating predators that feed on smaller fish, squid, and crustaceans"),
            "Mackerel": str("Mackerel fish eats Small Crustaceans: Feed heavily on tiny swimming animals like copepods, krill, and small shrimp."),
    }


    print("Fish diet and what bait to use to catch the Fish:")
    print(Diet[lab])
    print()

#MAY NEED TO ADD TO / CHANGE LATER 
    return f"""
    Fish: {lab}<br>
"""



if __name__=="__main__":
    app.run()



"""
#open camera
cam = cv2.VideoCapture(0)

#get default width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

#create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    #write frame to output file
    out.write(frame)

    #display the frame
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1)
     


    if key == ord(" "):
        print("photo taken")
        cv2.imwrite("captured_image.jpg", frame)
        break

    #q' to exit the loop
    elif cv2.waitKey(1) == ord('q'):
        break

#Release the capture objects
cam.release()
out.release()
cv2.destroyAllWindows()

"""







#barracuda is a carnivorous fish that eats smaller fish, squids, and crustaceans
#red snapper:
#Small Fish: is a carnivorous that eats various small fish living near the sea bottom.
#Crustaceans: Crabs, mantis shrimp (stomatopods), and regular shrimp.

#parrotfish are primarily herbivores that eat algae, coral polyps, and small bits of rock or detritus
#Mahi-mahi are fast-swimming carnivorous apex predators that feed on small pelagic fish, squid, and crustaceans
#Crevalle Jack is a carnivorous predator whose diet consists mainly of smaller schooling fish, shrimp, crabs, and squid
#Tuna are active, meat-eating predators that feed on smaller fish, squid, and crustaceans
#Mackerel fish eats Small Crustaceans: Feed heavily on tiny swimming animals like copepods, krill, and small shrimp.



#JMD $270 to JMD $650 per pound barracuda
#$($3,570 JMD) per pound mahi mahi

#$1,980 JMD to $2,300 JMD per pound red snapper

#JMD $900 to JMD $1,400 per pound parrotfish

#JMD 145.19 and JMD 257.13 per pound(lb) Tuna
#$390 – $945 per lb
#JMD $390 and JMD $944 Crevalle Jack