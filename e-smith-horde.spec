Summary: e-smith specific Horde configuration and templates.
%define name e-smith-horde
Name: %{name}
%define version 1.13.0
%define release 22
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-horde-1.13.0-02.conf_php.patch
Patch1: e-smith-horde-1.13.0-03.mime_drivers_php.patch
Patch2: e-smith-horde-1.13.0-04.prefs_php.patch
Patch3: e-smith-horde-1.13.0-05.registry_php.patch
Patch4: e-smith-horde-1.13.0-06.mysql_init.patch
Patch5: e-smith-horde-1.13.0-07.createlinks_metadata.patch 
Patch6: e-smith-horde-1.13.0-08.30horde_mysql_create_tables.patch
Patch8: e-smith-horde-1.13.0-09.horde_menu_array.patch
Patch9: e-smith-horde-1.13.0-10.mimp.patch
Patch10: e-smith-horde-1.13.0-11.40horde_mysql_create_indexes.patch
Patch11: e-smith-horde-1.13.0-12.horde_registry_php_modification.patch
Patch12: e-smith-horde-1.13.0-13.mysql_update_privs.patch
Patch13: e-smith-horde-1.13.0-14.inline_path_change.patch
Patch14: e-smith-horde-1.13.0-15.horde_db.patch  
Patch15: e-smith-horde-1.13.0-16.horde_upgrade.patch
Patch16: e-smith-horde-1.13.0-17.horde_create_indexes_2.patch
Patch17: e-smith-horde-1.13.0-18.horde_administration.patch
Patch18: e-smith-horde-1.13.0-19.horde_mysql_init_rename.patch
Patch19: e-smith-horde-1.13.0-20.horde_314.patch
Patch20: e-smith-horde-1.13.0-21.horde_315.patch
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
Requires: horde >= 3.1
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
* Thu Nov 15 2007 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-22
- Updated horde registry.php template, per horde 3.1.5 [SME: 3572]

* Wed May 9 2007 Shad L. Lords <slords@mail.com> 1.13.0-21
- Updates to support SME Server 8
- Include pear modules from e-smith-imp and e-smith-info

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sun Mar 25 2007 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-20
- Updated horde conf.php, prefs.php, and registry.php, per horde 3.1.4 [SME: 2783]

* Tue Jan 23 2007 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-19
- This patch renames the last remaining mysql.init event tied to horde so that now
  all of the events pertaining to horde are clearly identified. [SME: 1363]

* Wed Dec 27 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-18
- Patch to add a DB entry that will enable the Horde Administration menu to be visible 
  for the Admin user.  To use (config setprop horde Administration enabled followed by 
  signal-event email-update or expand-template /home/httpd/html/horde/config/conf.php).  [SME: 2191]

* Wed Dec 27 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-17
- Patch that corrects the duplicate index errors seen when installing or upgrading
  to SME 7.1.  [SME: 2194]

* Sun Dec 24 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-16
- Patch that corrects the duplicate column errors on new 7.1 installs and
  upgrades from SME 7.0 to 7.1.  [SME: 2190]

* Sat Dec 09 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Tue Dec 5 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-15
- Added additional directive to 85HordeAccess to fix a security issue.  [SME: 2136]

* Fri Nov 25 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-14
- Patch that changes the inline viewer path for excel and powerpoint.  Inline viewers
  are still defaulted to false.

* Thu Nov 09 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-13
- Patch that moves the mysql.init call for 77mysql_update_privs from smeserver-kronolith
  to e-smith-horde

* Thu Oct 5 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-12
- Removed imp, ingo, and turba specific horde/config/registry.php settings and moved
  them to their own specific e-smith RPMs.


* Mon Oct 2 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-11
- Patch to 40horde_mysql_create_indexes which will now create the indexes for the
  horde_prefs table.

* Thu Sep 28 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-10
- Added code to the horde/conf.php/125Authentication template that will use the 
  horde composite driver if mimp is installed and status set to enabled.  The
  Composite driver is needed so horde can login to either imp or mimp.
- Added 999mimp template to horde/config/conf.php that will check if mimp is 
  configured as a service and enabled.  If so, then the composite authentication 
  driver will be used so that mimp and imp can coexist.  Otherwise imp will be 
  used for authentication. The composite driver information appears below the 
  footer like the example from http://wiki.horde.org/MIMPHowTo?referrer=AuthCompositeHowTo
  To activate - config set mimp service status enabled|disabled.  Disabled by default.
  signal-event email-update

