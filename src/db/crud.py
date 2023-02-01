# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/db/crud.py
# Compiled at: 2023-02-01 04:15:08
# Size of source mod 2**32: 2117 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_stmts ::= _stmts . stmt
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
continues ::= _stmts . lastl_stmt continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmtl ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifpoplaststmtl ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtl ::= testexpr . POP_TOP c_stmts_opt
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jmp_true ::= POP_JUMP_IF_TRUE . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr . l_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  20        36  POP_BLOCK        
->                38  BEGIN_FINALLY    
                  40  WITH_CLEANUP_START
                  42  WITH_CLEANUP_FINISH
                  44  POP_FINALLY           0  ''
                  46  LOAD_CONST               False
                  48  RETURN_VALUE     
                50_0  COME_FROM            34  '34'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_stmts ::= _stmts . stmt
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
compare ::= compare_single . 
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
continues ::= _stmts . lastl_stmt continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmtl ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifpoplaststmtl ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtl ::= testexpr . POP_TOP c_stmts_opt
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jmp_true ::= POP_JUMP_IF_TRUE . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts ::= returns . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= return . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr . l_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  32        44  POP_BLOCK        
->                46  BEGIN_FINALLY    
                  48  WITH_CLEANUP_START
                  50  WITH_CLEANUP_FINISH
                  52  POP_FINALLY           0  ''
                  54  LOAD_CONST               False
                  56  RETURN_VALUE     
                58_0  COME_FROM            42  '42'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_stmts ::= _stmts . stmt
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
compare ::= compare_single . 
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
continues ::= _stmts . lastl_stmt continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmtl ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel JUMP_BACK come_froms
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifpoplaststmtl ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtl ::= testexpr . POP_TOP c_stmts_opt
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jmp_true ::= POP_JUMP_IF_TRUE . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms testexpr . l_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_l_stmts_opt . JUMP_BACK come_froms
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts . POP_BLOCK BEGIN_FINALLY COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  42        44  POP_BLOCK        
->                46  BEGIN_FINALLY    
                  48  WITH_CLEANUP_START
                  50  WITH_CLEANUP_FINISH
                  52  POP_FINALLY           0  ''
                  54  LOAD_CONST               None
                  56  RETURN_VALUE     
                58_0  COME_FROM            42  '42'
from pydantic import BaseModel
from typing import Union
from db import models
from db.db import SessionLocal

class User(BaseModel):
    user_id: int
    phone_number: str
    password: str
    about_me: str
    pin_chat_ids: list


def find_user--- This code section failed: ---

 L.  17         0  LOAD_GLOBAL              SessionLocal
                2  LOAD_METHOD              begin
                4  CALL_METHOD_0         0  ''
                6  SETUP_WITH           82  'to 82'
                8  STORE_FAST               's'

 L.  18        10  LOAD_FAST                's'
               12  LOAD_METHOD              query
               14  LOAD_GLOBAL              models
               16  LOAD_ATTR                users
               18  CALL_METHOD_1         1  ''
               20  LOAD_METHOD              filter
               22  LOAD_FAST                'condition'
               24  CALL_METHOD_1         1  ''
               26  LOAD_METHOD              first
               28  CALL_METHOD_0         0  ''
               30  STORE_FAST               'result'

 L.  19        32  LOAD_FAST                'result'
               34  POP_JUMP_IF_TRUE     50  'to 50'

 L.  20        36  POP_BLOCK        
               38  BEGIN_FINALLY    
               40  WITH_CLEANUP_START
               42  WITH_CLEANUP_FINISH
               44  POP_FINALLY           0  ''
               46  LOAD_CONST               False
               48  RETURN_VALUE     
             50_0  COME_FROM            34  '34'

 L.  21        50  LOAD_GLOBAL              User
               52  LOAD_FAST                'result'
               54  LOAD_ATTR                user_id
               56  LOAD_FAST                'result'
               58  LOAD_ATTR                phone_number

 L.  22        60  LOAD_FAST                'result'
               62  LOAD_ATTR                password

 L.  22        64  LOAD_FAST                'result'
               66  LOAD_ATTR                about_me

 L.  22        68  LOAD_FAST                'result'
               70  LOAD_ATTR                pin_chat_ids

 L.  21        72  LOAD_CONST               ('user_id', 'phone_number', 'password', 'about_me', 'pin_chat_ids')
               74  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
               76  STORE_FAST               'user'
               78  POP_BLOCK        
               80  BEGIN_FINALLY    
             82_0  COME_FROM_WITH        6  '6'
               82  WITH_CLEANUP_START
               84  WITH_CLEANUP_FINISH
               86  END_FINALLY      

 L.  23        88  LOAD_FAST                'user'
               90  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `BEGIN_FINALLY' instruction at offset 38


def by_phone_number_spec(phone_number):
    return models.users.phone_number == phone_number


def get_user--- This code section failed: ---

 L.  29         0  LOAD_GLOBAL              SessionLocal
                2  LOAD_METHOD              begin
                4  CALL_METHOD_0         0  ''
                6  SETUP_WITH           90  'to 90'
                8  STORE_FAST               's'

 L.  30        10  LOAD_FAST                's'
               12  LOAD_METHOD              query
               14  LOAD_GLOBAL              models
               16  LOAD_ATTR                users
               18  CALL_METHOD_1         1  ''
               20  LOAD_METHOD              filter
               22  LOAD_GLOBAL              models
               24  LOAD_ATTR                users
               26  LOAD_ATTR                phone_number
               28  LOAD_FAST                'phone_number'
               30  COMPARE_OP               ==
               32  CALL_METHOD_1         1  ''
               34  LOAD_METHOD              first
               36  CALL_METHOD_0         0  ''
               38  STORE_FAST               'result'

 L.  31        40  LOAD_FAST                'result'
               42  POP_JUMP_IF_TRUE     58  'to 58'

 L.  32        44  POP_BLOCK        
               46  BEGIN_FINALLY    
               48  WITH_CLEANUP_START
               50  WITH_CLEANUP_FINISH
               52  POP_FINALLY           0  ''
               54  LOAD_CONST               False
               56  RETURN_VALUE     
             58_0  COME_FROM            42  '42'

 L.  33        58  LOAD_GLOBAL              User
               60  LOAD_FAST                'result'
               62  LOAD_ATTR                user_id
               64  LOAD_FAST                'result'
               66  LOAD_ATTR                phone_number

 L.  34        68  LOAD_FAST                'result'
               70  LOAD_ATTR                password

 L.  34        72  LOAD_FAST                'result'
               74  LOAD_ATTR                about_me

 L.  34        76  LOAD_FAST                'result'
               78  LOAD_ATTR                pin_chat_ids

 L.  33        80  LOAD_CONST               ('user_id', 'phone_number', 'password', 'about_me', 'pin_chat_ids')
               82  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
               84  STORE_FAST               'user'
               86  POP_BLOCK        
               88  BEGIN_FINALLY    
             90_0  COME_FROM_WITH        6  '6'
               90  WITH_CLEANUP_START
               92  WITH_CLEANUP_FINISH
               94  END_FINALLY      

 L.  35        96  LOAD_FAST                'user'
               98  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `BEGIN_FINALLY' instruction at offset 46


