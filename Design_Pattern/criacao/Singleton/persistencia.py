# classic implementation of Singleton Design pattern
class Singleton:
    __shared_instance = 'databasePath'

    @staticmethod
    def getInstance():

        """Metodo de acesso stático"""
        if Singleton.__shared_instance == 'databasePath':
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):

        """virtual private constructor"""
        if Singleton.__shared_instance != 'databasePath':
            raise Exception("Essa é uma classe singleton !")
        else:
            Singleton.__shared_instance = self


# main method
if __name__ == "__main__":
    # create object of Singleton Class
    obj = Singleton()
    print(obj)

    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)