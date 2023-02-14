import datetime
import time


class my_task_pump(): #classe pour les pumps

    name = None
    period = -1
    execution_time = -1
    last_deadline = -1
    last_execution_time = None
    stp = False  # variable pour arreter de remplir si le tank est plein
    ############################################################################
    def __init__(self, name, period, execution_time, last_execution):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.last_execution_time = last_execution
        stp =False #variable pour arreter de remplir si le tank est plein


    ############################################################################
    def run(self):
        global tank
        print("Execution du pump : " + self.name)
        if (self.name == "1"):
            value = 10
        else:
            value = 20

        if((tank+value)<50):
            tank += value
            time.sleep(self.execution_time)
            print("Valeur du tank actuelle :",tank)
        else:
            print(f"Pump {self.name} est finie. Le Tank est plein !")
            stp=True

        print(f"Pump {self.name} est finie.")


####################################################################################################


class my_task_machine(): #class pour les machines

    name = None
    period = -1
    execution_time = -1
    last_deadline = -1
    last_execution_time = None
    stp = False  # variable pour arreter de produire si le tank est vide

    ############################################################################
    def __init__(self, name, period, execution_time, last_execution):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.last_execution_time = last_execution
        stp = False  # variable pour arreter de produire si le tank est vide


    ############################################################################
    def run(self):
        global tank
        global stock1
        global stock2

        print("Execution de la machine : " + self.name)

        if( tank > 5 and self.name=="2" or tank> 25 and self.name=="1") :
            if (self.name == "1"):
                value = 25
                tank -= value
                stock1 += 1
                time.sleep(self.execution_time)
                print("valeur du stock of wheels actuelle : ", stock1)
                print("Et valeur du tank actuelle :", tank)

            elif (self.name=="2"):
                value = 5
                tank -= value
                stock2 +=1

                time.sleep(self.execution_time)
                print("Valeur du stock of motors actuelle : ", stock2)
                print("Et valeur du tank actuelle :", tank)


        else :
            print(f"Machine {self.name} est finie. Le Tank est vide !")
            stp=True
        print(f"Machine {self.name} est finie.")


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

    tank = 0

    stock1 = 0 #nb wheels
    stock2 = 0 #nb motors

    last_execution = datetime.datetime.now()
    print("__ Execution du programme pendant 1 minute __")

    # Instanciation of task objects
    task_list_pumps = []
    t1 =my_task_pump(name="1", period=5, execution_time=2,last_execution=last_execution)
    t2 =my_task_pump(name="2", period=15, execution_time=3, last_execution=last_execution)
    task_list_pumps.append(t1)
    task_list_pumps.append(t2)

    task_list_machines = []
    t3 = my_task_machine(name="1", period=5, execution_time=5, last_execution=last_execution)
    t4 = my_task_machine(name="2", period=5, execution_time=3, last_execution=last_execution)
    task_list_machines.append(t3)
    task_list_machines.append(t4)

    start_time = datetime.datetime.now()
    while (datetime.datetime.now() - start_time).seconds < 60:

        if (tank>= 50): #prioriser les machines
            for task_to_run in task_list_machines :
                task_to_run.run()
                if (task_to_run.stp == True):
                    break;
        if((stock1 / 4 ) > stock2) :#prioriser la machine 1
            t4.run()

            for task_to_run in task_list_pumps :
                task_to_run.run()
                if(task_to_run.stp==True) :
                    break;
        if ((stock1 / 4 ) < stock2) :#prioriser la machine 2
            t3.run()

            for task_to_run in task_list_pumps:
                task_to_run.run()
                if (task_to_run.stp == True):
                    break;

        #sinon on fait au hasard en executant les pums et les machines

        for task_to_run in task_list_pumps:
            task_to_run.run()
            if (task_to_run.stp == True):
                break;
        for task_to_run in task_list_machines :
            task_to_run.run()
            if (task_to_run.stp == True):
                break;



# If the tank is full, Pumps should have a really low priority
# If[nbwheels / 4 > nbmotors] the Machine 1 will have a higher priority
# If[nbwheels / 4 < nbmotors] the Machine 2 will have a higher priority

# For each task in my task list :
    # If the rules don’t allow my task to be executed : discarded
    # Then I decide which task has the more priority regarding other rules
# I run my task


    print("Fin des taches")
    print("La valeur finale du Tank est : ",tank)
    print("La valeur finale du stock 1, stock des wheels est : ",stock1)
    print("La valeur finale du stock 2, stock des motors est : ", stock2)
#At the end we want to have the maximum of [1 engine + 4 wheels] available

