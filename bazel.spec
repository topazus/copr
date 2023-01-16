%global debug_package %{nil}

Name:           bazel
Version:        6.0.0
Release:        1%{?dist}
Summary:        Correct, reproducible, and fast builds for everyone.
License:        Apache License 2.0
URL:            https://github.com/bazelbuild/bazel
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip

BuildRequires:  java-11-openjdk-devel
BuildRequires:  zlib-devel pkgconfig gcc-c++ which unzip zip
BuildRequires:  python3 python-absl-py

Requires:       java-11-openjdk-devel

%description
Correct, reproducible, and fast builds for everyone.

%prep
%setup -q -c -n bazel-%{version}

%build
bash compile.sh
# generate shell completion files
#./output/bazel build scripts:bazel-complete.bash
bash scripts/generate_bash_completion.sh --bazel=output/bazel --output=output/bazel.bash
python3 scripts/generate_fish_completion.py --bazel=output/bazel --output=output/bazel.fish

%install
install -pDm755 output/bazel %{buildroot}%{_bindir}/bazel-real
install -pDm755 scripts/packages/bazel.sh %{buildroot}%{_bindir}/bazel

install -pDm644 output/bazel.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -pDm644 scripts/zsh_completion/_bazel %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -pDm644 output/bazel.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/%{name}.fish

%files
%{_bindir}/bazel
%{_bindir}/bazel-real

%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_conf.d/%{name}.fish

%changelog
