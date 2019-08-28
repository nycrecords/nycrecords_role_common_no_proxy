[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)  
[![Build Status](https://travis-ci.org/nycrecords/nycrecords_role_common_no_proxy.svg?branch=master)](https://travis-ci.org/nycrecords/nycrecords_role_common_no_proxy)
[![Galaxy](https://img.shields.io/badge/galaxy-joelbcastillo.nycrecords_role_common_no_proxy-blue.svg)](https://galaxy.ansible.com/lean_delivery/nginx)
![Ansible](https://img.shields.io/ansible/role/d/43008.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F43008%2F&query=$.min_ansible_version)

NYCRecords Common (No-Proxy)
=========

Setup the base requirements for a NYC Department of Records RHEL Server without proxy configuration. 

This should only be used to servers hosted in the cloud (e.g. in AWS or Azure) or for development servers that will not be used within Citynet (the City's internal network).

Requirements
------------

- RedHat Subscription
  - You'll need to sign up for a RedHat Subscription. You can sign up for a free Developer subscription on https://developers.redhat.com

This role requires root access (required to manage subscriptions on RedHat). Either run it in a playbook with a global `become: yes` or invoke the role in your playbook like:
```yaml
- hosts: all
  roles:
    - role: nycrecords.nycrecords_role_common_no_proxy
      become: yes
```

Role Variables
--------------
Available variables are listed below, along with default values (see defaults/main.yml):

```
repos:
    - rhel-server-rhscl-{{ ansible_distribution_major_version }}-rpms
    - rhel-{{ ansible_distribution_major_version }}-server-optional-rpms
```  
The repositories to subscribe to from RedHat. You can view a list of these by running the following command on a registered server: `subscription-manager repos --list`

`rhsub_system_name: nycrecords_common_{{ '%Y%m%d-%H%M%S' | strftime(ansible_date_time.epoch) }}`  
Defines the name used to register the machine with RedHat Subscription Management. Default to nycrecords_common_YYYYmmdd-HHMMSS (e.g. nycrecords_common_20190102-030405)

`rhsub_username: ${RHSM_USERNAME}`  
The username for your RedHat Subscription

`rhsub_password: ${RHSM_PASSWORD}`  
The username for your RedHat Subscription

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  become: yes
  vars_files:
    - vars/main.yml
  roles:
    - nycrecords.nycrecords_role_common_no_proxy
```

Inside `vars/main.yml`:
```yaml
repos:
  - rhel-server-rhscl-7-rpms
  - rhel-7-server-optional-rpms
rhsub_username: myusername
rhsub_password: my5ecur3P@ssw.rd
rhsub_system_name: my_unique_system_name
```

License
-------

Apache-2.0

Author Information
------------------

This role was created by the [NYC Records Development Team](https://github.com/nycrecords) in 2019.
