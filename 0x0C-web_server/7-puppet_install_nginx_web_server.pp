# Puppet script installs and configures nginx server

# install nginx
package {'nginx':
  ensure => installed,
}

# Configure Nginx server
# GET '/' returns "Hello World!"

# Create an index.html file containing 'Hello World!'
file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}
# route '/redirect_me' goes to another page
file {'/etc/nginx/sites-available/defualt':
  ensure  => file,
  content => "
		server {
			listen 80;
			server_name _;
			root /var/www/html;
			index index.html;
		
			location / {
				try_files ${uri} ${uri}/ =404;
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
