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


def test_combined_example():
    """
    This checks pyJanus against the Examples/CombinedExample.cpp program
    """
    xml_path = f"{os.path.dirname(__file__)}/../../Examples/CombinedExample.xml"
    janus = pyJanus.Janus(xml_path)

    angle_of_attack = janus.get_variabledef("angleOfAttack")
    reynolds_number = janus.get_variabledef("reynoldsNumber")
    ambient_density = janus.get_variabledef("ambientDensity")
    true_airspeed = janus.get_variabledef("trueAirspeed")
    reference_area = janus.get_variabledef("referenceArea")
    drag = janus.get_variabledef("drag")

    angle_of_attack.set_value(10)
    reynolds_number.set_value(0.36e6)
    ambient_density.set_value(1.225)
    true_airspeed.set_value(100.0)
    reference_area.set_value(25.0)

    assert round(drag.get_value(), 2) == 1531.25
