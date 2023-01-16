
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname tomviz
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Cross platform, open source application for the processing, visualization, and analysis of 3D tomography data
License:        BSD-3 Clause
URL:            https://github.com/openchemistry/tomviz
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: desktop-file-utils libappstream-glib


Requires: python3-numpy

%description
The Tomviz project is developing a cross platform, open source application for the processing, visualization, and analysis of 3D tomographic data.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%if %{with check}
%check
%ctest
%endif


desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop


%changelog
