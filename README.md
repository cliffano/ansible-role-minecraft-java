<img align="right" src="https://raw.github.com/cliffano/ansible-role-minecraft-java/master/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/ansible-role-minecraft-java/workflows/CI/badge.svg)](https://github.com/cliffano/ansible-role-minecraft-java/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/ansible-role-minecraft-java/badge.svg)](https://snyk.io/test/github/cliffano/ansible-role-minecraft-java)

Ansible Role Minecraft Java
---------------------------

Ansible role for provisioning [Minecraft Java edition](https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc) on Linux machine.

Usage
-----

Add the role to playbook:

    - hosts: all

      vars:
        minecraft_version: 1.21
        install_dir: /opt/minecraft
        java_opts: -Xmx2048M - Xms1024M

      roles:
        - cliffano.minecraft-java
