
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname fpm
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A package manager and build system for Fortran
License:        MIT
URL:            https://github.com/fortran-lang/fpm
Source:         https://github.com/fortran-lang/fpm/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-fortran pkg-config wget git

Requires: gcc-fortran

%description
Fortran Package Manager (fpm) is a package manager and build system for Fortran.

%prep
%autosetup -n %{appname}-master -p1

%build
mkdir tmp
curl -LJ https://github.com/fortran-lang/fpm/releases/download/v0.2.0/fpm-0.2.0.f90 > tmp/fpm.f90
gfortran -J tmp tmp/fpm.f90 -o tmp/fpm
tmp/fpm build --flag "-g -fbacktrace -O3"

%install
install -pDm755 build/gfortran*/app/fpm %{buildroot}%{_bindir}/fpm

%if %{with check}
%check
tmp/fpm test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
