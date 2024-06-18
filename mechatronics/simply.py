import numpy as np                  #numpy for storing and managing data effectively
import seaborn as sns               #seaborn for plotting graphs


class project:
   
   length=0
   rxns=[]
   loads=list([])
   

   def reactions(self,loads,length):         #  It gives reactions on support A and B
      right=0
      left=0
      total=0
      for load in loads:
         total+=(load[0]*load[1])
      right=total/length
      loads.reverse()
      total=0
      for load in loads:
         total+=((length-load[0])*load[1])
      left=total/length
      return (left,right)


   def give_bmd(self,loads,length):            #This function is responsible for calculating BMD at diffrent points
      ret=[]
      rxns=self.rxns
      loads.append([length*1.0,-1*rxns[1]])
      loads.append([0.0,-1*rxns[0]])
      load_dct=dict({})
      for load in loads:
         load_dct[load[0]]=-1*load[1]
      cur_load=list([])
      total=0
      for point in np.arange(length+0.1,-0.1,-0.01):
         point=round(point,2)
         load_x=load_dct.get(point)
         if load_x==None:
            pass
         else:
            cur_load.append([point,load_x])
      
         net=0
         for load in cur_load:
            net+=(load[0]-point)*load[1]
         ret.append([point,net])
      
      x_points=[point[0] for point in ret]
      y_points=[-1*point[1] for point in ret]
      return (x_points,y_points)
      

    
   def __init__(self):
      self.input()
    
   def input(self):                          #This function is responsible for taking input from user
        print(" A\t\t\t\t\t\t  B")
        print(" __________________________________________________           SIMPLY SUPPORTED BEAM") 
        print(" /\\\t\t\t\t\t\t /\\")
        print("/__\\\t\t\t\t\t\t/__\\  ")
        print("\n \n")
        self.length =int(input("Enter length of Beam in meter=")) #Entring option
        self.loads=list([])
        inp=0
        while inp!="exit":
            print("1. Point Load")                    #options to perform actions
            print("2. Uniform Load")
            print("3. For Plotting")
            inp=int(input("Enter="))
            if inp==2:
                density=int(input("Enter Density of Uniform Load="))
                start=int(input("Enter starting point of Uniform Load fom left end="))
                end=int(input("Enter ending point of Uniform Load from left end="))
                for point in np.arange(start,end,0.01):
                    self.loads.append([round(point,2),density*0.01])
            elif inp==1:
                load=int(input("Enter load value="))
                start=int(input("Enter point of Load from left end="))
                self.loads.append([round(start,2),load])
            else:
                self.loads.sort()
                self.rxns=self.reactions(self.loads,self.length)          # calculating reactions
                break

        self.plot_bmd()                                                    # calling functions for plotting
        return 0
   
   def set_graph(self):                       #This function is responsible for styling the graph
      sns.set(rc={'axes.edgecolor':'black','xtick.color': 'black','axes.grid':'True','figure.figsize':(12,10)})
      
   
   def plot_bmd(self):                #This function is responsible for plotting BMD
      self.set_graph()
      points=self.give_bmd(self.loads,self.length)
      graph=sns.lineplot(x=points[0],y=points[1],label="BMD")
      graph.set_title("BMD",fontsize=50)
      graph.set_xlabel("Meters", size = 20)
      graph.set_ylabel("Kilo-Newton-Meters(BMD)\n", fontsize = 20)
      graph.legend()
   



project()

        