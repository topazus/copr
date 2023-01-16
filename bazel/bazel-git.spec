%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname bazel

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Correct, reproducible, and fast builds for everyone.
License:        Apache License 2.0
URL:            http://bazel.io/
#Source:

BuildRequires:  java-11-openjdk-devel

BuildRequires:  zlib-devel pkgconfig gcc-c++ which
BuildRequires:  unzip zip

BuildRequires:  python3 python-absl-py git wget

Requires:       java-11-openjdk-devel

%description
Correct, reproducible, and fast builds for everyone.

%prep
git clone --depth=1 https://github.com/bazelbuild/bazel .
wget -O bazel https://github.com/bazelbuild/bazel/releases/download/5.2.0/bazel-5.2.0-linux-x86_64
chmod +x bazel

%build
#./bazel build //src:bazel-dev

# generate smaller build
./bazel build //src:bazel --compilation_mode=opt scripts:bazel-complete.bash scripts:bazel.fish
#bash scripts/generate_bash_completion.sh --bazel=output/bazel --output=output/bazel.bash
#python3 scripts/generate_fish_completion.py --bazel=output/bazel --output=output/bazel.fish

%install
install -pDm755 bazel-bin/src/bazel %{buildroot}%{_bindir}/bazel-real
install -pDm755 scripts/packages/bazel.sh %{buildroot}%{_bindir}/bazel

install -pDm644 bazel-bin/scripts/bazel-complete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -pDm644 scripts/zsh_completion/_bazel %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -pDm644 bazel-bin/scripts/bazel-complete.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/%{appname}.fish

%files
%{_bindir}/bazel
%{_bindir}/bazel-real

%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_conf.d/%{appname}.fish

%changelog