def get_user_by_id--- This code section failed: ---

 L.  39         0  LOAD_GLOBAL              SessionLocal
                2  LOAD_METHOD              begin
                4  CALL_METHOD_0         0  ''
                6  SETUP_WITH           86  'to 86'
                8  STORE_FAST               's'

 L.  40        10  LOAD_FAST                's'
               12  LOAD_METHOD              query
               14  LOAD_GLOBAL              models
               16  LOAD_ATTR                users
               18  CALL_METHOD_1         1  ''
               20  LOAD_METHOD              filter
               22  LOAD_GLOBAL              models
               24  LOAD_ATTR                users
               26  LOAD_ATTR                user_id
               28  LOAD_FAST                'user_id'
               30  COMPARE_OP               ==
               32  CALL_METHOD_1         1  ''
               34  LOAD_METHOD              first
               36  CALL_METHOD_0         0  ''
               38  STORE_FAST               'result'

 L.  41        40  LOAD_FAST                'result'
               42  POP_JUMP_IF_TRUE     58  'to 58'

 L.  42        44  POP_BLOCK        
               46  BEGIN_FINALLY    
               48  WITH_CLEANUP_START
               50  WITH_CLEANUP_FINISH
               52  POP_FINALLY           0  ''
               54  LOAD_CONST               None
               56  RETURN_VALUE     
             58_0  COME_FROM            42  '42'

 L.  43        58  LOAD_GLOBAL              User
               60  LOAD_FAST                'result'
               62  LOAD_ATTR                user_id
               64  LOAD_FAST                'result'
               66  LOAD_ATTR                phone_number

 L.  44        68  LOAD_FAST                'result'
               70  LOAD_ATTR                password

 L.  44        72  LOAD_FAST                'result'
               74  LOAD_ATTR                about_me

 L.  43        76  LOAD_CONST               ('user_id', 'phone_number', 'password', 'about_me')
               78  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
               80  STORE_FAST               'user'
               82  POP_BLOCK        
               84  BEGIN_FINALLY    
             86_0  COME_FROM_WITH        6  '6'
               86  WITH_CLEANUP_START
               88  WITH_CLEANUP_FINISH
               90  END_FINALLY      

 L.  45        92  LOAD_FAST                'user'
               94  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `BEGIN_FINALLY' instruction at offset 46


def register_user(phone_number: str, password: str, about_me: str):
    with SessionLocal.begin as (s):
        user = models.users(phone_number=phone_number, password=password,
          about_me=about_me,
          pin_chat_ids=[])
        s.adduser
        s.commit


def change_profile(username: str, new_about_me: str):
    with SessionLocal.begin as (s):
        s.querymodels.users.filter(models.users.phone_number == username).update{'about_me': new_about_me}
        s.commit
