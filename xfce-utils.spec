Summary:	Utilities for the Xfce Desktop Environment
Summary(pl.UTF-8):	Narzędzia dla środowiska Xfce
Name:		xfce-utils
Version:	4.8.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce-utils/4.8/%{name}-%{version}.tar.bz2
# Source0-md5:	7f48198f4bee3edf7869064c2922c609
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-gxmessage.patch
URL:		http://www.xfce.org/projects/xfce-utils
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	libxfce4util-devel >= 4.8.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.8.0
Requires:	gtk-update-icon-cache
Requires:	gxmessage
Requires:	hicolor-icon-theme
Requires:	libxfce4ui >= 4.8.0
Requires:	perl-XML-Parser
Requires:	which
Requires:	xfce4-dirs >= 4.6
Requires:	xscreensaver >= 5.13
Requires:	xorg-app-xrdb
Requires:	xorg-app-xinit
Requires:	xorg-app-xsetroot
Conflicts:	xfce4-session < 0.1.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the Xfce Desktop Environment.

%description -l pl.UTF-8
xfce-utils zawiera narzędzia dla środowiska Xfce.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce.desktop

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce4.desktop

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xfce4/xfconf-migration
%attr(755,root,root) %{_libdir}/xfce4/xfconf-migration/xfconf-migration-4.6.pl
%{_sysconfdir}/xdg/autostart/xfconf-migration-4.6.desktop
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/Xft.xrdb
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/xinitrc
%{_datadir}/dbus-1/services/*.service
%dir %{_docdir}/xfce-utils
%dir %{_docdir}/xfce-utils/html
%{_docdir}/xfce-utils/html/C
%{_docdir}/xfce-utils/html/*.css
%lang(da) %{_docdir}/xfce-utils/html/da
%lang(el) %{_docdir}/xfce-utils/html/el
%lang(gl) %{_docdir}/xfce-utils/html/gl
%lang(it) %{_docdir}/xfce-utils/html/it
%lang(ja) %{_docdir}/xfce-utils/html/ja
%lang(sv) %{_docdir}/xfce-utils/html/sv
%lang(tr) %{_docdir}/xfce-utils/html/tr
%lang(ug) %{_docdir}/xfce-utils/html/ug
%lang(zh_CN) %{_docdir}/xfce-utils/html/zh_CN

%{_iconsdir}/hicolor/*/*/*

%{_desktopdir}/xfce4-about.desktop
%{_desktopdir}/xfhelp4.desktop
%{_desktopdir}/xfrun4.desktop
%{_datadir}/xsessions/xfce4.desktop
