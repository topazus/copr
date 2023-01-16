%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname xmake

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Modern C++ Terminal Emulator
License:        GPL
URL:            https://github.com/contour-terminal/contour
#Source0:

BuildRequires:  gcc-c++
BuildRequires:  git wget

%description
Modern C++ Terminal Emulator

%prep

git clone --depth=1 https://github.com/xmake-io/xmake .

%build
make build -j4

%install
mkdir -p %{buildroot}/usr
make install PREFIX=%{buildroot}/usr

%check

%files


%changelog
