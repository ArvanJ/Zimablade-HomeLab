
# 🧠 NodeHaus PXE Imaging Server: From MDT to FOG

## 📌 Introduction
This project documents the full setup of a PXE-based imaging server using the **FOG Project** on Ubuntu 24.04, hosted from a homelab environment branded as **NodeHaus**. The goal is to replace traditional **MDT + Windows Server imaging** with a faster, open-source, cross-platform alternative backed by TrueNAS and remote management via Tailscale.

Created by Arvan Jindam (me 🙋‍♂️), this setup was designed to power lab imaging, Windows/Linux deployment, and remote boot control while keeping all images on a shared NAS.

---

## ⚙️ Hardware & Base System

### 🖥 PXE Server (NodeHaus PXE)
- **OS**: Ubuntu 24.04  
- **Hostname**: `pxeserver`  
- **IP Address**: `<ip-address>`  
- **FOG Version**: 1.5.10.1660  
- **Drive**: 31GB (boot only)  

### 🗄️ NAS Storage (Zima2TB on TrueNAS)
- **IP**: `<ip-address>`  
- **Mount Path**: `/mnt/Zima2TB`  
- **Image Path**: `/mnt/Zima2TB/MDTDeploymentService/fogimages`  
- **Connection**: CIFS via `fstab`

---

## 🧰 Setup Script

```bash
#!/bin/bash
# NodeHaus PXE + FOG Setup Script

# 1. Install base packages
apt update && apt install -y \
  git apache2 php php-cli php-fpm php-mysql \
  mariadb-server mariadb-client \
  php-curl php-mbstring php-xml php-gd php-intl php-bcmath \
  curl cifs-utils

# 2. Create mount path and credentials file
mkdir -p /mnt/Zima2TB
cat <<EOF > /etc/fognas-credentials
username=nasuser
password=naspass
EOF
chmod 600 /etc/fognas-credentials

# 3. Add to /etc/fstab if not present
grep -q Zima2TB /etc/fstab || echo "//<ip-address>/Zima2TB /mnt/Zima2TB cifs credentials=/etc/fognas-credentials,uid=fogproject,gid=www-data,file_mode=0777,dir_mode=0777,nounix,noserverino 0 0" >> /etc/fstab

# 4. Mount NAS
mount -a

# 5. Clone and move FOG installer
cd ~
git clone https://github.com/FOGProject/fogproject.git
mv fogproject /home/pxe/fogproject
cd /home/pxe/fogproject/bin

# 6. Optional: edit storage location
[ -f /opt/fog/.fogsettings ] && sed -i "s|storageLocation=.*|storageLocation='/mnt/Zima2TB/MDTDeploymentService/fogimages'|" /opt/fog/.fogsettings

# 7. Install FOG
./installfog.sh
```

---

## 🔐 Remote Access with Tailscale
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

> Access your server at: `http://<ip-address>/fog/management`

---

## 🧪 PXE Booting Linux Mint (Live)
```bash
sudo mount -o loop "/mnt/Zima2TB/MDTDeploymentService/Operating Systems/linuxmint-22.1-xfce-64bit.iso" /mnt/mint
sudo mkdir -p /var/www/html/os/linuxmint
sudo cp /mnt/mint/casper/vmlinuz /var/www/html/os/linuxmint/
sudo cp /mnt/mint/casper/initrd.lz /var/www/html/os/linuxmint/
rsync -av /mnt/mint/ /var/www/html/os/linuxmint/files/
```

PXE Menu Entry:
```cfg
LABEL linuxmint
    MENU LABEL Boot Linux Mint 22.1 XFCE
    KERNEL http://<ip-address>/os/linuxmint/vmlinuz
    INITRD http://<ip-address>/os/linuxmint/initrd.lz
    APPEND boot=casper netboot=http url=http://<ip-address>/os/linuxmint/files/ locale=en_US.UTF-8 keyboard-setup/layoutcode=us
```

---

## 🔁 Transition from MDT

1. Deploy MDT image to test system  
2. PXE boot into FOG → Full Host Registration  
3. Assign an image definition  
4. Capture image as "Single Disk Resizable"  
5. Use FOG to deploy going forward

---

## 📚 Next Steps

- PXE entries: Ubuntu, Kali, GParted  
- Snapins for domain join, post-deploy setup  
- Migrate production MDT server → FOG  
- Add SSL and user auth roles

---

## 🙌 Credits

Maintained by: [@ArvanJindam](https://github.com/arvanjindam)  
Assistant AI: ChatGPT
