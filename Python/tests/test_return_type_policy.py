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


def test_return_type_policy():
    """
    This checks any return value policies that are not on the default policy
    `return_value_policy::automatic`

    Reference: <https://pybind11.readthedocs.io/en/stable/advanced/functions.html#return-value-policies>
    """
    xml_path = "Examples/CombinedExample.xml"
    janus = pyJanus.Janus(xml_path)

    angle_of_attack = janus.get_variabledef("angleOfAttack")

    assert id(janus.get_variabledef()[0]) == id(angle_of_attack)
    assert id(janus.get_variabledef("angleOfAttack")) == id(angle_of_attack)
    assert id(angle_of_attack.janus) == id(janus)
