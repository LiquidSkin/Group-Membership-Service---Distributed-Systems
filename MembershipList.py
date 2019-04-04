from Server import process_list
from random import randint
from collections import defaultdict
number = 3
process_status = {}
active_processes = []
passive_processes = []
Membership_list= {}

def create_process_list():
    for i in range(len(process_list)):
      n = repr(process_list[i])
      process = 'm' + n
      with open("processes.json") as file:
         content = file.read()
         if process in content:
             process_status[process] = 'Active'
             active_processes.append(process)
             passive_processes.append(process)








def Membership_List(active_processes, passive_processes, size):

     for i in range(0,size):
         Membership_list.setdefault(active_processes[i],[])
         list = []
         while len(list) < 3:
             n = randint(0, size-1)
             if passive_processes[n] not in list and active_processes[i] != passive_processes[n]:
                   list.append(passive_processes[n])
         Membership_list[active_processes[i]] = list
         #print(list)










create_process_list()
#print(process_status)
#print(active_processes)
#print(passive_processes)
size = len(active_processes)
Membership_List(active_processes,passive_processes,size)
print(Membership_list)