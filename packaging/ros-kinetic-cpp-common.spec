Name:           ros-kinetic-cpp-common
Version:        0.6.5
Release:        0
Summary:        ROS roscpp core package
Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roscpp_core
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  pkgconfig(console_bridge)
Requires:       libconsole_bridge0
Requires:       pkgconfig(console_bridge)

%define         ros_distro kinetic
%define         ros_root /opt/ros
%define         install_path %{ros_root}/%{ros_distro}
	
%description
cpp_common contains C++ code for doing things that are not necessarily ROS
related, but are useful for multiple packages. This includes things like the
ROS_DEPRECATED and ROS_FORCE_INLINE macros, as well as code for getting
backtraces. This package is a component of roscpp.

%package        traits
Summary:        ROS cpp traits package
Group:          Development/Libraries
BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin
Provides:      ros-kinetic-roscpp-traits

%description    traits
This package is a traits component of roscpp.

%package        rostime
Summary:        ROS time package
Group:          Development/Libraries
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  pkgconfig(console_bridge)
Requires:       libconsole_bridge0
Requires:       ros-kinetic-cpp-common
Provides:       ros-kinetic-rostime

%description    rostime
This package is a time component of roscpp.

%package        serialization
Summary:        ROS cpp serialization package
Group:          Development/Libraries
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  pkgconfig(console_bridge)
Requires:       ros-kinetic-cpp-common
Requires:       ros-kinetic-roscpp-traits
Requires:       ros-kinetic-rostime
Requires:       libconsole_bridge0
Provides:       ros-kinetic-roscpp-serialization

%description    serialization
This package is a serialization component of roscpp.

%prep
%setup -q
cp %{SOURCE1001} .

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd cpp_common
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{install_path}" \
        -DCMAKE_PREFIX_PATH="%{install_path}" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}
popd

pushd roscpp_traits
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{install_path}" \
        -DCMAKE_PREFIX_PATH="%{install_path}" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}
popd

pushd rostime
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{install_path}" \
        -DCMAKE_PREFIX_PATH="%{install_path}" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}
popd

pushd roscpp_serialization
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{install_path}" \
        -DCMAKE_PREFIX_PATH="%{install_path}" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}
popd

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd cpp_common
pushd build
make install DESTDIR=%{buildroot}
popd
popd

pushd roscpp_traits
pushd build
make install DESTDIR=%{buildroot}
popd
popd

pushd rostime
pushd build
make install DESTDIR=%{buildroot}
popd
popd

pushd roscpp_serialization
pushd build
make install DESTDIR=%{buildroot}
popd
popd

%files -f cpp_common/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%files traits -f roscpp_traits/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%files rostime -f rostime/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%files serialization -f roscpp_serialization/build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)