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
#include <pybind11/stl.h>

#include <Janus/Janus.h>
#include <Ute/aString.h>

using namespace janus;
using namespace dstoute;

namespace py = pybind11;

template <typename... Args>
using overload_cast_ = py::detail::overload_cast_impl<Args...>;

void init_Janus(py::module_ &m)
{
  py::class_<Janus>(m, "Janus")
      .def(py::init<>())
      .def(py::init<const std::string &>(), py::arg("filename"))

      .def("get_variabledef",
           overload_cast_<>()(&Janus::getVariableDef))
      .def("get_variabledef",
           overload_cast_<const aString &>()(&Janus::getVariableDef),
           py::return_value_policy::reference)

      .def_property_readonly("xml_filename", &Janus::getXmlFileName)

      .def("__repr__",
           [](Janus &self)
           {
             std::ostringstream out;
             out << "Janus(xml_filename='" << self.getXmlFileName() << ")"
                 << " at JanusInstance<"
                 << self.getVariableDef().front().getJanusInstance() << ">";
             return out.str();
           })
      .def("__str__",
           [](const Janus &self)
           {
             std::ostringstream out;
             out << "Janus(xml_filename='" << self.getXmlFileName() << ")";
             return out.str();
           });
}
