%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname polyml

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a Standard ML implementation originally written in an experimental language called Poly.
License:        MIT
URL:            https://github.com/polyml/polyml
#Source:

BuildRequires:  gcc-c++ make pkg-config

%description
Poly/ML is a Standard ML implementation originally written in
 an experimental language called Poly.

%prep
git clone --depth=1 https://github.com/polyml/polyml .

%build
%configure
%make_build

%install
make install

%check


%files
/usr/bin/poly
/usr/bin/polyc
/usr/bin/polyimport

/usr/lib64/libpolymain.a
/usr/lib64/libpolyml.a
/usr/lib64/libpolyml.so
/usr/lib64/libpolyml.so.13
/usr/lib64/libpolyml.so.13.0.0

/usr/lib64/pkgconfig/polyml.pc
/usr/lib64/polyml/modules/IntInfAsInt

/usr/share/man/man1/*.1.gz

%changelog
