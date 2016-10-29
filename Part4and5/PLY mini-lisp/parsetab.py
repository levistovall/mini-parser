
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '135FD93ABDFCBBA39CE6980836C91B8B'
    
_lr_action_items = {'QUOTE':([0,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,25,27,28,30,33,],[1,-16,-17,-20,-18,-15,-22,-21,1,-4,1,1,-10,-12,-11,-9,29,-5,-14,1,-13,]),'$end':([0,2,3,5,6,7,8,9,10,11,12,13,15,27,28,33,],[-19,-16,-17,-20,-2,-18,-15,-3,-22,-21,0,-1,-4,-5,-14,-13,]),'NUM':([0,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,30,33,],[3,-16,-17,-20,-18,-15,-22,-21,3,-4,3,3,-10,-12,-11,-9,-5,-14,3,-13,]),'LPAREN':([0,1,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,29,30,33,],[4,14,-16,-17,-20,-18,-15,-22,-21,4,-4,4,4,-10,-12,-11,-9,-5,-14,30,4,-13,]),'TRUE':([0,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,30,33,],[5,-16,-17,-20,-18,-15,-22,-21,5,-4,5,5,-10,-12,-11,-9,-5,-14,5,-13,]),'TEXT':([0,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,30,33,],[7,-16,-17,-20,-18,-15,-22,-21,7,-4,7,7,-10,-12,-11,-9,-5,-14,7,-13,]),'RPAREN':([2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,23,24,26,27,28,30,31,32,33,],[-16,-17,-20,-18,-15,-22,-21,-8,-4,-8,-8,-10,-7,-11,-9,27,28,-6,-5,-14,-8,32,33,-13,]),'SIMB':([0,2,3,4,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,30,33,],[8,-16,-17,16,-20,-18,-15,-22,-21,8,-4,8,8,-10,-12,-11,-9,-5,-14,8,-13,]),'LAMBDA':([17,],[25,]),'NIL':([0,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,30,33,],[10,-16,-17,-20,-18,-15,-22,-21,10,-4,10,10,-10,-12,-11,-9,-5,-14,10,-13,]),'MAPP':([4,],[17,]),'FALSE':([0,2,3,5,7,8,10,11,14,15,16,18,19,20,21,22,27,28,30,33,],[11,-16,-17,-20,-18,-15,-22,-21,11,-4,11,11,-10,-12,-11,-9,-5,-14,11,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'item':([14,16,18,30,],[18,18,18,18,]),'bool':([0,14,16,18,30,],[2,2,2,2,2,]),'quoted_list':([0,14,16,18,30,],[6,19,19,19,19,]),'list':([1,],[15,]),'empty':([14,16,18,30,],[20,20,20,20,]),'call':([0,14,16,18,30,],[9,21,21,21,21,]),'exp':([0,],[12,]),'atom':([0,14,16,18,30,],[13,22,22,22,22,]),'items':([14,16,18,30,],[23,24,26,31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',130),
  ('exp -> quoted_list','exp',1,'p_exp_qlist','yacc.py',134),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',138),
  ('quoted_list -> QUOTE list','quoted_list',2,'p_quoted_list','yacc.py',142),
  ('list -> LPAREN items RPAREN','list',3,'p_list','yacc.py',147),
  ('items -> item items','items',2,'p_items','yacc.py',151),
  ('items -> empty','items',1,'p_items_empty','yacc.py',155),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',159),
  ('item -> atom','item',1,'p_item_atom','yacc.py',163),
  ('item -> quoted_list','item',1,'p_item_list','yacc.py',171),
  ('item -> call','item',1,'p_item_call','yacc.py',175),
  ('item -> empty','item',1,'p_item_empty','yacc.py',179),
  ('call -> LPAREN MAPP LAMBDA QUOTE LPAREN items RPAREN RPAREN','call',8,'p_call_mapp','yacc.py',183),
  ('call -> LPAREN SIMB items RPAREN','call',4,'p_call','yacc.py',189),
  ('atom -> SIMB','atom',1,'p_atom_simbol','yacc.py',199),
  ('atom -> bool','atom',1,'p_atom_bool','yacc.py',203),
  ('atom -> NUM','atom',1,'p_atom_num','yacc.py',207),
  ('atom -> TEXT','atom',1,'p_atom_word','yacc.py',211),
  ('atom -> <empty>','atom',0,'p_atom_empty','yacc.py',215),
  ('bool -> TRUE','bool',1,'p_true','yacc.py',219),
  ('bool -> FALSE','bool',1,'p_false','yacc.py',223),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',227),
]
