# This file creates a simple '/tmp/school' file with Puppet

file {'/tmp/school':
	ensure => present,
	content => "I love Puppet",
	group => "www-data",
	owner => "www-data",
	mode => "0744",
}
