Vagrant.configure("2") do |config|
    config.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
        vb.cpus = "1"
    end

    config.vm.define "ubuntu" do |ubuntu|
        ubuntu.vm.box = "bento/ubuntu-18.04"
        ubuntu.vm.network "private_network", ip: "192.168.50.100"
        ubuntu.vm.synced_folder "shared/", "/home/vagrant/shared"
        ubuntu.vm.provision :shell, inline: <<SCRIPT
            apt-get update
SCRIPT
    end
end