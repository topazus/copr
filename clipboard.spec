%global debug_package %{nil}
%global appname clipboard

Name:           %{appname}
Version:        0.2.1r2
Release:        1%{?dist}
Summary:        clipboard Cut, copy, and paste anything, anywhere, all from the terminal.
License:        GPL
URL:            https://github.com/Slackadays/Clipboard
Source:         https://github.com/Slackadays/Clipboard/archive/%{version}.tar.gz

BuildRequires:  gcc-c++ cmake

%if 0%{?fedora}
BuildRequires:  libwayland-client libX11-devel
%elif 0%{?suse_version}
BuildRequires:  libwayland-client0 libX11-devel
%endif

%description
clipboard Cut, copy, and paste anything, anywhere, all from the terminal. Quick, easy, and unified.

%prep
%autosetup -n Clipboard-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%if 0%{?fedora}
export QA_RPATHS=$(( 0x0001|0x0010 ))
%endif
%cmake_install

%check

%files
/usr/bin/clipboard
/usr/lib/libclipboardwayland.so
/usr/lib/libclipboardx11.so

%changelog
