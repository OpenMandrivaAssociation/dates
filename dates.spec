%define name dates 
%define version 0.4.3
%define release %mkrel 1

%define fakename gtkdatesview
%define major 0
%define libname %mklibname %{fakename}_ %major

Summary: Dates is a simple calendar application
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pimlico-project.org/sources/dates/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://pimlico-project.org/dates.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libedataserver-devel
BuildRequires: libgtk+2-devel
BuildRequires: desktop-file-utils

Requires: %libname = %version

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Dates is a small, lightweight calendar, featuring an innovative, unified,
zooming view and is designed primarily for use on hand-held devices. 

%package -n %libname
Summary: Tasks libraries
Group: System/Libraries

%description -n %libname
Libraries package for %{name}.

%package -n %libname-devel
Summary: Development package for %{name}
Group: Development/Other
Requires: %libname = %version
Provides: %libname-devel = %version-%release

%description -n %libname-devel
Development package for %{name}

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --remove-category="Application" \
  --remove-category="Office" \
  --remove-category="Project Management" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/applications/*

%post
%update_icon_cache hicolor
%update_menus

%postun
%clean_icon_cache hicolor
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog 
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_mandir/man1/*
%_datadir/%{name}/*
%_datadir/icons/hicolor/*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/lib*.a
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%_libdir/pkgconfig/*


