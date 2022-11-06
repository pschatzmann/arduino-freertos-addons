# FreeRTOS-addons

Standard FreeRTOS uses C based API. However I prefer to have some nice C++ abstractions. That's when I disovered the [freertos-addons project from Michael Becker](https://github.com/michaelbecker/freertos-addons). 

I have converted it to an Arduino Library, so that it can be used e.g. on an ESP32.

## Current Features

+ C++ Wrappers [![Coverity Scan Build Status](https://scan.coverity.com/projects/9669/badge.svg)](https://scan.coverity.com/projects/michaelbecker-freertos-addons)
  - A collection of C++ wrappers encapsulating FreeRTOS functionality, allowing you to write your RTOS application in C++ while still using FreeRTOS. This wrapper layer does all the integration work for you.
  - This library is for you if you are planning on using C++ and FreeRTOS in your project but don't want to spend the time integrating the two.
  - Everything was tested successfully using FreeRTOS versions 8.2.3, 9.0.0, and 10.0.0.
  - There are numerous demo / unit test projects using these wrappers and various features they provide. Last count we are at 48 Demo projects showing how you might use the C++ Wrapper library.
  - Licensing now follows the [MIT Open Source License](https://opensource.org/licenses/MIT), the same as [FreeRTOS](https://www.freertos.org/a00114.html) starting from version 10.0.0.
  - [Project web page](http://michaelbecker.github.io/freertos-addons/)
  - [Full cross-referenced documentation](http://michaelbecker.github.io/freertos-addons/cppdocs/html/index.html). Documents were auto-generated and cross-referenced using Doxygen.

+ C Add-on Wrappers
  - A collection of C Add-on functionality for FreeRTOS. Right now these consist of:
  - Memory Pools: Fixed size memory allocation buffers. Using these elminates the possibility of memory fragmentation. There is overhead associated with these, so it's better if you are maximizing the size of each allocation.
  - Reader / Writer Locks: These allow multiple threads to simultaneously access a shared resource all as readers. If something needs to change, then a Writer lock needs to be taken which will allow a singe thread to modify the shared resource.
  - Workqueues: These allow you to queue "work" (i.e. a function) to a different thread. Useful if you have a lot of "one off" things that need to be done in different threads but they happen very asynchronous.
  - Licensing now follows the [MIT Open Source License](https://opensource.org/licenses/MIT), the same as [FreeRTOS](https://www.freertos.org/a00114.html) starting from version 10.0.0.
  - There are numerous demo / unit test projects using these wrappers and various features they provide. Last count we are at 10 Demo projects showing how you might use the C libraries.
  - In addition, to support these there are implementations of standard optimized compter science singly linked lists, doubly linked circular lists, queues, and stacks.
  - [Full cross-referenced documentation](http://michaelbecker.github.io/freertos-addons/cdocs/html/index.html). Documents were auto-generated and cross-referenced using Doxygen.

## Documentation

- [Class Documentation](https://pschatzmann.github.io/arduino-freertos-addons/docs/html/annotated.html)

### Installation in Arduino

You can download the library as zip and call include Library -> zip library. Or you can git clone this project into the Arduino libraries folder e.g. with

```
cd  ~/Documents/Arduino/libraries
git clone pschatzmann/arduino-freertos-addon.git
```

I recommend to use git because you can easily update to the latest version just by executing the ```git pull``` command in the project folder.
