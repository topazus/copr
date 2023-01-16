%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}

Name:           bml-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        The Basic Matrix Library (bml)
License:        GPL
URL:            https://github.com/lanl/bml
Source:         https://github.com/lanl/bml/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ gcc-gfortran cmake pkg-config
BuildRequires:  openblas-devel


%description
The basic matrix library (bml) is a collection of various matrix data formats (for dense and sparse) and their associated algorithms for basic matrix operations.

%prep
%autosetup -n %{appname}-master -p1

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
%doc README.md

%{_includedir}/*.h
%{_includedir}/*.mod

%{_libdir}/cmake/BML/BML*.cmake
%{_libdir}/libbml.so
%{_libdir}/libbml.so.1.3.1
%{_libdir}/libbml_fortran.so
%{_libdir}/libbml_fortran.so.1.3.1
%{_libdir}/pkgconfig/bml.pc


%changelog
