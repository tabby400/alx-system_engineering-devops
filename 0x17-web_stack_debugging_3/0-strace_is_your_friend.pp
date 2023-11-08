# strace used to fix apache 500 error

exec {'new word':
    command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    provider => shell,
}
