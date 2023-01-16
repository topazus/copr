%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname vscode-insider

Name:           %{appname}
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Visual Studio Code Insiders
License:        MIT
URL:            https://code.visualstudio.com/
Source0:        https://update.code.visualstudio.com/latest/linux-x64/insider
Source1:        https://raw.githubusercontent.com/topazus/copr/main/vscode-insider/vscode-insider.desktop

Requires:       libxkbfile xdg-utils

%description
Visual Studio Code Insiders

%prep
%autosetup -n VSCode-linux-x64 -p1

%build


%install
mkdir -p %{buildroot}/opt/vscode-insider
cp -r * %{buildroot}/opt/vscode-insider

install -pDm644 ./resources/app/resources/linux/code.png %{buildroot}/usr/share/icons/vscode-insider.png

install -pDm644 ./resources/completions/bash/code-insiders %{buildroot}/usr/share/bash-completion/completions/code-insiders
install -pDm644 ./resources/completions/zsh/_code-insiders %{buildroot}/usr/share/zsh/site-functions/_code-insiders

install -pDm644 %{SOURCE1} %{buildroot}/usr/share/applications/vscode-insider.desktop

%check

%files
%dir /opt/vscode-insider
/opt/vscode-insider/*

/usr/share/icons/vscode-insider.png
/usr/share/bash-completion/completions/code-insiders
/usr/share/zsh/site-functions/_code-insiders
/usr/share/applications/vscode-insider.desktop

%ghost /usr/bin/code-insiders

%post
ln -s /opt/vscode-insider/bin/code /usr/bin/code-insiders

%changelog
