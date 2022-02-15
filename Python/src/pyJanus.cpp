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
        .def(py::init<const std::string &>());
    py::implicitly_convertible<std::string, aString>();

    py::class_<VariableDef>(m, "VariableDef")
        // .def(py::init<const std::string &>()), py::arg()
        // .def("setValue", &setValue);
        .def("__repr__",
             [](const VariableDef &self)
             {
                 std::ostringstream out;
                 out << "VariableDef("
                     << "name='" << self.getName() << "', "
                     << "varID='" << self.getVarID() << "', "
                     << "units='" << self.getUnits() << "', "
                     << "initialValue='" << self.getInitialValue() << "'"
                     << ")";
                 return out.str();
             });

    // <variableDef name="angleOfAttack" varID="angleOfAttack" units="deg" initialValue="0.0">

    py::class_<Janus>(m, "Janus")
        .def(py::init<const std::string &>(), py::arg("filename"))
        .def("get_variabledef",
             static_cast<VariableDefList &(Janus::*)()>(&Janus::getVariableDef))
        .def("get_variabledef",
             static_cast<VariableDef &(Janus::*)(const aString &)>(&Janus::getVariableDef))
        .def_property("xml_filename", &Janus::getXmlFileName, nullptr)
        .def("aString", [](const std::string &s)
             { return s; })
        .def("__repr__",
             [](const Janus &self)
             {
                 return "<pyJanus.Janus('" + self.getXmlFileName() + "')>";
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
