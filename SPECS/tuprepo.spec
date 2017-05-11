Name:           tuprepo
Version:        1
Release:        0
Summary:        network repo for TUP CentOS Servers

Group:          System Environment/Base
License:        GPL
URL:            http://theurbanpenguin.com
Source0:        tuprepo-1.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Create a YUM repo file in the /etc/yum.repos.d/ folder

%prep
%setup -q


%install
mkdir -p "$RPM_BUILD_ROOT"
cp -R * "$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/CentOS-Tup.repo




