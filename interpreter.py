#CISC 3160 Project - Leard Kelmendi - Professor Neng-Fa Zhou - Spring 2022
#Does not support parenthesis at the moment.

import os
import sys
import re

if len(sys.argv) < 2:
    print('you must supply an input file')
    quit()

variables = {}
chr = 0
source = ''

with open(sys.argv[1]) as file:
    source = file.read()

#Eats blank spacing
def extraspace():
    global chr
    while chr < len(source) and source[chr] in [' ', '\t', '\n', ';']:
        chr += 1

def handle_assignment():
    global chr

    #Finding variable name
    var_name = re.search(r'^([a-zA-Z0-9]+[_]*[a-zA-Z0-9]*)', source[chr:])[0]

    #Moving cursor over the length of variable name, extra spacing, and assignment operator '='.
    chr += len(var_name)
    extraspace()
    chr += 1
    extraspace()

    value1 = ''
    operation = ''
    value2 = ''
    end_value = ''

    #Finding first value
    if (re.match(r'^([1-9]+[0-9]*)', source[chr:])) or (re.match(r'^[0]', source[chr:])):
        while chr < len(source) and (not source[chr] in ['\n', '+', '/', '-', '*', ' ', ';']):
            value1 += source[chr]
            chr += 1

        extraspace()

        #Finding operator
        if re.match(r'^([+|-])', source[chr:]):
            operation += source[chr]
            chr += 1
        elif re.match(r'^([*|/])', source[chr:]):
            operation += source[chr]
            chr += 1

        extraspace()
        
        #Finding second value
        if re.match(r'^([1-9]+[0-9]*)', source[chr:]):
            while chr < len(source) and (not source[chr] in ['\n', '+', '/', '-', '*', ' ', ';']):
                value2 += source[chr]
                chr += 1

        extraspace()

        #Determining operation and end value if needed
        if operation == '+':
            end_value = int(value1) + int(value2)
        elif operation == '-':
            end_value = int(value1) - int(value2)
        elif operation == '*':
            end_value = int(value1) * int(value2)
        elif operation == '/': 
            end_value = int(value1) / int(value2)
        else:
            end_value = ''

        #If an operation is being done, print end value. Otherwise, just print the assigned value.
        if len(operation) != 0:
            print(var_name, '=', end_value)
        else:
            print(var_name, '=', value1)

    else:
        print('invalid assignment')
        quit()

while chr < len(source):
    if re.match(r'^([a-zA-Z0-9]+[_]*[a-zA-Z0-9]*)\s+?=', source[chr:]):
        handle_assignment()