# Setting ssh configuration with Puppet

file { '/etc/ssh/ssh_config':
    ensure => 'file',
    owner  => '10.251.0.2',
    group  => '10.251.0.2',
    mode   => '0600'
}

file_line { 'set-ssh-config':
    path => '/etc/ssh/ssh_config',
    line => "PasswordAuthentication no\n"
}

