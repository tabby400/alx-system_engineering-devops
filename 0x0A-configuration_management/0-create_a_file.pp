#file tracked by puppet

file { '/tmp/school': # file location
  ensure  => 'file',
  mode    => '0744', # file permissions
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet', # what file has
}
