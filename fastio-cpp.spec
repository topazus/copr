%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname fastio-cpp

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Significantly faster input/output for C++20
License:        GPL
URL:            https://github.com/flameshot-org/flameshot
#Source:

BuildRequires:  gcc-c++ cmake git

%description
Significantly faster input/output for C++20

%prep
git clone --depth=1 https://github.com/cppfastio/fast_io.git .

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%files
/usr/include/fast_io*

/usr/man/man3/concat.3.gz
/usr/man/man3/native_file.3.gz
/usr/man/man3/print.3.gz
/usr/man/man3/to.3.gz

%changelog
