%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname flint
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        FLINT (Fast Library for Number Theory)
License:        LGPL
URL:            https://github.com/wbhart/flint2
Source:         https://github.com/wbhart/flint2/archive/trunk/flint2-trunk.tar.gz

BuildRequires: gcc-c++ cmake pkg-config python3-devel mpfr-devel ntl-devel lapack-devel

Requires: mpfr ntl lapack


%description
FLINT (Fast Library for Number Theory) is a C library in support of computations
in number theory. It's also a research project into algorithms in number theory.

FLINT 2 is a complete rewrite of the FLINT library from scratch. It includes
much cleaner code and in many cases much faster algorithms and implementations.

%prep
%autosetup -n flint2-trunk -p1

%build
%cmake
%cmake_build

%install
%cmake_install


%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE*
%{_includedir}/flint/*.h
%{_libdir}/libflint.so
%{_libdir}/libflint.so.16.1.0
%{_libdir}/libflint.so.16

%changelog
