import textx

grammar = '''
Program:
  commands*=Command
;

Command:
  PrintCommand | AssignCommand | MoveCommand | ShowSpacesCommand | ShowMoveCommand
;

PrintCommand:
  'SHOW' 'GAME PIECE'
;

AssignCommand:
  'MY' ('MONEY' 'IS' amount=INT 'DOLLARS' | 'GAME PIECE' 'IS' identifier=ID)
;

MoveCommand:
  'MOVE' 'GAME PIECE' number=INT 'SPACES'
;

ShowSpacesCommand:
  'SHOW'
;

ShowMoveCommand:
  'GAME PIECE' number=INT 'SPACES'
;

Comment:
  /\/\/.*$/
;
'''

def interpreter(program): 
    try:
        varmap = {'total_spaces_moved': 0}  
        codeopoly_mm = textx.metamodel_from_str(grammar)
        codeopoly_model = codeopoly_mm.model_from_str(program)
     
        for c in codeopoly_model.commands:
            class_name = c.__class__.__name__
            if class_name == "AssignCommand":
                varmap['game_piece'] = c.identifier
                print(f"GAME PIECE IS {c.identifier}")
                print(f"CURRENT SPACE BY {c.identifier} IS {varmap['total_spaces_moved']}")
            elif class_name == "MoveCommand":
                if 'game_piece' in varmap:
                    varmap['total_spaces_moved'] += c.number 
                    print(f"{varmap['game_piece']} MOVED {c.number} SPACES")
                    print(f"CURRENT SPACE BY {varmap['game_piece']} IS {varmap['total_spaces_moved']}")
                else:
                    print("No game piece assigned yet. Cannot move.")
            elif class_name == "ShowSpacesCommand":
                if 'game_piece' in varmap:
                    print(f"GAME PIECE MOVED {varmap['game_piece']}: {varmap['total_spaces_moved']}")
                else:
                    print("No game piece assigned yet.")
            elif class_name == "PrintCommand":
                if 'game_piece' in varmap:
                    if varmap['total_spaces_moved'] == 0:
                        print(f"{varmap['game_piece']} AT 0 SPACES")
                    else:
                        print(f"Showing game piece: {varmap['game_piece']}")
                else:
                    print("No game piece assigned yet.")

            varmap['total_spaces_moved'] = 0

    except:
                print("IF YOU SEE THIS MESSAGE PLEASE CLICK HELP AND SAMPLE PROGRAMS BUTTON")
