# Env marker example

This is a package that demonstrates the use of a new environment marker for python packaging.
Using `; free_treading == 'True'`, one can specify installation of dependencies only for the case of free threaded python.

This is implemented through changes in `packaging`, which are currently in the `env-marker-free-threading` branch
in [a fork of `gh:pypa/packaging`](https://github.com/zklaus/packaging).
Because pip uses a vendored copy of `packaging`, there is [a corresponding fork of `pip`](https://github.com/zklaus/pip),
which contains these changes in the vendored `packaging`.

For both packages distributions are available on TestPyPI as [`packaging_ft`](https://test.pypi.org/project/packaging_ft/) and [`pip-ft`](https://test.pypi.org/project/pip-ft/), respectively.

To facilitate testing, there are also conda packages available in the `zklaus` channel as `zklaus::packaging` and `zklaus::pip`.


## Testing
To test this out, conda environments can be created using the environment yaml files `env-w-freethreading.yaml` and `env-wo-freethreading.yaml`.
They will create environments that allow pip installing the present repo, where for the freethreading variant cython should be installed via pip,
whereas the non-freethreading variant will *not* install cython.
