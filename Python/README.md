# pyJanus

```console
git clone --recursive https://github.com/alwinw/Janus.git
cd Python
pip install --verbose .[test]
```

From the top level

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
jvm = pyJanus.JanusVariableManager("../../../Examples/CombinedExample.xml")
jvm.get_variabledef()
```
