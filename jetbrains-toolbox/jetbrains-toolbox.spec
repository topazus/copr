%global debug_package %{nil}

Name:           jetbrains-toolbox
Version:        1.20.8804
Release:        1%{?dist}
Summary:        Manage your JetBrains IDEs the easy way
License:        custom
URL:            https://www.jetbrains.com/toolbox-app/
Source0:        https://download.jetbrains.com/toolbox/jetbrains-toolbox-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-toolbox/jetbrains-toolbox.desktop
Source2:        https://intellij-icons.jetbrains.design/icons/AllIcons/nodes/toolbox.svg

BuildRequires:  pkg-config desktop-file-utils
Requires:       jetbrains-jre

%description
Manage your JetBrains IDEs the easy way

%prep
%autosetup -n jetbrains-toolbox-%{version}

%build

%install
install -pDm755 jetbrains-toolbox %{buildroot}%{_bindir}/jetbrains-toolbox

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/jetbrains-toolbox.desktop
install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/jetbrains-toolbox.svg

%check

%files
%{_bindir}/jetbrains-toolbox
%{_datadir}/applications/jetbrains-toolbox.desktop
%{_datadir}/icons/hicolor/scalable/apps/jetbrains-toolbox.svg

%changelog
