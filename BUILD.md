# Build

## Git Submodules

If cloning this project, specify the submodules using `git clone --recursive`

For already cloned repositories, use `git submodule update --init --recursive`

A patch has been created for the modifications for pugixml:

```sh
# Make changes and then create the patch
cd ThirdParty/pugixml
git diff --cached > pugixml_dstg.patch
cp ./pugixml_dstg.patch ../pugixml_dstg.patch
cd ../..
```

To apply this patch:

```sh
cd ThirdParty/pugixml
cp ../pugixml_dstg.patch ./pugixml_dstg.patch
git apply ./pugixml_dstg.patch
rm ./pugixml_dstg.patch
cd ../..
```

## Janus Library Only

From within the top-level directory:

For newer versions of CMake:

```sh
mkdir build
cmake . -B build [options]
cmake --build build [options]
```

When building with MSVC, use the "--config" flag to set the build type:

```sh
cmake --build build --config [Release|Debug]
```

## Janus Library and C++ Examples

From within the top-level directory:

```sh
mkdir build
cmake . -B build -DBUILD_EXAMPLES=ON
cmake --build build [options]
```

To run the examples, you will need to be in the Examples/ directory. For example:

```sh
cmake --build build -j8 --config Release
cd Examples
../build/Examples/Release/CombinedExample.exe
#> Output value: 1531.25 (expected: 1531.25)
../build/Examples/Release/GriddedTableExample.exe
#> Output value: 0.01 (expected: 0.01)
#> Output value: 0.58 (expected: 0.58)
#> Output value: 0.595 (expected: 0.595)
../build/Examples/Release/JanusVariableManagerExample.exe
#> Output value: 1.94384 (expected: 1.94384)
#> Output value: 1.94384 (expected: 1.94384)
#> Output value: 3.88769 (expected: 3.88769)
../build/Examples/Release/MathMLExample.exe
#> Output value: 0.463648 (expected: 0.463648)
#> sign( 0.1, 0.2): 0.1 (expected: 0.1)
#> cosd( 0.1): 0.999998 (expected: 0.999998)
#> sind( 0.1): 0.00174533 (expected: 0.00174533)
#> tand( 0.1): 0.00174533 (expected: 0.00174533)
#> cscd( 0.1): 572.958 (expected: 572.958)
#> secd( 0.1): 1 (expected: 1.0)
#> cotd( 0.1): 572.957 (expected: 572.957)
#> arccosd( 0.1): 84.2608 (expected: 84.2608)
#> arcsind( 0.1): 5.73917 (expected: 5.73917)
#> arctand( 0.1): 5.71059 (expected: 5.71059)
#> bound( 0.1, 0.5, 1.0): 0.5 (expected: 0.5)
../build/Examples/Release/SetVarDefExample.exe
# FIXME
cd ..
```

## Janus Library and pyJanus

From within the top-level directory you can instal pyJanus with pip

Linux

```sh
export MAKEFLAGS=-j8
pip install --verbose .[test]
```

Windows Powershell and MSVC: make sure to use the x64 command prompt for 64-bit python

```powershell
$env:MAKEFLAGS='-j8'
pip install --verbose .[test]
```

If you wish to only compile the .pyd you can run:

```sh
mkdir build
cmake . -B build -DBUILD_PYBINDINGS=ON -DSKBUILD_PROJECT_VERSION=dev -DBUILD_EXAMPLES=ON
cmake --build build -j8 --config Release
```
