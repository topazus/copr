%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           boost-git
Version:        1.81.0
Release:        1%{?dist}
Summary:        Super-project for modularized Boost
License:        ASL
URL:            https://github.com/boostorg/boost
Source:         https://github.com/boostorg/boost/releases/download/boost-%{version}/boost-%{version}.tar.xz

BuildRequires:  gcc-c++ cmake git

%description
Super-project for modularized Boost

%prep
%autosetup -n boost-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%files
/usr/include/boost/
/usr/lib64/cmake/
/usr/lib64/libboost_*

%changelog
