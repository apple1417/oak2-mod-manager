cmake_minimum_required(VERSION 3.24)

project(oak2_mod_manager)

set(UNREALSDK_FLAVOUR OAK2)
set(EXPLICIT_PYTHON_ARCH amd64)
set(EXPLICIT_PYTHON_VERSION 3.14.6)
set(EXPLICIT_PYTHON_HASH_BASE SHA256=75afa83f93b284d19040e24bc440ab741c09582c0d5310504d607a4e08c3dbaf)
set(EXPLICIT_PYTHON_HASH_TEST SHA256=2e903c82f7fc7081aa59e21752309dd6a1180297950d6b0587c39da606549867)
set(EXPLICIT_PYTHON_HASH_EMBEDDABLE SHA256=c3a89aa7ead530bcac4729f3db7d000fbadb6ca7aa0461c2841867172aa0752a)

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
