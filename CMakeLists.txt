cmake_minimum_required(VERSION 3.24)

project(oak2_mod_manager)

set(UNREALSDK_FLAVOUR OAK2)
set(EXPLICIT_PYTHON_ARCH amd64)
set(EXPLICIT_PYTHON_VERSION 3.13.1)

add_subdirectory(libs/pyunrealsdk)

add_subdirectory(libs/pluginloader EXCLUDE_FROM_ALL)
set_target_properties(pluginloader_dsound PROPERTIES
    EXCLUDE_FROM_ALL false
)

pyunrealsdk_add_module(keybinds src/keybinds/keybinds.cpp)

install(
    TARGETS
        pluginloader_dsound
    RUNTIME DESTINATION
        .exe_folder
)

install(
    TARGETS
        keybinds
    DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/src/keybinds/
)
