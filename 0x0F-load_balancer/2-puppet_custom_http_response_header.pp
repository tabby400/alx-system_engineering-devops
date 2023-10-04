# creating  a custom HTTP header response with
# puppet and automating it



exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header': # line matches http searched
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run': # exwc resourse used
  command => '/usr/sbin/service nginx restart',
}
