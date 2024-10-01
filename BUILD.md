# Build

## Git Submodules

If cloning this project, specify the submodules using `git clone --recursive`

For already cloned repositories, use `git submodule update --init --recursive`

A patch has been created for the modifications for pugixml:

```console
# Make changes and then create the patch
cd ThirdParty/pugixml
git diff --cached > pugixml_dstg.patch
cp ./pugixml_dstg.patch ../pugixml_dstg.patch
```

To apply this patch:

```console
cd ThirdParty/pugixml
cp ../pugixml_dstg.patch ./pugixml_dstg.patch
git apply ./pugixml_dstg.patch
```

## Janus Library Only

From within the top-level directory:

For newer versions of CMake:

```console
mkdir build
cmake . -B build [options]
cmake --build build [options]
```

When building with MSVC, use the "--config" flag to set the build type:

```console
cmake --build build --config [Release|Debug]
```

## Janus Library and C++ Examples

From within the top-level directory:

```console
mkdir build
cmake . -B build -DBUILD_EXAMPLES=ON
cmake --build build [options]
```

To run the examples, you will need to copy the XML files in the Examples/ directory to the location of the built binaries.

## Janus Library and pyJanus

From within the top-level directory you can instal pyJanus with pip

```console
export MAKEFLAGS=-j8
pip install --verbose .[test]
```

If you wish to only compile the .pyd you can run:

```console
mkdir build
cmake . -B build -DBUILD_PYBINDINGS=ON -DPY_VERSION_INFO=dev -DBUILD_EXAMPLES=ON
cmake --build build -j8 --config Release
```
