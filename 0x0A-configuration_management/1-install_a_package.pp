#  This Puppet script installs v2.1.0 of Flask with pip

package { 'Flask':
    ensure => '2.1.0',
    name   => 'Flask',
}
