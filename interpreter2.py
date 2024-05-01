import textx

grammar = '''
Program:
  commands*=Command
;

Command:
  PrintCommand | AssignCommand | ShowCongratulationsCommand
;

PrintCommand:
  'SHOW' message=STRING
;

AssignCommand:
  'MY' 'MONEY' 'IS' amount=INT 'DOLLARS'
;

ShowCongratulationsCommand:
  'SHOW' 'CONGRATULATIONS! YOU WIN!' 'IF' 'MY' 'MONEY' 'IS' 'BIGGER THAN' threshold=INT 'DOLLARS'
;

Comment:
  /\/\/.*$/
;
'''

def interpreter(program):
    try:
        varmap = {'MONEY': 0}
        codeopoly_mm = textx.metamodel_from_str(grammar)
        codeopoly_model = codeopoly_mm.model_from_str(program)
     
        for c in codeopoly_model.commands:
            class_name = c.__class__.__name__
            if class_name == "AssignCommand":
                varmap['money'] = c.amount
                print(f"Assigned {c.amount} dollars to MONEY")
            elif class_name == "PrintCommand":
                print(c.message)
            elif class_name == "ShowCongratulationsCommand":
                if 'money' in varmap:
                    if varmap['money'] > c.threshold:
                        print("CONGRATULATIONS! YOU WIN!")
                    else:
                        print("YOU HAVEN'T WON YET")
                else:
                    print("MONEY NOT ASSIGNED YET")
    except:
                print("IF YOU SEE THIS MESSAGE PLEASE CLICK HELP AND SAMPLE PROGRAMS BUTTON")
