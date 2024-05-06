

## RUN with root
docker run --name convert -p 8080:80 -v D:\tmp\config:/root/.config -v D:\tmp\output_files:/app/output_files -v D:\tmp\tmp:/tmp -v D:\tmp\var:/var -v D:\tmp\root:/root/.cache/dconf -v D:\tmp\appuser\1: /home/appuser/.config -v D:\tmp\appuse\2:/home/appuser/.cache/dconf --read-only myimage:v1

## RUN without root
docker run --name convert -p 8080:80 -v D:\tmp\output_files:/app/output_files -v D:\tmp\tmp:/tmp -v D:\tmp\var:/var -v D:\tmp\appuser\1:/home/appuser/.config -v D:\tmp\appuser\2:/home/appuser/.cache/dconf --read-only myimage:v1