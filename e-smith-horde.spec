# $Id: e-smith-horde.spec,v 1.16 2009/10/14 02:19:12 mrjhb3 Exp $

Summary: e-smith specific Horde configuration and templates.
%define name e-smith-horde
Name: %{name}
%define version 4.2.0
%define release 8
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-horde_3.3-upgrade.patch
Patch2: e-smith-horde_3.3.2-upgrade.patch
Patch3: e-smith-horde_cookie_domain.patch
Patch4: e-smith-horde_3.3.4-upgrade.patch
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
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: dcb-e-smith-horde
Obsoletes: smeserver-horde-menuarray
Obsoletes: smeserver-trean < 0.1-8

%changelog
* Tue Oct 13 2009 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-8  
- Upgrade horde templates to reflect changes in Horde 3.3.5 [SME: 5509]   

* Sat Jun 20 2009 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-7
- Upgrade to horde templates to reflect changes in Horde 3.3.4 [SME: 5372]

* Thu Dec 24 2008 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-6
- Updated spec file to remove requires and obsoletes of php-pear-HTTP-Request
  information moved to e-smith-imp for both sme7 and sme8 [SME: 4821]

* Sun Dec 21 2008 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-5
- Update to Spec file to obsolete smeserver-trean < 0.1-8  [SME: 4860]

* Sat Dec 20 2008 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-4
- Patch to conf.php template to set a blank cookie domain so that FQDN and non-FQDN
- access to webmail will work. Remove klutz template from registry.php [SME: 4787]

* Sat Dec 06 2008 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-3
- Upgrade to horde templates to reflect changes in Horde 3.3.2

* Sat Dec 06 2008 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-2       
- Upgrade to horde templates to reflect changes in Horde 3.3  [SME: 4831]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 4.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

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
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
