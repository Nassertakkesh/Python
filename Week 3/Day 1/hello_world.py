# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "hello", name )	# with a comma
print( "hello" + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
age = 42
print( "hello" + str( age) )	# with a +	-- this one should give us an error!
print( "hello", age )	# with a comma

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( f"I love to eat {fave_food1} and {fave_food2}" ) # with an f string
print( "i love to eat {} and {}".format(fave_food1,fave_food2 ))
 
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    