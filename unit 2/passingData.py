# when we are building complex programs, we need a
# way to pass in data that is not always
# from the user

# Function arguments and parameter are ways to
# pass in data to a function from possibly
# another function.

# Function parameters- this is placeholder data for
# A function. variables inside the curly brackets

# Memory trick - PARAMETER AND PLACEHOLDER BOTH
# START WITH THE LETTER P
# Def check_water_Depth(depth):
#print(depth)
#print(depth > 10) # true if depth is greater than 10 feet
# return depth

# Function arguments- This is the real data that we pass into
# the function call
# memory trick- if you make a real world argment with a person
# you need to come with real facts (data)
#Check_Water_Depth(3)

# return - this keyword allows us to pass data from inside 1 function
# into another function

def username(name):
    return name

def confirmlogin():
    name = username ("Brown")
    print(name)

    Confirmlogin()
    username("Brown")

    def robloxprofile(username, dob, location, currency, creditcard):
        print("roblox profile ")