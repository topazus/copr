
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname maim
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        takes screenshots of your desktop
License:        GPL
URL:            https://github.com/naelstrof/maim
Source:         https://github.com/naelstrof/maim/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ cmake
BuildRequires:	libX11-devel libXrender-devel libXfixes-devel
BuildRequires:	libXrandr-devel libXcomposite-devel libpng-devel
BuildRequires:	libjpeg-turbo-devel mesa-libGL-devel glm-devel libwebp-devel
BuildRequires:	libslopy-devel libicu-devel


%description
maim (Make Image) is a utility that takes screenshots of your desktop. It's meant to overcome shortcomings of scrot and performs better in several ways.

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
%license license.txt
%doc README.md
%{_bindir}/%{appname}
%{_mandir}/man1/maim.1.gz

%changelog