* Wed Sep 27 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-09
- Added code so that what I am calling the horde menuarray can be enabled or 
  disabled globally for all potential horde add-on modules via a db property.  
  config setprop horde MenuArray disabled|enabled.  Enabled by default.
  If enabled, all horde add-on module icons will be visible in the webmail view.
  Each individual horde module can also be set to display or not to display in the 
  array as well.  See specific add-on module RPM for more information.

* Wed Sep 27 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-08
- Patch to update the horde mysql creation of tables and indexes for horde 3.1.x

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-07
- Patch to createlinks and templates.metadata files to reflect updated names from
  patch 6

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-06
- Patch to update and rename mysql.init calls so they can be identified with horde

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-05
- Patch to update horde templates in registry.php for horde 3.1.x

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-04
- Patch to update horde templates in prefs.php for horde 3.1.x

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-03
- Patch to update horde templates in mime_drivers.php for horde 3.1.x

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-02
- Patch to update horde templates in conf.php for horde 3.1.x
- Added an 120AdminAuthentication section which adds admin@primary_domain as a horde
  administrator which now needs to be used to grant various permissions in horde 3.1.x

* Mon Sep 11 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.13.0-01
- Roll development stream for horde 3.1.x

* Thu Jul 20 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.12.0-04
- Removed Nag, Mnemo, Kronolith, Mimp, Gollem, and Trean template fragments from
  registry.php so they can be included with their own specific smeserver- RPM's. [SME: 1742]

* Thu Jul 06 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.12.0-03
- Template patch to 00header that incorporates the updates for horde 3.0.11 [SME: 1710]

* Wed Apr 05 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.12.0-02
- Patch that incorporates the updates for horde 3.0.10 [SME: 1157]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Sat Mar 4 2006 John H. Bennett III <bennettj@thebennetthome.com> 1.11.1-28
- Removed config.jhb directory from /etc/e-smith/templates/home/httpd/html/horde/ [SME: 893]

* Thu Feb 23 2006 John H. Bennett III <bennettj@thebennetthome.com> 1.11.1-27
- Bumped revision number so changes can be tracked via bug tracker [SME: 893]

* Thu Feb 23 2006 John H. Bennett III <bennettj@thebennetthome.com> 1.11.1-26
- Added email-update event to createlinks so that horde conf.php, prefs.php, 
  registry.php, and mime_drivers.php templates will be expanded.  If not a
  post-upgrade, reboot has to be run for this to happen or a manual expansion
  of the templates, in order for new settings to be put in place.

* Sun Feb 19 2006 John H. Bennett III <bennettj@thebennetthome.com> 1.11.1-25
- Updated conf.php, prefs.php, registry.php, and mime_drivers.php templates
  to match the contents of horde 3.0.9.  Some templates were renumbered so
  that when they are expanded they match what are in the *.dist file.
  This should make it easier to find changes going forward [SME: 840]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.1-24
- Force horde password to >= 57 characters [SME: 201]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.1-23
- Bump release number only

* Thu Nov 24 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-22]
- Remove Requires: gd [SF: 1365954]
- Add Requires: php-mbstring [SF: 1283048]

* Thu Nov 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-21]
- Force Horde password to length > 8 chars. [SF: 1365309]

* Thu Nov 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-20]
- Update config so it's not reported as out of date. [SF: 1312522]

* Thu Nov 17 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-19]
- And Require for gd [SF: 1283048, 1356104] [RH: 173095]

* Sun Nov 13 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-18]
- Add Requires for php-domxml and php-gd [SF: 1283048, 1356104]

* Mon Sep 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-17]
- Add Requires header for enscript. [SF: 1274096]

* Fri Aug 26 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-16]
- Fix path to xlhtml binary in mime_drivers template (allows browser
  based viewing of Excel And Powerpoint files). [SF: 1274096]

* Fri Aug 26 2005 Shad Lords <slords@mail.com>
- [1.11.1-15]
- Add wv and xlhtml to requires [SF: 1274096]

* Tue Jun 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-14]
- Put template-{begin,end} fragments in the right place! [SF: 1220733,1222197]

* Fri Jun 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-13]
- Add missing template-begin and template-end fragments for new templated php
  files. [SF: 1220733,1222197]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-12]
- Add templates (courtesy Greg Swallow) for {prefs,registry,mime_drivers}.php.
  [SF: 1220733]

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-11]
- Add /usr/share/pear-addons to php search path.

