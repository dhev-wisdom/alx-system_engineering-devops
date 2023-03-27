# Setting ssh configuration with Puppet

file { '/etc/ssh/ssh_config':
    ensure => 'file',
    owner  => '98.98.98.98',
    group  => '98.98.98.98',
    mode   => '0600'
}

file_line { 'set-ssh-config':
    path => '/etc/ssh/ssh_config',
    line => "PasswordAuthentication no\n"
}

