import textx

grammar = '''
Program:
  commands*=Command
;

Command:
  PrintCommand | AssignCommand | AddValueCommand
;

PrintCommand:
  'SHOW' variable=ID
;

AssignCommand:
  'MY' variable=ID 'IS' value=INT
;

AddValueCommand:
  'COLLECT PASS GO' value=INT 'DOLLARS TO' variable=ID
;

Comment:
  /\/\/.*$/
;
'''

def interpreter(program):
    try:
        varmap = {}  # Initialize variable map
        codeopoly_mm = textx.metamodel_from_str(grammar)
        codeopoly_model = codeopoly_mm.model_from_str(program)
    
        for c in codeopoly_model.commands:
            class_name = c.__class__.__name__
            if class_name == "AssignCommand":
                varmap[c.variable] = c.value
                print("ASSIGNED {} DOLLARS TO {} VARIABLE".format(c.value, c.variable))
            elif class_name == "PrintCommand":
                if c.variable in varmap:
                    print("VALUE OF {} VARIABLE IS {} DOLLARS".format(c.variable, varmap[c.variable]))
                else:
                    print("'{}' PLEASE ASSIGN VALUE USING KEYWORD MY".format(c.variable))
            elif class_name == "AddValueCommand":
                if c.variable in varmap:
                    varmap[c.variable] += c.value
                    print("{} DOLLARS ADDED TO {} VARIABLE \nNEW MONEY VARIABLE VALUE IS {} DOLLARS".format(c.value, c.variable, varmap[c.variable]))
                else:
                    print("'{}' VALUE NOT ASSIGNED".format(c.variable))
    except:
                print("IF YOU SEE THIS MESSAGE PLEASE CLICK HELP AND SAMPLE PROGRAMS BUTTON")
