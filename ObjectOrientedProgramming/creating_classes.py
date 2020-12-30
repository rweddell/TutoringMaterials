
class Person():

    def __init__(self, name, height=None, job=None, favorite_color=None):
        self._name = name
        self._height = height
        self._job = job
        self._favorite_color = favorite_color
        self.activities = []

    def update_height(self, new_height):
        self._height = new_height

    def update_job(self, new_job):
        self._job = new_job

    def say_hello(self):
        print('Hi! My name is {}!'.format(self._name))

    def say_job(self):
        print("I'm a {}!".format(self._job))
    

# person1 = Person(name='Lester', height=5.85)

# person1.update_job('bus driver')

# person1.say_hello()

# person1.say_job()

# person1.favorite_color = 'chartreuse'

# print(person1.favorite_color)