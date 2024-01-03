def singleton(class_instance):
    instances = {}
    def get_instance(*args,**kwargs):
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args,**kwargs)
        return instances[class_instance]
    return get_instance

@singleton
class MongoDbConnection():
    def __init__(self,name)->None:
        self.name = name
        print("MongoDbConnection initialised")

dbA =MongoDbConnection("ashik")
dbB = MongoDbConnection("mary")

if __name__ == "__main__":
    print(dbA == dbB)   
print(dbA.name)
print(dbB.name)