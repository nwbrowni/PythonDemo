# all class methods need a self parameter
# overriding is done by setting default parameter values
#   - (greetertype = None) is a default parameter... similar to having a function where that parameter is not included

class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def Greet(self):
        print(self.greeting + "!")

    def GreetWithName(self, name):
        self.Greet()
        print("Nice to meet you, " + name + "!")

class DoorGreeter(Greeter):
    # constructor of parent class inherited by default
    def WelcomeIn(self):
        print("Please come in.")

    def Greet(self):
        self.WelcomeIn()
        #Greeter.Greet(self)  # same outcome as super().Greet(), but need the self reference
        super().Greet()

    def GreetWithNAme(self, name):
        self.WelcomeIn()
        #Greeter.GreetWithName(self, name)  # same outcome as super().GreetWithName(), but need the self reference
        super().GreetWithName(name)

class GreeterFactory:
    def BuildGreeter(self, greetertype = None):
        if (greetertype == "Midwesterner"):
            return Greeter("Howdy")
        elif (greetertype == "Italian"):
            return Greeter("Chow")
        elif (greetertype == "Spanish"):
            return Greeter("Hola")
        elif (greetertype == "Formal"):
            return Greeter("Good day")
        else:
            return Greeter("Hello")

    def BuildCustomGreeter(self, greeting):
        return Greeter(greeting)

    def BuildDoorGreeter(self, greetertype = None):
        if (greetertype == "Midwesterner"):
            return DoorGreeter("Howdy")
        elif (greetertype == "Italian"):
            return DoorGreeter("Chow")
        elif (greetertype == "Spanish"):
            return DoorGreeter("Hola")
        elif (greetertype == "Formal"):
            return DoorGreeter("Good day")
        else:
            return DoorGreeter("Hello")

    def BuildCustomDoorGreeter(self, greeting):
        return DoorGreeter(greeting)

class GreeterMenu:
    def PrintGreeterMenu(self):
        print("Greeter Menu:")
        print("1) Default")
        print("2) Midwestern Greeter")
        print("3) Italian Greeter")
        print("4) Spanish Greeter")
        print("5) Formal Greeter")
        print("6) Custom Greeter")
        print("7) EXIT")
        return input(">> ")

class DoorGreeterMenu:
    def PrintDoorGreeterMenu(self):
        print("Greeter Menu:")
        print("1) Default")
        print("2) Midwestern Door Greeter")
        print("3) Italian Door Greeter")
        print("4) Spanish Door Greeter")
        print("5) Formal Door Greeter")
        print("6) Custom Door Greeter")
        print("7) EXIT")
        return input(">> ")

class GreeterTypeMenu:
    def PrintGreeterTypeMenu(self):
        print("Greeter Type Menu:")
        print("1) Greeter")
        print("2) Door Greeter")
        print("3) EXIT")
        return input(">> ")

class GreeterApp:
    def __init__(self):
        self.greeterfactory = GreeterFactory()
        self.greetertypemenu = GreeterTypeMenu()
        self.greetermenu = GreeterMenu()
        self.doorgreetermenu = DoorGreeterMenu()
        self.run = True
        
        while (self.run):
            print()
            response = self.greetertypemenu.PrintGreeterTypeMenu()
            self.run = self.HandleGreeterTypeMenuResponse(response)

        print()

    def HandleGreeterMenuResponse(self, response):
        if (response == "1"):
            g = self.greeterfactory.BuildGreeter()
            g.Greet()
        elif (response == "2"):
            g = self.greeterfactory.BuildGreeter("Midwesterner")
            g.Greet()
        elif (response == "3"):
            g = self.greeterfactory.BuildGreeter("Italian")
            g.Greet()
        elif (response == "4"):
            g = self.greeterfactory.BuildGreeter("Spanish")
            g.Greet()
        elif (response == "5"):
            g = self.greeterfactory.BuildGreeter("Formal")
            g.Greet()
        elif (response == "6"):
            print()
            customgreeting = input("Please enter a custom greeting: ")
            g = self.greeterfactory.BuildCustomGreeter(customgreeting)
            g.Greet()
        elif (response == "7"):
            return False
        else:
            print(response + " is not a valid response.")
            return True
        
        return True

    def HandleDoorGreeterMenuResponse(self, response):
        if (response == "1"):
            g = self.greeterfactory.BuildDoorGreeter()
            g.Greet()
        elif (response == "2"):
            g = self.greeterfactory.BuildDoorGreeter("Midwesterner")
            g.Greet()
        elif (response == "3"):
            g = self.greeterfactory.BuildDoorGreeter("Italian")
            g.Greet()
        elif (response == "4"):
            g = self.greeterfactory.BuildDoorGreeter("Spanish")
            g.Greet()
        elif (response == "5"):
            g = self.greeterfactory.BuildDoorGreeter("Formal")
            g.Greet()
        elif (response == "6"):
            print()
            customgreeting = input("Please enter a custom greeting: ")
            g = self.greeterfactory.BuildCustomDoorGreeter(customgreeting)
            g.Greet()
        elif (response == "7"):
            return False
        else:
            print(response + " is not a valid response.")
            return True
        
        return True

    def HandleGreeterTypeMenuResponse(self, response):
        run = True

        if (response == "1"):
            while (run):
                print()
                greeterresponse = self.greetermenu.PrintGreeterMenu()
                run = self.HandleGreeterMenuResponse(greeterresponse)
        elif (response == "2"):
            while (run):
                print()
                doorgreeterresponse = self.doorgreetermenu.PrintDoorGreeterMenu()
                run = self.HandleDoorGreeterMenuResponse(doorgreeterresponse)
        elif (response == "3"):
            return False
        else:
            print(response + " is not a valid response.")
            return True

        return True
