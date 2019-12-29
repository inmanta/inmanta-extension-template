# Use release 0 for prerelease version.
%define release 0
%define version {{ cookiecutter.extension_version }}
%define buildid %{nil}
%define venv inmanta-venv
%define _p3 %{venv}/bin/python3
%define site_packages_dir %{venv}/lib/python3.6/site-packages
%define _unique_build_ids 0
%define _debugsource_packages 0
%define _debuginfo_subpackages 0
%define _enable_debug_packages 0
%define debug_package %{nil}

%define sourceversion %{version}%{?buildid}

Name:           python3-{{ cookiecutter.project_name }}
Version:        %{version}

Release:        %{release}%{?buildid}%{?tag}%{?dist}
Summary:        {{ cookiecutter.project_description }}

Group:          Development/Languages
License:        {{ cookiecutter.license }}
URL:            {{ cookiecutter.git_repo_url }}
Source0:        {{ cookiecutter.project_name }}-%{sourceversion}.tar.gz
Source1:        deps-%{sourceversion}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python3-inmanta
BuildRequires:  systemd

Requires:  python3-inmanta

# Use the correct python for bycompiling
%define __python %{_p3}

%description

%prep
%setup -q -n {{ cookiecutter.project_name }}-%{sourceversion}
%setup -T -D -a 1 -n {{ cookiecutter.project_name }}-%{sourceversion}

%build


%install
cp -r --no-preserve=ownership /opt/inmanta %{venv}

# Save packages installed by dependencies
files=$(find "%{site_packages_dir}" -maxdepth 1 -mindepth 1 ! -path "%{site_packages_dir}/inmanta_ext")

# Install {{ cookiecutter.extension_name }}
%{_p3} -m pip install --pre --no-index --find-links dependencies .

# Only keep new packages
rm -rf ${files}

# Only retain inmanta_ext/{{ cookiecutter.extension_name }} in inmanta_ext folder
find "%{site_packages_dir}/inmanta_ext" -maxdepth 1 -mindepth 1 ! -path "%{site_packages_dir}/inmanta_ext/{{ cookiecutter.extension_name }}" |xargs rm -rf

# Byte-compile source code
packages_to_bytecompile=("{{ cookiecutter.slice_package_name }}" "inmanta_ext")
for p in "${packages_to_bytecompile[@]}"; do
   find "%{site_packages_dir}/${p}" -name '*.py' |xargs -I file_name python3.6 -c 'import py_compile; py_compile.compile(file="file_name", cfile="file_namec", doraise=True)'
   find "%{site_packages_dir}/${p}" -name '*.py' |xargs rm -f
   find "%{site_packages_dir}/${p}" -name '__pycache__' |xargs rm -rf
done

mkdir -p %{buildroot}/opt/inmanta/
cp -r %{venv}/lib/ %{buildroot}/opt/inmanta/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/inmanta/lib/

%preun
# Stop and disable the inmanta-server service before this package is uninstalled
%systemd_preun inmanta-server.service

%postun
# Restart the inmanta-server service after an upgrade of this package
%systemd_postun_with_restart inmanta-server.service

%changelog
* {% now 'utc', '%a %b %d %Y' %} {{ cookiecutter.author }} <{{ cookiecutter.author_email }}> - {{ cookiecutter.extension_version }}
- Initial release
