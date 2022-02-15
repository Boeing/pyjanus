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

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <Janus/Janus.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

struct Document
{
    Document(const std::string &name, int pages) : name(name), pages(pages) {}

    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }

    void set(int pages_) { pages = pages_; }
    void set(const std::string &name_) { name = name_; }

    int add(int i, int j = 2)
    {
        return i + j;
    }

    std::string name;
    int pages;
};

struct Book : Document
{
    Book(const std::string &name, int pages) : Document(name, pages) {}
    std::string flick() const { return "next page!"; }
};

using namespace janus;
namespace py = pybind11;

PYBIND11_MODULE(pyJanus, m)
{
    py::class_<Document>(m, "Document")
        .def(py::init<const std::string &, int>(), py::arg("name"), py::arg("pages"))
        .def_property("name", &Document::getName, &Document::setName)
        .def("set", static_cast<void (Document::*)(int)>(&Document::set), "Set the Document's pages")
        .def("set", static_cast<void (Document::*)(const std::string &)>(&Document::set), "Set the Document's name")
        .def("add", &Document::add, "A function which adds two numbers",
             py::arg("i"), py::arg("j") = 2)
        .def("__repr__",
             [](const Document &a)
             {
                 return "<pyJanus.Document named '" + a.name + "'>";
             });

    py::class_<Book, Document>(m, "Book")
        .def(py::init<const std::string &, int>(), py::arg("name"), py::arg("pages"))
        .def("flick", &Book::flick)
        .def("__repr__",
             [](const Document &a)
             {
                 return "<pyJanus.Book named '" + a.name + "'>";
             });

    m.def("library", []()
          { return std::unique_ptr<Document>(new Book("xml", 10)); });

    py::class_<VariableDef>(m, "VariableDef")
    // .def(py::init<const std::string &>()), py::arg()
    // .def("setValue", &setValue);
    .def("__repr__",
             [](const VariableDef &a)
             {
                 return "<pyJanus.VariableDef('')>";
             });

    py::class_<Janus>(m, "Janus")
        .def(py::init<const std::string &>(), py::arg("filename"))
        .def("get_variabledef",
             static_cast<VariableDefList& (Janus::*)()>(&Janus::getVariableDef))
        .def("get_variabledef",
             static_cast<VariableDef& (Janus::*)(dstoute::aOptionalSizeT)>(&Janus::getVariableDef))
        .def_property("xml_filename", &Janus::getXmlFileName, nullptr)
        .def("__repr__",
             [](const Janus &a)
             {
                 return "<pyJanus.Janus('" + a.getXmlFileName() + "')>";
             });

// cmake --build build -j8 --config Release
// cd build/Python/Release
//
// import pyJanus
// j = pyJanus.Janus("../../../Examples/CombinedExample.xml")
// j.get_variabledef()

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
