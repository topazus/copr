%global debug_package %{nil}

Name:           go
Version:        1.19.4
Release:        1%{?dist}
Summary:        The Go Programming Language
License:        BSD
URL:            https://github.com/golang/go

#Source:         https://go.dev/dl/go%{version}.src.tar.gz
Source:         https://github.com/golang/go/archive/go%{version}.tar.gz

BuildRequires:  pkg-config golang

%description
Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.

%prep
%autosetup -n %{name}

%build
./make.bash -v

%install
install -d "%{buildroot}/usr/bin" "%{buildroot}/usr/lib/go" "%{buildroot}/usr/share/doc/go" \
  "%{buildroot}/usr/lib/go/pkg/linux_amd64_"{dynlink,race}

cp -a bin pkg src lib misc api test "%{buildroot}/usr/lib/go"

# We can't strip all binaries and libraries,
# as that also strips some testdata directories and breaks the tests.
# Just strip the packaged binaries as a compromise.
strip $STRIP_BINARIES "%{buildroot}/usr/lib/go"{/bin/*,/pkg/tool/*/*}

cp -r doc/* "%{buildroot}/usr/share/doc/go"

ln -sf /usr/lib/go/bin/go "%{buildroot}/usr/bin/go"
ln -sf /usr/lib/go/bin/gofmt "%{buildroot}/usr/bin/gofmt"
ln -sf /usr/share/doc/go "%{buildroot}/usr/lib/go/doc"

install -Dm644 VERSION "%{buildroot}/usr/lib/go/VERSION"

rm -rf "%{buildroot}/usr/lib/go/pkg/bootstrap" "%{buildroot}/usr/lib/go/pkg/tool/*/api"

# TODO: Figure out if really needed
rm -rf "%{buildroot}"/usr/lib/go/pkg/obj/go-build


%check


%files


%changelog
