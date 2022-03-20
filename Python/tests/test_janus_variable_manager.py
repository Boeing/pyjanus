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


def test_janus_variable_manager_example_00():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 00
    """
    xml_path = (
        f"{os.path.dirname(__file__)}/../../Examples/JanusVariableManagerExample.xml"
    )
    jvm = pyJanus.JanusVariableManager(xml_path)

    input00 = pyJanus.JanusVariable(
        "input00", pyJanus.janusInputVariable, pyJanus.janusMandatory, "m s-1", 0.0
    )
    output00 = pyJanus.JanusVariable(
        "output00", pyJanus.janusOutputVariable, pyJanus.janusMandatory, "kn", 0.0
    )
    jInput00 = jvm.push_back(input00)
    jOutput00 = jvm.push_back(output00)
    jv_input00 = jvm[jInput00]
    jv_output00 = jvm[jOutput00]

    assert jv_input00.is_available()
    assert jv_output00.is_available()

    assert round(jv_output00.get_value(), 0) == 0
    assert jv_input00.set_value(1.0)
    assert round(jv_output00.get_value(), 5) == 1.94384

    assert jvm[jInput00].set_value(0.0)
    assert round(jvm[jOutput00].get_value(), 0) == 0
    assert jvm[jInput00].set_value(1.0)
    assert round(jvm[jOutput00].get_value(), 5) == 1.94384


def test_janus_variable_manager_example_01():
    """
    This checks pyJanus against the Examples/SetVarDefExample.cpp program 01
    """
    xml_path = (
        f"{os.path.dirname(__file__)}/../../Examples/JanusVariableManagerExample.xml"
    )
    jvm = pyJanus.JanusVariableManager(xml_path)

    input00 = pyJanus.JanusVariable(
        "input00", pyJanus.janusInputVariable, pyJanus.janusMandatory, "m s-1", 0.0
    )
    output00 = pyJanus.JanusVariable(
        "output00", pyJanus.janusOutputVariable, pyJanus.janusMandatory, "kn", 0.0
    )
    jInput00 = jvm.push_back(input00)
    jOutput00 = jvm.push_back(output00)
    jv_input00 = jvm[jInput00]
    jv_output00 = jvm[jOutput00]

    assert round(jv_output00.get_value(), 0) == 0
    assert jv_input00.set_value(1.0)
    assert round(jv_output00.get_value(), 5) == 1.94384
    assert not jv_input00.set_value(1.0)
    assert jv_input00.set_value(2.0)
    assert round(jv_output00.get_value(), 5) == 3.88769
