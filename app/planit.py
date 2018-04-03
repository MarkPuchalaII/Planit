# The purpose of this program is to track and priorities my interests
# That I might know what is of my most immediate interest to focus on
# And what are not as much priorities as I might believe.

print("got an interest? Let's PLANOT out!")

def start():
    print("What would you like to do? \n",
        "1. Review  2. Test  3. Add  4. Remove  5. Quit")
    n = int(input())
    n = {
        1 : review(),
        2 : test(),
        3 : add(),
        4 : remove(),
        5 : quit(),
    }

def review() :
    print("yayyy")

start()
