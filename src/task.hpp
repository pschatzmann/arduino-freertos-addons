
#pragma once
#include "freertos-config.h"
#include "thread.hpp"

namespace cpp_freertos {
/**
 * @brief A Thread which has the Run method implemented as loop which is executing
 * the function that is passed in the constructor.
 * 
 */
class Task : public Thread {
public:
  Task(const char *Name, uint16_t StackDepth, UBaseType_t Priority,
       void (*fn)(), size_t numberOfLoops=0)
      : Thread(Name, StackDepth, Priority) {
    task = fn;
    count = numberOfLoops;
  }

  /**
   * @brief Custom Implementation which is executing the provided method in a loop
   * 
   */
  virtual void Run() {
    if (count==0){
      while (true) {
        task();
      }
    } else {
      for (size_t j=0;j<count;j++){
        task();
      }
    }
    // end task
    vTaskDelete(NULL);
    setThreadStarted(false);
  }

protected:
  void (*task)() = nullptr;
  size_t count=0;
};

} // namespace cpp_freertos