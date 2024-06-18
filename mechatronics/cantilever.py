import numpy as np
import seaborn as sns

class project:
   
   length=0
   rxns=[]
   loads=list([])
   
   def reactions(self,loads,length):
      left=0
      total=0
      total=0
      for load in loads:
         total+=(load[1])
      left=total
      return (left,)


   def give_bmd(self,loads,length):
      ret=[]
      rxns=self.rxns
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
      y_points=[point[1] for point in ret]
      return (x_points,y_points)
      
      
   def give_sfd(self,loads,length):
      ret=[]
      rxns=self.rxns
      loads.append([0.0,-1*rxns[0]])
      load_dct=dict({})
      for load in loads:
         load_dct[load[0]]=load[1]
      cur_load=list([])
      total=0
      for point in np.arange(length+0.1,0.0,-0.01):
         point=round(point,2)
         load_x=load_dct.get(point)
         if load_x==None:
            pass
         else:
            cur_load.append([point,load_x])
      
         net=0
         for load in cur_load:
            net+=-1*load[1]
         ret.append([point,net])
      
      x_points=[point[0] for point in ret]
      y_points=[point[1] for point in ret]
    
      return (x_points,y_points)
   
   def input(self):
        self.length =int(input("Enter length of Beam in meter="))
        self.loads=list([])
        inp=0
        while inp!="exit":
            print("1. Point Load")
            print("2. Uniform Load")
            print("3 exit to stop")
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
                self.rxns=self.reactions(self.loads,self.length)
                break

        self.option()
        return 0
   
   def set_graph(self):
      sns.set(rc={'axes.edgecolor':'black','xtick.color': 'black','axes.grid':'True','figure.figsize':(17.7,12.27)})
    
      
   
   def plot_bmd(self):
      self.set_graph()
      points=self.give_bmd(self.loads,self.length)
      graph=sns.lineplot(x=points[0],y=points[1],label="BMD")
      graph.set_title("BMD",fontsize=50)
      graph.set_xlabel("Meters", fontsize = 15)
      graph.set_ylabel("Kilo-Newton-Meters", fontsize = 15)
      graph.legend()
   
   def plot_sfd(self):
      self.set_graph()
      points=self.give_sfd(self.loads,self.length)
      graph=sns.lineplot(x=points[0],y=points[1],label="SFD")
      graph.set_title("SFD",fontsize=50)
      graph.set_xlabel("Meters", fontsize = 15)
      graph.set_ylabel("Kilo-Newton", fontsize = 15)
      graph.legend()
    
   def option(self):
      inp=int(input("1.SFD\n2.BMD"))
      if inp==1:
        self.plot_sfd()
      else:
        self.plot_bmd()