* Wed Apr 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-10]
- Hide horde Administration interface.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-09]
- Fix typo in mysql socket path.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-08]
- HordePassword migrate fragment fix.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-07]
- Add mysql socket path to conf.php.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-06]
- Fix newline in horde password.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-05]
- Fix perms on conf.php.
- Prefix conf.php template with template-begin-php
- Remove templates.metadata for untemplated mime_drivers.php
  and registry.php files and obsolete horde.php file.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-04]
- Add missing horde/config/conf.php template fragments.
- Fix a couple of problems with horde db update scripts.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-03]
- Fix error in horde db password migrate fragment.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-02]
- Apply Greg Swallow's configuration patches and add horde db
  migration script.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-01]
- Roll to new development stream for horde 3 update - 1.11.1

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Rename mysql.init shell scripts so that they don't end in .sql.
- Add missing template expansions for mysql.init scripts.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Obsolete conf-horde-startup script, and add templated shell
  scripts in its place.
- Add templates.metadata files for templated php config files
  so that permissions and ownerships are correct.

* Thu Jan 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Restrict access to test.php [MN00064810]
- Use generic_template_expand action in place of conf-horde.
  Add BuildRequires of e-smith-devtools. [MN00064130]

* Tue Jan 20 2004 Mark Knox <markk@e-smith.com>
- [1.11.0-01]
- Rolling to devel. Bug 10917. - 1.11.0

* Tue Jan 20 2004 Mark Knox <markk@e-smith.com>
- [1.10.0-01]
- Rolling to stable. Bug 10917. - 1.10.0

* Tue Jan  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-17]
- Fixed bad variable reference in conf-horde-startup. [msoulier 10855]

* Tue Jan  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-16]
- Fixed ordering of template expansion to symlink creation. [msoulier 10855]

* Tue Dec 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-15]
- Fixed ordering of password set and template expansion. Removed password set
  from update privs script. One place to set the password is enough.
  [msoulier 10855]

* Mon Dec 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-14]
- Fixed typo in conf-horde. [msoulier 7112]

* Fri Dec 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-13]
- Moved code to set the random horde password into conf-horde.
  [msoulier 7112]

* Thu Dec 18 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-12]
- Make sure that the horde password is alphabetical. [msoulier 7112]

* Tue Nov 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-11]
- Added migration of the user table. [msoulier 7112]

* Tue Nov 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-10]
- Moved the migration code to an sql script. [msoulier 7112]

* Sun Nov 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-09]
- Added a migrate fragment to remove an existing horde@% user. [msoulier 7112]

* Sun Nov 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-08]
- Changed the grant on the horde user to horde@localhost. [msoulier 7112]

* Thu Nov 20 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-07]
- Added default type and status fragments. [msoulier 10671]

* Fri Nov 14 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-06]
- Force perms of root:root 0640 on the mysql_set_password fragment [markk 4796]

* Fri Nov 14 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-05]
- Fixed bad return value from template fragment [markk 4796]

* Fri Nov 14 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-04]
- Fixed char range in random passwd generator [markk 4796]

* Fri Nov 14 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-03]
- s/template/templates/ in 'use' line [markk 4796]

* Fri Nov 14 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-02]
- Added code to randomise horde password in conf-horde-startup [markk 4796]

* Fri Nov 14 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-01]
- Rolling to devel stream

* Thu Nov 13 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-05]
- Added code to conf-horde-startup to remove dangling symlinks at
  /etc/e-smith/sql/init. [msoulier 9476]

* Wed Jul 16 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-04]
- Unlink sql/init symlinks before creating new ones, in case
  symlink exists and points to the wrong place. [charlieb 9476]
- Replace Copyright header with License header.

* Fri Jul 11 2003 Mark Knox <markk@e-smith.com>
- [1.8.0-03]
- Also allow index and references privs [markk 9359]

* Fri Jul 11 2003 Mark Knox <markk@e-smith.com>
- [1.8.0-02]
- Patch to allow alter_priv on horde db [markk 9359]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to stable stream number - 1.8.0

* Thu Jun 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.1-05]
- Last changelog was for e-smith-imp - no changes from 1.7.1-03
  [gordonr 9041]

* Thu Jun 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.1-04]
- Add imp|installed property so Mail button shows in the
  address book [gordonr 9041]

* Mon Apr 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.7.1-03]
- Restricted access to horde admin directory. [msoulier 8160]

