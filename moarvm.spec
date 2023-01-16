%global debug_package %{nil}
%if %fedora == 36
# Disable package-notes because its linker flag leaks to rakudo, bug #2070099
# https://src.fedoraproject.org/rpms/moarvm/blob/rawhide/f/moarvm.spec#_81
%undefine _package_note_file
%endif

Name:           moarvm
Version:        2022.12
Release:        1%{?dist}
Summary:        A VM with adaptive optimization and JIT compilation, built for Rakudo
License:        Artistic 2.0
URL:            https://github.com/MoarVM/MoarVM
Source0:        https://github.com/MoarVM/MoarVM/releases/download/%{version}/MoarVM-%{version}.tar.gz

BuildRequires:  gcc make perl
BuildRequires:  dyncall libatomic_ops-devel
BuildRequires:  libatomic_ops-devel libuv-devel libtommath-devel libffi-devel

%description
A VM with adaptive optimization and JIT compilation, built for Rakudo

%prep
%autosetup -n MoarVM-%{version}

#sed -i -- 's/\/usr\/local/\/usr/g' Configure.pl

rm -rf 3rdparty/libuv
rm -rf 3rdparty/libatomicops
rm -rf 3rdparty/dyncall
rm -rf 3rdparty/libtommath
#rm -rf 3rdparty/mimalloc

%build
%{__perl} Configure.pl --prefix=%{_usr} --libdir=%{_libdir} \
  --has-libuv --has-libffi \
  --has-libatomic_ops --has-libtommath --mimalloc
%make_build

%install
# solve rpath error
#export QA_RPATHS=$[ 0x0001 | 0x002 ]
%make_install

%check

%files
/usr/bin/moar

#%dir /usr/include/mimalloc
#/usr/include/mimalloc/*
%exclude %{_includedir}/mimalloc

%dir /usr/include/moar
/usr/include/moar/*
/usr/lib64/libmoar.so

%dir /usr/share/nqp
/usr/share/nqp/lib/MAST/Nodes.nqp
/usr/share/nqp/lib/MAST/Ops.nqp
/usr/share/pkgconfig/moar.pc

%changelog
