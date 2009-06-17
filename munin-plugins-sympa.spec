%define name	munin-plugins-sympa
%define version	20090617
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Munin sympa plugins
Group:		Networking/Other
License:	BSD
URL:		https://www.lists.uni-karlsruhe.de/munin/
Source0:	https://www.lists.uni-karlsruhe.de/munin/sympa4munin.tar.gz
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This package contains two plugins, one to monitor the elements in your
spool-directory and a second one which parses your sympa-log. 

%prep
%setup -c -q

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/munin/plugins
install -m 755 sympa_spool %{buildroot}%{_datadir}/munin/plugins
install -m 755 sympa_stats %{buildroot}%{_datadir}/munin/plugins

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/munin/plugins/*

