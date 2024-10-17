%global realname gettext
%global debug_package %{nil}
%global git_tag b55cb72


Name:		erlang-%{realname}
Version:	2.1.0
Release:	0.11.20101022git%{git_tag}.2
Summary:	Erlang internationalization library
Group:		Development/Erlang
License:	MIT
URL:		https://github.com/etnt/gettext
# wget http://github.com/etnt/gettext/tarball/b55cb72
Source0:	etnt-%{realname}-%{git_tag}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	erlang-erts
Requires:	erlang-erts >= R12B-5
Requires:	erlang-kernel >= R12B-5
Requires:	erlang-stdlib >= R12B-5
Requires:	erlang-sasl >= R12B-5


%description
Erlang internationalization library.


%prep
%setup -q -n etnt-%{realname}-%{git_tag}


%build
%make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
mkdir -p %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/include
install -m 644 ebin/%{realname}.app %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 ebin/*.beam %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 include/*.hrl %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/include


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README
%dir %{_libdir}/erlang/lib/%{realname}-%{version}
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/include
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/*.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/include/*.hrl



%changelog
* Fri May 06 2016 neoclust <neoclust> 2.1.0-0.11.20101022gitb55cb72.2.mga6
+ Revision: 1009759
- Rebuild post boostrap
- imported package erlang-gettext

