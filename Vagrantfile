# -*- mode: ruby -*-
# vi: set ft=ruby :

internal_ip = "172.28.128.3"
project_name = "uchislova"

Vagrant.configure(2) do |config|

  #config.vm.box = "larryli/vivid64"
  config.vm.box = "ubuntu/wily64"
  config.vm.network "private_network", ip: internal_ip
  config.vm.hostname = "slova"

  config.vm.provider :virtualbox do |v|
    v.memory = 1024
    v.gui = false
  end

  # for supress "stdin: is not a tty error"
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  config.vm.synced_folder ".", "/home/vagrant/" + project_name, id: "vagrant-root",
    owner: "vagrant",
    group: "vagrant",
    mount_options: ["dmode=775,fmode=664"]

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -q
    apt-get autoremove -y
    apt-get install mc npm -y
    apt-get install python3-venv -y
    npm install -g bower
    usermod -aG vagrant www-data
    echo '    IdentityFile /home/vagrant/.ssh/github' >> /etc/ssh/ssh_config
  SHELL


    # - install django and pip autocompletions
    # - create virtualenvironment
    # - install pip requirements
    # - install heroku tools

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    wget -q https://raw.githubusercontent.com/django/django/master/extras/django_bash_completion -O django_bash_completion
    echo source django_bash_completion >> ~/.bashrc
    pip completion --bash >> ~/.profile
    pyvenv virtualenvironment
    source /home/vagrant/virtualenvironment/bin/activate && pip install -r uchislova/requirements.txt
    wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
    git config --global user.email "mr.swasher@gmail.com"
    git config --global user.name "swasher"
  SHELL

  # этими строками создается проект джанго... но получается, что при повторном развертывании среды, когда проект уже
  # создан, эти настройки конфликтуют с уже имеющимся проектом... поэтому автоматическому созданию проекта джанго тут не место.
  # config.vm.provision "shell", privileged: false, inline: "source "+workon+" && cd "+project_name+" && django-admin.py startproject " + project_name + " ."
  # config.vm.provision "shell", privileged: false, inline: "source "+workon+" && cd "+project_name+" && django-admin.py startapp " + app_name

end
