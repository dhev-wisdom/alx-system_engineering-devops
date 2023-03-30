# Creates a file in /tmp.

file { 'school':
  name    => '/tmp/',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
