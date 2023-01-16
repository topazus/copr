%global debug_package %{nil}

Name:           rakudo
Version:        2022.12
Release:        1%{?dist}
Summary:        🦋 Rakudo – Raku on MoarVM, JVM, and JS
License:        Artistic 2.0
URL:            https://github.com/rakudo/rakudo
Source0:        https://github.com/rakudo/rakudo/releases/download/%{version}/rakudo-%{version}.tar.gz

BuildRequires:  gcc make perl
BuildRequires:  libatomic_ops-devel libuv-devel libtommath-devel libffi-devel mimalloc-devel
BuildRequires:  moarvm >= %{version}
BuildRequires:  nqp >= %{version}

Requires:       moarvm >= %{version}
Requires:       nqp >= %{version}

%description
This is Rakudo, a Raku Programming Language compiler for the MoarVM, JVM and Javascript virtual machines.

%prep
%autosetup -n rakudo-%{version}

%build
#perl Configure.pl --gen-moar --gen-nqp --backends=moar
perl Configure.pl --prefix=%{_prefix} --backends=moar
make %{?_smp_mflags}

%install
# solve rpath error
#export QA_RPATHS=$[ 0x0001 | 0x002 ]

%make_install
#cp -r install/ %{buildroot}/usr

%check
#%{__make} test

%files
/usr/bin/perl6*
/usr/bin/raku
/usr/bin/raku-debug
/usr/bin/rakudo*

%dir /usr/share/perl6
/usr/share/perl6/*

%changelog
