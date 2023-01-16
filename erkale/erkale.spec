
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname erkale
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        ERKALE -- HF/DFT from Hel
License:        GPL
URL:            https://github.com/susilehtola/erkale
Source:         https://github.com/susilehtola/erkale/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: hdf5-devel libint-devel libxc-devel armadillo-devel gsl-devel openblas-devel


%description
ERKALE is a quantum chemistry program used to solve the electronic structure of atoms, molecules and molecular clusters.

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
%license COPYING
%doc README.md

%changelog
