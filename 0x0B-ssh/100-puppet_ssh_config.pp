# Setting ssh configuration with Puppet

file { '/etc/ssh/ssh_config':
    ensure => 'file',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode => '0600',
}

file_line { 'set-ssh-config':
    path => '/etc/ssh/ssh_config',
    line => "PasswordAuthentication no\n"
}

