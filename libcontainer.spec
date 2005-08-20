#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Simple C library that provides linked lists, stacks, queues and binary trees.
Summary(pl):	Prosta biblioteka C dostarczaj±ca list wi±zanych, stosów, kolejek i drzew binarnych.
Name:		libcontainer
Version:	0.1.0
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://www.readonly.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	2363c3604eba4f96ff8db74c5edca87a
URL:		http://www.readonly.co.uk/projects.html#LIBCONTAINER
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcontainer is a simple C library that you can use in your
applications to provide linked lists, stacks, queues and binary trees.
I would like to work on this a little more (linked-lists only support
bubble sort at the moment). There is a slight lack of documentation
but there are some examples in the test/ directory.

#%%description -l pl

%package devel
Summary:	Header files for libcontainer library
Summary(pl):	Pliki nag³ówkowe biblioteki libcontainer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcontainer library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libcontainer.

%package static
Summary:	Static libcontainer library
Summary(pl):	Statyczna biblioteka libcontainer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcontainer library.

%description static -l pl
Statyczna biblioteka libcontainer.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--enable-static=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
