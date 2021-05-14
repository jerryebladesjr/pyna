#!/bin/bash

ssh-copy-id -i ~/.ssh/id_rsa.pub bender@10.10.2.3
ssh-copy-id -i ~/.ssh/id_rsa.pub fry@10.10.2.4
ssh-copy-id -i ~/.ssh/id_rsa.pub zoidberg@10.10.2.5

