# Env marker example

This is a package that demonstrates the use of the `sys_abi_info` environment marker for Python packaging,
as specified in [PEP 780 – ABI features as environment markers](https://peps.python.org/pep-0780/).

`sys_abi_info` is a set of strings of the form `name::value`, which can be tested with `in` and `not in`.
Four features are always present:

| Feature         | Values             | Example               |
|-----------------|--------------------|-----------------------|
| `free_threaded` | `True`, `False`    | `free_threaded::True`  |
| `debug`         | `True`, `False`    | `debug::False`        |
| `pointer_bits`  | e.g. `32`, `64`    | `pointer_bits::64`    |
| `byteorder`     | `little`, `big`    | `byteorder::little`   |

Using `; "free_threaded::True" in sys_abi_info`, one can specify installation of dependencies only for the case of free-threaded Python.
A string that is not in the set simply makes `in` false and `not in` true; it is never an error.
This package uses the marker in [its `pyproject.toml`](pyproject.toml) like this:

```toml
dependencies = [
    'cython; python_version >= "3.7" and "free_threaded::True" in sys_abi_info',
    'numpy; platform_system == "Windows" and "pointer_bits::32" in sys_abi_info',
    'scipy; "pointer_bits::64" in sys_abi_info',
]
```

For the full specification, including how the features are determined on Python versions before 3.15, refer to the PEP.

This is implemented through changes in `packaging`, which are currently in the `env-marker-free-threading` branch
in [a fork of `gh:pypa/packaging`](https://github.com/zklaus/packaging).
Because pip uses a vendored copy of `packaging`, there is [a corresponding fork of `pip`](https://github.com/zklaus/pip),
which contains these changes in the vendored `packaging`.

## Testing
The effective working of the marker is tested in the CI of this repo:
for every combination of operating system, pointer size, and free-threaded or GIL-enabled build in the test matrix,
the package is installed with the patched `pip` and `packaging`,
and `check_env.py` verifies against the matching `expected-*.txt` file which of the dependencies were installed.

