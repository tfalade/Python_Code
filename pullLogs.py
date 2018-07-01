'''
Created on May 23, 2015

@author: tfalade
'''

'''
    To run the python code on the server, you have to be in the folder /usr/local/blackboard/logs to be able to access the Services.txt
'''
    

def pull_log_services(id):
    start_expression = id
    end_expression = 'at java.lang.Thread.run(Thread.java:'
    printline = False
    bigData = open('Services.txt','r')
    openBook = bigData.readlines()
    for line in openBook:
        if start_expression in line:
            printline = True
            
        elif end_expression in line:
            printline = False
            print(line.strip())
        if printline == True:
            print(line.strip())

//Illustration of how to run the code
      
pull_log_services('9a815cce-17fe-44c8-92e1-22dca41ad0d7')        