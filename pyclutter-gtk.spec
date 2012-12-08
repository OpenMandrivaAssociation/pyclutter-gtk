%define apiver 1.0
%define api 0.10
%define pyclutter 1.0.0

Summary:	Python bindings for clutter-gtk
Name:		pyclutter-gtk
Version:	0.10.0
Release:	5
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://www.clutter-project.org/sources/%{name}/%{apiver}/%{name}-%{version}.tar.bz2
Patch0:		pyclutter-gtk-0.10.0-link.patch
Patch1:		pyclutter-gtk-0.10.0-clutter-gtk-1.0.patch
Patch2:		pyclutter-gtk-0.10.0-git-changes-20100929.patch
Patch3:		pyclutter-gtk-0.10.0-no-scrollable.patch
Patch4:		pyclutter-gtk-0.10.0-no-zoomable.patch
Patch5:		pyclutter-gtk-0.10.0-no-standin.patch
Patch6:		pyclutter-gtk-0.10.0-no-viewport.patch
Patch7:		pyclutter-gtk-0.10.0-automake.patch
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pygtk2.0-devel >= 2.8.0
BuildRequires:	python-clutter-devel >= %{pyclutter}
BuildRequires:	python-cairo-devel >= 1.0.2
BuildRequires:	libxslt-proc

%description
Python bindings for clutter-gtk

#----------------------------------------------------------------------------

%package -n python-clutter-gtk
Summary:	Python bindings for clutter-gtk
Group:		Graphics
Provides:	pyclutter-gtk = %{version}-%{release}
Requires:	python-clutter >= %{pyclutter}

%description -n python-clutter-gtk
Python bindings for clutter-gtk

%package -n python-clutter-gtk-devel
Summary:	Python bindings for clutter-gtk
Group:		Development/Python
Requires:	python-clutter-gtk = %{version}-%{release}

%description -n python-clutter-gtk-devel
Python bindings for clutter-gtk - development files.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoreconf -fi
%configure2_5x --enable-docs
%make

%install
%makeinstall_std

%files -n python-clutter-gtk
%doc AUTHORS README NEWS
%{py_platsitedir}/cluttergtk

%files -n python-clutter-gtk-devel
%doc ChangeLog
%{_datadir}/pyclutter/%{apiver}/defs/*.defs
%{_libdir}/pkgconfig/%{name}-%{api}.pc


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2mdv2011.0
+ Revision: 667905
- mass rebuild

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 593861
- fix linkage

* Wed Feb 03 2010 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 500051
- import pyclutter-gtk


