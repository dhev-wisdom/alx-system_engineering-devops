#  This Puppet script installs v2.1.0 of Flask with pip

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
