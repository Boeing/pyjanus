#
# DST Janus Library (Janus DAVE-ML Interpreter Library)
#
# Defence Science and Technology (DST) Group
# Department of Defence, Australia.
# 506 Lorimer St
# Fishermans Bend, VIC
# AUSTRALIA, 3207
#
# Copyright 2005-2019 Commonwealth of Australia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

function(builder NAME)
  add_executable(${NAME} ${NAME}.cpp)
  target_link_libraries(${NAME} PUBLIC Janus)
  target_compile_features(${NAME} PRIVATE cxx_std_11)
endfunction()

set(FILES 
	${CMAKE_CURRENT_SOURCE_DIR}/CombinedExample.cpp
	${CMAKE_CURRENT_SOURCE_DIR}/GriddedTableExample.cpp
	${CMAKE_CURRENT_SOURCE_DIR}/JanusVariableManagerExample.cpp
	${CMAKE_CURRENT_SOURCE_DIR}/MathMLExample.cpp
	${CMAKE_CURRENT_SOURCE_DIR}/SetVarDefExample.cpp
)

foreach(FILE ${FILES})
  get_filename_component(FILE_NO_EXT "${FILE}" NAME_WE)
  builder("${FILE_NO_EXT}")
endforeach()
