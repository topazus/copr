%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global libname lsp-server

Name:           ocaml-%{libname}
Version:        1.8.3
Release:        1%{?dist}
Summary:        An LSP server for OCaml.
 
License:        BSD
URL:            https://github.com/ocaml/ocaml-lsp
Source0:        https://github.com/ocaml/ocaml-lsp/releases/download/1.8.3/jsonrpc-1.8.3.tbz

 
BuildRequires:  ocaml >= 4.12
BuildRequires:  ocaml-dune ocaml-yojson-devel ocaml-re-devel ocaml-ppx-deriving-yojson-devel
BuildRequires:  dot-merlin-reader ocaml-merlin ocaml-csexp-devel ocaml-result-devel
BuildRequires:  ocaml-odoc-devel
BuildRequires:  ocaml-findlib ocaml-ocamldoc

%description
OCaml-LSP is a language server for OCaml that implements Language Server Protocol (LSP).

This project contains an implementation of a language server for OCaml and a standalone library implementing LSP.


%prep
%autosetup -p0 -n jsonrpc-%{version}

%build
dune build %{?_smp_mflags}

%install
DESTDIR=%{buildroot} dune install

%check
dune runtest

%files
%license LICENSE
%doc README.md

