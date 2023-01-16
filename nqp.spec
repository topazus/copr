%global debug_package %{nil}
%if %fedora == 36
# Disable package-notes because its linker flag leaks to rakudo, bug #2070099
# https://src.fedoraproject.org/rpms/moarvm/blob/rawhide/f/moarvm.spec#_81
%undefine _package_note_file
%endif

Name:           nqp
Version:        2022.12
Release:        1%{?dist}
Summary:        Perl 6 compiler implementation that runs on MoarVM
License:        Artistic 2.0
URL:            https://github.com/Raku/nqp
Source0:        https://github.com/Raku/nqp/releases/download/%{version}/nqp-%{version}.tar.gz

BuildRequires:  gcc make perl
BuildRequires:  libatomic_ops-devel libuv-devel libtommath-devel libffi-devel mimalloc-devel
BuildRequires:  moarvm >= %{version}

Requires:       moarvm >= %{version}

%description
This is "Not Quite Perl" -- a lightweight Raku-like environment for virtual machines.

%prep
%autosetup -n nqp-%{version}

%build

# Disable package-notes because its linker flag leaks to rakudo
# only occur error in fedora 36
# /usr/bin/ld: cannot open linker script file /builddir/build/BUILD/MoarVM-2022.12/.package_note-moarvm-2022.12-1.fc36.x86_64.ld: No such file or directory
%undefine _package_note_file

rm -r 3rdparty/jna # make sure not to bundle 'jna'
%{__perl} Configure.pl --backends=moar --prefix=%{_usr}
make %{?_smp_mflags}

%install
# solve rpath error
#export QA_RPATHS=$[ 0x0001 | 0x002 ]
%make_install

%check

%files
/usr/bin/nqp
/usr/bin/nqp-m

%dir /usr/share/nqp
/usr/share/nqp/lib/

%changelog
