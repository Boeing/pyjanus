#
# pyJanus (Python Bindings for Janus)
#
# Copyright (c) 2022 Alwin Wang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import pyJanus


def test_set_var_def_example_00():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 00
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    input00 = janus.get_variabledef("input00")
    output00 = janus.get_variabledef("output00")

    input00.set_value(15)
    assert round(output00.get_value(), 0) == 19


def test_set_var_def_example_01():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 01
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    incrementer = janus.get_variabledef("incrementer")
    output01 = janus.get_variabledef("output01")

    incrementer.get_value()
    assert round(output01.get_value(), 0) == 6

    incrementer.get_value()
    assert round(output01.get_value(), 0) == 9

    incrementer.get_value()
    assert round(output01.get_value(), 0) == 12


def test_set_var_def_example_02():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 02
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    input02 = janus.get_variabledef("input02")
    output02 = janus.get_variabledef("output02")
    function02 = janus.get_variabledef("function02")

    input02.set_value(42)
    function02.get_value()
    assert round(output02.get_value(), 0) == 42


def test_set_var_def_example_03():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 03
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    input03 = janus.get_variabledef("input03")
    output03_00 = janus.get_variabledef("output03_00")
    function03 = janus.get_variabledef("function03")

    input03.set_value(123.456)
    function03.get_value()
    assert round(output03_00.get_value(), 3) == 123.456


def test_set_var_def_example_04():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 04
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    function04_00 = janus.get_variabledef("function04_00")
    function04_01 = janus.get_variabledef("function04_01")

    assert round(function04_00.get_value(), 2) == 56.78
    assert round(function04_01.get_value(), 2) == 56.78


def test_set_var_def_example_05():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 05
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    output05_00 = janus.get_variabledef("output05_00")
    output05_01 = janus.get_variabledef("output05_01")

    assert round(output05_00.get_value(), 1) == 0.0
    assert round(output05_01.get_value(), 1) == 40.0


def test_set_var_def_example_06():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 06
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/SetVarDefExample.xml"
    janus = pyJanus.Janus(xml_path)

    output06_00 = janus.get_variabledef("output06_00")
    output06_01 = janus.get_variabledef("output06_01")
    output06_02 = janus.get_variabledef("output06_02")
    output06_03 = janus.get_variabledef("output06_03")
    internal06_00 = janus.get_variabledef("internal06_00")
    internal06_01 = janus.get_variabledef("internal06_01")
    internal06_02 = janus.get_variabledef("internal06_02")
    internal06_21 = janus.get_variabledef("internal06_21")

    assert round(output06_00.get_value(), 1) == 2704.0
    assert round(internal06_00.get_value(), 1) == 0.0
    assert round(output06_01.get_value(), 1) == 52.0
    assert round(internal06_01.get_value(), 1) == 0.0
    assert round(output06_02.get_value(), 1) == 52.0
    assert round(internal06_02.get_value(), 1) == 0.0
    assert round(output06_03.get_value(), 1) == 231.0
    assert round(internal06_21.get_value(), 1) == 0.0
