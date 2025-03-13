#task3
class Robot:
    phrase="Hello World!"
    def __init__(self, name):
        self.name = name
        self.phrase = self.phrase

Robot=Robot("x")
print(Robot.name)
print(Robot.phrase)

#task4
class Robot:
    phrase = "Hello World!"

    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.name

    def get_phrase(self):
        return self.phrase

    def set_phrase(self, new_phrase):
        self.phrase = new_phrase

    def set_name(self, new_name):
        self.name = new_name

    def greet_another_by_name(self, other):
        return f"Hello {other.name}, I am {self.name}!"

    def self_replicate(self):
        return Robot(self.name + " Jr.")


robo = Robot("Robo")
print(robo.get_name())
print(robo.get_phrase())
robo.set_phrase("Greetings, human!")
print(robo.get_phrase())
bot = Robot("Bot")
print(robo.greet_another_by_name(bot))
robo_jr = robo.self_replicate()
print(robo_jr.get_name())
print(robo_jr.get_phrase())

#This task uses object-oriented concepts

#chat history with gen AI
# Task 3
# class Robot:
#     # Class variable
#     phrase = "Hello World!"
#
#     def __init__(self, name):
#         self.name = name
#         self.phrase = Robot.phrase  # Initialize phrase with the class variable
#
# # Create a robot instance and print the name and phrase
# robot = Robot("x")
# print(robot.name)  # Output: x
# print(robot.phrase)  # Output: Hello World!
#
# # Task 4
# class Robot:
#     phrase = "Hello World!"  # Class variable for greeting
#
#     def __init__(self, name):
#         self.set_name(name)  # Set the name using the setter method
#         self.phrase = Robot.phrase  # Initialize the phrase using class variable
#
#     def get_name(self):
#         return self.name
#
#     def get_phrase(self):
#         return self.phrase
#
#     def set_phrase(self, new_phrase):
#         self.phrase = new_phrase
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def greet_another_by_name(self, other):
#         return f"Hello {other.get_name()}, I am {self.get_name()}!"
#
#     def self_replicate(self):
#         return Robot(self.get_name() + " Jr.")
#
# # Create an instance of Robot
# robo = Robot("Robo")
# print(robo.get_name())  # Output: Robo
# print(robo.get_phrase())  # Output: Hello World!
#
# # Modify phrase and print it
# robo.set_phrase("Greetings, human!")
# print(robo.get_phrase())  # Output: Greetings, human!
#
# # Create another robot instance and greet it
# bot = Robot("Bot")
# print(robo.greet_another_by_name(bot))  # Output: Hello Bot, I am Robo!
#
# # Replicate Robo and print the new robot's name and phrase
# robo_jr = robo.self_replicate()
# print(robo_jr.get_name())  # Output: Robo Jr.
# print(robo_jr.get_phrase())  # Output: Greetings, human!
