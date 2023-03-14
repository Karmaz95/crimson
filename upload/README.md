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

> Just php simple backdoor.

* :small_red_triangle_down: normal.png

> Casual png file for initial upload.

* :small_red_triangle_down: PDF+PHP.pdf

> Polyglot with php code which fortunately evaluate to: RCE IS REAL.

* :small_red_triangle_down: uber.gif

> A GIF composed of 40k 1x1 images made Paperclip freeze until timeout.

* :small_red_triangle_down: xssproject.swf

> Make a website vulnerable to XSS if you can upload/include a SWF file into that website. 

> Example 1 => /xssproject.swf?js=alert(document.domain); 

> Example 2 => /xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open(‘?js=history.go(-1)’,’_self’);}

> Example 3 => /xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);


* :small_red_triangle_down: img_phpinfo.*

> Described here: https://secgeek.net/bookfresh-vulnerability/

* :small_red_triangle_down: eicar.com.txt

> Test the response of computer antivirus (AV) programs.

* :small_red_triangle_down: formula_injections.txt

> Excel formulas that will be executed when the user opens the file or when the user clicks on some link inside the excel sheet.

* :small_red_triangle_down:  exiftool.jpg

> Edit using text editor - swap domain_collab with custom domain

* :small_red_triangle_down:  req.pdf

> alerts and makes HTTP request to collab (works on Chrome)

* :small_red_triangle_down: steal-content.pdf

>  alerts and is a PoC of possible data leak from a PDF via HTTP request to collab (works on Chrome)

* :small_red_triangle_down: test.aspx

> Upload it through the web interface and attempt to access it manually or using file bruteforcing.

* :small_red_triangle_down: jku_attack.json

> Use Burp Suite to generate RSA key, replace it in the template and host it on your server. 
> Then replace KID, add JKU and modify payload in the JWT and sign the token using this RSA key.

* :small_red_triangle_down: pil_ghost.png

> Replace COMMAND_PLACEHOLDER with your command, for example "touch /tmp/pwn.txt" , "ping 127.0.0.1" or "sleep 10".
> You can change the extension (The default should be .eps)
