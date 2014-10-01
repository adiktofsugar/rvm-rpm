Name: rvm
Version: 0.1
Release: 1
BuildRequires: libyaml-devel libffi-devel autoconf automake libtool bison
Requires: libyaml-devel libffi-devel autoconf automake libtool bison
Summary: Rvm and ruby
License: Open

%description
Rvm with ruby, gem, and bundler, packaged as an rpm. System level install.

%build
mkdir -p $RPM_BUILD_ROOT/rvm
cp $RPM_SOURCE_DIR/rvm/rvm-stable.tar.gz $RPM_BUILD_ROOT/
cd $RPM_BUILD_ROOT/rvm
tar --strip-components=1 -xzf ../rvm-stable.tar.gz
sudo ./install --auto-dotfiles

sudo bash -c 'echo "" > /usr/local/rvm/gemsets/default.gems'
sudo bash -c 'echo "" > /usr/local/rvm/gemsets/global.gems'

sudo bash -c 'echo "
rvm_archives_path=/usr/local/rvm/archives
rvm_autolibs_flag=read-fail
" > /etc/rvmrc'

sudo cp -rf $RPM_SOURCE_DIR/rvm/archives/* /usr/local/rvm/archives/
sudo chgrp -R rvm /usr/local/rvm
sudo chmod -R g+wxr /usr/local/rvm

sudo /usr/local/rvm/bin/rvm install 2.1.3

sudo bash -c 'echo "
current=ruby-2.1.3
default=ruby-2.1.3
" > /usr/local/rvm/config/alias'

sudo /usr/local/rvm/bin/rvm 2.1.3@global do gem install /usr/local/rvm/archives/bundler-1.7.3.gem


%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/usr/local/rvm
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/profile.d

sudo cp -rf /usr/local/rvm/* $RPM_BUILD_ROOT/usr/local/rvm/
sudo cp /etc/profile.d/rvm.sh $RPM_BUILD_ROOT/etc/profile.d/rvm.sh
sudo cp /etc/rvmrc $RPM_BUILD_ROOT/etc/rvmrc

sudo chgrp -R rvm $RPM_BUILD_ROOT/usr/local/rvm
sudo chmod -R g+wxr $RPM_BUILD_ROOT/usr/local/rvm

%clean
#sudo rm -rf /usr/local/rvm
#sudo rm /etc/rvmrc
#sudo rm /etc/profile.d/rvm.sh

%files
/usr/local/rvm
/etc/rvmrc
/etc/profile.d/rvm.sh
