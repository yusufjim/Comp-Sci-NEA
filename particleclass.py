import pygame, sys
##########SUPER CLASS FOR COMPOSITE PARTICLES###########

from quarkclass import Quark

class Particle:
    quarkpos = [(500,150),(600,150),(550,250)]
    
    def __init__(self,name = "Main",quarkconfig = [None,None,None],partype = "",charge = 0,spin =0,strangeness = 0):
        self.name = name
        self.quarkconfig = quarkconfig
        self.partype = partype
        self.charge = charge
        self.spin = spin
        self.strangeness = strangeness
        self.partIdentify = [None,None,None]

    def isSpace(self):
        if None in self.quarkconfig:
            return True
        return False

    def clear(self):
        self.quarkconfig = [None,None,None]
        self.partype = ""
        self.charge = 0
        self.spin = 0
        self.strangeness = 0
        self.partIdentify = [None,None,None]
        
    

    def addQuark(self,quark):
        if self.isSpace() == True:
            for i in range(len(self.quarkconfig)):
                if self.quarkconfig[i] is None:
                    self.quarkconfig[i] = quark
                    self.partIdentify[i] = self.quarkconfig[i][0]
                    print(self.partIdentify)
                    return self.partIdentify
                    
                    break
        else:
            print("No space in quark")

    #edit function to use merge sort
    def sorting_func(self,quark):
        if self.isSpace() == False:
            for i in range(2):
                self.quarkconfig[i-1] = quark
                self.partIdentify[i-1] = self.quarkconfig[i-1][0]
                a = sorted(self.partIdentify)
                print (a)
                return a

        
            
        
        
    def getName(self):
        #"variablename".getName()
        return self.name

    def getPartype(self):
        #"variablename".getPartype()
        return self.partype

    def getCharge(self):
        #"variablename".getCharge()
        return self.charge

    def getSpin(self):
        #"variablename".getSpin()
        return self.spin

    def getQuarkpos(self):
        #"variablename".getQuarkpos()
        return self.quarkpos

    

    def getStrangeness(self):
        #"variablename".getStrangeness()
        return self.strangeness

    def quarkMakeup(self):
        return self.quarkconfig


    
class Proton(Particle):
    def __init__(self):
        Particle.__init__(self,"Proton",["Down","Up","Up"],"Baryon","1","1/2","0")



        
class AntiProton(Particle):
    def __init__(self):
       Particle.__init__(self,"Anti-Proton",["Anti-Down","Anti-Up","Anti-Up"],"Anti-Baryon","-1","1/2","0")

   
        
class Neutron(Particle):
   def __init__(self):
        Particle.__init__(self,"Neutron",["Down","Down","Up"],"Baryon","0","1/2","0")

  

    
class AntiNeutron(Particle):
    def __init__(self):
        Particle.__init__(self,"Anti-Proton",["Anti-Down","Anti-Down","Anti-Up"],"Anti-Baryon","0","1/2","0")

    


        
class KaonKplus(Particle):
    def __init__(self):
        Particle.__init__(self,"Kaon(K+)",["Anti-Strange","None","Up"],"Meson","1","0","0")

    


        
class KaonK0(Particle):
    def __init__(self):
        Particle.__init__(self,"Kaon(K0)",["Anti-Strange","Down","None"],"Meson","0","0","0")




class Sigmaplus(Particle):
    def __init__(self):
        Particle.__init__(self,"Sigma(∑+)",["Strange","Up","Up"],"Baryon","1","1/2","-1")



class Sigma0(Particle):
    def __init__(self):
        Particle.__init__(self,"Sigma(∑^0)",["Down","Strange","Up"],"Baryon","0","1/2","-1")

    


class Sigmaminus(Particle):
    def __init__(self):
        Particle.__init__(self,"Sigma(∑-)",["Down","Down","Strange"],"Baryon","-1","1/2","-1")

    


class Pionplus(Particle):
    def __init__(self):
        Particle.__init__(self,"Pion(π+)",["Anti-Down","None","Up"],"Meson","1","0","0")

           
class Pionminus(Particle):
    def __init__(self):
        Particle.__init__(self,"Pion(π-)",["Anti-Up","Down","None"],"Meson","0","0","0")



         
class Pion01(Particle):
    def __init__(self):
        Particle.__init__(self,"Pion(π^0)",["Anti-Up","None","Up"],"Meson","-1","0","0")

class Pion02(Particle):
    def __init__(self):
        Particle.__init__(self,"Pion(π^0)",["Anti-Down","Down","None"],"Meson","-1","0","0")

     
   
    

def main():
    #example to test if class is functioning
    proton = Proton()
    a = proton.getName()
    b = proton.getPartype()
    c = proton.getCharge()
    d = proton.getSpin()
    e = proton.getStrangeness()
    f = proton.quarkMakeup()


    print (a,b,c,d,e,f)
    
       

if __name__ == "__main__":
    main()
    
    
