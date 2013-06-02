# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       nemo-qml-plugin-email-qt5

# >> macros
# << macros

Summary:    Email plugin for Nemo Mobile
Version:    0.0.5
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-email
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-email-qt5.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(qmfclient5)
BuildRequires:  pkgconfig(mlite5)

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre


%qmake5

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/org/nemomobile/email/libnemoemail.so
%{_libdir}/qt5/imports/org/nemomobile/email/qmldir
# >> files
# << files
