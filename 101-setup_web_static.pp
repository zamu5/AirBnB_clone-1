#Redo the task #0 but by using Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get install -y nginx',
  before   => Exec['test']
}

exec {'test':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test',
  before   => Exec['shared']
}

exec {'shared':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['index']
}

exec {'index':
  provider => shell,
  command  => 'sudo touch /data/web_static/releases/test/index.html',
  before   => Exec['echo index']
}

exec {'echo index':
  provider => shell,
  command  => 'echo "Holberton School" > /data/web_static/releases/test/index.html',
  before   => Exec['current']
}

exec {'current':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['default']
}

exec {'default':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart']
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data']
}

file {'/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}