//
// pyJanus (Python Bindings for Janus)
//
// Copyright (c) 2022 Alwin Wang
//
// Permission is hereby granted, free of charge, to any Document obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit Documents to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMpagesS OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//

#include <pybind11/iostream.h>
#include <pybind11/pybind11.h>
#include <pybind11/pytypes.h>
#include <pybind11/stl.h>

#include <Janus/Janus.h>
#include <Ute/aString.h>

#include "pyrepr.hpp"

using namespace janus;
using namespace dstoute;

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

template <typename... Args>
using overload_cast_ = py::detail::overload_cast_impl<Args...>;

PYBIND11_MODULE(pyJanus, m)
{
    py::class_<aString>(m, "aString")
        .def(py::init<const std::string &>())
        .def("__repr__",
             [](const aString &self)
             {
                 std::ostringstream out;
                 out << "aString('" << self << "')";
                 return out.str();
             })
        .def("__str__",
             [](const aString &self)
             {
                 std::ostringstream out;
                 out << self;
                 return out.str();
             });
    py::class_<aFileString, aString>(m, "aFileString")
        .def(py::init<const std::string &>())
        .def("__repr__",
             [](const aFileString &self)
             {
                 std::ostringstream out;
                 out << "aString('" << self << "')";
                 return out.str();
             })
        .def("__str__",
             [](const aFileString &self)
             {
                 std::ostringstream out;
                 out << self;
                 return out.str();
             });
    py::implicitly_convertible<std::string, aString>();
    py::implicitly_convertible<std::string, aFileString>();

    py::class_<VariableDef>(m, "VariableDef")
        .def(py::init<Janus *, DomFunctions::XmlNode &>(),
             py::arg("janus"), py::arg("element_definition"))

        .def_property_readonly("janus", &VariableDef::getJanusInstance)
        .def_property_readonly("name", &VariableDef::getName)
        .def_property_readonly("var_id", &VariableDef::getName)
        .def_property_readonly("units", &VariableDef::getUnits)
        .def_property_readonly("initial_value", &VariableDef::getInitialValue)

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

    py::class_<Janus>(m, "Janus")
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

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}

// cmake . -B build -DBUILD_PYBINDINGS=ON -DPY_VERSION_INFO=0.0.1
// cmake --build build -j8 --config Release
//
// cd build/Python/Release
//
// ipython
// import pyJanus
// j = pyJanus.Janus("../../../Examples/CombinedExample.xml")
// j.get_variabledef()
// j.get_variabledef("angleOfAttack")
