%define name pyclutter-gtk
%define version 0.10.0
%define rel 1
%define release %mkrel %rel

%define apiver 1.0
%define api 0.10
%define pyclutter 1.0.0

Summary:       Python bindings for clutter-gtk
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.clutter-project.org/sources/%name/%apiver/%{name}-%{version}.tar.bz2
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-gtk-devel >= %version
BuildRequires: pygtk2.0-devel >= 2.8.0
BuildRequires: python-clutter-devel >= %pyclutter
BuildRequires: python-cairo-devel >= 1.0.2
BuildRequires: libxslt-proc

%description
Python bindings for clutter-gtk

#----------------------------------------------------------------------------

%package -n python-clutter-gtk
Summary:       Python bindings for clutter-gtk
Group:         Graphics
Provides:      pyclutter-gtk = %{version}-%{release}
Requires: python-clutter >= %pyclutter

%description -n python-clutter-gtk
Python bindings for clutter-gtk

%package -n python-clutter-gtk-devel
Summary:       Python bindings for clutter-gtk
Group: Development/Python
Requires: python-clutter-gtk  = %{version}-%{release}

%description -n python-clutter-gtk-devel
Python bindings for clutter-gtk - development files.


%prep
%setup -q

%build
%configure2_5x --enable-docs
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files -n python-clutter-gtk
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{py_platsitedir}/cluttergtk

%files -n python-clutter-gtk-devel
%defattr(-,root,root)
%doc ChangeLog
%{_datadir}/pyclutter/%{apiver}/defs/*.defs
%{_libdir}/pkgconfig/%{name}-%{api}.pc
