//
// pyJanus (Python Bindings for Janus)
//
// Copyright (c) 2022 Alwin Wang
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//

#include <pybind11/pybind11.h>
#include <Janus/Janus.h>

using namespace janus;

namespace py = pybind11;

template <typename... Args>
using overload_cast_ = py::detail::overload_cast_impl<Args...>;

void init_VariableDef(py::module_ &m)
{
  py::class_<VariableDef>(m, "VariableDef")
      .def(py::init<Janus *, DomFunctions::XmlNode &>(),
           py::arg("janus"), py::arg("element_definition"))

      .def_property_readonly("janus", &VariableDef::getJanusInstance)
      .def_property_readonly("initial_value", &VariableDef::getInitialValue)
      .def_property_readonly("name", &VariableDef::getName)
      .def_property_readonly("units", &VariableDef::getUnits)
      .def_property_readonly("var_id", &VariableDef::getVarID)

      .def("get_value", &VariableDef::getValue)
      .def("set_value",
           overload_cast_<const double &, bool>()(&VariableDef::setValue),
           py::arg("value"), py::arg("is_forced") = false)

      .def("__repr__",
           [](VariableDef &self)
           {
             std::ostringstream out;
             out << "VariableDef("
                 << "name='" << self.getName() << "', "
                 << "var_id='" << self.getVarID() << "', "
                 << "units='" << self.getUnits() << "', "
                 << "initial_value='" << self.getInitialValue() << "', "
                 << "value='" << self.getValue() << "') "
                 << "from JanusInstance<" << self.getJanusInstance() << ">";
             return out.str();
           })
      .def("__str__",
           [](const VariableDef &self)
           {
             std::ostringstream out;
             out << self.getName() << ": " << self.getValue() << " " << self.getUnits();
             return out.str();
           });
}