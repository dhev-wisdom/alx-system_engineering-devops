sshkey { 98.98.98.98:
  ensure => present,
  type   => 'ssh-rsa',
  key    => '~/.ssh/school'
}

sshd_config { 'PasswordAuthentication':
  ensure => present,
  value  => 'no',
}

