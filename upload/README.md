# UPLOAD

> This directory contains files for testing upload functionality.

* :small_red_triangle_down: DOS_bilion_laughs.*

> [YAML example](https://dev.to/efrat19/the-billion-laughs-attack-yaml-anchors-explained-3767) 
> [XML example](https://www.geeksforgeeks.org/xml-external-entity-xxe-and-billion-laughs-attack/)

* :small_red_triangle_down: DOS_pixel_flood.jpg 

> [Data compression bomb](https://hackerone.com/reports/390)

* :small_red_triangle_down: DOS_txt.png

> [zTXt chunk with zlib compression](https://hackerone.com/reports/454)

* :small_red_triangle_down: cmd.zip

> The decompressed files could be created in unexpected folders - after upload look for cmd.php

* :small_red_triangle_down: sympasswd.zip

> Upload a link containing soft links to other files, then, accessing the decompressed files you will access the linked files.

* :small_red_triangle_down: simple_backdoor.php

> Just php simple backdoor

* :small_red_triangle_down: normal.png

> Casual png file for initial upload.

* :small_red_triangle_down: PDF+PHP.pdf

> Polyglot with php code which fortunately evaluate to: RCE IS REAL
