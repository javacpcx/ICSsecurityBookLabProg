#include "beremiz.h"
#ifndef __POUS_H
#define __POUS_H

#include "accessor.h"
#include "iec_std_lib.h"

__DECLARE_ENUMERATED_TYPE(LOGLEVEL,
  LOGLEVEL__CRITICAL,
  LOGLEVEL__WARNING,
  LOGLEVEL__INFO,
  LOGLEVEL__DEBUG
)
// FUNCTION_BLOCK LOGGER
// Data part
typedef struct {
  // FB Interface - IN, OUT, IN_OUT variables
  __DECLARE_VAR(BOOL,EN)
  __DECLARE_VAR(BOOL,ENO)
  __DECLARE_VAR(BOOL,TRIG)
  __DECLARE_VAR(STRING,MSG)
  __DECLARE_VAR(LOGLEVEL,LEVEL)

  // FB private variables - TEMP, private and located variables
  __DECLARE_VAR(BOOL,TRIG0)

} LOGGER;

void LOGGER_init__(LOGGER *data__, BOOL retain);
// Code part
void LOGGER_body__(LOGGER *data__);
// PROGRAM PROGRAM0
// Data part
typedef struct {
  // PROGRAM Interface - IN, OUT, IN_OUT variables

  // PROGRAM private variables - TEMP, private and located variables
  __DECLARE_LOCATED(BOOL,Y0)
  __DECLARE_LOCATED(BOOL,Y1)
  __DECLARE_LOCATED(BOOL,Y2)
  __DECLARE_LOCATED(BOOL,Y3)
  __DECLARE_LOCATED(BOOL,Y4)
  __DECLARE_LOCATED(WORD,D0)
  __DECLARE_LOCATED(WORD,D1)
  __DECLARE_LOCATED(WORD,D2)
  __DECLARE_LOCATED(WORD,D3)
  __DECLARE_LOCATED(INT,M1)
  __DECLARE_LOCATED(INT,M2)
  __DECLARE_LOCATED(INT,M3)
  __DECLARE_LOCATED(INT,M4)
  TOF TOF0;
  TON TON0;
  __DECLARE_VAR(BOOL,_TMP_OR9_OUT)
  __DECLARE_VAR(BOOL,_TMP_GT16_OUT)

} PROGRAM0;

void PROGRAM0_init__(PROGRAM0 *data__, BOOL retain);
// Code part
void PROGRAM0_body__(PROGRAM0 *data__);
#endif //__POUS_H
