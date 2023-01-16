%global debug_package %{nil}

Name:           dyncall
Version:        1.3
Release:        1%{?dist}
Summary:        A Generic Dynamic FFI package
License:        custom
URL:            https://dyncall.org/
Source0:        https://dyncall.org/r%{version}/dyncall-%{version}.tar.gz

BuildRequires:  gcc make

%description
he dyncall library encapsulates architecture-, OS- and compiler-specific function call semantics in a virtual bind argument parameters from left to right and then call interface allowing programmers to call C functions in a completely dynamic manner.

%prep
%autosetup -n %{name}-%{version}

%build
./configure --prefix=%{buildroot}/usr
make %{?_smp_mflags}

%install
make install

%check

%files
/usr/include/dyncall*.h
/usr/include/dynload.h
/usr/lib/libdyncall_s.a
/usr/lib/libdyncallback_s.a
/usr/lib/libdynload_s.a

%changelog
