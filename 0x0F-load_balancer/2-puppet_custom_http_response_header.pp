class { 'nginx':
	header => {
		'X-Served-By' => '$host',
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
