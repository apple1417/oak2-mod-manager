cmake_minimum_required(VERSION 3.24)

project(oak2_mod_manager)

set(UNREALSDK_FLAVOUR OAK2)
set(EXPLICIT_PYTHON_ARCH amd64)
set(EXPLICIT_PYTHON_VERSION 3.14.3)
set(EXPLICIT_PYTHON_HASH_BASE SHA256=ec781bb03f9638d136b24da7c83b4db1652ce767848aa856a30bb87cfdb1abe4)
set(EXPLICIT_PYTHON_HASH_TEST SHA256=8a2aad571579eff81cfdc7452efd5b867653cb2b6b2c83cbd7184501a29eb832)
set(EXPLICIT_PYTHON_HASH_EMBEDDABLE SHA256=e69d3609130b1c06948620651d0f0ab2183ff978c2b174ddf3d3cae7ff226b89)

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
