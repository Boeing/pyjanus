cmake_minimum_required(VERSION 3.4)
project(pyJanus)

add_subdirectory(pybind11)
pybind11_add_module(pyJanus src/pyJanus.cpp)

target_compile_definitions(
  pyJanus
  PRIVATE VERSION_INFO=${PY_VERSION_INFO}
)