export tag="latest"
export game="swimming_squid"

docker run -it --rm --name ${game} \
-v ./ai/user-1/code-123:/game/ai/1P \
-v ./records:/game/records \
-v ./var:/game/var  \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=host.docker.internal:0 \
${game}:${tag} \
sh -c "python -m mlgame -1 -f 30 -r /game/records -i /game/ai/1P/ml_play.py /game --level_file /game/var/level.json"