* Thu Apr 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.1-02]
- Changed IMP's displayed name to "webmail" from "Mail" [gordonr 7694]

* Wed Apr 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.1-01]
- Included changes from Dan Brown's 1.7.0-04db [gordonr 7694]
  * Sun Apr  6 2003 Dan Brown <dan@familybrown.org>
  - [1.7.0-04db]
  - Changed mailer to use sendmail due to "relaying denied"
  errors
  * Sun Apr  6 2003 Dan Brown <dan@familybrown.org>
  - [1.7.0-03db]
  - Created new horde-update action, and added conf-horde to it.
  * Sat Apr  5 2003 Dan Brown <dan@familybrown.org>
  - [1.7.0-02db]
  - Added conf-horde and conf-horde-startup to email-update action
  * Tue Mar 11 2003 Dan Brown <dan@familybrown.org>
  - [1.7.0-01db]
  - Updated horde.php and registry.php config files to agree with horde 2.2

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-04]
- Deleted ./config/{horde, mime_drivers, registry}.php/template-begin
  and modified %build [lijied 3295]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.7.0-03]
- Deleted ./config/{horde, mime_drivers, registry}.php/template-end
  modified %build [lijied 3295]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-02]
- Log horde details to syslog, not /tmp/horde.log [gordonr 3706]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-01]
- dev stream to 1.7.0
- Roll to development stream [gordonr 3706]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Roll to maintained version number to 1.6.0

* Thu Oct  3 2002 Mark Knox <markk@e-smith.com>
- [1.5.2-08]
- Make sure we connect to the horde db in sql fragments [markk 4958]
- Clarify ordering of sql fragments [markk 4958]

* Thu Oct  3 2002 Mark Knox <markk@e-smith.com>
- [1.5.2-07]
- Split horde mysql setup into three parts [markk 4958]

* Wed Oct  2 2002 Mark Knox <markk@e-smith.com>
- [1.5.2-06]
- Split horde mysql setup script into two parts [markk 4958]

* Wed Sep 25 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-05]
- Fix missing quotes around directory name in last change [charlieb 4958]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-04]
- Only add mysql.create.horde.sql symlink to /etc/e-smith/sql/init if
  horde db doesn't already exist. [charlieb 4958]

* Mon Sep  9 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-03]
- Remove conf-horde from all but post-install/post-upgrade events -
  the configuration isn't a function of any config variables [charlieb 4782]

* Fri Sep  6 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-02]
- Split conf-horde into conf-horde and conf-horde-startup - conf-horde-start
  runs post-install and post-upgrade.  [charlieb 4782]
- Expand horde templates and create horde database unconditionally.
  [charlieb 4782]

* Mon Jul 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-01]
- Add conf-horde link to bootstrap-console-save event [charlieb 1939]

* Tue Jun 18 2002 Mark Knox <markk@e-smith.com>
- [1.5.1-01]
- Use SMTP instead of sendmail [markk 3920]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Changing version to development stream number to 1.5.0

* Thu May 30 2002 Tony Clayton <apc@e-smith.com>
- [1.4.12-01]
- start mysql.init with BACKGROUND=>'false' in conf-horde [tonyc 3751]

* Thu May 30 2002 Mark Knox <markk@e-smith.com>
- [1.4.11-01]
- Added a missing menu settings fragment for horde.php [markk 3740]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.4.10-01]
- RPM rebuild forced by cvsroot2rpm

* Tue May  7 2002 Mark Knox <markk@e-smith.com>
- [1.4.9-01]
- Always install mysql tables (fixes upgrade issues) [markk 2825]

* Thu Apr 25 2002 Mark Knox <markk@e-smith.com>
- [1.4.8-01]
- Fixed check on returned record conf-horde that was causing script failures
  on a clean install [markk]

* Thu Apr 25 2002 Mark Knox <markk@e-smith.com>
- [1.4.7-01]
- Added missing files in mime_drivers template dir. [markk 3249]

* Tue Apr 23 2002 Mark Knox <markk@e-smith.com>
- [1.4.6-01]
- Templates mime_drivers.php with Rich's changes [markk 3230]

* Thu Apr 18 2002 Adrian Chung <adrianc@e-smith.com>
- [1.4.5-01]
- Remove trailing blank line from registry.php template.

* Wed Apr 17 2002 Adrian Chung <adrianc@e-smith.com>
- [1.4.4-01]
- Update location of MySQL DB import script.

