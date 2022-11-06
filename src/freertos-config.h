
#pragma once

#define CPP_FREERTOS_NO_EXCEPTIONS
#define CPP_FREERTOS_NO_CPP_STRINGS

#ifndef CPP_FREERTOS_DEFAULT_NAMESPACE
#define CPP_FREERTOS_DEFAULT_NAMESPACE 1
#endif

#ifdef ESP32
#  define _taskENTER_CRITICAL() taskENTER_CRITICAL(&esp32Mutex)
#  define _taskEXIT_CRITICAL() taskEXIT_CRITICAL(&esp32Mutex)
#else
#  define _taskENTER_CRITICAL() taskENTER_CRITICAL()
#  define _taskEXIT_CRITICAL() taskEXIT_CRITICAL()
#endif

#if CPP_FREERTOS_DEFAULT_NAMESPACE
namespace cpp_freertos{}
using namespace cpp_freertos;
#endif

