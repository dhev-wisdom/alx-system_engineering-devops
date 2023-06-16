# Puppet script to install and set up Nginx with custom header

exec { 'update':
	provider => shell,
	command  => 'sudo apt-get update -y',
}

package { 'nginx':
	ensure => 'installed',
}

class { 'nginx':
	header => {
		'X-Served-By' => '$hostname',
	},
}

nginx::resource::server {'default':
	listen      => ['80 default_server'],
	server_name => '_',
	location    => {
		'/' => {
			root  => '/var/www/html/',
			index => 'index.html index.htm',
		},
	},
}

file { '/var/www/html/index.html':
  content => '<html><body><h1>Holberton School!</h1></body></html>',
  ensure => 'file',
}
