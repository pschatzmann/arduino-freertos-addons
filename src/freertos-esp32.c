/**
 * @file freertos-esp32.c
 * @author Phil Schatzmann
 * @brief In standard RTOS taskENTER_CRITICAL_EXT() does not require a parameter. In the ESP32
 * implementation however we need to provide one. We use a common esp32Mutex variable!
 * @version 0.1
 * @date 2022-11-06
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifdef ESP32
#include "FreeRTOS.h"
#include "task.h"
portMUX_TYPE esp32Mutex = portMUX_INITIALIZER_UNLOCKED;
#endif