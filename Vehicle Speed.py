class Vehicle:
    def __init__(self,ID,MaxSpeed,IncreaseAmount):  #constructor
        #ID STRING
        #MaxSpeed INTEGER
        #CurrentSpeed INTEGER
        #IncreaseAmount INTEGER
        #HorizontalPosition INTEGER
        
        self.__ID=ID   
        self.__MaxSpeed=MaxSpeed
        self.__IncreaseAmount=IncreaseAmount
        self.__CurrentSpeed=0
        self.__HorizontalPosition=0
        
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self,CurrentSpeed):
        self.__CurrentSpeed=CurrentSpeed
        
    def SetHorizontalPosition(self,HorizontalPosition):
        self.__HorizontalPosition=HorizontalPosition
        
    def IncreaseSpeed(self):
        self.__CurrentSpeed=self.__CurrentSpeed+self.__IncreaseAmount
        self.__HorizontalPosition=self.__HorizontalPosition+self.__CurrentSpeed
        
    def Output(self):
        print('Horizontal Position:',self.__HorizontalPosition)
        print('Current Speed:',self.__CurrentSpeed)
        
    
class Helicopter(Vehicle):
    def __init__(self,ID,MaxSpeed,IncreaseAmount,VerticalChange,MaxHeight):
        Vehicle.__init__(self,ID,MaxSpeed,IncreaseAmount)
        #VerticalChange INTEGER
        #MaxHeight INTEGER
        #VerticalPosition INTEGER
        
        self.__VerticalChange=VerticalChange
        self.__MaxHeight=MaxHeight
        self.__VerticalPosition=0
        
    def IncreaseSpeed(self):
        self.__VerticalPosition=self.__VerticalPosition+self.__VerticalChange
        Vehicle.SetCurrentSpeed(self,(Vehicle.GetCurrentSpeed(self)+Vehicle.GetIncreaseAmount(self)))
        Vehicle.SetHorizontalPosition(self,(Vehicle.GetHorizontalPosition(self)+Vehicle.GetCurrentSpeed(self)))
        
        
    def Output(self):
        print ('Horizontal Position:',Vehicle.GetHorizontalPosition(self))
        print ('Current Speed:',Vehicle.GetCurrentSpeed(self))
        print ('Vertical Position:',self.__VerticalPosition)
    
    
MyCar=Vehicle("Tiger",100,20)
MyCar.IncreaseSpeed()
MyCar.IncreaseSpeed()
MyCar.Output()

print('\n')

MyHelicopter=Helicopter("Lion",350,40,3,100)
MyHelicopter.IncreaseSpeed()
MyHelicopter.IncreaseSpeed()
MyHelicopter.Output()
        
        
        
        
        