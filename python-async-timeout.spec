%global srcname async-timeout
%global common_desc asyncio-compatible timeout context manager\
The context manager is useful in cases when you want to apply timeout\
logic around block of code or in cases when asyncio.wait_for() is not \
suitable. Also it's much faster than asyncio.wait_for() because timeout\
doesn't create a new task.

Name:           python-%{srcname}
Version:        1.2.1
Release:        1%{?dist}
Summary:        asyncio-compatible timeout context manager

License:        ASL 2.0
URL:            https://github.com/aio-libs/async-timeout
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
%{common_desc}

# This module is Python 3 only
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest-runner

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n async-timeout-%{version}

%build
%py3_build

%install
%py3_install

%check
# pytest_aiohttp is not available in the repos
#%%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/async_timeout/
%{python3_sitelib}/async_timeout-*.egg-info/

%changelog
* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Mar 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuild for Python 3.6

* Thu Nov 17 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-3
- Add missing BR
- Rename the pkg

* Sun Nov 13 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-2
- Update files section and the description

* Fri Nov 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-1
- Initial spec

