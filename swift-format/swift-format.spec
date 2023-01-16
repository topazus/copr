%undefine _missing_build_ids_terminate_build
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname swift-format

%if %{?fedora} == 34
%bcond_without check
%endif

%if %{?fedora} >= 35
%global __brp_check_rpaths %{nil}
%endif

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A command-line tool and Xcode Extension for formatting Swift code
License:        MIT
URL:            https://github.com/nicklockwood/SwiftFormat
Source:         https://github.com/nicklockwood/SwiftFormat/archive/master/SwiftFormat-master.tar.gz

BuildRequires:  gcc wget


%description
SwiftFormat is a code library and command-line tool for reformatting Swift code on macOS or Linux.

%prep
%autosetup -n SwiftFormat-master -p1
mkdir -p $HOME/swift-env
wget -O- https://swift.org/builds/swift-5.4.2-release/centos8/swift-5.4.2-RELEASE/swift-5.4.2-RELEASE-centos8.tar.gz | tar xvzf - -C $HOME/swift-env

%build
$HOME/swift-env/swift-5.4.2-RELEASE-centos8/usr/bin/swift build -c release

%install
install -pDm755 .build/release/swiftformat %{buildroot}%{_prefix}/local/bin/swiftformat

%if %{with check}
%check
$HOME/swift-env/swift-5.4.2-RELEASE-centos8/usr/bin/swift test
%endif

%files
%license LICENSE*
%doc README.md
%{_prefix}/local/bin/swiftformat

%changelog
