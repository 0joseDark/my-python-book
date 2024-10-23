Existem vários módulos Python que permitem implementar o **Wake-on-LAN (WOL)**, que é uma técnica usada para ligar computadores remotamente através de pacotes de rede. Dois módulos populares para isso são:

1. **`wakeonlan`**: Um módulo simples que envia um pacote mágico (Magic Packet) para um dispositivo na rede.

   - Instalação:  
     ```
     pip install wakeonlan
     ```

   - Exemplo de uso:
     ```python
     from wakeonlan import send_magic_packet

     send_magic_packet('AA:BB:CC:DD:EE:FF')  # MAC address do dispositivo
     ```

2. **`wol`**: Outro módulo que pode ser usado para enviar pacotes WOL, com algumas opções adicionais.

   - Instalação:
     ```
     pip install wol
     ```

   - Exemplo de uso:
     ```python
     import wol

     wol.send_wol('AA:BB:CC:DD:EE:FF', ip_address='192.168.1.255')
     ```

Ambos funcionam de maneira semelhante, enviando o **pacote mágico** necessário para despertar uma máquina. Certifique-se de que o Wake-on-LAN está ativado no BIOS da máquina de destino e que a placa de rede suporta essa função.
