#!/bin/bash

DELAY=0.1s
if [ -n "$1" ]; then
    DELAY=$1
fi

function open {
printf "                                ...',;;:cccccccc:;,..
                             ..,;:cccc::::ccccclloooolc;'.
                          .',;:::;;;;:loodxk0kkxxkxxdocccc;;'..
                        .,;;;,,;:coxldKNWWWMMMMWNNWWNNKkdolcccc:,.
                     .',;;,',;lxo:...dXWMMMMMMMMNkloOXNNNX0koc:coo;.
                  ..,;:;,,,:ldl'   .kWMMMWXXNWMMMMXd..':d0XWWN0d:;lkd,
                ..,;;,,'':loc.     lKMMMNl. .c0KNWNK:  ..';lx00X0l,cxo,.
              ..''....'cooc.       c0NMMX;   .l0XWN0;       ,ddx00occl:.
            ..'..  .':odc.         .x0KKKkolcld000xc.       .cxxxkkdl:,..
          ..''..   ;dxolc;'         .lxx000kkxx00kc.      .;looolllol:'..
        ..'..    .':lloolc:,..       'lxkkkkk0kd,   ..':clc:::;,,;:;,'..
        ......   ....',;;;:ccc::;;,''',:loddol:,,;:clllolc:;;,'........
            .     ....'''',,,;;:cccccclllloooollllccc:c:::;,'..
                    .......'',,,,,,,,;;::::ccccc::::;;;,,''...
                      ...............''',,,;;;,,''''''......
                           ............................\n"
}
################################################################################
function closing {
printf "                             ...'',;;;;::;;;,'..
                            ..,;:cloodddxxxkkkkkkkkxol;..
                         .';codxxkkk000000000000kkkkkkxdoc,..
                       .,codxk0000000000000000000000000kkxddoc,..
                    .':ldxk00000000000000000000000000000000kkxxol:'
                 .,:ldxkk000000000K000000000000000K0000000000kkxkkx:.
              ..,coxkk000000000000000kk000000000000000000000000kxxxxl'
             .,;codxxkk00000000kkk0KK0XNWWWWWWWWWNX0kkkkk00000kkxdool;.
           .';::ccldk00KKKK00oc;..,x00KNNXXXXXNNX0000000000kkkkkkxoc:,..
         ..,;,'..,o00000kkxo,       ,lkKKKKKK0K0d,.;ldk000KK0kxxxdoc:'..
        ..,,'.  .,lk0xxxdol:,..       .,ldddl:,.   .,codkk00kxdollc:,...
        ..'.......',;:c::cclccc::;,,,',,;::::;,;;:clodddxdol:;::;'......
           .....  ...''',,,;;;:ccllloooooooooooooolllcccc:;;,....
                    .......'',,,,,,;;;:::ccclllccc:::;;;,''...
                      ..............'''',,;;;;;,,,''''......
                           .............................\n"
}
################################################################################
function closed {
printf "                                 ...'',;;;;;;;,,...
                            ..,:loxkk000000KKKKKK00xdc,..
                         .,cox000KXXXXXXXXXXXXXXXXXXXK00xo:,..
                      ..;lx000KKKKK000000000000000KKKKXXXXK00xl;..
                   ..,:oxk00000000000000000000000000000000KKKKKK0d:.
                ..;codxkk000kkkkkkkxxxxxxxxxxxxxxxxkkkkkk000000KK0kl'
              ..;ldxkkkkkkxxxxxddddddddddddddddddddddddxxxxxxkkk000xc.
            ..,:oxxkkkkkxxxxdddddddddddddddddddddddddddddddddxxkkkkxl;.
          ..,;codxxkkkxxddddddddddddddddddddddddddddddddxdxxxk000kxdo:..
         .';::::cldk000kkkxxxxxxdddddddddddddddddddddxxxxxkk0000xkddl;..
        .';:;,..,ckXXXKKK0KK000kxk0doddxxdddddddxxxxxxkk0000kkkkkxdoc,..
        .',,''..,:oxxxxxxxkkxkkxk00xxk000000000000KKKKKKK000kxdllll:,..
         .........',,,:ccllllooooxkxxx000kk0000000000000000kxdoc,'...
                 ......',;;::cc::clllloddoox0xdxxkxxxxddollllc:'.
                      .....'',,,,,,,;;;;;::cllc::ccc::;;,,,'...
                          ..................'''..'''......\n"
}

clear
open
sleep $DELAY

clear
closing
sleep $DELAY

clear
closed
sleep $DELAY

clear
closing
sleep $DELAY

clear
open
