%global debug_package %{nil}

Name:           rust-bindgen
Version:        0.63.0
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries

License:        BSD-3-Clause
URL:            https://crates.io/crates/bindgen
Source:         https://github.com/rust-lang/rust-bindgen/archive/refs/tags/v%{version}.0.tar.gz

BuildRequires:  rust-packaging >= 21

%description
Automatically generates Rust FFI bindings to C (and some C++) libraries.

%prep
%autosetup -n %{crates_dir}-%{version}


%build
%cargo_build

%install


%check


%changelog