#!/bin/bash

tools=(
  "CVE-2021-42063"
  "CVE-2018-8033"
  "CVE-2021-20323"
  "CVE-2023-29489"
  "crlfi"
  "Open redirect"
  "CVE-2019-9670"
  "CVE-2023-27524"
  "CVE-2020-27838"
  "CVE-2021-40438"
  "CVE-2020-3187"
  "CVE-2020-35489"
  "CVE-2017-7269"
  "CVE-2021-24917"
  "CVE-2023-4568"
  "CVE-2018-0296"
  "laravel-ignition-Rxss"
  "CVE-2023-5089"
  "CVE-2020-3452"
  "critix-netscaler-memory-leak"
  "CVE-2023-24044"
  "CVE-2015-7297"
  "CVE-2018-11784"
  "CVE-2015-1635"
  "CVE-2022-0165"
  "phpinfo-files-leaks"
  "shell-history-leaks"
  "CVE-2000-0114"
  "CVE-2024-1208"
  "CVE-2023-46805"
  "appspec-yaml-leaks"
  "CVE-2024-24919"
  "behat-config-leaks"
  "CVE-2019-12616"
  "CVE-2024-4956"
)


for tool in "${tools[@]}"; do
  pip install "$tool"
  pip3 install "$tool"
done

echo "Installation complete."
