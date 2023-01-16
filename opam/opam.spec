%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname opam

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A source-based package manager
License:        LGPL
URL:            https://opam.ocaml.org/
Source:         https://github.com/ocaml/opam/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc gcc-c++ make pkg-config git openssl

%if 0%{?fedora} >= 34
BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-seq-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-opam-file-format-devel
BuildRequires:  ocaml-dose3-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-mccs-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-dune

BuildRequires:  glpk-devel
%endif
BuildRequires:  zlib-devel

Requires:       bubblewrap m4 patch

%description
Opam is a source-based package manager for OCaml. It supports multiple simultaneous compiler installations, flexible package constraints, and a Git-friendly development workflow.

%prep
%autosetup -n %{appname}-master -p1

%build
%if 0%{?fedora} >= 34
%configure
make
%else
make cold CONFIGURE_ARGS="--prefix %{buildroot}%{_prefix}"
%endif

%install
%make_install

%check

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/opam-installer
%{_mandir}/man1/*.1.gz

%changelog
