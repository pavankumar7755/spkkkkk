#PRAVATE  METHOD("__")
#PUBLIC METHOD ("   ")
#PROTECTED METHOD("_")



"""class myclass:
      def __init__(self):
            self.__privte_var=10
      def _private_method(self):
            return "this is a private method "
      
obj = myclass()
print(obj._private_method())
#print(obj.__privte_var)      

      """


"""
class female:
    def __age(self):
        print("my age is :")

pandu = female()
print(pandu._age())"""

  

class phone:
    def _gallery(self):
        print("i have access to my wallet")

class motherphone(phone):
    def display(self):
        print(self._gallery())

photos = motherphone()
print(photos.display())                

