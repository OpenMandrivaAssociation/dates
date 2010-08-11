%define name dates 
%define version 0.4.11
%define release %mkrel 2

Summary: Simple calendar application
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0: dates-0.4.7-format-strings.patch
Patch1: dates-0.4.11-fix-tabs-in-makefiles.patch
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://pimlico-project.org/dates.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libedataserver-devel
BuildRequires: libgtk+2-devel
BuildRequires: intltool

%description
Dates is a small, lightweight calendar, featuring an innovative, unified,
zooming view and is designed primarily for use on hand-held devices. 

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang Dates

%clean
rm -rf $RPM_BUILD_ROOT

%files -f Dates.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog 
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_mandir/man1/*
%_datadir/%{name}/*
%_datadir/icons/hicolor/*



