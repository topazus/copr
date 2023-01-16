%global debug_package %{nil}

Name:           microsoft-jdk17
Version:        17.0.2
Release:        1%{?dist}
Summary:        OpenJDK Java 17 development kit (Microsoft build)
License:        custom
URL:            https://www.microsoft.com/openjdk
Source:         https://aka.ms/download-jdk/microsoft-jdk-17.0.2.8.1-linux-x64.tar.gz

BuildRequires:  pkg-config

%description
Microsoft Build of OpenJDK™
Free. Open Source. Freshly Brewed!

%prep
%autosetup -n jdk-17.0.2+8 -p1

%build


%install
mkdir -p %{buildroot}%{_prefix}/lib/jvm/microsoft-jdk17
cp -a * %{buildroot}%{_prefix}/lib/jvm/microsoft-jdk17

%check


%files
%{_prefix}/lib/jvm/microsoft-jdk17/*

%changelog
