# pyJanus

```console
git clone --recursive https://github.com/alwinw/Janus.git
cd Python
pip install --verbose .[test]
```

From the top level (maybe change to build_pyd)

```console
rm -rf build
mkdir build
cmake . -B build -DBUILD_PYBINDINGS=ON -DPY_VERSION_INFO=dev -DBUILD_EXAMPLES=ON
cmake --build build -j8 --config Release
```

```console
cd build/Python/Release
ipython
import pyJanus
pyJanus.__file__
j = pyJanus.Janus("../../../Examples/CombinedExample.xml")
j.get_variabledef()
j.get_variabledef("angleOfAttack")
# help(pyJanus.JanusVariableManager)

jvm.get_variabledef()
```

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
