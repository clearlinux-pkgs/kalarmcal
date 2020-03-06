#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kalarmcal
Version  : 19.12.3
Release  : 20
URL      : https://download.kde.org/stable/release-service/19.12.3/src/kalarmcal-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/kalarmcal-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/kalarmcal-19.12.3.tar.xz.sig
Summary  : The KAlarm client library
Group    : Development/Tools
License  : LGPL-2.1
Requires: kalarmcal-data = %{version}-%{release}
Requires: kalarmcal-lib = %{version}-%{release}
Requires: kalarmcal-license = %{version}-%{release}
Requires: kalarmcal-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kpimtextedit-dev

%description
See Mainpage.dox for more information.

%package data
Summary: data components for the kalarmcal package.
Group: Data

%description data
data components for the kalarmcal package.


%package dev
Summary: dev components for the kalarmcal package.
Group: Development
Requires: kalarmcal-lib = %{version}-%{release}
Requires: kalarmcal-data = %{version}-%{release}
Provides: kalarmcal-devel = %{version}-%{release}
Requires: kalarmcal = %{version}-%{release}
Requires: kalarmcal = %{version}-%{release}

%description dev
dev components for the kalarmcal package.


%package lib
Summary: lib components for the kalarmcal package.
Group: Libraries
Requires: kalarmcal-data = %{version}-%{release}
Requires: kalarmcal-license = %{version}-%{release}

%description lib
lib components for the kalarmcal package.


%package license
Summary: license components for the kalarmcal package.
Group: Default

%description license
license components for the kalarmcal package.


%package locales
Summary: locales components for the kalarmcal package.
Group: Default

%description locales
locales components for the kalarmcal package.


%prep
%setup -q -n kalarmcal-19.12.3
cd %{_builddir}/kalarmcal-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583512063
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583512063
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kalarmcal
cp %{_builddir}/kalarmcal-19.12.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kalarmcal/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang libkalarmcal5-serializer
%find_lang libkalarmcal5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_kalarm.desktop
/usr/share/qlogging-categories5/kalarmcal.categories
/usr/share/qlogging-categories5/kalarmcal.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KAlarmCal/KAlarmCal/Akonadi
/usr/include/KF5/KAlarmCal/KAlarmCal/AlarmText
/usr/include/KF5/KAlarmCal/KAlarmCal/CollectionAttribute
/usr/include/KF5/KAlarmCal/KAlarmCal/CompatibilityAttribute
/usr/include/KF5/KAlarmCal/KAlarmCal/DateTime
/usr/include/KF5/KAlarmCal/KAlarmCal/EventAttribute
/usr/include/KF5/KAlarmCal/KAlarmCal/KACalendar
/usr/include/KF5/KAlarmCal/KAlarmCal/KADateTime
/usr/include/KF5/KAlarmCal/KAlarmCal/KAEvent
/usr/include/KF5/KAlarmCal/KAlarmCal/KARecurrence
/usr/include/KF5/KAlarmCal/KAlarmCal/Repetition
/usr/include/KF5/KAlarmCal/kalarmcal/akonadi.h
/usr/include/KF5/KAlarmCal/kalarmcal/alarmtext.h
/usr/include/KF5/KAlarmCal/kalarmcal/collectionattribute.h
/usr/include/KF5/KAlarmCal/kalarmcal/compatibilityattribute.h
/usr/include/KF5/KAlarmCal/kalarmcal/datetime.h
/usr/include/KF5/KAlarmCal/kalarmcal/eventattribute.h
/usr/include/KF5/KAlarmCal/kalarmcal/identities.h
/usr/include/KF5/KAlarmCal/kalarmcal/kacalendar.h
/usr/include/KF5/KAlarmCal/kalarmcal/kadatetime.h
/usr/include/KF5/KAlarmCal/kalarmcal/kaevent.h
/usr/include/KF5/KAlarmCal/kalarmcal/kalarmcal_export.h
/usr/include/KF5/KAlarmCal/kalarmcal/karecurrence.h
/usr/include/KF5/KAlarmCal/kalarmcal/repetition.h
/usr/include/KF5/KAlarmCal/kalarmcal/version.h
/usr/include/KF5/kalarmcal_version.h
/usr/lib64/cmake/KF5AlarmCalendar/KF5AlarmCalendarConfig.cmake
/usr/lib64/cmake/KF5AlarmCalendar/KF5AlarmCalendarConfigVersion.cmake
/usr/lib64/cmake/KF5AlarmCalendar/KF5AlarmCalendarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AlarmCalendar/KF5AlarmCalendarTargets.cmake
/usr/lib64/libKF5AlarmCalendar.so
/usr/lib64/qt5/mkspecs/modules/qt_KAlarmCal.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AlarmCalendar.so.5
/usr/lib64/libKF5AlarmCalendar.so.5.13.3
/usr/lib64/qt5/plugins/akonadi_serializer_kalarm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kalarmcal/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libkalarmcal5-serializer.lang -f libkalarmcal5.lang
%defattr(-,root,root,-)

