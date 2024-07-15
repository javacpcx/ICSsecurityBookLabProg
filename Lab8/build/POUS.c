void LOGGER_init__(LOGGER *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->MSG,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->LEVEL,LOGLEVEL__INFO,retain)
  __INIT_VAR(data__->TRIG0,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void LOGGER_body__(LOGGER *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  if ((__GET_VAR(data__->TRIG,) && !(__GET_VAR(data__->TRIG0,)))) {
    #define GetFbVar(var,...) __GET_VAR(data__->var,__VA_ARGS__)
    #define SetFbVar(var,val,...) __SET_VAR(data__->,var,__VA_ARGS__,val)

   LogMessage(GetFbVar(LEVEL),(char*)GetFbVar(MSG, .body),GetFbVar(MSG, .len));
  
    #undef GetFbVar
    #undef SetFbVar
;
  };
  __SET_VAR(data__->,TRIG0,,__GET_VAR(data__->TRIG,));

  goto __end;

__end:
  return;
} // LOGGER_body__() 





void PROGRAM0_init__(PROGRAM0 *data__, BOOL retain) {
  __INIT_LOCATED(BOOL,__IX100_0,data__->Y0,retain)
  __INIT_LOCATED_VALUE(data__->Y0,__BOOL_LITERAL(FALSE))
  __INIT_LOCATED(BOOL,__IX100_1,data__->Y1,retain)
  __INIT_LOCATED_VALUE(data__->Y1,__BOOL_LITERAL(FALSE))
  __INIT_LOCATED(BOOL,__IX100_2,data__->Y2,retain)
  __INIT_LOCATED_VALUE(data__->Y2,__BOOL_LITERAL(FALSE))
  __INIT_LOCATED(BOOL,__IX100_3,data__->Y3,retain)
  __INIT_LOCATED_VALUE(data__->Y3,__BOOL_LITERAL(FALSE))
  __INIT_LOCATED(BOOL,__IX100_4,data__->Y4,retain)
  __INIT_LOCATED_VALUE(data__->Y4,__BOOL_LITERAL(FALSE))
  __INIT_LOCATED(WORD,__QW104,data__->D0,retain)
  __INIT_LOCATED_VALUE(data__->D0,0)
  __INIT_LOCATED(WORD,__QW105,data__->D1,retain)
  __INIT_LOCATED_VALUE(data__->D1,0)
  __INIT_LOCATED(WORD,__QW106,data__->D2,retain)
  __INIT_LOCATED_VALUE(data__->D2,0)
  __INIT_LOCATED(WORD,__QW107,data__->D3,retain)
  __INIT_LOCATED_VALUE(data__->D3,0)
  __INIT_LOCATED(INT,__IW100,data__->M1,retain)
  __INIT_LOCATED_VALUE(data__->M1,0)
  __INIT_LOCATED(INT,__IW101,data__->M2,retain)
  __INIT_LOCATED_VALUE(data__->M2,0)
  __INIT_LOCATED(INT,__IW102,data__->M3,retain)
  __INIT_LOCATED_VALUE(data__->M3,0)
  __INIT_LOCATED(INT,__IW103,data__->M4,retain)
  __INIT_LOCATED_VALUE(data__->M4,0)
  TOF_init__(&data__->TOF0,retain);
  TON_init__(&data__->TON0,retain);
  __INIT_VAR(data__->_TMP_OR9_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_GT16_OUT,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void PROGRAM0_body__(PROGRAM0 *data__) {
  // Initialise TEMP variables

  __SET_VAR(data__->,_TMP_OR9_OUT,,OR__BOOL__BOOL(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (BOOL)__GET_LOCATED(data__->Y0,),
    (BOOL)__GET_LOCATED(data__->Y1,)));
  __SET_LOCATED(data__->,Y0,,__GET_VAR(data__->_TMP_OR9_OUT,));
  __SET_VAR(data__->TON0.,IN,,__GET_LOCATED(data__->Y3,));
  __SET_VAR(data__->TON0.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON0);
  __SET_VAR(data__->TOF0.,IN,,__GET_VAR(data__->TON0.Q,));
  __SET_VAR(data__->TOF0.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TOF_body__(&data__->TOF0);
  __SET_LOCATED(data__->,Y3,,__GET_VAR(data__->TOF0.Q,));
  __SET_VAR(data__->,_TMP_GT16_OUT,,GT__BOOL__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_LOCATED(data__->M1,),
    (INT)__GET_LOCATED(data__->M2,)));
  __SET_LOCATED(data__->,Y3,,__GET_VAR(data__->_TMP_GT16_OUT,));

  goto __end;

__end:
  return;
} // PROGRAM0_body__() 





