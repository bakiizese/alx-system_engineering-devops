#puppet code that kills proceses
exec { 'pkill':
    command => 'pkill -15 killmenow',
}
