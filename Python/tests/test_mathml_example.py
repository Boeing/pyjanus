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


def test_mathml_example():
    """
    This checks pyJanus against the Examples/MathMLExample.cpp program
    """
    xml_path = "Examples/MathMLExample.xml"
    janus = pyJanus.Janus(xml_path)

    x = janus.get_variabledef("x")
    y = janus.get_variabledef("y")
    result = janus.get_variabledef("result")
    sign = janus.get_variabledef("sign")
    cosd = janus.get_variabledef("cosd")
    sind = janus.get_variabledef("sind")
    tand = janus.get_variabledef("tand")
    cscd = janus.get_variabledef("cscd")
    secd = janus.get_variabledef("secd")
    cotd = janus.get_variabledef("cotd")
    arccosd = janus.get_variabledef("arccosd")
    arcsind = janus.get_variabledef("arcsind")
    arctand = janus.get_variabledef("arctand")
    bound = janus.get_variabledef("bound")

    x.set_value(0.1)
    y.set_value(0.2)

    assert round(result.get_value(), 6) == 0.463648
    assert round(sign.get_value(), 1) == 0.1
    assert round(cosd.get_value(), 6) == 0.999998
    assert round(sind.get_value(), 8) == 0.00174533
    assert round(tand.get_value(), 8) == 0.00174533
    assert round(cscd.get_value(), 3) == 572.958
    assert round(secd.get_value(), 1) == 1.0
    assert round(cotd.get_value(), 3) == 572.957
    assert round(arccosd.get_value(), 4) == 84.2608
    assert round(arcsind.get_value(), 5) == 5.73917
    assert round(arctand.get_value(), 5) == 5.71059
    assert round(bound.get_value(), 1) == 0.5
