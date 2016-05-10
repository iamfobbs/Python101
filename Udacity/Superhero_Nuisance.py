def fix_machine(debris, product):
     ### WRITE YOUR CODE HERE ###
     word = debris.find(product)
     return word
    


### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
# print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
# print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
# print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

