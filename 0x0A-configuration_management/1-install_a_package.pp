# installing flask using puppet
package { 'Flask':
  ensure   => 'latest',
  provider => 'pip3',
}

