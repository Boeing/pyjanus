# pyJanus

## Installation from Source

```sh
git clone --recursive https://github.com/Boeing/pyjanus
cd Python
pip install --verbose .[test]
```

If you have already cloned the repository, didn't use `--recursive` you will have to do the following:

```sh
git submodule update --recursive
```

You can also build the the standalone `pyd` file without using `pip`.

```sh
rm -rf build
mkdir build
cmake . -B build -DBUILD_PYBINDINGS=ON -DPY_VERSION_INFO=dev -DBUILD_EXAMPLES=ON
cmake --build build -j8 --config Release
```

## `pyd` Example Usage

You can use the built `pyd` file, for example `build/Python/Release/pyJanus.cp311-win_amd64.pyd`.

```console
cd build/Python/Release # Or equivalent
ipython
>>> import pyJanus
>>> pyJanus.__file__
..\\pyjanus\\build\\Python\\Release\\pyJanus.cp311-win_amd64.pyd
>>> j = pyJanus.Janus("../../../Examples/CombinedExample.xml")
>>> j.get_variabledef()
[VariableDef(name='angleOfAttack', var_id='angleOfAttack', units='deg', initial_value='0', value='0') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='reynoldsNumber', var_id='reynoldsNumber', units='ND', initial_value='360000', value='360000') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='ambientDensity', var_id='ambientDensity', units='kg m-3', initial_value='1.225', value='1.225') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='trueAirspeed', var_id='trueAirspeed', units='m s-1', initial_value='100', value='100') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='referenceArea', var_id='referenceArea', units='m2', initial_value='25', value='25') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='dragCoefficient', var_id='dragCoefficient', units='ND', initial_value='nan', value='0.005') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='dynamicPressure', var_id='dynamicPressure', units='Pa', initial_value='nan', value='6125') from JanusInstance<000001CD8D5062C0>,
 VariableDef(name='drag', var_id='drag', units='N', initial_value='nan', value='765.625') from JanusInstance<000001CD8D5062C0>]
>>> j.get_variabledef("angleOfAttack")
VariableDef(name='angleOfAttack', var_id='angleOfAttack', units='deg', initial_value='0', value='0') from JanusInstance<000001CD8D5062C0>
>>> help(pyJanus.JanusVariableManager)
Help on class JanusVariableManager in module pyJanus:

class JanusVariableManager(Janus)
 |  Method resolution order:
 |      JanusVariableManager
 |      Janus
 |      pybind11_builtins.pybind11_object
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __getitem__(...)
 |      __getitem__(self: pyJanus.JanusVariableManager, arg0: pyJanus.JanusIndex) -> pyJanus.JanusVariable
 |
 |  __init__(...)
 |      __init__(self: pyJanus.JanusVariableManager, arg0: str) -> None
 |
 |  push_back(...)
 |      push_back(*args, **kwargs)
 |      Overloaded function.
# snip
```

Another example usage:

```py
import pyJanus
jvm = pyJanus.JanusVariableManager("../../../Examples/JanusVariableManagerExample.xml")
input00 = pyJanus.JanusVariable("input00", pyJanus.janusInputVariable, pyJanus.janusMandatory, "m s-1", 0.0)
output00 = pyJanus.JanusVariable("output00", pyJanus.janusOutputVariable, pyJanus.janusMandatory, "kn", 0.0)
jInput00 = jvm.push_back(input00)
jOutput00 = jvm.push_back(output00)
jv_input00 = jvm[jInput00]
jv_output00 = jvm[jOutput00]
```

## Testing

Tests can be run by calling `python -m pytest` from the root directory.

## Release

```sh
rm -rf dist/
rm -rf python_janus.egg-info
python setup.py sdist bdist_wheel
```

```sh
python -m twine check dist/*
python -m twine upload dist/*
```
