# Build

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
