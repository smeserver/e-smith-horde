# $Id: e-smith-horde.spec,v 1.23 2010/11/08 03:54:17 mrjhb3 Exp $

Summary: e-smith specific Horde configuration and templates.
%define name e-smith-horde
Name: %{name}
%define version 4.2.0
%define release 14
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-horde_3.3-upgrade.patch
Patch2: e-smith-horde_3.3.2-upgrade.patch
Patch3: e-smith-horde_cookie_domain.patch
Patch4: e-smith-horde_3.3.4-upgrade.patch
Patch5: e-smith-horde_3.3.5-upgrade.patch
Patch6: e-smith-horde_3.3.6.patch
Patch7: e-smith-horde_username.hook.patch
Patch8: e-smith-horde_mime_drivers.php.patch
Patch9: e-smith-horde_3.3.8.patch
Patch10: e-smith-horde_3.3.10.patch 
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
* Sun Nov 07 2010 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-14
- Upgrade horde templates to reflect changes in Horde 3.3.10 [SME:6348]

* Mon May 10 2010 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-13
- Upgrade horde templates to reflect changes in Horde 3.3.8 [SME: 5938]

* Sun Feb 14 2010 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-12
- Patch to change horde's templated mime_drivers.php file so some additional
  settings can be customized [SME: 5224]
- config setprop horde inlineMSWord true|false <-- default is false
- config setprop horde inlineMSExcel true|false <-- default is false
- config setprop horde inlineMSPowerpoint true|false <-- default is false
- config setprop horde inlineWordperfect true|false <-- default is false
- config setprop horde inlineAudio true|false <-- default is true

* Sat Feb 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-11
- Patch to make sure username is always saved in lowercase to horde db's [SME:5775]

* Sat Feb 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-10
- Upgrade horde templates to reflect changes in Horde 3.3.6 [SME: 5774]

* Tue Oct 13 2009 John H. Bennett III <bennettj@johnbennettservices.com> 4.2.0-9
- Really apply patch from previous attempt [SME: 5509]

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
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

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
