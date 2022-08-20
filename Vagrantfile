# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/8"
  config.vm.network "private_network", type: "dhcp"
  config.vm.network "forwarded_port", guest: 5000, host: 8080
end
