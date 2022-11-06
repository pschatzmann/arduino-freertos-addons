# setup of Arduino Library from https://github.com/espeak-ng/espeak-ng.git 
import os, command, shutil
from subprocess import run


# get latest original source code
def execute_git(fromUrl, name):
    if not os.path.exists(name):
        res = command.run(["git", "clone", fromUrl, name]) 
    else:
        currentDir = os.getcwd()
        os.chdir(name)
        res = command.run(["git","pull"]) 
        os.chdir(currentDir)
    print(res.output) 
    return res

def make_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

# make sure that we have an empty src directory
def clean_src():
    if not os.path.exists("src"):
        make_dir("src")
    if not os.path.exists("src/freertos-addon"):
        make_dir("src/freertos-addon")
    if not os.path.exists("src/freertos-addon/c++"):
        make_dir("src/freertos-addon/c++")
    if not os.path.exists("src/freertos-addon/c"):
        make_dir("src/freertos-addon/c")

# copy all relevant files
def copy_files():
    shutil.copytree('original/c++/Source', 'src/freertos-addon/c++', dirs_exist_ok=True) 
    shutil.copytree('original/c++/Source/include', 'src', dirs_exist_ok=True) 
    shutil.copytree('original/c/Source', 'src/freertos-addon/c', dirs_exist_ok=True) 
    shutil.copytree('original/c/Source/include', 'src', dirs_exist_ok=True) 


# deletes a file if it exists
def remove(file):
    if os.path.exists(file):
        os.remove(file)

# create a new file
def createFile(fileName, text):
    remove(fileName)
    text_file = open(fileName, "w")
    text_file.write(text)
    text_file.close()

# replace texts in a file
def file_replace_text(fileName, fromStr, toStr):
    text_file = open(fileName, "r")
    # read whole file to a string
    data = text_file.read()
    text_file.close()
    # write updated file
    text_file = open(fileName, "w")
    new_txt = data.replace(fromStr,toStr, 1)
    text_file.write(new_txt)
    text_file.close()

def fileContains(fileName, str):
    text_file = open(fileName, "r")
    # read whole file to a string
    data = text_file.read()
    result = str in data
    text_file.close()
    return result


def add_config_to_all_files():
    allcpp = "#pragma once\n\n"
    allc = "#pragma once\n\n"
    for root, dirs, files in os.walk("src"):
        path = root.split(os.sep)
        for file in files:
            old_path = root+"/"+file
            if not file.startswith(".") and file.endswith(".hpp"):
                print(old_path)
                if (not fileContains(old_path,"freertos-config.h")):
                    file_replace_text(old_path, "#","#include \"freertos-config.h\"\n\n#")
            inc = old_path.replace("src/","")
            if file.endswith(".hpp"):
                allcpp+="#include \""+inc+"\"\n"
            if file.endswith(".h"):
                allc+="#include \""+inc+"\"\n"

    text_file = open("src/freertos-all.h", "w")
    text_file.write(allcpp)
    text_file.close()
    text_file = open("src/freertos-all-c.h", "w")
    text_file.write(allc)
    text_file.close()

def config():
    str = """
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

"""
    return str

##-----------------------
## Main logic starts here
res = execute_git("https://github.com/michaelbecker/freertos-addons.git", "original")
if res.exit==0:
    clean_src()
    copy_files()
    shutil.rmtree("src/freertos-addon/c++/include", ignore_errors=True)
    shutil.rmtree("src/freertos-addon/c/include", ignore_errors=True)
    createFile("src/freertos-config.h",config())
    createFile("src/semphr.h","#include \"freertos/semphr.h\"")
    createFile("src/timers.h","#include \"freertos/timers.h\"")
    createFile("src/task.h","#include \"freertos/task.h\"")
    createFile("src/queue.h","#include \"freertos/queue.h\"")
    createFile("src/event_groups.h","#include \"freertos/event_groups.h\"")
    createFile("src/task.h","#pragma once\n\n#include \"freertos/task.h\"\n\nextern portMUX_TYPE esp32Mutex;")
    remove("src/freertos-addon/c++/include/tickhook.hpp")
    remove("src/freertos-addon/c++/ctickhook.cpp")
    file_replace_text("src/critical.hpp","taskENTER_CRITICAL","_taskENTER_CRITICAL")
    file_replace_text("src/critical.hpp","taskEXIT_CRITICAL","_taskEXIT_CRITICAL")

    add_config_to_all_files()

    command.run(["doxygen"]) 
    print("setup completed")
else:
    print("Could not execute git command")