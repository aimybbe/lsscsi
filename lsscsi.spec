%define name    lsscsi
%define version 0.21
%define release 1

Summary: 	List SCSI devices (or hosts) and associated information
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		Utilities/System
Source0:	http://www.torque.net/scsi/%{name}-%{version}.tgz
Url:		http://www.torque.net/scsi/lsscsi.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-root/
Packager:	dgilbert at interlog dot com

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

Author:
--------
    Doug Gilbert <dgilbert at interlog dot com>

%prep

%setup -q

%build

./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install

[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

make install \
        DESTDIR=$RPM_BUILD_ROOT

%post

%postun

%clean

[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man8/*


%changelog
* Wed Jul 9 2008 - dgilbert at interlog dot com
- changes for lk 2.6.25/26 SCSI midlayer rework
  * lsscsi-0.20
* Thu Jan 25 2007 - dgilbert at interlog dot com
- add transport information (target+initiator)
  * lsscsi-0.19
* Fri Mar 24 2006 - dgilbert at interlog dot com
- cope with dropping of 'generic' symlink post lk 2.6.16
  * lsscsi-0.18
* Mon Feb 06 2006 - dgilbert at interlog dot com
- fix disappearance of block device names in lk 2.6.16-rc1
  * lsscsi-0.17
* Fri Dec 30 2005 - dgilbert at interlog dot com
- wlun naming, osst and changer devices
  * lsscsi-0.16
* Tue Jul 19 2005 - dgilbert at interlog dot com
- does not use libsysfs, add filter argument, /dev scanning
  * lsscsi-0.15
* Fri Aug 20 2004 - dgilbert at interlog dot com
- add 'timeout'
  * lsscsi-0.13
* Sun May 9 2004 - dgilbert at interlog dot com
- rework for lk 2.6.6, device state, host name, '-d' for major+minor
  * lsscsi-0.12
* Fri Jan 09 2004 - dgilbert at interlog dot com
- rework for lk 2.6.1
  * lsscsi-0.11
* Tue May 06 2003 - dgilbert at interlog dot com
- adjust HBA listing for lk > 2.5.69
  * lsscsi-0.10
* Fri Apr 04 2003 - dgilbert at interlog dot com
- fix up sorting, GPL + copyright notice
  * lsscsi-0.09
* Sun Mar 2 2003 - dgilbert at interlog dot com
- start to add host listing support (lk >= 2.5.63)
  * lsscsi-0.08
* Fri Feb 14 2003 - dgilbert at interlog dot com
- queue_depth name change in sysfs (lk 2.5.60)
  * lsscsi-0.07
* Mon Jan 20 2003 - dgilbert at interlog dot com
- osst device file names fix
  * lsscsi-0.06
* Sat Jan 18 2003 - dgilbert at interlog dot com
- output st and osst device file names (rather than "-")
  * lsscsi-0.05
* Thu Jan 14 2003 - dgilbert at interlog dot com
- fix multiple listings of st devices (needed for lk 2.5.57)
  * lsscsi-0.04
* Thu Jan 09 2003 - dgilbert at interlog dot com
- add --generic option (list sg devices), scsi_level output
  * lsscsi-0.03
* Wed Dec 18 2002 - dgilbert at interlog dot com
- add more options including classic mode
  * lsscsi-0.02
* Fri Dec 13 2002 - dgilbert at interlog dot com
- original
  * lsscsi-0.01
