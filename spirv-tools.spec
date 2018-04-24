%global commit 26a698c34788bb69123a1f3789970a16cf4d9641
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20180407
%global gitrel .%{commit_date}.git%{shortcommit}

Name:           spirv-tools
Version:        2018.1
Release:        0.4%{?gitrel}%{?dist}
Summary:        API and commands for processing SPIR-V modules

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/SPIRV-Tools
Source0:        %url/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python2-devel
BuildRequires:  python2-simplejson
BuildRequires:  spirv-headers-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V..

%package        libs
Summary:        Library files for %{name}
Provides:       %{name}-libs%{?_isa} = 2018.3.0

%description    libs
library files for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}

%prep
%autosetup -p1 -n SPIRV-Tools-%{commit}

%build
%__mkdir_p %_target_platform
pushd %_target_platform
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/python%{python2_version} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
        -GNinja ..
%ninja_build
popd

%install
%ninja_install -C %_target_platform

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/spirv-as
%{_bindir}/spirv-cfg
%{_bindir}/spirv-dis
%{_bindir}/spirv-lesspipe.sh
%{_bindir}/spirv-link
%{_bindir}/spirv-opt
%{_bindir}/spirv-stats
%{_bindir}/spirv-val

%files libs
%{_libdir}/libSPIRV-Tools-link.so
%{_libdir}/libSPIRV-Tools-opt.so
%{_libdir}/libSPIRV-Tools-shared.so
%{_libdir}/libSPIRV-Tools.so

%files devel
%{_includedir}/spirv-tools/
%{_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{_libdir}/pkgconfig/SPIRV-Tools.pc

%changelog
* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.4.20180407.git26a698c
- Bump provides to 2018.3.0

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.3.20180407.git26a698c
- Update for vulkan 1.1.73.0

* Wed Feb 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.2.20180205.git9e19fc0
- Add isa to the provides

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2018.1-0.1.20180205.git9e19fc0
- Fix version
- Fix pkgconfig file
- Add version provides to -libs package

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.5.20180205.git9e19fc0
- Update for vulkan 1.0.68.0
- Try building as shared object
- Split libs into -libs subpackage

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.4.20171023.git5834719
- Use ninja to build

* Mon Jan 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.3.20171023.git5834719
- Add python prefix to fix the stupid Bodhi tests

* Wed Jan 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.2.20171023.git5834719
- Split binaries into main package

* Thu Jul 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 2016.7-0.1.20171023.git5834719
- First build

