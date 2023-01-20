%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname dmd

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        dmd D Programming Language compiler

License:        ASL 2.0 or MIT
URL:            https://dlang.org/
#Source:
Source1:        https://raw.githubusercontent.com/topazus/copr/master/dmd.conf

BuildRequires:  gcc-c++ git

%description
The D programming language is an object-oriented, imperative,
multi-paradigm system programming language. It has type inference,
automatic memory management and syntactic sugar for common types,
bounds checking, design by contract features, and a concurrency-aware
type system.

%prep
git clone --depth=1 https://github.com/dlang/dmd
git clone --depth=1 https://github.com/dlang/phobos

if [ ! -d $HOME/dlang ]; then
  curl -fsS https://dlang.org/install.sh | bash -s dmd
fi

%build
source ~/dlang/dmd-2.101.2/activate

# dmd
pushd dmd/compiler/src
	dmd -O build.d
	./build dmd
popd

# druntime
pushd dmd/druntime
  make %{?_smp_mflags} -f posix.mak \
    BUILD=release \
    DMD="../generated/linux/release/*/dmd" \
    PIC=1 \
    ENABLE_RELEASE=1
popd

# phobos
pushd phobos
  make %{?_smp_mflags} -f posix.mak \
    BUILD=release \
    DMD="../dmd/generated/linux/release/*/dmd" \
    PIC=1 \
    ENABLE_RELEASE=1
popd

# dmd was built with gdmd, now build dmd with that dmd
pushd dmd/compiler/src
	mv ../../generated/linux/release/*/ gdmd-built-dmd/
	cat gdmd-built-dmd/dmd.conf
	sed -i 's#P%/..#P%#g' gdmd-built-dmd/dmd.conf
	cat gdmd-built-dmd/dmd.conf

	./gdmd-built-dmd/dmd -O build.d
	./build dmd
popd

%install
# install files manually since the install script distributed put files all over the place
# dmd
install -Dm755 %{_builddir}/dmd/generated/linux/release/*/dmd %{buildroot}%{_bindir}/dmd

install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/dmd.conf

mkdir -p %{buildroot}%{_mandir}
cp -r %{_builddir}/dmd/compiler/docs/man/* %{buildroot}%{_mandir}/

mkdir -p %{buildroot}%{_datadir}/dmd/samples/
cp -r dmd/compiler/samples/* %{buildroot}%{_datadir}/dmd/samples/

# phobos
# phobos
install -dm755 %{buildroot}/usr/lib
cp -r $(find phobos/generated/linux/release/ \( -iname "*.a" -a \! -iname "*.so.a" \) -o \( -iname "*.so*" -a \! -iname "*.o" -a \! -iname "*.a" \) ) %{buildroot}/usr/lib

mkdir -p %{buildroot}%{_includedir}/dlang/dmd
cp -r dmd/druntime/import/* %{buildroot}%{_includedir}/dlang/dmd
cp -r phobos/{*.d,etc,std} %{buildroot}%{_includedir}/dlang/dmd


%files
%{_bindir}/dmd
%{_datadir}/dmd
%{_sysconfdir}/dmd.conf
%{_mandir}/man*/*

/usr/lib/libphobos*

%{_includedir}/dlang

%changelog
