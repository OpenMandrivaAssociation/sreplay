Summary:	Tool that performs system call replay
Name:		sreplay
Version:	0.2.9
Release:	4
License:	LGPL
Group:		Development/Kernel
Url:		http://weather.ou.edu/~apw/projects/sreplay/
Source0:	http://weather.ou.edu/~apw/projects/sreplay/%{name}-%{version}.tar.bz2
ExcludeArch:	x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Sreplay is a tool that performs system call replay of strace logs on UNIX-like
operating systems. It is written in assembly and C. It supports simple
dynamically-linked application replay under i386 and ppc64 Linux at present.

%prep

%setup -q

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
install %{name} %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/%{name}
