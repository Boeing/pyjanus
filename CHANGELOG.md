## Unreleased

Move third-party dependencies into git submodules

### Fix

- **thirdparty**: resolve pugixml start-end tags mismatch
- **thirdparty**: update pybind11 to resolve use of undefined type '_frame'
- **thirdparty**: add QhullUser.cpp for qh_fprintf
- **thirdparty**: update cmake to use git submodule
- **thirdparty**: update cmake to use git submodule

### Refactor

- **thirdparty**: make qhull a thirdparty git submodule
- **thirdparty**: add dstg changes to pugixml as a git patch
- **thirdparty**: make pugixml a thirdparty git submodule
- **thirdparty**: make dirent a thirdparty git submodule

## v0.3.0 (2023-07-12)

Pull upstream updates from <https://github.com/fltdyn/Janus>

### Added

- **upstream** Add convert units

### Changed

- **upstream** Improve jansfunc

### Fixed

- **upstream** Resolve MinGW namespace clash

## v0.2.2 (2022-03-21)

Fix error with example xmls not being found during testing

## Added

- Automated cibuildwheel for Windows, Linux and macOS, py3.7-py3.10

### Fixed

- Path resolution to example xmls for pytest

## v0.2.1 (2022-03-21)

Fix cross-platform build of pyJanus

### Added

- Automated pip build and pytest for Windows MSVC, Ubuntu GCC and macOS Clang

### Changed

- Removed python 3.8 f-string features for backwards compatibility with python 3.7

### Fixed

- Add `POSITION_INDEPENDENT_CODE` flag for static libraries when compiling pybindings (<https://github.com/pybind/pybind11/issues/466>)
- Fixes linking error on Linux systems

## v0.2.0 (2022-03-19)

Cross-platform build of Janus and pyJanus

### Fixed

MinGW:

- Rename `signal.h` to `sgnl.h` to avoid namespace conflict with MinGW header (<https://github.com/mingw-w64/mingw-w64/blob/master/mingw-w64-headers/crt/signal.h>)
- Added cmake flag `-Wa,-mbig-obj` for compiling large files

macOS:

- Use `sleep()` on macOS, not `Sleep()`(<https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sleep.3.html>)
- Use `<functional>` not `<tr1/functional>` on macOS > OS X 10.9
- Specify `std::abs` to avoid error call to 'abs' is ambiguous (<https://cplusplus.github.io/LWG/issue2192>)
- Reorder templates to prevent unqualified lookup error (<https://clang.llvm.org/compatibility.html#dep_lookup>)
- Specified ascii code for degrees symbol to prevent illegal character encoding warning (<https://www.ascii-code.com/>)
- Add `cxx_std_11` for Examples cmake

### Added

- GitHub action to build on Windows MSVC, Windows MingGW, Ubuntu GCC, macOS Clang

## v0.1.1 (2022-03-15)

Initial release of pyJanus on pypi: <https://pypi.org/project/python-janus/>

### Fixed

- Large sdist .tar.gz bundles due to third party library documentation being included
- Add missing third party source files to MANIFEST.in

## v0.1.0 (2022-03-12)

Initial release of python bindings for Janus

### Added

- Bindings created using pybind11
- Examples/ directory used as test suite
- Wrapping of Janus and JanusVariableManager major methods and properties

### Changed

- Initial python API creation

### Fixed

- Return value policies leading to incorrect ownership ([pybind 11docs](https://pybind11.readthedocs.io/en/stable/advanced/functions.html#return-value-policies))
