# Puppet script installs and configures nginx server

# install nginx
package {'nginx':
	ensure => installed,
}

# Configure Nginx server
# GET '/' returns "Hello World!"
# route '/redirect_me' goes to another page

file {'/etc/nginx/sites-available/defualt':
	ensure  => file,
	content => "
		server {
			listen 80;
			server_name _;
			root /var/www/html/;
			index index.html;
		
			location / {
				return 200 'Hello World!';
			}

			location /redirect_me {
				return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
			}
		}
	",
}

# Enable default site
file {'/etc/nginx/sites-enabled/default':
	ensure => 'link',
	target => '/etc/nginx/sites-available/default',
	force  => true,
}

# Restart nginx
service {'nginx':
	ensure => running,
	enable => true,
}
