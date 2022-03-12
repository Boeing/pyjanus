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

import pyJanus


def test_gridded_table_example():
    """
    This checks pyJanus against the Examples/GriddedTableExample.cpp program
    """
    xml_path = "Examples/GriddedTableExample.xml"
    janus = pyJanus.Janus(xml_path)

    angle_of_attack = janus.get_variabledef("angleOfAttack")
    reynolds_number = janus.get_variabledef("reynoldsNumber")
    drag_coefficient = janus.get_variabledef("dragCoefficient")

    angle_of_attack.set_value(10)
    reynolds_number.set_value(0.36e6)
    assert round(drag_coefficient.get_value(), 2) ==  0.01

    angle_of_attack.set_value(30)
    assert round(drag_coefficient.get_value(), 2) == 0.58

    reynolds_number.set_value(0.70e6)
    assert round(drag_coefficient.get_value(), 3) == 0.595
