%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname zig
%define file_link https://ziglang.org/builds/zig-0.10.0-dev.3685+dae7aeb33.tar.xz

Name:           %{appname}-git
Version:        0.10.0
Release:        1%{?dist}
Summary:        General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software
License:        MIT
URL:            https://github.com/ziglang/zig
#Source:

BuildRequires:  cmake pkg-config wget
BuildRequires:  clang lld llvm-libs clang-devel llvm-devel lld-devel

%description
A general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

%prep
wget %file_link
tar xf zig-*.tar.xz

%build
cd zig-*/
%cmake
%cmake_build

%install
cd zig-*/
%cmake_install

%check

%files


%changelog
