%define name	munin-plugins-sympa
%define version	20090617
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Munin sympa plugins
Group:		Networking/Other
License:	BSD
URL:		https://www.lists.uni-karlsruhe.de/munin/
Source:     https://www.lists.uni-karlsruhe.de/munin/sympa4munin.tar.gz
Patch:      munin-plugins-sympa-fix-spool-script.patch
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This package contains two plugins, one to monitor the elements in your
spool-directory and a second one which parses your sympa-log. 

%prep
%setup -c -q
%patch -p 1

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/munin/plugins
install -m 755 sympa_spool %{buildroot}%{_datadir}/munin/plugins
install -m 755 sympa_stats %{buildroot}%{_datadir}/munin/plugins

perl -pi -e 's|^#!/usr/local/bin/perl|#!%{_bindir}/perl|' \
    %{buildroot}%{_datadir}/munin/plugins/sympa_stats

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/munin/plugins/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20090617-4mdv2011.0
+ Revision: 620421
- the mass rebuild of 2010.0 packages

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20090617-3mdv2010.0
+ Revision: 387124
- fix sympa_spool plugin

* Wed Jun 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20090617-2mdv2010.0
+ Revision: 386699
- fix shellbang
- import munin-plugins-sympa


* Wed Jun 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20090617-1mdv2010.0
- first mandriva package
