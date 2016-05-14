def jungle_animal(animal, my_speed):
    if animal == 'zebra': 
        print "Try to ride a zebra!" 
    if animal == 'cheetah': 
        if my_speed <= 115: 
            print "Stay calm and wait!" 
     print "Run!" 
    if animal != 'zebra' or 'cheetah': 
        print "Introduce yourself!"
        
        
def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    if animal == "Zebra":
        print "Try to ride it"
    elif animal == "cheetah":
        if my_speed > 115:
            return "Run"