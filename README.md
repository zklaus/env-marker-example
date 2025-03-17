# Env marker example

This is a package that demonstrates the use of new environment markers for Python packaging,
following the proposal laid out in [tentative PEP 790](https://github.com/zklaus/peps/blob/new-environment-markers/peps/pep-0790.rst).

Using `; 'free_threading' in sys_abi_features`, one can specify installation of dependencies only for the case of free threaded python.
The tentative PEP stipulates a few more possibile markers; for details refer there.

This is implemented through changes in `packaging`, which are currently in the `env-marker-free-threading` branch
in [a fork of `gh:pypa/packaging`](https://github.com/zklaus/packaging).
Because pip uses a vendored copy of `packaging`, there is [a corresponding fork of `pip`](https://github.com/zklaus/pip),
which contains these changes in the vendored `packaging`.

## Testing
The effective working of these new markers is tested in the CI of this repo.
