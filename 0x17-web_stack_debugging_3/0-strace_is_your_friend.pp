# fix php

exec { 'fix_phpp_in_wp_settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
