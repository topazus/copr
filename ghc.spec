%global debug_package %{nil}

Name:           ghc
Version:        9.4.3
Release:        1%{?dist}
Summary:        The Glorious Glasgow Haskell Compiler.
License:        ASL 2.0
URL:            https://www.haskell.org/
Source:         https://downloads.haskell.org/~ghc/%{version}/ghc-%{version}-src.tar.xz

BuildRequires:  llvm make autoconf pkg-config
BuildRequires:  perl glibc-devel ncurses-devel gmp-devel autoconf automake libtool gcc gcc-c++ make perl python
BuildRequires:  happy alex git


%description
GHC is a state-of-the-art, open source, compiler and interactive environment for the functional language Haskell.

%prep
%autosetup -n ghc-%{version}

%build
#export GHC=/home/ruby/ghc-9.4.3-x86_64-unknown-linux/bin/ghc
export GHC=/home/ruby/haskell/bin/ghc
# set CC to llvm
#export CC=/usr/bin/clang
#BUILDCC="/usr/bin/gcc -std=gnu99"
./boot.source
./configure --prefix=%{buildroot}/usr
#  --enable-bootstrap-with-devel-snapshot

%make_build
#hadrian/build %{?_smp_mflags}

%install
%make_install

%check


%files


%changelog
