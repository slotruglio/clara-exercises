# Esercizio 2
Assumo che non ci siano file da escludere dal backup, come potrebbe essere il file ".DS_Store" su mac. 

Assumo che il backup sia effettuato ogni domenica alle 1:00 di notte.

Assumo inoltre che il server remoto sia raggiungibile tramite chiave ssh. Successivamente in questo documento verrà spiegato un possibile modo per configurare l'autenticazione tramite chiave ssh.

## Soluzione
La riga di crontab è la seguente:
``` bash
0 1 * * 0 /path/to/backup.sh
```

Il file [backup.sh](backup.sh) contiene il codice che permette di effettuare il backup e l'invio tramite ssh.

In questo file vengono definite le seguenti variabili:
* USER: nome utente del server remoto
* IP: indirizzo ip del server remoto
* DATE: data di esecuzione dello script (si genera automaticamente)
* SOURCE: cartella da copiare
* DESTINATION: cartella di destinazione del backup sul server remoto

In particolare utilizza rsync con le seguenti opzioni:
* -r: permette di copiare ricorsivamente i file.
* -a: permette di copiare i file mantenendo i permessi, le date, i link simbolici, ecc.
* -z: permette di comprimere i dati durante il trasferimento.

Ho scelto di aggiungere l'opzione della compressione perché in base alla dimensione della cartella da copiare potrebbe essere utile ridurre la dimensione dei dati da trasferire sia per velocizzare il trasferimento che per ridurre lo spazio occupato sul server remoto.

Inoltre ho scelto di salvare il backup in una cartella con il nome della data di esecuzione dello script per poter avere un backup per ogni esecuzione dello script e poter quindi recuperare facilmene una versione precedente del backup.

## Configurazione dell'autenticazione tramite chiave ssh
Per configurare l'autenticazione tramite chiave ssh è necessario generare una chiave ssh sul server locale e copiare la chiave pubblica sul server remoto.

Per fare ciò ci sono diversi modi, uno di questi prevede di utilizzare il comando ssh-keygen per generare la chiave rsa e il comando ssh-copy-id per copiare la chiave pubblica sul server remoto. I comandi sono i seguenti:
``` bash
ssh-keygen -t rsa
ssh-copy-id user@192.168.1.100
```