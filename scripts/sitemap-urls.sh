#!/bin/bash

parse_xml() {
  xml=`curl -s $1 -k --max-time 30`
  locations=$(tr '\n' ' ' <<< "$xml" | grep -oP "(?<=<loc>)(.*?)(?=</loc>)")
  sub_xmls=(`grep -e ".xml$" <<< $locations`)
  pages=(`grep -v -e ".xml$" <<< $locations`)

  printf '%s\n' "${pages[@]}" >&1

  for xml_url in "${sub_xmls[@]}"
  do
    parse_xml $xml_url
  done
}

parse_xml $1
