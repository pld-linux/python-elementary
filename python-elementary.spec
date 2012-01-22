Summary:	Python bindings for Elementary library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Elementary
Name:		python-elementary
Version:	0.7.3
Release:	1
License:	LGPL v3+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	30ddcbd13b917689676bc3de55cd10ca
Patch0:		%{name}-cython.patch
Patch1:		%{name}-update.patch
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	elementary-devel >= 0.8.0
BuildRequires:	eina-devel >= 1.0.0
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-evas >= 0.7.3
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	elementary-libs >= 0.8.0
Requires:	eina >= 1.0.0
Requires:	evas >= 1.0.0
Requires:	python-evas >= 0.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Elementary library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Elementary.

%package devel
Summary:	Python bindings for Elementary library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Elementary - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	elementary-devel >= 0.8.0
Requires:	eina-devel >= 1.0.0
Requires:	evas-devel >= 1.0.0
Requires:	python-evas-devel >= 0.7.3

%description devel
Python bindings for Elementary library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Elementary - pliki programistyczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/elementary/c_elementary.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{py_sitedir}/elementary
%attr(755,root,root) %{py_sitedir}/elementary/c_elementary.so
%{py_sitescriptdir}/elementary
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/python-elementary.pc
