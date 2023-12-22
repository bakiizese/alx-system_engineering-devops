#intalling packege using puppet
exec { 'Flask':
    command => 'sudo pip3 install flask=2.1.0',
}
