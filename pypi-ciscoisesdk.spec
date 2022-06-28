#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ciscoisesdk
Version  : 2.0.3
Release  : 15
URL      : https://files.pythonhosted.org/packages/3e/31/0212f95203b05aaddc68c9a1af1018f3b1abd63c7cdf98075e598252ccc6/ciscoisesdk-2.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/31/0212f95203b05aaddc68c9a1af1018f3b1abd63c7cdf98075e598252ccc6/ciscoisesdk-2.0.3.tar.gz
Summary  : Cisco Identity Services Engine Platform SDK
Group    : Development/Tools
License  : MIT
Requires: pypi-ciscoisesdk-license = %{version}-%{release}
Requires: pypi-ciscoisesdk-python = %{version}-%{release}
Requires: pypi-ciscoisesdk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
=============
ciscoisesdk
=============
**ciscoisesdk** is a *community developed* Python library for working with the Identity Services Engine APIs.
Our goal is to make working with Cisco Identity Services Engine in Python a *native* and *natural* experience!

%package license
Summary: license components for the pypi-ciscoisesdk package.
Group: Default

%description license
license components for the pypi-ciscoisesdk package.


%package python
Summary: python components for the pypi-ciscoisesdk package.
Group: Default
Requires: pypi-ciscoisesdk-python3 = %{version}-%{release}

%description python
python components for the pypi-ciscoisesdk package.


%package python3
Summary: python3 components for the pypi-ciscoisesdk package.
Group: Default
Requires: python3-core
Provides: pypi(ciscoisesdk)
Requires: pypi(fastjsonschema)
Requires: pypi(future)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(xmltodict)

%description python3
python3 components for the pypi-ciscoisesdk package.


%prep
%setup -q -n ciscoisesdk-2.0.3
cd %{_builddir}/ciscoisesdk-2.0.3
pushd ..
cp -a ciscoisesdk-2.0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656375009
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . xmltodict
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . xmltodict
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ciscoisesdk
cp %{_builddir}/ciscoisesdk-2.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ciscoisesdk/9901a51ee03eb167026e7a7a6f20ea2473b39328
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} xmltodict
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ciscoisesdk/9901a51ee03eb167026e7a7a6f20ea2473b39328

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