* Tue Apr  9 2002 Mark Knox <markk@e-smith.com>
- [1.4.3-01]
- Added <?php ... ?> tags in template begin and end. [markk]

* Tue Apr  9 2002 Mark Knox <markk@e-smith.com>
- [1.4.2-01]
- Merged in Dan Brown's contrib updates for Horde 2.0 [markk 2825]
- Updated conf-horde to handle new config templates, and converted to new DB
  APIs [markk 2825]
- Converted 85HordeAccess fragment to new DB API [markk 2825]

* Tue Apr 9 2002 Mark Knox <markk@e-smith.com>
- [1.4.1-01]
- rollRPM: Rolled version number to 1.4.1-01. Includes patches up to 1.4.0-03.

* Thu Jan  3 2002 Adrian Chung <adrianc@e-smith.com>
- [1.4.0-03]
- Cleanup fragment code in 85HordeAccess.

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-02.

* Tue May 29 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-02]
- untie/retie %conf hash in conf-horde when calling serviceControl

* Wed Mar 28 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-01]
- branching to development stream
- includes patches upto 1.2.0-11

* Fri Mar 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.2.0-11]
- changed destructive 'local %conf' to 'my %conf' in httpd.conf fragment

* Wed Mar 21 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-10]
- modified conf-horde again, to fix typo:
  e-smith-sql => e-smith/sql
- run mysql.init after creating symlink
- make sure to only create symlink if databases aren't
  already there.

* Wed Mar 21 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-09]
- modified conf-horde to use new mysql.init queue
  mechanism.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Mon Jan 29 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-07]
- chown()'s an processTemplate should only be done if horde is 
  enabled, (inside if enabled block), but outside of 
  /var/lib/mysql/horde directory existence check.

* Mon Jan 29 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-06]
- added Includes line to Directory access block for horde
  so that SSI's can be used in the imp/SSLonly directory.

* Mon Jan 29 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-05]
- correct logic in conf-horde script.
- always do chown()'s and processTemplate call
- outside of if block

* Sat Jan 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-04]
- Correct missing # in the "PHP not enabled" warning in the httpd config.
- Change if-return to if-elsif-else construct in template fragment code.
- Remove %post and %postun scripts

* Fri Jan 26 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-03]
- move dependency checks to after the database entry has been
  initialized.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- add dependency checks in template fragments as well
- they won't expand if PHP isn't enabled.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-15.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-15]
- added dependency check for PHP in conf-horde script

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-14]
- fix missing comma in conf-horde

* Wed Jan 24 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-13]
- added background => false so that mysql service
  control calls are not backgrounded.

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-12]
- move mysql related chowns into block protected by check
  for mysql data directory.

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-11]
- check for defined $runlevel in conf-horde.

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-10]
- Use serviceControl()

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-9]
- added email-update event link

* Mon Jan  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-8]
- got rid of initialized variable.  check for existence
  of /var/lib/mysql/horde/* instead.
- if runlevel 7, shutdown mysqld, do stuff, then restart it
- set ownership of /var/lib/mysql/horde/* after creation.

* Mon Jan  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-7]
- fixed typo: added space back in to 85HordeAccess template.

* Mon Jan  8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-6]
- Fix some pathnames
- Change dependency MySQL => mysql

* Mon Jan  8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-5]
- Only do %post and %postun actions in runlevel 7
- Just call action script in %post anyway, don't repeat the code here.
- Remove backticks from action script, avoid backgrounded actions in
  script - use perl methods instead to do chown/chgrp.
- Always default to disabled.
- Make  85HordeAccess depend on horde service - enforce horde/imp
  dependency in the UI.

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-4]
- wrap 85HordeAccess fragment in httpd.conf so that it
  only expands if IMP is on -- since IMP is the only service
  that uses horde right now.

* Wed Nov 22 2000 Adrian Chung <adrianc@e-smith.com>
- Delayed chown by 5 seconds instead of immediate.

* Wed Nov 22 2000 Adrian Chung <adrianc@e-smith.com>
- Changed basedir in conf-horde event to /usr for mysql import

* Wed Nov 22 2000 Adrian Chung <adrianc@e-smith.com>
- Rolled to 1.1.0, this stream for 4.1/7.0.

* Tue Nov 14 2000 Adrian Chung <adrianc@e-smith.com>
- initial release

%description
This package adds necessary e-smith template fragments to enable
horde specific configuration items.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

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
