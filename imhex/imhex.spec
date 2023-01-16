
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname imhex
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A Hex Editor for Reverse Engineers, Programmers and people
License:        GPL
URL:            https://werwolv.net/
Source:         https://github.com/WerWolv/ImHex/archive/master/ImHex-master.tar.gz

BuildRequires:  gcc-c++ cmake pkg-config meson ninja-build
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  libtree-devel perl-File-LibMagic perl-libintl-perl
BuildRequires:  capstone-devel file-devel glfw-devel glm-devel
BuildRequires:  mesa-libGL-devel mbedtls-devel python3-devel freetype-devel gtk3


%description
A Hex Editor for Reverse Engineers, Programmers and people that value their eye sight when working at 3 AM.

%prep
%autosetup -n ImHex-master -p1

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


%changelog
