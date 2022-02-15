# Build

## Library Only

From within the top-level directory:

```console
mkdir build
cmake . -B build
cmake --build build -j8  --config Release
```

## Library and Examples

From within the top-level directory:

```console
mkdir build
cmake . -B build -DBUILD_EXAMPLES=ON
cmake --build build -j8
```

## Example Only

From within the top-level directory:

```console
mkdir build
cmake . -B build -DCMAKE_PREFIX_PATH=C:/Users/Alwin/Documents/Git/Janus/Debug/
cmake --build build -j8
```

## Library and Python Bindings

```console
mkdir -p build
cmake . -B build -DBUILD_PYBINDINGS=ON -DPY_VERSION_INFO=0.0.1
cmake --build build -j8 --config Release
```
