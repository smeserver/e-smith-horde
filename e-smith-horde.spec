# $Id: e-smith-horde.spec,v 1.8 2008/09/16 18:04:56 bytegw Exp $

Summary: e-smith specific Horde configuration and templates.
%define name e-smith-horde
Name: %{name}
%define version 3.2
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-horde-3.2.1-header.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base >= 4.9.44, horde >= 2.0, mysql
Requires: e-smith-lib >= 1.15.1-16
Requires: enscript
Requires: php-domxml
Requires: php-gd
Requires: php-mbstring
Requires: wv
Requires: xlhtml
Requires: horde >= 3.2
Requires: php-pear
%if "%{?rhel}" == "5"
Obsoletes: pear-date
Obsoletes: pear-db
Obsoletes: pear-file
Obsoletes: pear-log
Obsoletes: pear-mail
Obsoletes: pear-mail_mime
Requires: php-pear(Date)
Requires: php-pear(File)
Requires: php-pear(HTTP)
Requires: php-pear(Log)
Requires: php-pear(Services_Weather)
Requires: php-pecl(Fileinfo)
%else
Requires: pear-date
Requires: pear-db
Requires: pear-file
Requires: pear-log
Requires: pear-mail
Requires: pear-mail_mime
%endif
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: dcb-e-smith-horde
Obsoletes: smeserver-horde-menuarray

%changelog
* Tue Jun 24 2008 John H. Bennett III <bennettj@johnbennettservices.com> 3.2-2
- Upgrade patch for Horde 3.2.1 [SME: 4532]

* Mon Jun 2 2008 John H. Bennett III <bennettj@johnbennettservices.com> 3.2-1
- Initial production build
- Jump in package name to reflect new version of horde

%description
This package adds necessary templates and configuration items
so that Horde will work properly on SME Server

%prep
%setup
%patch1 -p1

%build
for i in post-install post-upgrade
do
    mkdir -p root/etc/e-smith/events/$i
done
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
