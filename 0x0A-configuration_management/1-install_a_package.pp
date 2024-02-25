#!/usr/bin/env puppet

# Install Flask package with version 2.1.0
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin'],
  refreshonly => true,
}

file { '/usr/local/bin/flask':
  ensure => link,
  target => '/usr/local/bin/flask',
  require => Exec['install_flask'],
}
