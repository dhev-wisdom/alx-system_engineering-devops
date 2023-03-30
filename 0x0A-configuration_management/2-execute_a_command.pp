# Killa a proces with Puppet

exec { 'killmenow':
    command => 'pkill killmenow',
    onlyif  => 'pgrep killmenow',
}
